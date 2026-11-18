# dangai-edicao — skill do Claude Code para editar no Dangai

Ensina o Claude Code a editar shorts de recap de anime no [Dangai](https://github.com/faahpla/dangai):
gancho, ritmo, cenas por palavra, enquadramento 9:16 no rosto, legenda, música e conferência final.

## Instalar

```bash
git clone https://github.com/leviclementino1-creator/dangai-edicao-skill.git ~/.claude/skills/dangai-edicao
```

No Windows, a pasta é `%USERPROFILE%\.claude\skills\dangai-edicao`.

## Ligar o Dangai ao Claude

1. No Dangai (2.10.4 ou mais novo): Configurações > Módulos > ligue **Claude (MCP)**.
2. Na seção "Claude (MCP)", clique em **Copiar comando** e cole uma vez no terminal.
3. Abra uma conversa nova no Claude Code e peça: "edita esse recap no Dangai".

Na primeira vez a skill pergunta como você edita (Gerar recap ou editor normal), qual preset de
legenda usar, se usa suas cenas favoritas etc., e guarda em `perfil.local.md` (só no seu PC).
Em todo projeto novo ela pede: o anime/episódio, o roteiro e o áudio da narração.
