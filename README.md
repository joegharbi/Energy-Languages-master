# Energy-Languages research repository

This repository contains benchmark implementations and measurement outputs used in energy-efficiency experiments across C, Erlang, Go, and Java.

## Repository layout

- `C/`, `Erlang/`, `Go/`, `Java/`  
  Benchmark implementations and per-language automation scripts (`compile_all.py` + benchmark `Makefile`s).
- `results/analysis/`  
  Aggregated CSV datasets and derived analysis tables used for reporting.
- `old_measurements/`  
  Historical measurement exports kept for traceability.
- Root scripts (`compile_all.py`, `norm.py`, `norm2.py`, `ration.py`, `gen-input.sh`)  
  Utilities for orchestration, post-processing, and benchmark input generation.

## Reproducibility notes

- Benchmark `Makefile`s are Windows-oriented (`cmd`, `timeout`, `taskkill`, `copy`, `del`) and designed for Scaphandre-based energy capture.
- Input files expected by some benchmarks are generated with `gen-input.sh`.
- Language folders include benchmark JSON exports produced during measurements.
- Historical and published CSV outputs are preserved; generated binaries/caches are ignored through `.gitignore`.

## Important references

- Computer Language Benchmark Game: https://benchmarksgame-team.pages.debian.net/benchmarksgame/
- Scaphandre documentation: https://hubblo-org.github.io/scaphandre-documentation/
- Windows RAPL driver: https://github.com/hubblo-org/windows-rapl-driver
