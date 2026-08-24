Songs => 1 blob server. Problems?

1. AVAILABILITY: 1 song/server => dies => inaccess
   Fix: REDUNDANCY: replicate ea song across servers (eg: 3 replicas), (ideally: diff zones (data centers))
   How: ROUTING: metadata DB records their locations

2. HOT PARTITION: popular songs => server overload: More replicas

3. GEO-LATENCY => CDN (prioritize popular songs)