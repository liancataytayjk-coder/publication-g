# Presidents and the Philippine economy

*Good policy or good luck? Philippine economic performance across presidential
administrations, 1961–2026.* A replication of Blinder and Watson (2016,
*American Economic Review*) on Philippine data.

Status: complete draft. Data, replication gate (passed), estimation, figures and the journal manuscript are done. Rebuild everything with `./run_all.sh`. What remains for the author is in `paper/SUBMISSION_CHECKLIST.md`.

| File | What it is |
| --- | --- |
| `CLAUDE.md` | Project brief: questions, hypotheses, reference specification, decisions log, pre-registered replication gate, open questions |
| `docs/feasibility_note.md` | What can and cannot be done, and with what data |
| `data/manual/administrations.csv` | Presidents' term dates, with source |
| `data/raw/source_log.md` | One row per raw data file |
| `replication/blinder_watson2016_targets.csv` | The reference paper's numbers the replication must hit |
| `paper/manuscript.docx`, `.pdf` | The manuscript for the *Asian Economic Journal*, in the house style (rendered; edit `paper/manuscript_template.md`) |
| `docs/statistical_annex.docx` | Every generated table |
| `paper/SUBMISSION_CHECKLIST.md` | What remains before submission |
| `scripts/09_replication_package.py` | Builds the Zenodo replication package in `deliverables/` (`.zenodo.json`, `CITATION.cff` hold its metadata) |
| `docs/session_handoff.Rmd` | How to resume in a new session |
| `output/tables/`, `output/figures/` | All estimates and figures, written by scripts |
| `paper/references.bib` | References, each checked on Crossref |
| `scripts/` | Helper scripts (Crossref check, figure style, document rendering) |

`./run_all.sh` rebuilds everything from `data/raw/`, including the styled
documents and their PDFs (the PDF step needs LibreOffice with its Math module).
