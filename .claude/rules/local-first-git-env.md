# Local-first, git e segredos

1. **Local-first.** Postgres via Docker, app roda na máquina do Conrado até validação
   com Sandro/Guilherme. Deploy (VPS/Coolify) só depois do golden test passar.
   Local ≠ mock: banco de verdade, API de verdade desde o início.

2. **Git normal.** Branch → PR → merge. Merge só com gates verdes (testes/lint) e
   depois de checar trabalho paralelo na base (`git fetch` + comparar).

3. **Segredos em `.env`** (no `.gitignore`), nunca hardcoded. `.env.example` versionado.

4. **Planilhas-fonte não versionam** (estão no `.gitignore`). Ficam em
   `../01_DESTILACAO/fontes/` — read-only, nunca modificar.
