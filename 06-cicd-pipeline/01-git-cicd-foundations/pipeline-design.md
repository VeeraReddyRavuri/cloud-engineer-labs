What triggers your pipeline?
    A commit to the repo
What are the stages in order?
```

lint ──┐
       ├──→ build ──→ scan ──→ push ──→ deploy ──→ health check
test ──┘                                               │
                                              ┌────────┴────────┐
                                           pass ✓            fail ✗
                                              │                 │
                                           done            rollback

```
Where does CI end and CD begin?
    - CI ends when all checks are passed and a deployble artifact is produced
    - CD begins when the artifact is deployed to a running environment
Which part is GitOps (pull-based)?
    -  the GitOps part is specifically when your pipeline commits the new image tag to the manifest repo and stops. From that point the cluster agent (ArgoCD) pulls and applies. Not all of CD is GitOps.
What happens if the health check fails?
    - we trigger rollback to previous successful commit in the manifest repo