# Erlang benchmarks

This folder contains Erlang implementations of the benchmark set and Erlang-specific automation.

## Contents

- Benchmark folders: `fannkuch-redux`, `mandelbrot`, `n-body`, `reverse-complement`
- `compile_all.py`: runs benchmark actions by scanning `Makefile`s
- `average.py`: utility script for result aggregation
- CSV outputs (`Erlang.csv`, `avg26_23.csv`, `otp23vs26.csv`, `output.csv`)

## Notes

- Erlang benchmark sources are maintained through `*.hipe` files copied by Makefiles.
- JSON files in benchmark folders are measurement exports and are kept for reproducibility.
- Generated `.beam` and temporary `.erl` build files are ignored by `.gitignore`.
