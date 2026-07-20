#!/usr/bin/env python3
"""PreToolUse guard para `git push`.

Motivo: os padrões de permissão do Claude Code são prefix-globs, não regex —
`Bash(git push --force:*)` no deny NÃO pega `git push origin main --force`,
porque o git aceita flags em qualquer posição. Este hook faz parsing do argv
e bloqueia independentemente da ordem dos argumentos.

Bloqueia:
  - force push em qualquer forma (--force, -f, --force-with-lease[=...],
    --force-if-includes) e refspec com prefixo `+` (força implícita);
  - push em massa (--mirror, --all);
  - execução remota (--receive-pack=..., --exec=...);
  - push para `main` (a política do projeto é branch -> PR -> merge).

Analisa SOMENTE invocações reais de `git push`: corpos de heredoc são
descartados e o comando é quebrado em segmentos por ; && || | e quebra de
linha, para não confundir texto (ex.: uma mensagem de commit que cita
`git push --force`) com execução.

Saída: exit 0 libera (a decisão segue para o settings.json); exit 2 bloqueia
e mostra o motivo ao usuário e ao Claude.
"""
import json
import re
import shlex
import sys

FORCE_FLAGS = {"--force", "-f", "--force-with-lease", "--force-if-includes"}
BULK_FLAGS = {"--mirror", "--all"}
EXEC_PREFIXES = ("--receive-pack", "--exec")
PROTECTED = {"main", "refs/heads/main"}

HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1")
SEPARATORS = re.compile(r"&&|\|\||[;\n|]")


def strip_heredocs(command):
    """Remove o corpo de cada heredoc — é dado, não comando."""
    while True:
        m = HEREDOC.search(command)
        if not m:
            return command
        tag = m.group(2)
        rest = command[m.end():]
        end = re.search(rf"^\s*{re.escape(tag)}\s*$", rest, re.MULTILINE)
        cut = m.end() + (end.end() if end else len(rest))
        command = command[:m.start()] + " " + command[cut:]


def push_args(segment):
    """Devolve os argumentos se o segmento for uma invocação de `git push`."""
    try:
        tokens = shlex.split(segment)
    except ValueError:
        return None
    # descarta atribuições de ambiente à frente (VAR=x git push ...)
    while tokens and re.fullmatch(r"\w+=.*", tokens[0]):
        tokens.pop(0)
    if len(tokens) < 2:
        return None
    argv0 = tokens[0].replace("\\", "/").rsplit("/", 1)[-1]
    if argv0 not in ("git", "git.exe") or tokens[1] != "push":
        return None
    return tokens[2:]


def blocked_reason(args):
    for a in args:
        base = a.split("=", 1)[0]
        if base in FORCE_FLAGS:
            return f"force push bloqueado ({a}). Nunca reescreva historia publicada."
        if base in BULK_FLAGS:
            return f"push em massa bloqueado ({a})."
        if base.startswith(EXEC_PREFIXES):
            return f"execucao remota bloqueada ({a})."
        if a.startswith("+") and ":" in a:
            return f"refspec com '+' forca o push ({a}). Bloqueado."

    positional = [a for a in args if not a.startswith("-")]
    for a in positional[1:]:  # positional[0] e o remote
        if a.split(":")[-1] in PROTECTED:
            return (
                "push direto para 'main' bloqueado. "
                "Fluxo do projeto: branch -> PR -> merge."
            )
    return None


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    command = payload.get("tool_input", {}).get("command", "")
    if "push" not in command:
        sys.exit(0)

    for segment in SEPARATORS.split(strip_heredocs(command)):
        args = push_args(segment)
        if args is None:
            continue
        reason = blocked_reason(args)
        if reason:
            print(f"[guard-git-push] {reason}", file=sys.stderr)
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
