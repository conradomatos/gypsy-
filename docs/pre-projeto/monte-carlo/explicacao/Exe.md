---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, pre-projeto, monte-carlo]
---


1. **Primeiro** roda o dashboard pra configurar os cenários e exportar o JSON
2. **Depois** abre o Claude Code pra analisar

Passo a passo:

**Agora:** Abre o terminal (PowerShell), navega pra pasta e roda o dashboard:

```
cd "D:\00 - CLAUDE_CODE\Monte_Carlo"
python dashboard.py
```

Configura os parâmetros nas duas abas como quiser, e clica **"EXPORTAR JSON P/ CLAUDE"** no canto superior direito. Isso cria o `monte_carlo_resultado.json` na pasta.

**Depois:** Fecha o dashboard. Duplo-clique no **"Abrir Claude Code.bat"**. Quando abrir, diz:

```
Leia o monte_carlo_resultado.json e execute as 5 tarefas do CLAUDE.md
```

Ele já sabe o que fazer porque leu o CLAUDE.md.