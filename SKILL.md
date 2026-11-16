---
name: dangai-edicao
description: Editar um short de recap de anime no Dangai do Levi do começo ao fim, como se fosse ele — cortar o episódio no Gerar recap, roteiro, voz, escolher as cenas (ritmo, gancho, coerência), abrir no editor com a Edição rápida e ajustar enquadramento, ponto de entrada, câmera, legenda e som. Também cobre como controlar o Dangai instalado ou o de dev (CDP), o formato do .dangai e do rascunho, as medidas offline (rosto, corte) e as armadilhas já vistas. Use em QUALQUER pedido de "edita no Dangai", "faz o processo todo", "compara com a sugestão do app", "ajusta enquadramento/legenda/cenas do projeto", ou para entender por que a Edição rápida errou.
---

# Editar no Dangai (o fluxo do Levi)

Dangai = Electron + Remotion, repo `faahpla/dangai` (clone em `G:\ClaudeEditor\dangai`).
`modulos/recap` e `modulos/thumb` são do Levi; o resto (núcleo) é do Faah — mudança no
núcleo entra pequena, um assunto por commit, e o Levi avisa o Faah. Responder ao Levi em
português, curto e simples.

## 0. Regras antes de tudo

- **O roteiro é a fonte da verdade**; o áudio só dá os tempos.
- Biblioteca e projetos reais do Levi: **só leitura**, salvo pedido explícito. Apagar = Lixeira
  (nunca de vez). Recortar um episódio muda os ids das cenas (ver Armadilhas).
- Nada pago sem confirmar. Nunca imprimir/copiar chave de API (não dar `cat` no settings).
- Teste de UI em perfil temporário (`G:\tmp-thumbui\abrir.cmd`, porta 9353) — a não ser que
  ele peça "no meu Dangai".
- Quando o Levi estiver jogando: não abrir janela nem usar GPU sem avisar.
- Antes de editar um `.dangai` em disco: **feche o projeto no app** (o auto save grava por cima).
  Fechar com calma: `(Get-Process Dangai | ? MainWindowTitle).CloseMainWindow()`.
- O botão de casa (canto superior esquerdo) no editor vira **"Limpar?"** no 1º clique —
  nunca clicar duas vezes.
- Publicar versão: só quando ele pedir (fluxo no fim).

## 1. Controlar o Dangai

**Instalado** (o dele): abrir com porta de depuração e dirigir por CDP.
```powershell
Start-Process "$env:LOCALAPPDATA\Programs\Dangai\Dangai.exe" -ArgumentList "--remote-debugging-port=9354"
```
Se o Dangai já está aberto, a 2ª instância morre (instância única): feche antes.
O empacotado **não** deixa importar o store; use DOM, eventos de entrada e a ponte
`window.dangai...` (ex.: `window.dangai.modulos.recap.salvarCenas(rascunhoId, escolhas)`).

**Dev** (`G:\tmp-thumbui\abrir.cmd`, porta 9353, perfil `G:\tmp-thumbui\p`): o store importa
por `await import('/store/project.ts')` (NÃO `/@fs/...`, que cria outra instância). Para ver a
Biblioteca no perfil de teste: `window.dangai.saveSettings({ libraryDir: 'G:/Dangai Recap/Biblioteca' })`
+ reload. Matar: processos com `tmp-thumbui` na linha de comando.

Scripts (em `scripts/`, porta como 1º argumento ou constante no topo):
- `cdp.mjs js <arquivo.js>` / `cdp.mjs foto <png>` — avaliar JS (async, `return ...`) e tirar print.
- `soltar.mjs x y <caminho...>` — **soltar arquivos** na janela (`Input.dispatchDragEvent` com
  `files`): episódio no "Novo recap", `.dangai` na janela (1 arquivo abre o projeto).
- `clicarxy.mjs x y`, `tecla.mjs ArrowRight 3` — clique e teclas (setas andam 1 quadro).
- `clicar.js` + `c.sh "<texto>"` — clica no 1º botão visível com aquele texto.
- Agulha da timeline: régua em y≈545; 0:00 em x≈131, ~13,8 px/s (janela 1920 px). Tempo atual:
  procure no DOM o texto `^\d:\d\d\.\d\d$`.
