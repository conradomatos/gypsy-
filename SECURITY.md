# Política de segurança — Gypsy

Repositório privado da Concept Engenharia.

## Segredos

- **Nunca** commitar token, chave, senha ou credencial. Usar `.env` (fora do git) ou o
  secret manager do provedor. Modelo em `.env.example`.
- `.env` e `.env.*` são ignorados pelo git (ver `.gitignore`); só `.env.example` versiona.
- Planilhas-fonte (`destilacao/fontes/`) são read-only e ficam fora do git.

## Se um segredo vazar no histórico

1. **Rotacionar** a credencial imediatamente no provedor (o valor exposto é comprometido,
   mesmo após remoção).
2. Remover do histórico (`git filter-repo` / BFG) e forçar atualização — combinar com o Conrado.
3. Registrar o incidente no `docs/LOG.md`.

## Reporte

Falha de segurança → contato direto com Conrado Matos (conrado@conceptengenharia.com.br).
Não abrir issue pública com detalhe explorável.
