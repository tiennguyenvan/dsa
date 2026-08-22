Mobile Media (aud/vid/img) => ONLINE(Servers) vs OFFLINE (Device) storing. Trade-offs?

1. LATENCY/AVAIL
	- Online: Network issue => delay, unavail
	- Offline: instant, always avail

2. APP SIZE/DEVICE STORAGE
	- Online: smaller app
	- Offline: larger => slow installation, limit by device storage

3. CONTENT UPDATES
	- Online: any time, instant
	- Offline: resubmit + review => delay

4. SERVER COST
	- Online: BE, CDN, bandwidth
	- Offline: zero

5. USER COST
   - Online: consume user data + battery
   - Offline: no user data + battery for downloading

=> Hybrid: 
	- large/update frequently => Online
	- essential/small/static => Offline