- Caminhos com `\` dentro de heredoc/`-e` do Bash perdem a barra: use `/` ou escreva o script
  num arquivo com a ferramenta Write.

## 2. O Gerar recap, passo a passo

1. **Episódio**: tela inicial > Módulos > *Gerar recap* > soltar o `.mkv` em *Novo recap*
   (o mesmo episódio retoma o rascunho que já existe). *Analisar* (motor do recap) ou
   *Analisar com o AnCut*. Confirmar Abertura/Encerramento sugeridos e **Salvar**.
   Pronto ≈ 4 min (395 cenas no S03E07). Com "Enviar sempre para o AnCut" o episódio vai pro AnCut.
2. **Roteiro**: *Meu roteiro* cola o texto dele. O gancho "vira 2 ou 3 cenas no passo Cenas".
   A imagem de cada frase é só o MOMENTO, não a cena final.
3. **Voz**: *Importar áudio* (pode soltar 2: gancho + resto, emenda pela ordem do nome).
   Cortar pausas **Justo** (padrão novo) > *Aplicar* > *Aprovar voz*. ElevenLabs quase não
   tem pausa longa (89,5 → 89,1 s).
4. **Cenas**: 26 frases, cada uma com cenas + "palavraInicio" (em que palavra a cena entra).
   - Frase **travada** (cadeado) não muda no *Sugerir de novo*; destravar = clicar nos botões
     com title `Travada: ...`.
   - *Sugerir de novo* (rodapé) refaz as não travadas.
   - *Abrir no editor* (com *Edição rápida* marcada) monta o projeto numa pasta nova em
     `G:\Dangai Recap\Biblioteca\_projetos\<anime SxxEyy - data>`.

## 3. Escolher cenas (o que o Levi espera)

- **Ritmo**: ~1,5 s por cena (ele fez 55 cenas em 89 s; o app sugere ~32 = lento demais).
  Frase longa = 2 a 4 cenas, cortando nas **palavras de peso** (nome, número, verbo forte,
  CAIXA ALTA). Flash de 0,35–0,5 s numa palavra é ok.
- **Gancho**: sempre 2 ou 3 cenas; a 1ª mostra quem a frase cita, a mais forte possível.
  Cada cena do gancho tem que ser **bonita, fácil de entender sozinha e bater com a palavra**;
  pode vir de qualquer ponto do episódio (não precisa ser sequência). Julgar **no recorte 9:16**,
  nunca pela miniatura 16:9: close extremo vira só olho, perfil vira meia cara, plano aberto vira
  gente minúscula. Variar ângulo/assunto entre cenas seguidas (nada de duas Maomao de frente
  iguais). Exemplo aprovado (S03E07, 16/11): "MANO!" Maomao de perfil virando o copo (0263) →
  "apostou ELA MESMA" ela de mão levantada (0175) → "COMPETIÇÃO" homens rindo de copo erguido +
  o proprietário (0188, fx 0,3) → "DE BEBIDA" saquê sendo servido em close (0258). Ele recusou:
  close extremo (0209), cara a cara em perfil (0214), corpo no chão sem contexto (0248).
- Só a cena do **gancho** pode repetir — de preferência como fecho no fim ("voltar a beber").
- Coerência: a imagem bate com a palavra (moedas em "300 moedas", corpo caindo em "APAGA",
  arrozal em "arroz"). Preferir rosto expressivo, plano médio/close, impacto.
- **Clipe precisa durar o trecho** (senão congela no último quadro): conferir a duração do
  plano ≥ tempo que a cena fica na tela; se não, escolha outro ou mova o corte pra outra palavra.
- Método: folha por frase com as sugestões (fita) + todos os planos no intervalo do evento e
  ±8 s do momento (`scripts/folhas.py`, rosa = escolha do app, azul = fita). Das 60 cenas que
  escolhi no S03E07, 27 vieram de fora da sugestão.
- Gravar as escolhas pela ponte (`salvarCenas`, origem `usuario`, `travada: true`) e recarregar
  a tela (`location.reload()` → Gerar recap → Continuar).

## 4. Depois de abrir no editor

- **Música**: a da Edição rápida é melhor que a minha (feedback dele 13/11) — não trocar por gosto.
- **SFX**: os da Edição rápida (pop abre, riser metálico no gancho, riser+impacto na troca de
  música) + no máximo alguns **ligados a uma ação visível**, baixos. Nada de meme (sus, among us,
  "wow") — ele chamou de "aleatórios".
- **Transições**: a Edição rápida põe `transitionIn: "zoom-in"` no começo de cada parte —
  **ele não gosta**. Deixar todas `"cut"`.
- **Revisar o vertical de TODAS as cenas** (`recortes.py`) antes de entregar — ele achou ~14
  ruins no S03E07 mesmo com o rosto do motor certo: nuca/costas em primeiro plano, janela vazia,
  manga/braço, gente minúscula em plano aberto, borrão de alguém passando no começo. Corrigir com
  `focusX` (para onde está a ação), `sourceStart` (pular o borrão) ou trocar a cena.
  `scripts/janela-cena.py` mostra o quadro inteiro com a janela 9:16 + o resto do clipe.
- **Legenda**: o preset dele é **Kiumaz v1** (Bangers, amarelo, escala 2,1, y 0,45, elástica
  7 quadros, curva 0,45→1,11→1, marcar tudo, pontuação "Só ? ! %", contorno 11). A Edição
  rápida usa o "estilo salvo", que pode estar com outra fonte/curva. Atalho: copiar
  `captionFont`, `captionAnimationFrames`, `captionPontuacao`, `captionAnimationCurve` de um
  projeto que ele aprovou (ex.: `...S03E07 - edicao do Claude`).
- **Câmera**: pelo conteúdo — zoom-in em rosto, pan em plano aberto, zoom-out pra revelar.
  Intensidade ≤ 0,14 (0,2 empurra o rosto pra borda).
- **Enquadramento 9:16**: nunca "no olho". Pegue o centro do rosto que o motor achou e calcule
  `focusX = (cx − 0,158) / 0,684` (janela 9:16 = 0,316 da largura de um 16:9). Ferramenta:
  `_medida/rostos-diag.ts` no repo (refaz a decisão de rosto pelo cache, mostra os rostos por
  cena). Conferir no preview do app no quadro de MAIOR zoom.
- **Ponto de entrada** (`sourceStart`): pular o começo quando tem alguém borrado passando na
  frente / pan borrado.
- Folhas de conferência: `scripts/recortes.py <projeto> saida` (recorte 9:16 no começo e fim de
  cada cena) e `scripts/janela.py` (quadro inteiro com a janela 9:16 desenhada).

## 5. Formatos

**`.dangai`** (JSON): `plan.scenes[] {imageIndex, imageIndexB, start, end, effect, intensity,
curve, sourceStart, transitionIn}`; `images[] {path, fileName, focusX, focusY, focusAuto}`;
`trilhas[] {faixa, at, durationSec, inicioSec, usarSec, gainDb, fadeInSec, fadeOutSec, ducking,
modulos.recap.papel}` (peaks/rms podem ir vazios); `captions` + `caption*` (Color, Font, Scale,
Y, Animation, AnimationFrames, AnimationCurve, Mark, Pontuacao, Shadow, Stroke);
`transcript.words[] {text,start,end}`; `biblioteca` (a aba Cenas: `blocos`, `porBloco`,
`unioes`); `modulos.recap` (rascunhoId, secoes). `audio.path` absoluto + `rel`.

**Rascunho** `%APPDATA%\Dangai\modulos\recap\recaps\<id>.json`: `roteiros[]`, `atual`,
`voz.takes[] {id, palavras[{texto,start,end,fraseId}], trechos[{fraseId,offset,duracao}]}`,
`cenas.escolhas[] {fraseId, cenas[{candidato{planoIds,inSec,outSec,origem,keyframe}, palavraInicio}], fita, travada}`, `eventos`.

**Episódio**: `episodio.json` com `planos[] {id, start, end, arquivo, keyframe, personagens, falantes}`
(id→caminho em `episodios/indices.json`; recap externo em `<Biblioteca>/_indices/<id>/`).
Shots em `shots/NNNN.mp4`, keyframes `NNNN_{0,1,2}.jpg`, corte em `metadata/shot_bounds.json`.

## 6. Armadilhas já vistas (S03E07, 13–16/11)

- **Trocar uma cena direto no `.dangai`** (app fechado): mude `images[i].path/fileName/focusX`
  (`focusAuto:false` se o foco é escolha sua) e `scenes[k].sourceStart`. Uma entrada de
  `images` pode ser **dividida por duas cenas** (o 0192 do gancho e do fim) — duplique antes de
  mexer. No fim tire as entradas sem uso e renumere `imageIndex`: a faixa "Cenas N" do topo
  conta `images`, não blocos. Guarde backup em `G:/tmp-medida\` antes de cada rodada.
- Mantenha a aba Cenas do recap igual ao projeto: `salvarCenas` pela ponte (app aberto) com a
  troca (`inSec` = início do plano + `sourceStart`). Não gravar o rascunho em disco pelo Claude:
  o `%APPDATA%` dele (MSIX) é virtual e o Dangai não vê.
- `Start-Process` do Dangai às vezes não sobe (porta recusada): confira
  `http://127.0.0.1:9354/json/version` e abra de novo. O Levi pode fechar o app entre os pedidos.
