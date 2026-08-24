188,888 vendor machines connect 1 server at mid night

1. AVAILABLITY: single failure point: regional replicas, LB, autoscale

2. SERVER/DB OVERLOAD (thundering herd): 
	=> client: spread report windows evently or random
	=> server: rate limit + queue

3. RELIABILITY: 
   - cellular net/machine crash issue: local store, retry (idempotency) w backoff
   - send critical issue immediately 