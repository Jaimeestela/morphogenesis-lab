# Experiment prompt template (GPT)

## Template

```
Experiment: [name, e.g. Gray-Scott 2D with parameters X]
Objective: [what to validate or produce]
Parameters:
  - [param1]: value
  - [param2]: value
  - seed: [integer or "random"]
Expected outputs:
  - [relative path, e.g. data/outputs/patterns/gs_snapshot_001.png]
Success criteria:
  - [e.g. no NaNs, stable pattern, DXF with N layers]
```

## Example

```
Experiment: Gray-Scott 2D spots
Objective: Generate a stable spot pattern and save snapshots.
Parameters:
  - F: 0.03
  - k: 0.062
  - Du, Dv: 0.0002, 0.0001
  - nx, ny: 256, 256
  - steps: 10000
  - seed: 42
Expected outputs:
  - data/outputs/patterns/gs_u_*.png, gs_v_*.png
Success criteria:
  - max(u), max(v) finite; visual spot pattern.
```
