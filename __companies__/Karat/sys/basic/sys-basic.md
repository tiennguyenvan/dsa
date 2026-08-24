# Interview

| Time      | Section          | Focus                           |
| --------- | ---------------- | ------------------------------- |
| 0–2 min   | Introduction     | Language, format                |
| 2–20 min  | System knowledge | One broad request-flow scenario |
| 20–35 min | Coding problem 1 | Medium or below                 |
| 35–50 min | Coding problem 2 | Medium or below                 |

# System design

## FULL FLOWS
### DNS
Client (Browser <=> DNS: convert domain to ips -> real `CDN` or `API Gateway` or `BE Public` addr)
Client -> `POST /posts/{postId}/comments`

### CDN (CloudFront/Cloudflare)
 * Caching (media, css, html, js):
    - Client sends GET, CDN checks its edge cache
    - Cache hit ? `return` : `call API->cache resp->return`
 * Cache Data:
    - Key: (url+query+hdr)
    - TTL: time-to-live
    - Cache-control: caching rules returned in hdr from origin: `public, max-age=60, ..`
        - public: any one can cache
        - private: only browser can cache, CDN should not
        - no-store: no one should cache
        - max-age=60: browser TTL
        - s-max-age=300: CDN TTL
    - Invalidation (costly so TTL wisely): after `posting comments`, remove `GET comments`
    - Secrect Origin hdr: used by BE/API Gw to reject traffic that bypass CDN
 * DDOS, WAF 

### WAF
`WAF` (Web Application Firewall). Can be attached to CDN or API Gateway
Block suspicious requests detected by:
 * SQL injection patterns
 * `XSS` (Scross Site Scripting)
    - Stored XSS: js in db
    - Reflected XSS: https://example.com/search?q=<script>...</script> and server render `q` directly into HTML
    - DOM XSS: if dev do el.innerHTML = location.hash.slice(1) : the it could insert script from url
    - => 
        - esc/sanitize content
        - CSP (`Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'`): 
        - HttpOnly cookies: when `Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Lax`
            - `HttpOnly` = js cannot read this cookies
            - `Secure`: browser sends it through HTTPS 
            - => so no need Header: Authentication: Bearer <JWT>
 * Banned IPs/Bots

