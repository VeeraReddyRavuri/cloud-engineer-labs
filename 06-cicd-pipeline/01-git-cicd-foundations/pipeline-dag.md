```

lint ──┐
       ├──→ build ──→ scan ──→ push ──→ deploy ──→ health check
test ──┘                                               │
                                              ┌────────┴────────┐
                                           pass ✓            fail ✗
                                              │                 │
                                           done            rollback

```