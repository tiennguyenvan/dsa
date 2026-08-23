188,888 vendor machines connect 1 server at mid night

1. SERVER/DB OVERLOAD (thundering herd): 
	=> spread report windows evently or random
	=> buffer/queue

2. AVAILABLITY: single failure point: regional replicas, LB, autoscale

3. RELIABILITY: 
   - cellular net/machine crash issue: local store, retry (idempotency) w backoff
   - send critical issue immediately 