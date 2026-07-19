---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Deploy pipeline — Gypsy

## Fluxo do dia a dia (desenvolvimento)

```
1. git checkout -b claude/nome-do-modulo     ← cria branch
2. Claude Code edita arquivos locais         ← escreve engine + teste + hook + tela
3. npx vitest run                            ← roda testes no terminal (obrigatório)
4. npm run dev                               ← testa no browser localhost:5173
5. git add . && git commit                   ← commita local
6. git push origin claude/nome-do-modulo     ← sobe pro GitHub
7. PR no GitHub                              ← GitHub Actions roda testes
8. Merge na main                             ← só se CI verde
9. Coolify detecta push → build → deploy     ← automático
```

## Onde cada coisa vive

```
LOCAL (tua máquina):
  D:\00 - CLAUDE_CODE\01. PROJETOS\04-GYPSY\
    src/engines/           ← Code escreve aqui
    npx vitest run         ← testa aqui
    npm run dev            ← roda aqui, browser localhost:5173

GITHUB (remoto):
    git push               ← código sobe pra cá
    PR + GitHub Actions    ← CI roda testes automaticamente
    merge na main          ← só se testes passarem

VPS (produção):
    Coolify                ← detecta merge, faz build + deploy
    app.costai.com.br      ← usuário acessa aqui
```

## Diferenças do PWC

- Projeto Supabase SEPARADO (novo projeto, novo banco)
- Segundo app no Coolify (mesmo VPS 72.60.13.91)
- Repo GitHub separado (a definir nome)
- Domínio separado (a definir)

## Testes antes do merge

```
1. Vitest → rodar engines/__tests__/ (obrigatório)
2. Golden test → validar contra HOLLOS (obrigatório)
3. Build → vite build passa sem erro
4. Merge → só depois dos 3 acima
```

## Coolify

- Mesmo servidor do PWC
- Porta diferente
- Caddy roteia pelo domínio
- Env vars VITE_* via Dockerfile ARG (build time)