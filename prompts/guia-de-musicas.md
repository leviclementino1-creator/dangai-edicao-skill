# Prompt: montar (ou melhorar) o seu guia de músicas

Cole isto no seu Claude Code (com a skill `dangai-edicao` instalada) e troque o que está entre `< >`.

---

Quero montar o meu guia de músicas para a skill dangai-edicao, do jeito que o guia do Levi está na
seção 4 ("MÚSICA — como escolher"). Minhas músicas ficam em: `<C:\caminho\da\pasta\de\musicas>`.

1. Liste todas as músicas da pasta (e subpastas).
2. Para cada uma, meça a onda (RMS de 0,2 s com o ffmpeg) e me diga onde ela "entra com tudo"
   (o drop: o primeiro bumbo/grave forte depois de uma subida) e onde é calma.
3. Me pergunte, uma de cada vez ou em grupos de até 4, como eu uso cada música:
   - em que clima (ação/progressão, épico, emocional/triste, romance, suspense, comédia/slice of life,
     curiosidade neutra);
   - se é de gancho, de pós-gancho, de meio do vídeo ou do vídeo todo;
   - se é específica de um anime ou de um tipo de vídeo (e onde NUNCA usar);
   - em que segundo eu gosto de entrar nela;
   - se combino duas (como a Montagem Batchi: a slowed no gancho e a instrumental na virada, no corte exato).
4. Grave tudo em `guia-de-musicas.local.md` na pasta da skill, numa tabela igual à do Levi:
   `música (arquivo) | pasta | quando usar | onde entrar`, mais um resumo por clima no fim.
5. Me mostre o guia pronto para eu corrigir.

Regras que valem sempre: a música do gancho entra audível desde o 0 s (sem ducking, sem fade longo),
o drop cai no fim do riser da saída do gancho, troca de música só quando o clima muda (com sharp riser +
impacto no corte), volume ~−26 LUFS no mix, e nunca som de sino como impacto.

---

Para **melhorar** um guia que já existe: "Abra o meu `guia-de-musicas.local.md`, ouça de novo a onda das
músicas que não têm 'onde entrar' e me pergunte o que falta. Depois do próximo vídeo, compare a música
que você escolheu com a que eu deixei/troquei e anote no guia o que aprendeu."
