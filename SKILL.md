---
name: dangai-edicao
description: Editar um short de recap de anime no Dangai do começo ao fim, no estilo do Levi e do Fabinho/Faah (o mesmo estilo; só a legenda muda) — pelo Gerar recap (Levi: episódio, roteiro, voz, aba Cenas, Edição rápida) ou pelo editor normal (Fabinho: narração + roteiro .txt, cenas na Biblioteca, timeline). Cobre ritmo, gancho, imagem por palavra, enquadramento 9:16, ponto de entrada, efeito, transição, legenda, som, cor e roteiro; controlar o Dangai por CDP; o formato do .dangai e do rascunho; medidas offline e armadilhas. Use em QUALQUER pedido de "edita no Dangai", "faz o processo todo", "edita do meu jeito", "compara com a sugestão do app", "ajusta enquadramento/legenda/cenas do projeto", ou para entender por que a Edição rápida errou.
---

# Editar no Dangai (o fluxo do Levi e o do Fabinho)

**O estilo de edição é UM só** (Levi e Fabinho editam igual — confirmado pelo Levi 17/11): ritmo,
gancho, imagem por palavra, enquadramento, entrada, efeito, transição, som, cor e roteiro estão na
**seção 9** e valem para os dois. **Só a legenda muda** (Levi: preset Kiumaz v1, seção 4; Fabinho:
amarelo `#FFDD00`, seção 9). O que muda também é o **caminho** dentro do app:

| quem | como edita | seções |
|---|---|---|
| **Levi** (leviclementino1-creator) | *Gerar recap*: episódio → roteiro com IA → voz → aba Cenas → *Abrir no editor* com a Edição rápida | 2, 3, 4 (e 5, 6) |
| **Fabinho** (Faah, dono do núcleo) | **editor normal**: solta a narração, o roteiro `.txt`, marca as cenas na Biblioteca e acerta na timeline | **8 e 9** |

Na dúvida de quem é o projeto (para a legenda e o fluxo): `modulos.recap` no `.dangai` = Gerar recap (Levi).

Dangai = Electron + Remotion, repo `faahpla/dangai` (clone em `G:\ClaudeEditor\dangai` *só no PC do
Levi*; no PC do Fabinho, `E:\Projetos\dangai`).
`modulos/recap` e `modulos/thumb` são do Levi; o resto (núcleo) é do Faah — mudança no
núcleo entra pequena, um assunto por commit, e o Levi avisa o Faah. Responder ao Levi em
português, curto e simples.

## 0. Regras antes de tudo

- **O roteiro é a fonte da verdade**; o áudio só dá os tempos.
- Biblioteca e projetos reais do Levi: **só leitura**, salvo pedido explícito. Apagar = Lixeira
  (nunca de vez). Recortar um episódio muda os ids das cenas (ver Armadilhas).
- Nada pago sem confirmar. Nunca imprimir/copiar chave de API (não dar `cat` no settings).
- Teste de UI em perfil temporário (`G:\tmp-thumbui\abrir.cmd`, porta 9353, *só no PC do Levi*) —
  a não ser que ele peça "no meu Dangai". No PC do Fabinho: `DANGAI_DADOS=<pasta>` + `npm run dev`
  em `E:\Projetos\dangai` (outra pasta de dados; não grava por cima das configurações dele).
- **Nunca mostrar o `settings.json`** (tem chaves de API). Para achar os projetos, leia SÓ o campo
  `recentes` (um `node -e` que imprime o `path` de cada item) e as pastas onde eles estão.
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

**Dev** (*só no PC do Levi*: `G:\tmp-thumbui\abrir.cmd`, porta 9353, perfil `G:\tmp-thumbui\p`;
no do Fabinho: `npm run dev` com `DANGAI_DADOS`): o store importa
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

## 2. O Gerar recap, passo a passo *(só para quem usa o Gerar recap)*

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
     `G:\Dangai Recap\Biblioteca\_projetos\<anime SxxEyy - data>` (*só no PC do Levi*).

## 3. Escolher cenas (o que o Levi espera)

### CHECKLIST DA SELEÇÃO — toda cena passa por aqui ANTES de gravar (Levi, 16–17/11)

Ele achou cada um destes erros no Nia S01E07 e pediu: "isso tudo já deveria ser critério na
seleção de cenas". Não deixe para corrigir depois.

1. **Bate com a palavra** e se entende sozinha (nome → rosto dele na palavra; número → o objeto;
   ação → o momento exato; reação → close de reação). Bonita no gancho; pode vir de qualquer
   ponto do episódio.
