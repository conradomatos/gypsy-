# Governança e fonte de verdade

- `docs/INDEX.md` define o documento canônico por assunto. Consulte antes de
  assumir qualquer documento como vigente.
- `registro_de_decisoes.md` prevalece sobre documentação antiga: uma decisão
  registrada mais recente vence um doc canônico ainda não atualizado.
- Documentos em `_historico/` ou marcados REVOGADO/HISTÓRICO **não orientam
  implementação** — existem só para auditoria.
- **Não inventar** regra de negócio, arquitetura, nome de tabela/campo, fórmula
  ou fluxo.
- Ao encontrar contradição entre documentos:
  1. pare;
  2. identifique os documentos envolvidos (caminho exato);
  3. explique o conflito;
  4. peça decisão ao Conrado. Não escolha sozinho.

## Ordem de precedência documental (autoridade)
1. Decisões registradas (`registro_de_decisoes.md`)
2. `docs/INDEX.md` (roteador do canônico)
3. Documento canônico específico do assunto
4. `CLAUDE.md` da raiz
5. `.claude/rules/`
6. Spec da feature
7. Plano da tarefa

Nota operacional: `CLAUDE.md` e `.claude/rules/` são carregados automaticamente
em toda sessão; os docs canônicos são lidos sob demanda. As rules são roteadores
curtos — se uma rule contradisser o `registro_de_decisoes` ou o doc canônico, o
documento vence e a rule deve ser corrigida.
