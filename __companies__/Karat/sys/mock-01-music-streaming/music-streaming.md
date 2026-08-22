Songs => blob servers. Problems?

1. AVAILABILITY: 1 song/server => dies => inaccess
   Fix: REDUNDANCY: replicate ea song across servers (eg: 3 replicas)
   How: ROUTING: metadata DB records their locations (ideally: diff zones (data centers))

2. HOT PARTITION: popular songs => more traffic => server overload
   Fix: More replicas

3. GEO-LATENCY: users far from servers => delay
   Fix: Cache on CDN edge servers near users (prioritize popular songs)