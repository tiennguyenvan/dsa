# Interview

| Time      | Section          | Focus                           |
| --------- | ---------------- | ------------------------------- |
| 0–2 min   | Introduction     | Language, format                |
| 2–20 min  | System knowledge | One broad request-flow scenario |
| 20–35 min | Coding problem 1 | Medium or below                 |
| 35–50 min | Coding problem 2 | Medium or below                 |

# System design

## Request flow
### DNS
Client <=> DNS: convert domain to ips -> real Cloudfront/API Gateway/BE Public addr
Client -> `POST /posts/{postId}/comments`

### CloudFront/CDN + DDoS protection

### API Gateway
Don't Expose BE directly.
BE hides in private network, only receive traffic from API Gateway
API Gateway offers:
 * HTTPS = HTML + TLS (Transport Layer Security, encrypt data) 
 * Handle JWT -> claims to BE
 * Rate limiting: 429 (too many requests) if full
   - Token Bucket: cap=10, refill=2/s => general
   - Leaky Bucket: qCap=10, processRate=2/s => only if know stable rate.
   - Fixed Window: cap: 100 reqs/every min (eg: 10:00:00-10:00:59, reset at window end) => for evenly distributed
   - Sliding Window: cap: 100 reqs/last 60s => may require more computation
 * Route matching: for microsvc/seperate concerns
   * /comment/* => Comment BE => While BE determin which app func/svc
   * /entityX/* => EntityX BE
 * [Optional] API Contract (OpenAPI/JSON Schema) validation, BE still handle DTO+service call
 * Transformation: eg: "postContent" : {} become "postBody": {} => legacy, matching external, ...
 * WAF (Web Application Firewall):  Block suspicious requests by rules:
   - SQL injection patterns
   - X-Site scripting
   - Banned IPs/Bots
   - Centralized logging: [requestID, method, route, status, errors, clientId]
   - API versioning: /v1 -> BE1, /v2 -> BE2

### Load balancer
 * distribute traffic btw healthy BE instances (GET /health/ready)
 * Table: [{ address:"10.0.1.10:8080", status:"healthy", weight:2, activeConnections:20, zone:"zone-a"}, ..]
 * add: autoscaler register new instance, LB check & add to table
 * recover: bad instances receives traffic again if healthy again
 * Distributed Algos:
   - Round Robin: #1 -> #2 -> #1 -> ..
   - Least Connections: choose least buzy (lowest activeConns) instance
   - Weighted: strongers (cpu, mem, cap, type, load test) get more traffic.
   - Consistent Hashing: same keys reach same instances

### IaC
	Backend instance
### Application layer
### Database write
### Publish event/queue
### Response -> 201 Created
### Async: follower fan-out + cache invalidation

## Core concerns
### JWT (JSON Web Token)
  ```
	User logs in:
	=> Authentication server verifies the credentials.
	=> Authentication server creates the JWT.
	=> Authentication server signs it using its private key.
	=> Frontend receives and stores the JWT for API requests.	
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
	=> RS256 is better when multiple APIs need to verify tokens without receiving the private key.
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
   - Same key + Diff Payload -> 409 Conflict

### Secrets management
 * Sensitive => secrets managers (AWS/Google SM, Azure Key Vault) => controled by IAM
   - DB_PASSWORD=<secret>
   - 3rd-party API Keys
   - ...	
 * Configurations => env vars
  
### Sensitive-data redaction
 * remove sensitive dat before send to monitoring tools (log, report): JWT, password, credit-card

## Caching
  * `POST` is normally not cached
  * Update/invalidate cached reads afterward
  * Logging, metrics and tracing


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
