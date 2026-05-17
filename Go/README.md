# Go benchmarks

This folder contains Go implementations of the benchmark set and Go-specific automation.

## Contents

- Benchmark folders: `fannkuch-redux`, `fasta`, `mandelbrot`, `n-body`, `reverse-complement`
- `compile_all.py`: runs benchmark actions by scanning `Makefile`s
- CSV outputs (`Go.csv`, `output.csv`): historical/generated measurement summaries

## Notes

- Go source files include benchmark-game variants (for example `*.go-*`).
- JSON files in benchmark folders are measurement exports and are retained for reproducibility.
- `output.csv` is generated during measurements and intentionally kept as experiment history.