- A escala da régua muda entre aberturas: depois de clicar na agulha, **leia o tempo** na tela
  antes de afirmar qual cena está no preview.
- Refazer com áudio novo e quase o mesmo roteiro: *Meu roteiro* → importar voz → levar as
  escolhas antigas por LCS das palavras da frase (`G:\ClaudeEditor\_capturas\e2e-apo\levar-escolhas.js`,
  com sinônimos tava/estava) → `salvarCenas` → *Abrir no editor*.

- **Recortar o episódio** deixa as escolhas antigas do rascunho apontando pra outras cenas
  (guardadas por número). Destravar e sugerir de novo.
- A Edição rápida errava o rosto quando o reconhecimento troca nomes (Maomao como "Fuyou") e
  quando o nome de quem fala não liga ao elenco ("Dono da terra"/"proprietário" ≠ "Guen"):
  use os **Apelidos** da Biblioteca. 2.8.5: o palpite da janela vai ao rosto mais perto e
  cabeça sem rosto perde de rosto visível.
- Soltar um vídeo na janela de um projeto montado redividia tudo (corrigido 2.8.2).
- Legenda elástica estourava a tela no pico do bounce (corrigido 2.8.4).
- Motor de corte: "continuidade" (2.8.3) tira corte fraco no meio de plano que continua;
  a chuva de moedas (0219/0220) ainda fica partida → *Mesclar* na Biblioteca (Ctrl+clique).
