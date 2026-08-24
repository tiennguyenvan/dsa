1. **Single Points of Failure**

   * WAF
   * Database
   * Message queue
   * API Handler
   * SMS Gateway
   * Third-party Lock API

2. **Scalability and Bottlenecks**

   * One shared database
   * WAF bottleneck
   * Database connection exhaustion
   * Uneven load across LBs/servers
   * No caching
   * Queue backlog
   * No autoscaling shown

3. **Data Consistency**

   * Database update succeeds but queue publish fails
   * Queue publish succeeds but database update fails
   * SMS succeeds but lock action fails
   * Duplicate or out-of-order processing

4. **Message Queue Reliability**

   * Lost messages
   * Duplicate messages
   * Out-of-order messages
   * Poison messages
   * Unlimited backlog
   * No retry/failure handling shown

5. **Third-Party Dependencies**

   * Outages
   * Slow responses
   * Rate limits
   * Timeouts
   * Partial failure between SMS and Lock APIs

6. **Observability**

   * Only S6 connects to logging
   * No centralized logs
   * No metrics, tracing, alerting
   * Cannot trace one request end-to-end

7. **Availability and Recovery**

   * No database failover
   * No backup/disaster recovery shown
   * No regional redundancy
   * No network-partition handling
   * No health-check/failover behavior shown

8. **Security**

   * No authentication/authorization shown
   * No service-to-service authentication
   * No encryption boundaries shown
   * No secret/API-key management
   * Replay attacks
   * No audit trail for lock actions
   * No tenant isolation

9. **Compatibility**

   * No request/message schema versioning shown
