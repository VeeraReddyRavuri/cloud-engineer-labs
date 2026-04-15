## ALB Components:
### Listener:
    - Watches incoming requests on a specific port
### Rule:
    - logic attached to a listener that decides where (Target group) to send the incoming traffic
### Target Group:
    - Its a collection of destinations that recieve traffic

2. With these health check settings — interval: 20s, unhealthy threshold: 4, timeout: 3s — how long before a failing target is marked unhealthy? 20 * 4 = 80 sec

3. Why does your pipeline wait before checking CloudWatch alarms after deploy? Because it must account to the health check time which gives ALB time to check if the Target group is healthy or not becuase until then it shows healthy

4. In your blue/green setup — which AWS component do you change to shift traffic from Blue to Green? weight of the target group on the listener rule