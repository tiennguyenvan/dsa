Songs => 1 blob server. Problems?

1. AVAILABILITY: 1 song/server => dies => inaccess
   Fix: REDUNDANCY: replicate ea song across servers (eg: 3 replicas), (ideally: diff zones (data centers))
   How: ROUTING: metadata DB records their locations

2. HOT PARTITION: popular songs => more traffic => server overload
   Fix: More replicas

3. GEO-LATENCY: users far from servers => delay
   Fix: Cache on CDN edge servers near users (prioritize popular songs)