ML Inference Svc for Sport News App. Ana for scaling needs for next year?

=> for user recommendation

1. TRAFFIC GROWTH
	- user growth, reqs/s => more instances + compute cap
	- peak traffic by events/seasons => concurr usrs => auto scale + padding

2. ML INFERENCE
	- resp latency, predicts/s/instance, cpu/gpu/mem used
	=> +resources, model optimize/batch(multi reqs a time), more instances

3. DATA GROWTH/TRAINING GROWTH
	- size, train freq/time take (hourly train but take 2h to train)
	=> +storage/cpu/gpu, reduce train freq
	=> distributed train (split across instances)
	=> incremental train (on new data only)

4. RELIABILITY
	- downtime/latency, error rate, instance health (cpu,mem,netconn)
	=> diff zone distribute, LB, retry, fallback to cached or general feed