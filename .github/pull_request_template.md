<!-- Commits e textos em PT-BR. -->

## O quê
<!-- Descreva a mudança em uma ou duas frases. -->

## Contexto / SP
<!-- SP / módulo / feature / tarefa ativos. Link para spec ou decisão registrada. -->

## Como testar / Evidência
<!-- Comandos executados e resultados. Enquanto não há scaffold, não invente comandos. -->

## Checklist
- [ ] Segue a fonte de verdade (INDEX + registro_de_decisoes); sem divergir sem decisão registrada
- [ ] Sem segredo/token hardcoded; sem `any`/`@ts-ignore`
- [ ] Regra de negócio fora de view/serializer/componente; `Decimal` p/ dinheiro (se aplicável)
- [ ] Teste cobrindo a regra (se há código); golden test não regride (se aplicável)
- [ ] `git diff` revisado; base checada contra trabalho paralelo