### API Gateway
Don't Expose BE directly.
BE hides in private network, only receive traffic from API Gateway
API Gateway offers:
 * HTTPS = HTTP + TLS (Transport Layer Security, encrypt data, modern protocol) > old SSL (secure socket layer) 
 * Handle JWT -> claims to BE
 * Rate limiting: 429 (too many requests) if full
   - Token Bucket: cap=10 tokens, refill=2/s (evry sec: add 2 tokens to No tokens left)
     - 4reqs => 6tokens left, 1s later=> refill so 8tokens left but never above 10
     - This allow bursts (API Gw send 10 requests at a time but still keep available tokens at 0, allowing cooldown). Token bucket always sends immdidately, not hold
   - Leaky Bucket: qCap=10, processRate=2/s => only if know stable rate.
     - Hold requests and send to BE at the processRate
   - Fixed Window: cap: 100 reqs/every min (eg: 10:00:00-10:00:59, reset at window end) => for evenly distributed
   - Sliding Window: cap: 100 reqs/last 60s => may require more computation
 * Route matching: for microsvc/seperate concerns
   * /comment/* => Comment BE => While BE determin which app func/svc
   * /entityX/* => EntityX BE
 * [Optional] API Contract (OpenAPI/JSON Schema) validation, BE still handle DTO+service call
 * Transformation: eg: "postContent" : {} become "postBody": {} => legacy, matching external, ...
 * Centralized logging: [requestID, method, route, status, errors, clientId]
 * API versioning: /v1 -> BE1, /v2 -> BE2

### Load balancer
 * distribute traffic btw healthy BE instances (GET /health/ready)
 * Table: [{ address:"10.0.1.10:8080", status:"healthy", weight:2, activeConnections:20, zone:"zone-a"}, ..]
 * activeConnections = how many clients connecting to a BE
 * add: autoscaler registers new instance => LB check & add to table
 * recover: bad instances receives traffic again if healthy again
 * Distributed Algos:
   - Round Robin: #1 -> #2 -> #1 -> ..
   - Least Connections: choose least buzy (lowest activeConns) instance
   - Weighted: strongers (cpu, mem, cap, type, load test) get more traffic.
   - Consistent Hashing: same keys reach same instances


### Database HA (High Availability)
`Primary` => (Replication) => `Standby`, if Primary failover, `Standby` becomes Primary 
* `HA manager`: auto monitor health, failover, promotion (=> BE points to new Primary w same DB hostname)
* `DBMS`: auto stream trans from `Prim` to `Read Replica`, handle `Backup` (scheduled snapshots, trans logs)

Replication choices:
* Sync: Prim waits Standby's confirm before commit succeeds: reliable but slow => for important only
* Async: Prim commits first, write to Standby later: fast but may lost data

Terms:
 * RPO (Recovery Point Objective): how old data in Standby allowed when getting promoted
 * RTO (Recovery Time Objective): max downtime, otherwise considered failover

### Event Broker (Kafka, RabbitMQ, AWS SNS + SQS.)
Instead of processing related logics, BE send `Event` (eg: `CommentCreated`) to event brokers and resp 201 immediately. Brokers queue and process afterward
 * Each broker has multiple topics, each topic has multiple queues, each queue has workers to process. Eg:
 * CommentCreated Topic:
   ├→ Noti Queue -> workers -> notify post author/replied users
   ├→ Feed/Fan-out Queue -> workers -> update follower feeds
   ├→ Cache Invalidation Queue -> workers -> del comment:post:123 + CDN API Purge: /posts/123/comments

 * Fan-out (distribute event to many affected users):
     -  Fan-out on write: author creates post, write post to all followers' feed => lot writes if many followers
     -  Fan-out on read: user open feed, read changes from that user followed => slow read if followed lots
     -  Hybrid: celeb -> on read, else, on write
 * Error Handling:
     - Pass -> ACK 
     - Fail -> Retry (w Idempotency) -> Fail again -> Dead-Letter Queue (DLQ).
     -  OutboxDB:
        - BE always saves a copy of `CommentCreated` msg to OutboxDB
        - So if msg cannot reach brokers (unvailable, BE error after commit, ...)
       => So later, Outbox worker schedually feeds msgs to Event Brokers to process

--------------------------------------------------------------------------------
## CORE CONCEPTS
### JWT (JSON Web Token)
  ```
	User logs in:
	=> Authentication server verifies the credentials.
	=> Authentication server creates the JWT.
	=> Authentication server signs it using its private key
  => Responds:
      Option 1: Bearer JWT => Client save for API request Header: Authentication: Bearer: <JWT>
      Option 2: `Set-Cookie: access_token=<JWT>; HttpOnly; Secure; SameSite=Lax; Path=/`
	      => Browsers saved (HttpOnly Cookies: js cannot read) and auto attach for API requests.	
	{
   		Header: { 
			alg: RS256, 
			kid: "keyId to find public key" 
		},		
   		Payload: { 
			sub: userId, // the subject
    	iss: auth.url.com, // trusted issuer issued the JWT
      aud: comment-api, // audience: api that will use this JWT
			scope: "comments:read comments:write",
			iat: issueAt
			exp: expAt
    	},
    	Signature: auth_srv_sign_w_private_key(base64url(header) . base64url(payload))
  	}

	Backend handle:	
	=> kid => find public key of the authentication server
	=> Confirm: allowed alg (not blindly accept)?
	=> Verify signature
	=> Confirm: iss?aud?exp?
	=> Create UserPrincipal from claims (payload: sub+scope)
	=> Check scope: comments:write?	
  ```

### Encoding:
  ```
	SHA-256: just to create a hash from a data
	RS256: Uses SHA-256 + RSA: Private key signs, Public key verifies  		
	HS256 = HMAC-SHA256 using same shared secret for signing + verification.
	=> RS256 is better when multiple APIs need to verify tokens without sharing the private key (which can be used to fake the signature).
  ```
  
### Input validation and authorization
  * Validation:
  	- 0 < Content len < limit
    - Post exists and accepts comments
    - sanitize: supported tags, spam/bad words
    - Use parameterized SQL
  * Authorization
    - JWT has comments:write
    - User can access this post
    - User is not banned, blocked or restricted
  
### Idempotency/retry handling
 * FE send same <client-generated-UUID> for same request/retry
   - (could use requestHash(key,payload) to make sure the idempotency key is used for this request)
 * BE save key into db with the comment:
   - Same key + Same Payload -> return original response
   - Same key + Diff Payload (diff hash) -> 409 Conflict

### Secrets management
 * Sensitive => secrets managers (AWS/Google SM, Azure Key Vault) => controled by IAM
   - DB_PASSWORD=<secret>
   - 3rd-party API Keys
   - ...	
 * Configurations => env vars
  
### Sensitive-data redaction
 * remove sensitive dat before send to monitoring tools (log, report): JWT, password, credit-card

--------------------------------------------------------------------------------
## OBSERVIBILITY
 * LOGS: wat happen (reqId,eventId,route,status,error,clientId)
 * METRICS: sys health
  - API: traffic, latency, error rates
  - BE: CPU, Mem, unhealthy instances
  - DB: connections, slow queries, replica lag (how old standby data vs primary)
  - Broker: queue depth, fail retries rate, DLQ size (permanent failed msg)
  - CDN: cache-hit rate
 * TRACE: full journey of one request across services using spans collected 
   * Span = (svc,start_time,duration,status/error,parent_span,route,DB op)
    Trace ID: abc123
      Gateway          span01: 20ms
      └─ Backend       span02: 30ms
        ├─ Database    span03: 90ms
        └─ Broker      span04: 50ms
            └─ Worker  span05: 180ms `<-- SLOW`
  
### IaC
.... PENDING



--------------------------------------------------------------------------------
## HTTP CODES
## 2xx Success Codes
* 200 OK: Success.
* 201 Created: Resource built.
* 204 No Content: Success, empty body.

## 4xx Client Errors
* 400 Bad Request: Syntax error.
* 401 Unauthorized: Authentication required.
* 403 Forbidden: Access denied.
* 404 Not Found: Missing resource.
* 405 Method Not Allowed: Unsupported verb.
* 429 Too Many Requests: Rate limited.

## 5xx Server Errors
* 500 Internal Error: Generic crash.
* 502 Bad Gateway: Proxy failure.
* 503 Service Unavailable: Temporary downtime.
* 504 Gateway Timeout: Network delay.

--------------------------------------------------------------------------------
# PRACTICE
https://leetcode.com/discuss/post/7075294/splunk-cisco-karat-3rd-party-software-en-3qfx/
https://leetcode.com/discuss/post/1982184/coinbase-sde2-phone-screen-karat-by-anon-9t60/
https://leetcode.com/discuss/post/1688427/indeed-karat-phone-interview-word-search-cs3m/

[v] https://leetcode.com/discuss/post/6671660/karat-round-by-anonymous_user-r4np/
[v] https://www.reddit.com/r/leetcode/comments/1fkf8wg/atlassian_senior_dev_karat_interview_experience/