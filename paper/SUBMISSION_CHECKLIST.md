# Submission checklist

What remains before the manuscript can be submitted. The manuscript is
`paper/manuscript.docx`, rendered from `paper/manuscript_template.md` by
`scripts/08_paper.py`; edit the template, never the rendered file.

## For the author to supply or decide

- [x] **Author block:** Lian Cataytay, University of Southeastern Philippines,
      lrcataytay00745@usep.edu.ph (title page, with the affiliation in a footnote).
- [x] **Target journal:** *Asian Economic Journal*.
- [x] **Template:** the house style is the template for now (author's decision,
      2026-10-16). The AEJ author guide could not be opened from the computing
      environment (403); if its rules are supplied later we will apply them. The
      manuscript uses the house style
      (Times New Roman 12, double-spaced, 1-inch margins, author–date references,
      tables and figures one per page at the end): 26 pages, about 2,900 words of
      main text, a 233-word abstract, 8 tables and 6 figures.
- [ ] **Anonymous copy:** if AEJ uses anonymous review, we will produce a copy
      without the author block and with self-identifying text removed.
- [x] **Use-of-AI statement:** approved by the author (2026-10-16).
- [x] **Replication package built and tested:** `deliverables/phl-presidents-growth-replication.zip`
      (built by `scripts/09_replication_package.py`; a clean unzip, install and
      `./run_all.sh` reproduces every table, figure and number byte for byte).
- [ ] **Deposit on Zenodo** (author, with her own account): upload the zip at
      zenodo.org → New upload; the metadata (title, author, affiliation, keywords,
      licence CC BY 4.0, link to Blinder and Watson 2016) are in `.zenodo.json`.
      Check the licence choice and the third-party data terms listed in the
      package README before publishing. Then send us the DOI: it goes into the
      Declarations (`doi:[to be inserted on deposit]`) and the package is rebuilt.
- [ ] **Term dates:** spot-check `data/manual/administrations.csv` against the
      Official Gazette (it was not reachable from the computing environment).
- [ ] **Cover letter:** not needed for now (author's decision).

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
      (`output/figures/`), set in Times New Roman.
- [x] House style applied and checked (`check_style.py`: OK). The PDF was made
      with Liberation Serif, which has the same letter widths as Times New Roman;
      exporting the .docx from Word gives true Times New Roman.
- [x] Fragile results are presented as fragile (the luck share S).
- [x] `./run_all.sh` rebuilds everything from `data/raw/`.
