# Submission checklist

What remains before the manuscript can be submitted. The manuscript is
`paper/manuscript.docx`, rendered from `paper/manuscript_template.md` by
`scripts/08_paper.py`; edit the template, never the rendered file.

## For the author to supply or decide

- [ ] **Author block:** name, affiliation, email (placeholders `[Author name]`,
      `[Affiliation]`, `[email]` in the template's front matter).
- [ ] **Target journal:** candidates are *The Philippine Review of Economics*,
      *Asian Economic Journal* and *Journal of Asian Economics*. Once chosen, apply
      its format (word limit, abstract length, reference style, title page, blind
      review copy). The draft is about 5,000 words of text plus 8 tables and 6
      figures (about 15 pages in the preview).
- [ ] **Use-of-AI statement:** the Declarations contain a bracketed draft; check
      the chosen journal's policy and finalize the wording.
- [ ] **Repository URL** in the data and code statement (`[repository URL to be
      inserted]`). If the repository stays private, deposit a replication package
      (for example on Zenodo or openICPSR) and cite it.
- [ ] **Term dates:** spot-check `data/manual/administrations.csv` against the
      Official Gazette (it was not reachable from the computing environment).
- [ ] **Cover letter** (not yet drafted).

## References

- [x] Every reference in `paper/references.bib` was checked on Crossref on
      2026-10-16, except the one below.
- [ ] `census2017x13` (X-13ARIMA-SEATS reference manual) is a software manual with
      no DOI; confirm the year against the manual in the program archive.
- [ ] Newey and West (1987): Crossref gives only the first page (703); confirm the
      last page (708) against the journal.
- [ ] Optional: check the published AER version of Blinder and Watson (2016)
      against the NBER working paper (2014) used for the targets; if any target
      changed, update `replication/blinder_watson2016_targets.csv`, rerun
      `./run_all.sh` and log the change.

## Already done

- [x] Replication gate passed (Table 1); pre-registered plan committed before the
      first Philippine estimate (git commit `5d860df`).
- [x] Every number in the text and tables comes from `output/tables/` through
      `output/tables/paper_numbers.json`.
- [x] Figures are black and white, without titles, in PNG, TIFF and PDF
      (`output/figures/`).
- [x] Fragile results are presented as fragile (the luck share S).
- [x] `./run_all.sh` rebuilds everything from `data/raw/`.
