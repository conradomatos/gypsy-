# Subprojetos, hierarquia e gates

Hierarquia (níveis NÃO equivalentes):
Produto Gypsy → Subprojeto SP-xx → Módulo M-xxx → Feature F-xxx → Tarefa T-xxx.

## Isolamento
- Um SP por contexto. Não executar entregas de outro SP sem autorização.
- `/clear` ao trocar de SP.
- Informar sempre SP, módulo, feature e tarefa ativos.
- SP-00 Destilação tem `CLAUDE.md` próprio em `destilacao/` — segui-lo ao
  trabalhar nela.
- Trabalho preliminar num SP **não** significa gate aprovado.

## Gates e fluxo
- brainstorming antes da spec (quando necessário);
- spec antes da execução;
- protótipo validado (Claude Design) antes do frontend definitivo;
- aprovação humana em cada gate (Conrado; Sandro/Guilherme quando aplicável);
- não avançar automaticamente para o próximo SP;
- evidência obrigatória antes de declarar concluído (ver rule 07).

Mapa dos subprojetos: `docs/projeto-executivo/cigana/00_SUBPROJETOS.md`.
Fluxo detalhado: `.../01_arquitetura/pipeline_de_execucao.md`.
