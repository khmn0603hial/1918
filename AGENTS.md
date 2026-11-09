# Development instructions

- This repository starts from the user's V17.7 game baseline.
- Edit `index.html` and tracked assets for future game changes. Older numbered HTML/ZIP files elsewhere in the workspace are historical snapshots, not the development source.
- Keep the seven main battlefields and the operations/outer-sector rules unless the user requests changes.
- Do not add build outputs, browser profiles, downloaded sound archives, credentials, or old HTML snapshots to Git.
- Run `node tools/check.cjs` after JavaScript edits and `python tools/build.py` before providing a standalone HTML.
- Keep `VERSION` and `CHANGELOG.md` aligned with delivered game updates.
- Preserve third-party source and license notes when changing assets.
- The baseline check `python tools/build.py --verify-baseline` is only expected to pass for the original V17.7 source; later intentional game edits change its hash.
