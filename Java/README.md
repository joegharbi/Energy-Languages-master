# Java benchmarks

This folder contains Java implementations of the benchmark set and Java-specific automation.

## Contents

- Benchmark folders: `fannkuch-redux`, `fasta`, `mandelbrot`, `n-body`, `reverse-complement`
- `compile_all.py`: runs benchmark actions by scanning `Makefile`s
- `output.csv`: generated/historical measurement summary

## Notes

- Java source files include benchmark-game variants (for example `*.java-*` copies used by Makefiles).
- JSON files in benchmark folders are measurement exports and should be preserved.
- `.class` files are generated artifacts and are excluded by `.gitignore`.
