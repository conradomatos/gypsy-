# Git, segurança e comunicação

## Git e segurança
- Trabalhar em branch. Mostrar `git diff` antes de commit.
- Commit somente com autorização; push somente com autorização.
- Nunca force push. Nunca alterar `main` diretamente.
- Nunca remover bloqueios/denys globais para facilitar uma tarefa.
- Não ler nem expor `.env` e segredos.
- Não apagar arquivos ou histórico sem autorização.

## Comunicação e evidência
Ao finalizar uma tarefa, informar:
- SP, módulo, feature e tarefa;
- arquivos lidos, alterados e criados;
- decisões tomadas e decisões pendentes;
- testes executados e comandos executados;
- `git status`;
- riscos e limitações.

Diferenciar sempre: **fato encontrado · inferência · recomendação · decisão
aprovada**. Evidência antes de afirmar "pronto/passa/corrigido".