2. **Julgue no recorte 9:16**, nunca na miniatura 16:9.
3. **Corpo inteiro > plano médio > close.** Close extremo vira só olho/nariz/boca ("quanto mais
   perto, piorzinhas"). Close só quando a palavra pede o detalhe ("olhar", "tatuado").
4. **Movimento > cena parada**, desde que fique no centro (andar, virar, gesto, golpe). Meça:
   `movimento.py` (< 1 = parada).
5. **O MELHOR MOMENTO do clipe**: olhe o clipe INTEIRO (tira de 8 quadros no recorte) e ponha o
   `sourceStart` onde o rosto/a ação está melhor — não o começo por padrão (Gandolf comemorando:
   o fim; Nia: olho aberto, não piscando; tatuado vencedor: braços erguidos com a cabeça).
6. **Nada cortado nem borrado**: cabeça/olhos não colados na borda (lembre do zoom-in: ele aperta
   mais no fim — com rosto no topo, use zoom-out); sem borrão de alguém passando no começo; sem
   o borrão/transição do fim do clipe; sem tela vazia (janela, manga, nuca, costas).
7. **Enquadramento** `focusX` no rosto/ação (motor de rostos, fx=(cx−0,158)/0,684). Se o
   personagem anda: Câmera livre > Seguir o rosto — e confira (seção 4).
8. **Efeito pelo conteúdo**: zoom em rosto/objeto; deslize só em plano aberto; nunca o rodízio da
   Edição rápida.
9. **Sem repetir** clipe (só o do gancho volta); nada de duas cenas parecidas seguidas
   (mesmo personagem, mesmo ângulo).
10. **Não congela**: `sourceStart` + duração ≤ clipe.
11. **Close parado longo vira dupla** (plano médio, depois o close na palavra).
12. **Recursos**: grid em "um x outro" (dois personagens diferentes e legíveis); seta no detalhe
    que a fala cita; personagem vistoso de corpo inteiro "dá view" — encaixe onde a fala cita.
13. **Sem sangue/violência gráfica em destaque** (corpo ensanguentado no chão) e nada que fira a
    regra da plataforma.

**Conferência final obrigatória**: `scripts/folha-final.py <projeto.dangai> <saida>` — as cenas
como o Dangai mostra (recorte do focusX ou da câmera + zoom do efeito, 1º e último quadro).
Olhe as 49 antes de entregar; o Levi não pode ser quem acha.

*Como aplicar o estilo na aba Cenas do Gerar recap. O estilo completo (dos dois) está na seção 9 —
use a lista "Que imagem para cada tipo de palavra" para escolher cada cena. Folha de candidatas,
`salvarCenas`, frase travada e "Sugerir de novo" são só para quem usa o Gerar recap.*

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

## 4. Depois de abrir no editor (gosto do Levi, com a Edição rápida)

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
  Intensidade ≤ 0,14 (0,2 empurra o rosto pra borda). A Edição rápida põe os efeitos em
  **rodízio** (zoom-in, zoom-out, pan-left, pan-right, pan-up, pan-down) sem olhar a cena: o
  deslize tira o rosto do centro no 9:16 (Levi 17/11). Regra: **zoom em tudo que tem rosto ou
  objeto**; deslize só em plano aberto (arena, multidão).
- **Escolha da imagem no 9:16** (Levi 17/11, Nia S01E07): **corpo inteiro > plano médio > close**
  ("quanto mais perto, piorzinhas"); close extremo vira só olho/nariz. **Movimento do personagem**
  (andar, virar, gesto, golpe) é melhor que cena parada, desde que fique dentro do recorte.
  Medir: `_capturas/e2e-nia/movimento.py <projeto>` (diferença entre quadros dentro do recorte,
  < 1 = parada) e `mov-todos.py` (movimento de todo plano do episódio + melhor janela).
  Personagem vistoso de corpo inteiro (a atendente coelhinha) "dá view": pôr onde a fala cita.
- **Seguir o movimento** (Levi 17/11): personagem que anda/vira pela tela sai do centro com zoom
  OU com deslize fixo. Use a **Câmera livre > "Seguir o rosto"** do bloco
  (`scripts/seguir-rostos.mjs <lista [n,id,x]>` faz em lote: clica na parte de BAIXO do bloco —
  em cima fica o **x que APAGA o bloco**, Ctrl+Z desfaz: `scripts/ctrlz.mjs`). Depois **confira
  cada câmera** (simular início/fim): sem rosto de frente ela liga no CENTRO e apaga o seu
  focusX; às vezes pega o rosto errado (Nia pequena no canto em vez do Gandolf). Desligue
  (`camera: null`) nessas. Câmera ligada ignora o efeito: dê `from.scale 1 → to.scale 1.08` pra
  não ficar parada.
- **Ponto de entrada de TODAS as cenas** (Levi 17/11: "quanto mais no final da cena melhor, pra
  ver o rosto"): cena curta de clipe longo → olhar a tira do clipe inteiro no recorte 9:16 (8
  quadros, marcando o trecho usado) e mover `sourceStart` pro pedaço com o rosto/a ação. No S01E07
  8 de 36 pediam outro trecho (olho fechado no começo, personagem ainda levantando, cabeça cortada).
- **Ponto de entrada pelo melhor ângulo**: o clipe muda de ângulo dentro dele (a tatuagem: ombro
  de perto no começo, lutador inteiro do meio pro fim). Olhe a tira do clipe inteiro, não só o
  começo.
- **Grid** (tela dividida, `imageIndexB` + `sourceStartB`/`effectB`/`intensityB`; no rascunho
  `cena.baixo`): use em "um x outro" — dois personagens diferentes e legíveis (Nia de braços
  cruzados x Gandolf; tatuado socando x o outro lutador). Cada metade é 1080x960 = 63% da largura
  do 16:9.
- **Seta** (`sobreposicoes`, tipo `image`, faixa nova, `x`/`y` em % do quadro, `escala` sobre o
  arquivo inteiro no quadro): `modulos/thumb/assets/setas/seta-ajk.png`, escala ~0,3, efeito
  zoom-out 0,25 + fade 0,06 s, apontando o detalhe ("cara tatuado"). Simule com PIL antes.
- **Close longo vira dupla**: uma cena de close parada por 3 s → plano médio primeiro, close
  na palavra ("reconhecer a força" Nia olhando → "só de olhar" o olho).
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
`transcript.words[] {text,start,end}`; `biblioteca` (no editor normal, a Biblioteca: `blocos` = trechos do roteiro, `porBloco` = cenas
marcadas por trecho, `pesos`, `unioes` = tela dividida, `cortes` = fronteira puxada, em índice de palavra); `modulos.recap` (rascunhoId, secoes). `audio.path` absoluto + `rel`.

**Rascunho** *(só para quem usa o Gerar recap)* `%APPDATA%\Dangai\modulos\recap\recaps\<id>.json`: `roteiros[]`, `atual`,
`voz.takes[] {id, palavras[{texto,start,end,fraseId}], trechos[{fraseId,offset,duracao}]}`,
`cenas.escolhas[] {fraseId, cenas[{candidato{planoIds,inSec,outSec,origem,keyframe}, palavraInicio}], fita, travada}`, `eventos`.

**Episódio**: `episodio.json` com `planos[] {id, start, end, arquivo, keyframe, personagens, falantes}`
(id→caminho em `episodios/indices.json`; recap externo em `<Biblioteca>/_indices/<id>/`).
Shots em `shots/NNNN.mp4`, keyframes `NNNN_{0,1,2}.jpg`, corte em `metadata/shot_bounds.json`.

## 6. Armadilhas já vistas (S03E07, 13–16/11 — projetos do Gerar recap)

- **Trocar uma cena direto no `.dangai`** (app fechado): mude `images[i].path/fileName/focusX`
  (`focusAuto:false` se o foco é escolha sua) e `scenes[k].sourceStart`. Uma entrada de
  `images` pode ser **dividida por duas cenas** (o 0192 do gancho e do fim) — duplique antes de
  mexer. No fim tire as entradas sem uso e renumere `imageIndex`: a faixa "Cenas N" do topo
  conta `images`, não blocos. Guarde backup em `G:/tmp-medida\` (*só no PC do Levi*; em outro PC, uma pasta temporária) antes de cada rodada.
- Mantenha a aba Cenas do recap igual ao projeto: `salvarCenas` pela ponte (app aberto) com a
  troca (`inSec` = início do plano + `sourceStart`). Não gravar o rascunho em disco pelo Claude:
  o `%APPDATA%` dele (MSIX) é virtual e o Dangai não vê.
- `Start-Process` do Dangai às vezes não sobe (porta recusada): confira
  `http://127.0.0.1:9354/json/version` e abra de novo. O Levi pode fechar o app entre os pedidos.
- A escala da régua muda entre aberturas: depois de clicar na agulha, **leia o tempo** na tela
  antes de afirmar qual cena está no preview.
- Refazer com áudio novo e quase o mesmo roteiro: *Meu roteiro* → importar voz → levar as
  escolhas antigas por LCS das palavras da frase (`G:\ClaudeEditor\_capturas\e2e-apo\levar-escolhas.js`, *só no PC do Levi*,
  com sinônimos tava/estava) → `salvarCenas` → *Abrir no editor*.

- **Biblioteca sem o episódio**: com "Enviar sempre para o AnCut" o episódio é cortado na pasta do
  AnCut (`G:\App Corte Cenas\Output`); a Biblioteca só lê a `libraryDir` + a raiz do recap
  (`G:\Dangai Recap\Biblioteca`). No PC do Levi a `libraryDir` estava vazia → E07 sumia. Corrigido
  apontando pra pasta do AnCut (17/11) e no núcleo: vazia = pasta do AnCut (commit local, a publicar).
- `cdp.mjs` embrulha o JS num template do Node: **`\` some** (`"G:\App"` vira `G:App`). Caminho no JS
  enviado por CDP sempre com `/`.
- `window.dangai.getSettings()/saveSettings()` devolvem `{ok, value}`.
- **Antes de reabrir um `.dangai` editado à mão, valide** (`projectFileSchema.safeParse`, ver
  `_capturas/e2e-nia/rodada3.js`): um `focusX` undefined fez o Dangai dizer "está corrompido".
- **Troca de música** da Edição rápida cai onde a 1ª faixa ACABA (S01E07: 0:32, no meio da frase,
  e a faixa nova começa com 1 s mudo = buraco). Pôr a troca no começo de uma parte do roteiro, onde
  já tem o whoosh (`usarSec` da 1ª = início da parte; `at` da 2ª = esse tempo, `inicioSec` pulando
  o silêncio do começo da faixa — medir o RMS).
- **Música que some**: a Edição rápida pode começar a faixa tarde e o trecho cair no fim que
  some (S01E07: 57,8 s → fim em 90 s, vazio de 0:20 a 0:32). Medir o RMS por segundo da música
  e mover `inicioSec` pra o trecho não passar do fade.
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

## 8. Editor normal (sem Gerar recap) — o fluxo do Fabinho

Medido em 46 projetos dele (09–11/2026, `recentes` + pastas `%USERPROFILE%\Documents\Dangai\Projetos`
e `D:\Dopanimes\Projects`). Clipes = shots que o AnCut cortou, em `D:\Animes\<anime>\SxxEyy\shots\NNNN.mp4`
(às vezes quadro de mangá; filme em `D:\Filmes\Corte de Filmes\<filme>`); SFX em `%USERPROFILE%\Music\Sfx's`, músicas em `%USERPROFILE%\Music\Song's`.

1. **Narração**: soltar o `.mp3` bruto na tela inicial → pede o nome (o `.dangai` nasce e o auto save
   grava nele) → **Etapa de Áudio**: isolar voz (100), nivelar, EQ, compressor, normalizar e
   **velocidade 110–115%**. *Pronto* grava `<nome> (editado).wav` ao lado e segue.
2. **Roteiro**: o `.txt` dele na etapa Roteiro; sincroniza com a voz (o texto é a fonte, a voz só dá os tempos).
3. **Cenas = Biblioteca**: o roteiro vira **trechos** (cortados na vírgula e no ponto). Em cada trecho ele
   marca **1 a 3 cenas** na ordem; quando quer, puxa a fronteira para uma palavra (`cortes`), dá peso ou
   une duas em tela dividida (raro: 14 cenas em 2.285). *Aplicar* monta a timeline: cada trecho se
   divide entre as cenas dele, emenda no começo da fala, efeito em rodízio, intensidade 0,1, corte seco.
4. **Timeline** (o que ele acerta à mão, medido contra o que a Biblioteca monta — mesmas contas do
   `shared/trecho.ts`, script `comparar-com-a-biblioteca.mts`):
   - **Cortes: quase não mexe.** 95% dos cortes ficam onde a Biblioteca pôs (1.764 de 1.853); 4% andam
     (mediana 0,17 s, mais vezes para antes); 17 cortes novos e 9 tirados em 39 projetos. **O ritmo é
     decidido na Biblioteca** (quantas cenas por trecho), não na timeline.
   - **Enquadramento (`focusX`)**: arrasta à mão ~40% das cenas (900 de 2.285), deixa o rosto
     automático em ~19% e o centro no resto. O valor vai de 0 a 1 — puxa para onde está o rosto/ação.
   - **Ponto de entrada (`sourceStart`)**: muda em 22% das cenas, mediana ~1,3 s (pula o começo morto).
   - **Efeito**: troca ~18% do rodízio (230 de 1.287). Mais comum: `pan-up` → `pan-down` (46),
     `pan-left` → `zoom-out` (17), `pan-left`↔`pan-right` (25). No fim: zoom-out 451, pan-down 436,
     pan-right 372, pan-left 370, zoom-in 368, **pan-up só 281**. Intensidade **nunca** muda (0,1, curva linear).
   - **Transição**: ver seção 9.
   - **Giro** 90°/270° em ~1,5% das cenas (quadro em pé); tela dividida quase nunca.
5. **Som** nas faixas A1–A4 (o painel *Do meu jeito*, `shared/meu-jeito.ts`, já aprendeu isso dos
   projetos dele), **camada de ajuste de cor** no vídeo todo, **sobreposições** (foto, SETA.mov), legenda,
   thumb (módulo thumb) e render.

Para estudar um projeto dele: `scripts/fabinho/folhas-do-projeto.cjs` (tabela frase a frase + folha de
quadros no recorte 9:16, só ffmpeg) e `scripts/fabinho/medir-projetos.cjs`. Tabelas dos 46 projetos em
`referencia/fabinho/` (duas com o que aparece em cada cena).

## 9. O estilo de edição (dos dois)

Medido nos 46 projetos do Fabinho e confirmado pelo Levi como o estilo dele também (17/11). Os exemplos
são do Fabinho; vale o mesmo para os recaps do Levi. **Exceção: a legenda** (ver "Legenda" abaixo).

### Ritmo

- **1,23 s por cena** (mediana de 2.285 cenas; média 1,30, desvio 0,50; 80% entre 0,72 e 1,92 s).
  Por vídeo a mediana fica entre 0,97 e 1,78 s; **~46 cenas por minuto**. Mais curta ~0,3–0,5 s
  (flash numa palavra), mais longa ~2,5–3,5 s (frase que não tem o que cortar).
- **3 a 6 palavras por cena** (mediana 4). Corta **na vírgula** sempre; dentro da vírgula, na palavra de
  peso (nome, número, verbo). Ex.: *A Noelle é SUPERestimada* — "Ela sai de 'não consigo / acertar um
  alvo com água' / pra armadura de valquíria." (3 cenas); *Por que Grimmjow MORDEU Yhwach* — "Uryu, /
  Shunsui e Grimmjow / contra" (0,38 / 0,59 / 0,57 s: **um corte por nome** numa lista).
- Duração do vídeo: 61–78 s (até 05/11) ou 34–38 s (os curtos, desde 06/11).

### Gancho (a 1ª frase)

- **2 a 4 cenas** (mediana 3) de ~1,0–1,2 s; o gancho inteiro dura 2,7–4 s. Sempre clipe do anime
  (nunca foto). Efeito no gancho: zoom (95 de 148) ou pan lateral; quase nunca pan vertical.
- **1ª cena = quem a frase cita, na forma mais icônica**; a última cena do gancho mostra **literalmente a
  palavra de impacto**. Exemplos:
  - *A Noelle é SUPERestimada* (0–2): Noelle de armadura Valquíria de frente → voando com a armadura
    → armadura de longe, asas contra a luz; "Calma," = Noelle em close olhando brava pra câmera.
  - *O D foi feito Bonitão só pra SOFRER* (0–2): "O D foi desenhado bonito" D em close calmo →
    "por um único motivo..." D plano médio → "pra apanhar." **D com o rosto machucado**.
  - *Por que NINGUÉM Estranha o Grimório* (2): "cinco folhas do Asta?" = **o trevo de 5 folhas**.
  - *Por que Grimmjow MORDEU Yhwach* (0–2): as 3 cenas são **o Grimmjow mordendo** (a ação do título).
  - *Ninguém é Especial em Cyberpunk* (0–3): "David e Adam / Smasher não / eram especiais / em
    Cyberpunk?" = David, Smasher, David, Smasher (~0,7 s cada, alterna os dois nomes).
  - *A Maomao NÃO É Imune a Veneno* (0–1): Maomao com cara de nada → Maomao cortando o próprio braço.
- Seta (`SETA.mov` na V2) apontando o personagem do gancho quando ele não é óbvio (Lilia @0,3 s,
  Kiwi @1,1 s, Adam Smasher @0,1 s).

### Que imagem para cada tipo de palavra

- **Nome de personagem** → close/plano médio do rosto dele, trocando **na palavra do nome**
  (*Noelle SUPERestimada*: "o Nozel com cara de tanso" = Nozel em close sério; *COMO O AIZEN ENGANOU O
  ALMIGHTY*: "Só que não era o Renji. / Era o Aizen." troca do Renji pro Aizen no nome).
- **Pessoa real** (diretor, autor, animador, boxeador) → a cena continua um personagem fazendo a ação, e a
  **foto real entra por cima** (sobreposição na V2) na hora do nome: Kai Ikarashi (*O D foi feito
  Bonitão* @6,7 s), Glen Keane (*O quarto da Rapunzel* @4,6 s), Mike Pondsmith (*Adam Smasher* @16,5 s),
  Bartosz Sztybor (*Final Alternativo* @13 s), os boxeadores (*Magna* @13,1 s). Objeto real idem
  (a câmera Sony VX2000 @57,3 s no *D*).
- **Número / quantidade** → o objeto que mostra o número: *Grimório* "três folhas" = trevo de 3, "os de
  quatro" = trevo de 4 brilhando, "CINCO folhas" = trevo de 5 escuro; *Ram AMASSOU o Lye* "50% do poder"
  = Ram com o chifre brilhando; *Rapunzel* "18 anos presa numa torre" = Rapunzel lendo na cama com o
  cabelo enorme; *Adam Smasher* "96% do corpo" = Smasher de corpo inteiro.
- **Ação** → o plano exato da ação: *Noelle SUPERestimada* "O Asta quebra / os dois braços" = Asta caindo
  no fogo → Asta de braços pretos feridos; "solta uma lágrima" = Noelle chorando; *Rapunzel* "pintar as
  paredes" = pincel na parede; *Ram* "apanhou igual cachorro" = Lye levando a surra.
- **Emoção, gíria, reação** ("Mano,", "É sério isso mano?!", "Respeito.", "Nem fudeno.", "caraio") →
  close de **reação exagerada**: *Noelle censura* "É sério isso mano?!" = Asta chocado; *Noelle
  SUPERestimada* "Respeito." = Noelle olhando brava pra câmera, "Mano," = Noelle de boca aberta corada,
  "Nem fudeno." = Noelle em close furiosa.
- **Coisa concreta** → close do objeto: *Maomao Imune a Veneno* "comida envenenada" = frutas e bolinhos,
  "trigo-sarraceno" = campo de grãos, "marcas no braço" = braço enfaixado; *O D* "A trança / é o rabo"
  = a trança da Talia em movimento.
- **"No mangá" / "capítulo N"** → página ou quadro do mangá (*Grimório* cena 39; *Noelle vai PERDER*:
  5 quadros; *luta da Noelle criticada*: 3).
- **"Os fãs", "teve gente", "viralizou"** → print do post por cima (*Magna* @39,7 s), ou a cena citada
  (*Magna* "um frame com um desenho esquisitíssimo" = o próprio frame torto).
- **"Repara", "aquela ...", "Era o X"** → `SETA.mov` apontando o detalhe (*Talia* @14,9 s "Repara no
  estado", *Quem destruiu a família de D* @54,3 s "Era o Tanaka.", *Ciberpsicose* @17,3 s "aquela coroa
  na jaqueta").
- **Explicação abstrata** ("O problema é que", "Ou seja", "Outro problema também") → o personagem do
  assunto em plano médio/close neutro, ou o poder dele (magia, aura). Nunca tela vazia.
- O assunto do vídeo domina: em *Magna* a fala é sobre créditos, notas e IMDb, mas a imagem é sempre a
  **luta** (os melhores socos e caras), nada de print de site.

### Fechamento

- Última frase curta e opinativa, ou CTA, e a **imagem volta ao gancho** ou mostra o alvo da piada:
  *Noelle SUPERestimada* "Boa? Sim." = a mesma cena 0 do gancho (armadura) → "Nem fudeno." Noelle furiosa;
  *O D* "se prepara." = D sorrindo sinistro na chuva (a mesma da cena 12); *Rapunzel* "Me segue aí" =
  Rapunzel acenando (a mesma da cena 11); *Maomao Imune a Veneno* "Não sendo o charlatão ta valendo." =
  o Guen (o "charlatão"); *Grimmjow* "o golpe que o Almighty não conseguiu desfazer" = o golpe final do Ichigo.
- Repetir clipe é normal (~3,5 por vídeo), de preferência pra fechar ou para quem volta na fala.

### Enquadramento, entrada, efeito, transição

- Julgar **no recorte 9:16** (`folhas-do-projeto.cjs`). Rosto ou ação dentro da janela; ele arrasta
  `focusX` até o rosto — não aceita o centro quando o personagem está no canto.
- `sourceStart`: pular o começo morto do shot (mediana ~1,3 s) para a cena começar já no movimento.
- Efeito: rodízio do app com intensidade **0,1** (não mexer), mas **sem pan-up**: prefira pan-down ou
  zoom-out. No gancho, zoom ou pan lateral.
- **Transição**: nunca `zoom-in` (é a que a Edição rápida põe no começo de cada parte e o Levi tirou
  no S03E07). As que eles usam: desde 08/10, ~6 por vídeo (4–12), quase sempre **no
  começo de uma frase nova** (depois do ponto), mais na 1ª metade do vídeo: `light` e `pan-down`
  (~30% cada), `pan-left`, às vezes `pan-right`/`pan-up`; `crossfade` raríssimo; nunca `zoom-in`. O resto é corte seco.

### Legenda — a ÚNICA diferença entre os dois

**Levi**: preset **Kiumaz v1** (seção 4). **Fabinho** (estável desde 07/10):

Fonte padrão (Komika Axis: `captionFont` vazio), **amarelo `#FFDD00`**, escala **1,3**, y **0,38**,
**elástica 6 quadros**, curva `0,741 → 1,084 → 0,97 → 1`, marcar **palavra**, contorno **7**,
sombra distância 3 / desfoque 0 / opacidade 1 / ângulo 71, pontuação **manter** (desde 13/11).
~1,3 palavras por bloco (uma palavra por vez). Cor muda com o tema: *Rapunzel* (Disney) vermelho,
*A Joka* (Apotecária) rosa, escala 1,4, contorno 5.

### Som (faixas e volumes)

| faixa | o que vai | volumes |
|---|---|---|
| **A1** | SFX de corte: `Flash Whoosh Swoosh`/`Flash Swoosh` (troca de cena forte), `Camera Shutter 7` (corte/flash), `Stinger Camera Shut`, `Sharp Riser`; som de abertura no 0 s | whoosh −5, shutter 0, stinger 0, riser −3 |
| **A2** | 2ª camada de SFX (shutter, stinger, riser) e trechos curtos de tema (Death Note, Sharingan) | 0 / −15 |
| **A3** | **música de fundo** | −15 a −20 dB |
| A4 | sobra: meme de abertura ou outra música | — |

- **Abertura (0 s)**: `Re Zero - Return By Death` (0 dB), `Illuminati Meme` (−5), `Cartoon Pop Up`
  (−3/−5), `Sharingan` (−15) ou `Teleport DBZ` (−5).
- **Música**: era `GONE TOO FAR` a −15/−20 embaixo de tudo; em nov/2026 `Death Note Kyrie` (−15) no
  gancho e depois `Naruto Sasuke Theme` ou `Homelander Theme` (−20); por clima `Pensando`, `Comedy`,
  `HATE ME NOW` (−20); Disney com a trilha do filme (*Rapunzel*: `Kingdom Dance`, −25).
- `Sharp Riser` com fade-in ~0,7–1,2 s **terminando num corte**: no fim do gancho e perto do fim do vídeo.
- 15–30 sons num vídeo de 60–75 s, ~10 num de 35 s. Sem ducking. Os 13 projetos de setembro não têm
  nenhum som gravado no `.dangai`.

### Cor

Uma **camada de ajuste** no vídeo inteiro (nos projetos de out–nov/2026, sempre a mesma): exposição +0,05, contraste +0,1,
brancos +0,1, pretos −0,1, saturação +0,2, vibrance +0,2, curva mestre em S leve.

### Roteiro (quando for escrever ou revisar)

- **Tamanho**: 230–290 palavras (61–78 s) ou, desde 06/11, 110–125 palavras (34–38 s).
- **Frases**: ficaram mais longas — set/2026 7–10 palavras por frase, cheias de "…"; out–nov 11–17.
  Cada linha do `.txt` = uma ideia; 7–20 linhas.
- **Gancho**, em três fases: set/2026 **"MANO…" + pergunta TODA EM CAIXA ALTA** ("MANO… A RUI TÁ COM
  MEDO DO SUBARU?!"); até 23/10 **"POR QUE …?" em caixa alta** ("POR QUE A KIWI USA AQUELA MÁSCARA
  VERMELHA EM CYBERPUNK?"); depois **sem caixa alta**: "Por que …?", "Você sabia que …?" ou afirmação
  polêmica + "e eu vou explicar por quê." ("A Noelle é a personagem mais superestimada de Black Clover,
  e eu vou explicar por quê.").
- **CAIXA ALTA no corpo**: quase nunca; uma palavra de ênfase ("tem CINCO folhas", "LITERALMENTE A
  METADE IRMÃO"). No **nome do arquivo** sim, na palavra-chave (NINGUÉM, SUPERestimada, SOFRER, PERDER).
- **Fechamento**: frase curta de efeito ("Nem fudeno.", "Se o diretor gosta de você, se prepara.",
  "Aí você se entrega sozinho."), CTA ("Me segue aí, porque até as paredes da Disney escondem
  histórias!") ou a revelação do porquê.
- **Tom**: falado, com gíria ("mano", "caraio", "tanso", "foi de arrasta", "estressadinha", "nem
  fudeno") e conversa com quem assiste ("lembra?", "repara", "pensa nisso", "antes de me tacarem pedra").

## Scripts desta skill (`scripts/`)

Os `.py` (`folhas.py`, `recortes.py`, `janela*.py`) precisam de Python com `numpy` e `pillow` e o
`janela-cena.py` lê `G:/ClaudeEditor/...` por padrão: **só no PC do Levi** (ou instale `numpy pillow`).
Os `.mjs`/`.js` de CDP rodam em qualquer PC com o Dangai aberto na porta.

| script | o que faz |
|---|---|
| `cdp.mjs js <f.js>` / `foto <png>` | JS e print no Dangai (`PORTA=9353` = dev; padrão 9354 = instalado) |
| `soltar.mjs x y <arq...>` | solta arquivos na janela |
| `clicarxy.mjs x y`, `tecla.mjs <tecla> [n]` | clique e teclas |
| `c.sh "<texto>"` (+ `clicar.js`) | clica no botão com o texto |
| `dados-das-folhas.js <rascunho> <episodio> [take]` → `folhas.py` | folhas de candidatas por frase (*Gerar recap; só no PC do Levi*) |
| `recortes.py <projeto.dangai> <saida>` | recorte 9:16 no começo/fim de cada cena (*só no PC do Levi*) |
| `janela.py <projeto.dangai> <saida>` | quadro inteiro com a janela 9:16 desenhada (*só no PC do Levi*) |
| `folha-final.py <projeto.dangai> <saida>` | **conferência final**: todas as cenas como o Dangai mostra (focusX/câmera + zoom do efeito), 1º e último quadro |
| `seguir-rostos.mjs <lista>` / `ctrlz.mjs` | Seguir o rosto em lote (clica embaixo do bloco) / desfazer |
| `janela-cena.py <projeto.dangai> <saida> 3,10,26` | cenas escolhidas: 3 quadros com a janela + 3 do resto do clipe (achar `focusX`/`sourceStart`) (*só no PC do Levi*) |
| `fabinho/folhas-do-projeto.cjs <lista.txt> <saida>` | **qualquer PC (Node + ffmpeg)**: tabela frase a frase (fala, clipe, foco, entrada, efeito, transição) + folha com 1 quadro de cada cena no recorte 9:16 |
| `fabinho/medir-projetos.cjs <lista.txt> <saida.json>` | números de cada projeto: ritmo, gancho, foco, entrada, efeitos, legenda, faixas de som, cor |
| `fabinho/comparar-com-a-biblioteca.mts <lista.txt>` | o que a Biblioteca montaria (contas do `shared/trecho.ts`) × o que ficou: cortes iguais/movidos, efeitos trocados (`npx tsx`, `DANGAI_REPO` = clone do Dangai) |

`lista.txt` = um caminho de `.dangai` por linha. Tudo só **lê** os projetos.

No repo do Dangai (fora da skill, `_medida/`, ignorado pelo git): `rostos-diag.ts` (decisão de
rosto da Edição rápida contra um foco de referência) e o estudo do corte em
`G:\ClaudeEditor\_capturas\corte-v3\cont` (`regra.py`, régua do gabarito) — *só no PC do Levi*.
