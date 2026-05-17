# analysis outputs

This folder contains repository-level CSV datasets used by post-processing scripts.

## Main files

- `data.csv`: raw merged benchmark measurements used as input for analysis scripts
- `norm_by_function_and_c.csv`: normalized values per function against C
- `nrom_by_c.csv`: normalized language-level values against C (kept with original filename for backward compatibility)
- `normalized_mean.csv`, `ratio.csv`, `ration.csv`, `ration1.csv`: historical derived tables

## Generation

- `norm.py`, `norm2.py`, and `ration.py` read/write files in this folder.
- Some files are historical snapshots; keep them unless intentionally replaced during analysis refresh.
