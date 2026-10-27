# Demo: cleanup rules

**Framework:** none, plain Python. **Moving parts locally:** none.

`rules.py` holds one function, `decide()`, which picks an action for a resource: skip (keep tag), notify the owner, or snapshot then stop. It is a pure function, so you test it without any Azure account.

## Run it

```bash
cd app
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

```bash
pytest                    # 3 tests
python -c "from rules import decide; print(decide({'tags': {'owner': 'sam'}}))"   # notify_owner
```

## What is missing locally (added in the cloud work)

- Reading the daily cost export from Storage.
- The 7-day timer and the Teams notification.
- An Azure Function wrapper that calls `decide()` for each resource.

None of these change `decide()`; they feed it resources and act on its answer.
