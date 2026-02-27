---
name: Bug report
about: Report a bug in TaelCore
title: '[BUG] '
labels: bug
assignees: ''
---

## Describe the bug
A clear and concise description of what the bug is.

## Minimal reproducible example
```python
from taelcore import Taelcore
import numpy as np

X = np.random.rand(100, 50)
model = Taelcore(latent_dim=8)
model.fit(X)  # ← error happens here
```

## Error traceback
```
Paste full traceback here
```

## Environment
- OS: [e.g. Ubuntu 22.04]
- Python version: [e.g. 3.9.12]
- TaelCore version: [e.g. 1.3.1] (`pip show taelcore`)
- PyTorch version: [e.g. 1.13.0]
- giotto-tda version: [e.g. 0.5.1]

## Additional context
Any other context about the problem.
