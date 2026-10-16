# Presidents and the Philippine economy

*Good policy or good luck? Philippine economic performance across presidential
administrations, 1961–2026.* A replication of Blinder and Watson (2016,
*American Economic Review*) on Philippine data.

Status: Phase 1 (research design) complete. No Philippine estimates yet.

| File | What it is |
| --- | --- |
| `CLAUDE.md` | Project brief: questions, hypotheses, reference specification, decisions log, pre-registered replication gate, open questions |
| `docs/feasibility_note.md` | What can and cannot be done, and with what data |
| `data/manual/administrations.csv` | Presidents' term dates, with source |
| `data/raw/source_log.md` | One row per raw data file |
| `replication/blinder_watson2016_targets.csv` | The reference paper's numbers the replication must hit |
| `paper/references.bib` | References, each checked on Crossref |
| `scripts/` | Helper scripts (Crossref check, figure style, document rendering) |

The full pipeline (`run_all.sh`) will rebuild everything from `data/raw/` once
Phases 2 and 3 are in place.
