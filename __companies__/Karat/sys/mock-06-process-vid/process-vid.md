process > 10vid => crash + affect other processes. Temp solutions?

1. RATE LIMTER: create max 10 vid threads; above wait in Q
2. ISOLATION: seprate instances/machine, cap cpu/mem
3. RETRY: persist job state to retry (idempotency) + resume where left
