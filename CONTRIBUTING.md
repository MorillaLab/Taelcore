# Contributing to TaelCore

TaelCore is a published, pip-installable library — contributions that improve usability, add benchmarks, or extend the topological enrichment are very welcome!

## 🐛 Reporting Bugs

Open a [GitHub Issue](https://github.com/MorillaLab/Taelcore/issues) with:
- A minimal reproducible example
- Your environment (OS, Python version, PyTorch version, giotto-tda version)
- The full error traceback

## 💡 Suggesting Features

Open an issue tagged `enhancement`. For new TDA features or alternative linear combination strategies, please include a brief scientific justification.

## 🔧 Submitting Code

1. Fork the repo and create a branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install flake8 pytest
   ```
3. Make your changes in `Taelcore/` (core library) or add experiments in the appropriate notebook folder.
4. Run linting:
   ```bash
   flake8 Taelcore/ --max-line-length=127
   ```
5. Clear notebook outputs before committing.
6. Open a pull request against `main`.

## 📦 PyPI / Package Changes

If your contribution affects the installed package behaviour, please also update `Pip/taelcore/` and bump the version in `setup.py` following [semantic versioning](https://semver.org/).

## 📜 License

By contributing, you agree your work will be released under GPL-3.0.
