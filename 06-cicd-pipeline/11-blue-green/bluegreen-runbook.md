Pre-switch checklist — what must be true before switching ALB to Green
    - The Green env should pass all the health checks not just shallow but all the endpoints or paths need to be covered
Switch procedure — exact sequence of steps
    - Green env is provisioned with new instances launched and new image deployed
    - Green's health checks should pass
    - ALB confirms all the targets of Green return healthy
    - ALB weights updated --> blue to 0 and Green to 100
    - In-flight requests are completed on blue, connection draining happens
    - Blue is idle and ready for rollback
Monitoring window — what you check and for how long
    - Check if any new problems trigger that are not found during health checks, which can be checked for a period of 15 to 30min before terminating Blue env
Rollback procedure — exact sequence if alarms fire
    - ALB switches to green
    - wait for time required for ALB's health check threshold
    - Query CoudWatch for error rate alam status (CloudWatch alarm on 5xx error rate exceeding threshold
CloudWatch alarm on response latency exceeding threshold
ALB access logs showing error patterns)
        - if Alram found:
            - Roll back to blue
            - Revert manifest repo commit
            - Page on-call
        - In no alarm:
            - continue monitoring for some more time
            - Query cloudwatch again after few mins
                - if all clear:
                    - Terminate blue env
                - else:
                    - follow if no alarm step from above
Post-deploy cleanup — what happens after successful Green validation
We terminate blue env