- Corte novo mantém a identidade `v3` no `shot_bounds.json` (+ `refino: continua-1`) porque o
  AnCut instalado recortaria uma identidade desconhecida.

## 7. Publicar uma versão (quando ele pedir)

Entrada em `shared/novidades.ts` → commit → `npm version patch -m "%s\n\nCo-Authored-By: ..."`
→ `npx tsx --tsconfig tsconfig.node.json scripts/teste/v-novidades.ts` → `git pull --rebase`
→ `git push origin main --follow-tags` → acompanhar `gh run view <id> -R faahpla/dangai` e
conferir os assets (`Dangai-x.y.z-win-x64.exe`, `.blockmap`, `.zip`, `latest.yml`).
Testes: `npm run typecheck`, `npm test`; testes do módulo com esbuild
(`npx esbuild modulos/recap/teste/v-X.ts --bundle --platform=node --packages=external --jsx=automatic --tsconfig=tsconfig.web.json --define:import.meta.env.DEV=false --loader:.ttf=empty --loader:.png=empty --outfile=modulos/recap/teste/_v-X.cjs` e `node`).
Motor (Python): `%LOCALAPPDATA%\Dangai\recap\motor-runtime\venv\Scripts\python.exe -m unittest tests.test_X`
dentro de `modulos/recap/motor` (com `PYTHONDONTWRITEBYTECODE=1`).

## Scripts desta skill (`scripts/`)

| script | o que faz |
|---|---|
| `cdp.mjs js <f.js>` / `foto <png>` | JS e print no Dangai (`PORTA=9353` = dev; padrão 9354 = instalado) |
| `soltar.mjs x y <arq...>` | solta arquivos na janela |
| `clicarxy.mjs x y`, `tecla.mjs <tecla> [n]` | clique e teclas |
| `c.sh "<texto>"` (+ `clicar.js`) | clica no botão com o texto |
| `dados-das-folhas.js <rascunho> <episodio> [take]` → `folhas.py` | folhas de candidatas por frase |
| `recortes.py <projeto.dangai> <saida>` | recorte 9:16 no começo/fim de cada cena |
| `janela.py <projeto.dangai> <saida>` | quadro inteiro com a janela 9:16 desenhada |
| `janela-cena.py <projeto.dangai> <saida> 3,10,26` | cenas escolhidas: 3 quadros com a janela + 3 do resto do clipe (achar `focusX`/`sourceStart`) |

No repo do Dangai (fora da skill, `_medida/`, ignorado pelo git): `rostos-diag.ts` (decisão de
rosto da Edição rápida contra um foco de referência) e o estudo do corte em
`G:\ClaudeEditor\_capturas\corte-v3\cont` (`regra.py`, régua do gabarito).
