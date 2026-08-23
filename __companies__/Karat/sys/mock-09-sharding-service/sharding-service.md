shard photos by username a-z. Problems?

1. UNEVEN DIS+CHANGES: large users, popuplar name, change username => by photoid
2. HOT PARTITION: CDN, replica
3. SCALING: add/remove servers require lots of changes 
   => hash range `A:20->B:60->C:90 => #id=50->B` => update affected ranges only
   !even range => map range (virtual shard)