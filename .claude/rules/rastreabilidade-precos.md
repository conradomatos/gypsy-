> **RASCUNHO** (Claude, 2026-07-19) — proposta a partir das decisões da sessão.
> A versão final destas regras será escrita pelo Conrado.

# Rastreabilidade de preços

Todo número tem fonte. Preço, HH unitário e coeficiente de composição carregam:

- **fonte** (HOLLOS, MURILO, SINAPI, cotação, manual)
- **data-base** do valor
- **flag de imposto** (com/sem) quando aplicável

Herdado da destilação (Spec 0): as colunas `_fonte`, `_aba_origem`, `_linha_origem`,
`_confianca` das planilhas EXTRACAO_*.xlsx alimentam esses campos no seed.

Nunca preencher com estimativa um dado que não existe na fonte — campo vazio é
informação; número inventado é bug.
