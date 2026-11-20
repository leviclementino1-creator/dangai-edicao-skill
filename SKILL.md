---
name: dangai-edicao
description: Editar um short de recap de anime no Dangai do começo ao fim, no estilo do Levi e do Fabinho/Faah (o mesmo estilo; só a legenda muda) — pelo Gerar recap (Levi: episódio, roteiro, voz, aba Cenas, Edição rápida) ou pelo editor normal (Fabinho e Ajk: narração + roteiro .txt, cenas na Biblioteca, timeline; o gosto do Ajk na seção 11). Cobre ritmo, gancho, imagem por palavra, enquadramento 9:16, ponto de entrada, efeito, transição, legenda, som, cor e roteiro; controlar o Dangai por CDP; o formato do .dangai e do rascunho; medidas offline e armadilhas. Use em QUALQUER pedido de "edita no Dangai", "faz o processo todo", "edita do meu jeito", "compara com a sugestão do app", "ajusta enquadramento/legenda/cenas do projeto", ou para entender por que a Edição rápida errou.
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
| **Ajk** | **editor normal** (NÃO usa o Gerar recap): narração + roteiro `.txt` + cenas marcadas na Biblioteca, ajusta na timeline. Gosto próprio (legenda, som, transição, gancho) | **10 e 11** (+ 9 para o que é igual) |

Na dúvida de quem é o projeto (para a legenda e o fluxo): `modulos.recap` no `.dangai` = Gerar recap (Levi).
Sem `modulos.recap`, clipes em `E:\work\avatar cuts\...` e narração em `Downloads\Focus HUB\...` ou
`E:\AniPoison\Audios\...` = projeto do Ajk (seção 11).

Dangai = Electron + Remotion, repo `faahpla/dangai` (clone em `G:\ClaudeEditor\dangai` *só no PC do
Levi*; no PC do Fabinho, `E:\Projetos\dangai`; no PC do Ajk não tem clone — script que pede
`DANGAI_REPO` precisa de um `git clone --depth 1` numa pasta temporária).
`modulos/recap` e `modulos/thumb` são do Levi; o resto (núcleo) é do Faah — mudança no
núcleo entra pequena, um assunto por commit, e o Levi avisa o Faah. Responder ao Levi em
português, curto e simples.

## 00. PRIMEIRO: o perfil de quem edita (perguntar na 1ª vez)

Antes de editar, leia `perfil.local.md` (nesta pasta da skill; é de cada PC e não vai pro git).
**Não existe?** É a primeira vez neste PC: faça as perguntas abaixo, grave as respostas nele e
só então comece. Existe? Use sem perguntar de novo (pergunte só o que faltar, ou se a pessoa
disser que mudou).

Antes das perguntas, colete o que dá para MOSTRAR como opção (nada de pedir para digitar o que
o Dangai já sabe):
- `estado` do MCP (se não conectar: o módulo **Claude (MCP)** em Configurações > Módulos e o
  comando da seção dele — seção 1a);
- **o módulo "Gerar recap" ligado** (Configurações > Módulos): sem ele não há corte do episódio,
  reconhecimento de personagens (`reconhecer_personagens`/`listar_episodios` respondem "O modulo
  Gerar recap esta desligado"), Edição rápida nem o fluxo de recap. Desligado? Peça para ligar
  antes de começar (o editor normal + Biblioteca funciona sem ele, mas sem o corte);
- `presets_de_legenda` → os nomes dos presets que a pessoa já salvou no Dangai;
- `buscar_na_biblioteca {favoritas: true}` → quantas cenas favoritas ela tem;
- `recentes` do settings (SÓ esse campo) → se os projetos têm `modulos.recap` (usa o Gerar recap).

Perguntas (AskUserQuestion, no máximo 4 por vez, a recomendada primeiro):
1. **Como você edita?** Gerar recap (episódio → roteiro → voz → cenas, seções 2–4) ou editor
   normal (narração + roteiro `.txt` + Biblioteca, seção 8).
2. **Qual legenda?** Um dos presets salvos (liste os nomes), "o estilo que já está no projeto" ou
   "nenhuma". Aplicar com `presets_de_legenda {aplicar: "<nome>"}` e conferir `diferencas`
   (fontNome diferente = a fonte do preset não está instalada neste PC: avise).
3. **Cenas favoritas** (a estrela da Biblioteca — tem N): usar primeiro quando servirem / só no
   gancho / não usar.
4. **Música e efeitos:** os da Edição rápida (padrão) / uma pasta sua / sem música.
5. **Seta e outros overlays:** arquivo da seta + o som dela (o Levi: seta Pngtree + Ping), ou não usar.
6. **Cena ruim que eu achar na conferência:** troco direto (padrão do Levi: "sim ué") ou pergunto antes.
7. **Título, descrição e hashtags:** eu escrevo no fim (`editar.textos`) ou você faz.

Formato do `perfil.local.md` (curto, uma linha por item):
```
quem: Levi | fluxo: gerar-recap | legenda: Kiumaz v1 | favoritas: primeiro
musica: edicao-rapida | seta: <caminho> + Ping | cena-ruim: trocar-direto | textos: eu
```
Exemplo do Ajk (editor normal; a legenda depende do canal, ver seção 11):
```
quem: Ajk | fluxo: editor-normal | legenda: pelo canal (rosa / amarelo / LuckiestGuy) | favoritas: ?
musica: pelo canal (Pensando / GONE TOO FAR / CLIMA LINDO) | seta: E:\work\edits for faah\SETA.mov + Ping -3 | cena-ruim: ? | textos: ?
```
Fixo, sem perguntar: nada pago sem confirmar (Gemini, ElevenLabs, Fish), nunca imprimir chave.

**As duas favoritas que existem** (não confundir):
- **Dangai** (a estrela na Biblioteca): `favoritos.json` no userData, ids `<serie>/<SxxExx>/<shot>`.
  É esta que o MCP lê (`buscar_na_biblioteca {favoritas: true}`; cada clipe traz `favorita`).
  São as cenas que a pessoa gosta: quando uma serve para a palavra, ela ganha das outras.
- **AnCut** (Favs → anime → personagem, na tabela `favorite` do banco do AnCut): o Dangai não lê;
  entra junto quando um episódio vai/volta do AnCut. Para usar, peça à pessoa que favorite também
  na Biblioteca do Dangai.

## 01. Projeto novo: o que pedir (TODO projeto)

Todo vídeo novo precisa de três coisas. Se a pessoa não mandou tudo numa mensagem, peça **só o
que falta, numa mensagem curta** (com a lista abaixo) antes de começar. **Primeiro descubra o
tipo** (pelo roteiro, ou pergunte):
- **Recap de um episódio** ("o que aconteceu no ep 7") → Gerar recap: precisa do **episódio**.
- **Curiosidade / vários episódios** ("por que a Maomao…", "o poder da Shion") → **editor normal
  + Biblioteca** (seções 3 "Vídeo de CURIOSIDADE" e 8): basta o **nome do anime**; as cenas saem
  dos episódios já cortados na Biblioteca. Peça episódio só se o que o roteiro cita não estiver
  cortado lá (`buscar_na_biblioteca {anime}` mostra quais episódios existem).

1. **O anime** (curiosidade) **ou o anime + episódio** (recap): o arquivo (`.mkv`/`.mp4`) ou o
   nome + episódio. Só o nome? Procure primeiro no PC: Biblioteca (`buscar_na_biblioteca
   {anime, episodio}`), pastas do AnCut, Downloads. Não achou: peça o arquivo. **Nunca baixe
   episódio** por conta própria.
2. **O roteiro** (o texto que a voz fala). É a fonte da verdade da legenda e das cenas.
3. **O áudio** da narração (`.mp3`/`.wav`; pode vir em 2: gancho + resto). Sem áudio e quer voz
   gerada (ElevenLabs/Fish)? É pago: confirme antes.

**Opcional, mas sempre ofereça:** cenas extras que a pessoa já sabe ("isso acontece no ep 1",
"usa a cena da expulsão", um clipe ou print). Diga que ela pode mandar junto.

**Antes de escolher as cenas, leia o roteiro procurando o que é de OUTRO episódio** (flashback,
"depois de ser expulso", "lembra quando…", poder/personagem que não aparece no ep atual). Para
cada um:
- já está cortado na Biblioteca? Use (`buscar_na_biblioteca` pelo anime/episódio);
- não está: diga qual episódio é (se você sabe a história; se não, ofereça pesquisar — wiki/guia
  de episódios) e **peça o arquivo daquele episódio**, ou pergunte se ela prefere seguir só com o
  episódio atual. Não improvise com uma cena parecida do ep atual sem avisar (Laid-Off S01E07:
  "expulso da antiga guilda" é o ep 1; usei uma cena do ep 7 e o Levi notou).

Pode começar a **analisar o episódio** assim que ele chegar (o corte leva ~3–4 min, por trás)
enquanto espera o roteiro e o áudio. Deixe **"Reconhecer personagens" marcado**.

**Confira o reconhecimento de personagens depois do corte** *(só para quem corta o episódio pelo
Gerar recap ou pelo AnCut; o Ajk usa episódios já cortados em `E:\work\avatar cuts`)* (os nomes por cena no `episodio.json`:
`planos[].personagens`). Ele é o que faz a Edição rápida enquadrar o personagem que a frase cita, a
sugestão de cenas e a busca por personagem na Biblioteca. Monte a folha de keyframes e compare: o
nome bate com o rosto? No Laid-Off S01E07 (17/11) estava errado — a Lily saía "Ells, Margaret",
o Barrius "Radiant Dragon" — porque os grupos de rostos nunca foram batizados e o automático usou
fotos de referência ruins do anime. Nome errado: **não confie neles para escolher/enquadrar**
(escolha pelas folhas) e conserte, conforme quem cortou:
- **Cortado pelo motor do Dangai** (Biblioteca do recap): **pelo MCP (2.11.2+)**
  `reconhecer_personagens {acao:"iniciar", episodio:"ep_..."}` (o id vem de `listar_episodios`;
  agrupa em ~20 s–2 min, GPU) → ele devolve as folhas: uma linha por grupo com até 8 rostos e,
  por último, o elenco com foto → você dá o nome de cada grupo → `{acao:"confirmar", jobId,
  decisao:{nomes:{"0":"Nia Liston"}, ignorados:[], juntar:[], removidos:{}}}` (`cancelar` = nada
  muda). Sem MCP: `scripts/reconhecer.mjs` + `folha-grupos.py` pelo CDP, igual. As fotos viram referência: o próximo episódio do anime já vem
  certo. Regras dos nomes:
  - personagem que JÁ TEM NOME (`conhecido`) num grupo: use **esse mesmo texto** nos outros grupos
    dele (no Nia é "Nia Liston", não o "Liston, Nia" do elenco) — nome diferente vira outro personagem;
  - personagem novo: o nome **exato** do elenco;
  - grupo misturado, figurante ou rosto que você não tem certeza: **sem nome** (ignora) e, se for
    importante, pergunte. Rosto de outra pessoa infiltrado num grupo bom: `removidos {key: [i]}`.
  - Testado no Nia S01E04 (19/11): 56 grupos, elenco de 22 com foto; cancelado sem gravar.
  Quando a pessoa faz o projeto inteiro comigo (corte incluído), eu faço isso logo depois do corte,
  antes de escolher as cenas.
- **Cortado pelo AnCut** (cenas em `G:\App Corte Cenas\Output\...` *só no PC do Levi*; no do Ajk os shots ficam em `E:\work\avatar cuts\<anime>\SxxEyy\shots`; o Dangai responde "Cenas do
  AnCut: o recap so le"): o reconhecimento é **no AnCut** (Modo Descoberta; os grupos ficam em
  `<episódio>/metadata/discovery/descoberta.json`). Mexer no AnCut só com o OK da pessoa: mostre
  os grupos (`g000_*.jpg`) com o nome que você daria a cada um e peça para ela batizar lá (ou
  peça o OK para você fazer).

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

### 1a. PRIMEIRO: o MCP do Dangai (desde a 2.10.4) — use isto para editar

O módulo **Claude (MCP)** (Configurações > Módulos > ligar; a seção "Claude (MCP)" mostra o
comando) põe um servidor MCP dentro do Dangai. Conectado uma vez com
`claude mcp add --transport http dangai http://127.0.0.1:47321/mcp --header "Authorization: Bearer <senha>"`,
as ferramentas aparecem como `mcp__dangai__*`. **Editar o projeto aberto é por elas** — sem fechar o
app, sem mexer no `.dangai` em disco, sem clicar por coordenada, sem print da tela:

| ferramenta | o que faz |
|---|---|
| `estado` | projeto aberto, duração, nº de cenas/sons/imagens, Biblioteca |
| `listar_cenas` (de, ate) | cena n (1 = a 1ª): início/fim, clipe, entrada, focoX, efeito, câmera, grid, zoom fixo |
| `ver_cenas` (cenas[]) | **IMAGEM** do 1º e do último quadro de cada cena no recorte 9:16 (o folha-final, em ~1 s) |
| `ver_clipe` (caminho, focoX) | 8 quadros do clipe inteiro no 9:16 → escolher o **melhor momento** (entrada) |
| `editar` (lote) | TUDO num pedido: `cenas[]` {cena, clipe, entrada, focoX, efeito, intensidade, zoomFixo, origemDoZoom, camera:"desligar", grid:{clipe,entrada,focoX}\|"desligar"}, `sons.adicionar/remover`, `imagens.adicionar/remover` (seta: x/y em % do quadro, escala, rotacao), `legenda` (campos caption*), `textos` {titulos, descricao, hashtags} |
| `listar_faixas` | sons e imagens por cima com id (para remover) |
| `desfazer` | volta o último `editar` |
| `buscar_na_biblioteca` | clipes de qualquer episódio por texto/personagem/episódio/anime; `favoritas: true` = só as da estrela; cada clipe traz `favorita` |
| `presets_de_legenda` (aplicar) | os presets de legenda salvos, qual bate com o projeto (`diferencas`) e `aplicar: "<nome>"` |
| `listar_episodios` | os episódios do Gerar recap (`ep_...`, título, passo) |
| `reconhecer_personagens` (acao, episodio, jobId, decisao) | o **Reconhecer na mão**: `iniciar`/`ver` → folhas dos grupos de rostos + do elenco; `confirmar` com os nomes; `cancelar` (seção 01) |
| `abrir_projeto` (caminho) | abre um `.dangai` |

Regras de uso:
- **Um lote por rodada** (cada `editar` valida, grava e REABRE o projeto: ~8–10 s). Junte todas as
  mudanças; depois `ver_cenas` das cenas mexidas para conferir. Lote com erro (cena que não existe,
  arquivo que não existe, campo inválido) não grava nada.
- O checklist da seção 3 continua valendo: `ver_clipe` para achar o melhor momento, `ver_cenas`
  para conferir rosto/centro, `buscar_na_biblioteca` para curiosidade (cenas de outros episódios).
- **Seta + Ping juntos** no mesmo lote (seta do Levi + Ping −10 dB, ver seção 3).
- **Título, descrição e hashtags: escreva você** no `textos` do `editar` ao terminar (não precisa do
  Gemini). A thumbnail ainda é pelo módulo Thumbnail.
- *(só para quem usa o Gerar recap)* O MCP **não** cobre o Gerar recap (roteiro/voz/aba Cenas): esses passos continuam pela ponte
  `window.dangai.modulos.recap` por CDP (abaixo). O MCP entra depois do *Abrir no editor*.
- Sem o MCP conectado (módulo desligado, versão < 2.10.4): use o caminho antigo abaixo.
- Conectou o MCP no meio da conversa? As ferramentas só aparecem numa conversa nova. Até lá:
  `scripts/mcp.py <ferramenta> '<json>' [prefixo]` (senha em `DANGAI_MCP_SENHA`). Nunca montar o
  JSON-RPC em bash com `${2:-{}}`: o `}` quebra os argumentos e a ferramenta recebe `{}` CALADA
  (`listar_cenas` devolve tudo, `editar` diz "Nada para mudar").
- **`ver_cenas` não desenha a metade de baixo do grid** (só a de cima): grid se confere no preview
  do app.

### 1b. CDP (o caminho antigo, e para o Gerar recap)

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
(*só no PC do Levi*; no do Ajk: `C:/Users/ajk/Documents/Dangai/Recap/Biblioteca` ou `E:/work/avatar cuts`) + reload. Matar: processos com `tmp-thumbui` na linha de comando.

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
2. **Roteiro**: *Meu roteiro* cola o texto dele (linha em branco = parte; agrupe pelas seções dele).
   Depois de colar, o app chama o Gemini pra "Ler" o episódio e "Ligar" as frases (5+ min no
   Laid-Off S01E07, 17/11). Quando EU escolho as cenas, **Cancelar** na hora: o texto já está
   gravado, *Aprovar roteiro* funciona e a sugestão de cenas é local. O gancho "vira 2 ou 3 cenas no passo Cenas".
   A imagem de cada frase é só o MOMENTO, não a cena final.
3. **Voz**: *Importar áudio* (pode soltar 2: gancho + resto, emenda pela ordem do nome).
   **Quando EU edito para o Levi: Acelerar = 1,10x** antes de soltar o áudio (pedido dele 17/11:
   "110% sendo o normal"; o padrão do app nas Configurações pode estar em 100% — não confie nele,
   ponha o controle em 1,10x na tela). Fresh Air desligado, salvo pedido.
   Cortar pausas **Justo** (padrão novo) > *Aplicar* > *Aprovar voz*. ElevenLabs quase não
   tem pausa longa (89,5 → 89,1 s).
4. **Cenas**: 26 frases, cada uma com cenas + "palavraInicio" (em que palavra a cena entra).
   - Frase **travada** (cadeado) não muda no *Sugerir de novo*; destravar = clicar nos botões
     com title `Travada: ...`.
   - *Sugerir de novo* (rodapé) refaz as não travadas.
   - *Abrir no editor* (com *Edição rápida* marcada) monta o projeto numa pasta nova em
     `G:\Dangai Recap\Biblioteca\_projetos\<anime SxxEyy - data>` (*só no PC do Levi*).

## 3. Escolher cenas (o que o Levi espera)

### O que o Levi corrigiu à mão no Nia S01E07 (diff 17/11 — aprender com isso)

*Os caminhos `I:\Meu Drive\...` (biblioteca Eagle: seta Pngtree, Ping, OPPAI, MONEY) são **só no PC do
Levi**. No PC do Ajk a seta é `E:\work\edits for faah\SETA.mov` e os SFX ficam em
`C:\Users\ajk\Documents\sound effects` (Ping, Camera Shutter, Stinger, riser — ver seção 11).*

- **SFX ligado ao que se vê/ouve na fala**, tirando os genéricos: removeu os 2 whooshes de troca
  de parte; pôs `MONEY SOUND EFFECT` (−5 dB) em "ganhar uma FORTUNA" (0:01), `Ping` (−10 dB)
  junto com a seta na tatuagem, `Cartoon Bounce Sound Effect(OPPAI)` bem baixo (−26 dB) na
  atendente pondo as fichas no peito. Som de dinheiro no dinheiro.
- **REGRAS FIXAS (Levi 17/11)**:
  - **Toda seta leva o `Ping`** (`I:\Meu Drive	fpn.library\images\MG9JN2W3P9XE3.info\Ping sound
    effect.mp3`, −10 dB, no começo da seta). Sempre.
  - **A seta é a DELE**: `I:\Meu Drive	fpn.library\images\MG9JNBOML9R8M.info\—Pngtree—red thick
    line stroke arrow_5569080.png` (1200x1200, `aspecto` 1). **Nunca** a `seta-ajk.png` do módulo
    thumb. Dele: escala ~0,32, girada pra apontar o detalhe, sem efeito.
  - **`Cartoon Bounce (OPPAI)`** (`...MGSBW03VG6K3B.info\`) é ESPECÍFICO: só com peito bem
    próximo na tela ou balançando muito. Fora disso, não.
- **Seta**: trocou a minha pela **dele**, da biblioteca Eagle `I:\Meu Drive	fpn.library`
  (pasta Levi > Channels > **Kiumaz > PNG**; `—Pngtree—red thick line stroke arrow`), parada
  (sem efeito), girada (105°), escala 0,32, apontando de cima pra tatuagem. Use os PNGs/SFX da
  pasta **Kiumaz** dessa biblioteca (PNG, efeitos sonoros, Music, Ambient, Emojis):
  `images/<id>.info/` com `metadata.json` (nome, pasta); pastas no `metadata.json` da raiz.
- **Música**: manteve a troca no começo da parte (0:24,9), mas voltou o 1º trecho pra parte da
  faixa que ele gosta (56,4 s) e pôs **ducking** na 2ª (abaixa 6 dB sob a voz); a 2ª entra
  pulando o silêncio (1,5 s).
- **Enquadramento fino**: empurrou o focusX +0,05…+0,2 rumo ao centro do assunto (soco do
  tatuado, coelhinha, Nia no fim) e na torre de fichas foi pra 0,65 pra mostrar o Gandolf junto.
- **Zoom fixo do bloco** (`escala` 1,3 + `escalaOrigem` {x:0,y:1}) na Nia entregando as fichas:
  aproxima ancorado no canto onde está a ação.
- **Câmera livre**: na Nia de perfil (0302) fez a câmera **deslizar** (x −11 → −26) em vez de
  parada com zoom.

### Vídeo de CURIOSIDADE: cenas de vários episódios (Levi 17/11)

Recap = um episódio. **Curiosidade** ("Por que…?", "Você sabia…?", personagem, poder, história)
fala de coisas espalhadas pela série: a cena certa pode estar em OUTRO episódio. Então:
- A **Biblioteca** do Dangai (desde a 2.10.1 = a pasta do AnCut, `G:\App Corte Cenas\Output`, +
  a raiz do recap `G:\Dangai Recap\Biblioteca` — *só no PC do Levi*; no do Ajk: `E:\work\avatar cuts`
  + `C:\Users\ajk\Documents\Dangai\Recap\Biblioteca`) tem todos os episódios já cortados da série:
  busque por personagem/episódio (Ctrl+B, filtro de personagem) e use cena de qualquer um.
- No `.dangai`, uma cena de outro episódio é só o `path` do shot dele em `images[]`
  (`<saida do AnCut>\<anime>\SxxEyy\shots\<numero>.mp4`); os planos de cada episódio estão no
  `metadata/shots.json` do AnCut (personagem, tempo) ou no `episodio.json` do recap.
- Faltou o episódio que tem o momento? Corte ele (Gerar recap > Analisar, ou o AnCut) — ele entra
  na Biblioteca — e pegue a cena de lá.
- *(só para quem usa o Gerar recap)* O Gerar recap trabalha com UM episódio por rascunho: para curiosidade com vários, monte pelo
  recap do principal e troque/insira as cenas dos outros no editor (*Trocar cena* abre a
  Biblioteca inteira) ou direto no `.dangai`.

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
12. **Som que conta a cena**: SFX só onde a imagem/fala pede (dinheiro = MONEY; **seta = Ping,
    sempre**; OPPAI só com peito bem próximo/balançando), não whoosh genérico; música com ducking.
13. **Recursos**: grid em "um x outro" (dois personagens diferentes e legíveis); seta no detalhe
    que a fala cita; personagem vistoso de corpo inteiro "dá view" — encaixe onde a fala cita.
14. **Sem sangue/violência gráfica em destaque** (corpo ensanguentado no chão) e nada que fira a
    regra da plataforma.

**Conferência final obrigatória**: `scripts/folha-final.py <projeto.dangai> <saida>` (ou o
`ver_cenas` do MCP) — as cenas como o Dangai mostra (recorte do focusX ou da câmera + zoom do
efeito, 1º e último quadro). Olhe TODAS antes de entregar; o Levi não pode ser quem acha.

**E as 3 medidas, com número, não a olho** (Laid-Off S01E07, 17/11: o Levi achou olho gigante,
Nina no canto, boca sem olhos, rosto no copo e um começo borrado — tudo que a folha pequena
deixou passar porque eu medi o foco a olho numa miniatura):
1. **Rosto no centro**: `scripts/rostos-cenas.py` (detector do motor, 3 instantes por cena) →
   `focusX = (cx − 0,158)/0,684` do rosto de **quem a frase cita** (não o maior: o maior pode ser
   um queixo cortado na borda — foi o que jogou a Nina pro canto). Confira nas folhas `fc_N.jpg`
   (rostos em verde, janela em rosa). Rosto colado na borda (a janela não alcança): zoom fixo 1,3
   com `origemDoZoom.x` puxado pro lado dele.
2. **Close extremo = TROCAR ou GRID, nunca tela cheia** (Levi: "nunca mais usa assim"). Medida:
   altura do rosto > 0,75 do quadro 16:9, ou só olho/boca/pedaço de rosto (o detector nem acha).
   No grid, o close vai em cima e embaixo **outra pessoa** (nunca a mesma — "pessoa em comum").
   Exemplos que ficaram bons: Elsie close / Rein; Lily gritando / Elsie; Elsie "trabalhar pra
   ele" / os funcionários da guilda dele.
3. **Nada borrado**: `scripts/nitidez.py <projeto>` lista cena com trecho < 45% da nitidez do
   clipe (foco mudando no começo, fade, pan). Conserto: `entrada` depois do borrão (o 0199 do
   Laid-Off só fica nítido em ~1,5 s).
Também: cena que começa no peito/casaco e sobe pro rosto (tilt) → `entrada` já no rosto.

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
- *(só para quem usa o Gerar recap)* Método: folha por frase com as sugestões (fita) + todos os planos no intervalo do evento e
  ±8 s do momento (`scripts/folhas.py`, rosa = escolha do app, azul = fita). Das 60 cenas que
  escolhi no S03E07, 27 vieram de fora da sugestão.
- *(só para quem usa o Gerar recap)* Gravar as escolhas pela ponte (`salvarCenas`, origem `usuario`, `travada: true`) e recarregar
  a tela (`location.reload()` → Gerar recap → Continuar).

## 4. Depois de abrir no editor (gosto do Levi, com a Edição rápida) *(só para quem usa o Gerar recap)*

*A Edição rápida é do Gerar recap. Quem edita no editor normal (Fabinho, Ajk) monta pela Biblioteca:
ver seções 8–11. As regras de enquadramento, entrada e câmera daqui valem para qualquer um.*

- **Música**: a da Edição rápida é melhor que a minha (feedback dele 13/11) — não trocar por gosto.
  O que ele cobra: **o clímax (drop) da música entra junto com o fim do riser** da saída do gancho.
  Conferir na trilha: a 1ª música tem `inicioSec` = (drop do arquivo − saída do gancho), não o
  começo do arquivo. Entre 17/11 (e7e2dfc) e 18/11 (8c42e64) a Edição rápida tirava o drop
  quando a faixa mal cobria o trecho; projeto montado nessa janela precisa de conserto.
  **O detector de drop (`entradas.ts`) adianta nas músicas com subida antes da pancada**: na
  Montagem Batchi marcou 16,9 s e o clímax é 19,2 s (o Levi corrigiu à mão: `inicioSec` 13,08 =
  19,2 − 6,15). Sempre conferir o drop pela onda (RMS de 0,2 s: o salto do grave/batidas) antes
  de entregar. No Laid-Off ele também tirou a 2ª música (Naruto): uma música só no vídeo todo.
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
  Medir: `scripts/movimento.py <projeto>` (diferença entre quadros dentro do recorte,
  < 1 = parada; roda no PC do Ajk) e `mov-todos.py` (movimento de todo plano do episódio + melhor
  janela; em `_capturas/e2e-nia/`, *só no PC do Levi*).
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
  arquivo inteiro no quadro): a seta do Levi (Pngtree red thick line stroke, ver "REGRAS FIXAS"),
  **nunca** a `seta-ajk.png`; sempre com o `Ping`. Simule com PIL antes.
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

**No app instalado (Laid-Off S01E07, 17/11):**
- O botão **"Legendas"** da barra do editor é um interruptor: **DESLIGA a legenda** (não abre
  painel). O painel de estilo é o **"Estilo"**.
- Com o painel **Estilo aberto**, clique na régua da timeline cai nos controles dele (mudou o
  tamanho da legenda pra 290% sem querer). Feche o painel (clicar "Estilo" de novo) antes de
  clicar na timeline; depois confira os `caption*` no `.dangai`.
- Legenda do Levi = preset **Kiumaz v1** (está em `captionPresets` do settings; a Edição rápida
  já aplica). Confirmar campo a campo no `.dangai`: Bangers, amarelo, escala 2,1, y 0,45,
  elástica 7 quadros, marcar tudo, pontuação `limpar` ("Só ? ! %"), contorno 11, sombra 3 px.
  Ele cobra se parecer diferente: mostre que bate, e reaplique clicando no chip "Kiumaz v1".
- Mediu e ficou ruim? Ele quer a cena trocada **na hora**, sem perguntar ("sim ué").
- **Frase que cita outro episódio** ("depois de ser expulso da antiga guilda" = a expulsão do
  ep 1): a cena certa é a DAQUELE episódio. Procure com `buscar_na_biblioteca` (anime/episódio);
  se o episódio não está cortado, **peça o arquivo ao Levi** antes de improvisar com o que o ep
  atual tem (no Laid-Off S01E07 usei o Rein gritando "você me expulsou?!" do ep 7 e ele notou).
- Cena que não mostra QUEM a frase cita é cena errada, mesmo bonita ("a própria mestre tava
  tentando acabar com ela" com a Lily chocada → errado; é a Elsie sorrindo no "Essa guilda acabou!").

- **Trocar uma cena direto no `.dangai`** (app fechado): mude `images[i].path/fileName/focusX`
  (`focusAuto:false` se o foco é escolha sua) e `scenes[k].sourceStart`. Uma entrada de
  `images` pode ser **dividida por duas cenas** (o 0192 do gancho e do fim) — duplique antes de
  mexer. No fim tire as entradas sem uso e renumere `imageIndex`: a faixa "Cenas N" do topo
  conta `images`, não blocos. Guarde backup em `G:/tmp-medida\` (*só no PC do Levi*; em outro PC, uma pasta temporária) antes de cada rodada.
- *(só para quem usa o Gerar recap)* Mantenha a aba Cenas do recap igual ao projeto: `salvarCenas` pela ponte (app aberto) com a
  troca (`inSec` = início do plano + `sourceStart`). Não gravar o rascunho em disco pelo Claude:
  o `%APPDATA%` dele (MSIX) é virtual e o Dangai não vê.
- `Start-Process` do Dangai às vezes não sobe (porta recusada): confira
  `http://127.0.0.1:9354/json/version` e abra de novo. O Levi pode fechar o app entre os pedidos.
- A escala da régua muda entre aberturas: depois de clicar na agulha, **leia o tempo** na tela
  antes de afirmar qual cena está no preview.
- *(só para quem usa o Gerar recap)* Refazer com áudio novo e quase o mesmo roteiro: *Meu roteiro* → importar voz → levar as
  escolhas antigas por LCS das palavras da frase (`G:\ClaudeEditor\_capturas\e2e-apo\levar-escolhas.js`, *só no PC do Levi*,
  com sinônimos tava/estava) → `salvarCenas` → *Abrir no editor*.

- **Biblioteca sem o episódio** (*os caminhos `G:\` abaixo são só no PC do Levi*): com "Enviar sempre para o AnCut" o episódio é cortado na pasta do
  AnCut (`G:\App Corte Cenas\Output`); a Biblioteca só lê a `libraryDir` + a raiz do recap
  (`G:\Dangai Recap\Biblioteca`). No PC do Levi a `libraryDir` estava vazia → E07 sumia. Corrigido
  apontando pra pasta do AnCut (17/11) e no núcleo: vazia = pasta do AnCut (commit local, a publicar).
- `cdp.mjs` embrulha o JS num template do Node: **`\` some** (`"G:\App"` vira `G:App`). Caminho no JS
  enviado por CDP sempre com `/`.
- `window.dangai.getSettings()/saveSettings()` devolvem `{ok, value}`.
- **Antes de reabrir um `.dangai` editado à mão, valide** (`projectFileSchema.safeParse`, ver
  `_capturas/e2e-nia/rodada3.js`, *só no PC do Levi*): um `focusX` undefined fez o Dangai dizer "está corrompido".
- **Corrigido na 2.10.2** (17/11): a Edição rápida usa zoom (2 zoom-in, 1 zoom-out) em vez do
  rodízio com pan, corte seco na virada de parte, e a música respeita o fim que some
  (`fimUtilDaMusica`, 9 LU abaixo do integrado) e recomeça no começo do som. Projetos montados
  antes disso ainda têm o problema abaixo. A 2.10.1 pôs a pasta do AnCut como Biblioteca padrão.
- **Troca de música** da Edição rápida cai onde a 1ª faixa ACABA (S01E07: 0:32, no meio da frase,
  e a faixa nova começa com 1 s mudo = buraco). Pôr a troca no começo de uma parte do roteiro, onde
  já tem o whoosh (`usarSec` da 1ª = início da parte; `at` da 2ª = esse tempo, `inicioSec` pulando
  o silêncio do começo da faixa — medir o RMS).
- **Música que some**: a Edição rápida pode começar a faixa tarde e o trecho cair no fim que
  some (S01E07: 57,8 s → fim em 90 s, vazio de 0:20 a 0:32). Medir o RMS por segundo da música
  e mover `inicioSec` pra o trecho não passar do fade.
- *(só para quem usa o Gerar recap)* **Recortar o episódio** deixa as escolhas antigas do rascunho apontando pra outras cenas
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

## 10. Editor normal (sem Gerar recap) — o fluxo do Ajk

O Ajk **não usa o Gerar recap** (nem roteiro com IA, voz, aba Cenas, rascunho ou Edição rápida). Medido
em 20 projetos dele (07–19/11/2026, `recentes` + `C:\Users\ajk\Documents\Dangai\Projetos`), só leitura,
com `fabinho/medir-projetos.cjs` e `ajk/comparar-com-a-biblioteca.ts`. O único projeto do Gerar recap
(`Firefly Wedding S01E07`, 20/11, em `Documents\Dangai\Recap\Biblioteca\_projetos`) ficou fora das contas.

**Caminhos no PC do Ajk**

| o quê | onde |
|---|---|
| projetos `.dangai` | `C:\Users\ajk\Documents\Dangai\Projetos` |
| clipes (shots já cortados) | `E:\work\avatar cuts\<anime>\SxxEyy\shots\NNNN.mp4` (filme: `...\Black Clover\Filme (2023)\shots`; trailer: `...\CAPRI OFFICIAL TRAILER h264\...\shots`) |
| mangá / prints | `E:\work\edits for faah\Mangás\<anime>\` |
| seta | `E:\work\edits for faah\SETA.mov` (vídeo, ~2,5 s) |
| narração | `C:\Users\ajk\Downloads\Focus HUB\<título>\` e `E:\AniPoison\Audios\` |
| SFX | `C:\Users\ajk\Documents\sound effects` (+ `E:\AniPoison\bg songs\sfx\SFX`, `C:\Users\ajk\Media Hub\Library\raw`) |
| músicas | `C:\Users\ajk\Documents\music`, `E:\AniPoison\bg songs` |
| Biblioteca do recap | `C:\Users\ajk\Documents\Dangai\Recap\Biblioteca` |
| backup antes de mexer num `.dangai` | uma pasta em `%TEMP%` (nunca grave por cima do original) |

**Passo a passo**

1. **Narração**: soltar o `.mp3` na tela inicial → Etapa de Áudio com isolar voz, nivelar, EQ, compressor
   e normalizar **ligados em todos os 20**. Velocidade: 100% nos de 07–12/11, **120%** nos de 09–19/11
   (AniPoison, Rebecca, Shisui), **110%** nos mais novos (Jinshi 19/11). Pergunte se não souber.
2. **Roteiro `.txt`**: uma frase por linha (Focus HUB: 7–19 linhas; AniPoison: 16–34 linhas curtas,
   às vezes a frase quebrada em duas linhas).
3. **Biblioteca**: marca **1 ou 2 cenas por trecho** (mediana 1 nos curtos e no AniPoison, 2 nos
   Cyberpunk; até 4–6 num trecho longo). Peso às vezes (6 trechos na Capri/Lucy), tela dividida raro
   (9 em 20 projetos), puxar a fronteira quase nunca (1 vez). *Aplicar* monta a timeline.
4. **Timeline: o que ele corrige à mão** (o que a Biblioteca montou × o que ficou):
   - **Cortes: quase nada.** 97% ficam onde a Biblioteca pôs (847 de 875); 22 andam (~0,2–0,3 s,
     mais para antes), 3 novos, 3 tirados. **O ritmo sai das marcas na Biblioteca.**
   - **Troca de cena** na timeline em 5 de 20 projetos (a ordem final difere das marcas).
   - **Enquadramento**: arrasta o `focusX` em **42%** das cenas (374 de 892), deixa o rosto automático
     em 24% e o centro em 34%. Vai de 0 a 1: puxa até o rosto quando o personagem está no canto.
   - **Ponto de entrada** (`sourceStart`) em **18%** das cenas, mediana ~1,9 s (curtos da Apotecária
     2,3 s; AniPoison 1,9 s; Cyberpunk 1,0 s): pula o começo morto e pega o melhor momento.
   - **Efeito**: mantém o rodízio em 92% (troca 67 de 806). Trocas mais comuns: tirar o movimento
     (`nenhum`, ~17), `zoom-in` → `zoom-out` (~16), `pan-up` → `pan-down` (~7), `pan-left` ↔
     `pan-right`. Intensidade **sempre 0,1**, curva linear (ease-in-out em ~3%).
   - Câmera livre em ~3% das cenas; giro 0–5 por vídeo; tela dividida 0–4.
   - **Transição**: ver seção 11 (um `light` quando a história começa; o resto corte seco).
5. **Som** nas faixas A1–A4, **camada de ajuste** de cor no vídeo todo, `SETA.mov` quando o gancho
   precisa apontar alguém, legenda pelo preset do canal (tudo na seção 11), thumb e render.
6. **Conferir** antes de entregar (rodam no PC dele): `scripts/fabinho/folhas-do-projeto.cjs` (tabela
   frase a frase + folha 9:16) e `scripts/folha-final.py` (como o Dangai mostra, 1º e último quadro).

```powershell
# medir/comparar (só leitura). lista.txt = um .dangai por linha (use cópias numa pasta do %TEMP%)
node scripts\fabinho\medir-projetos.cjs lista.txt med.json
$env:DANGAI_REPO = "<clone do Dangai>"; node scripts\ajk\comparar-com-a-biblioteca.ts lista.txt cmp.json
node scripts\fabinho\folhas-do-projeto.cjs lista.txt folhas
```

## 11. Gosto do Ajk

Igual à seção 9 em: ritmo ~1,1–1,4 s por cena, ~4–5 palavras por cena, corte na vírgula e na palavra de
peso, rodízio de efeito com intensidade 0,1, rosto no recorte 9:16, cena de reação em gíria/emoção.
**Diferente** em: legenda (3 presets, pelo canal), cor, a transição `light` quando a história começa, música
mais alta na introdução, riser + stinger antes desse corte, e quase não repete cena nem volta ao gancho no fim.

### Os 3 tipos de vídeo dele (o tipo decide legenda, música e tamanho)

| tipo | projetos | tamanho | cenas | legenda | música | som no 0 s |
|---|---|---|---|---|---|---|
| **Curiosidade curta — Apotecária** (narração em `Focus HUB`) | Lakan, Lihua, Jinshi, Ah-Duo, Shisui, gatinha, venenos, Maomao casamento (8) | 29–38 s, 104–129 palavras, 7–12 linhas | 20–28; **1,36 s**/cena (~44/min); clipes de 3–9 episódios | **A rosa** | `Pensando.mp3` −20 dB, o vídeo todo | `Monologo.mp3` 0 dB |
| **Curiosidade longa — Cyberpunk / Black Clover** (`Focus HUB`) | Capri, Lucy, Rebecca, Yami (4) | 67–72 s, 239–258 palavras | 50–63; **1,18 s** (~49/min); 4–10 episódios + trailer, filme, mangá | **B amarelo** | `GONE TOO FAR` −15 na introdução → −20/−22 depois; às vezes troca na metade (OST de Edgerunners, type beat) | `cartoon-pop-up-2` 0 dB |
| **Recap de episódio — romance/shoujo** (narração em `E:\AniPoison`) | Ela descobriu, Ela mal conseguia, Essa princesa, Harij, Lorna, Minato, ELE TERMINOU (7) | 45–82 s, 197–344 palavras, 16–34 linhas | 41–75; **1,08 s** (~52/min); 1 episódio (no máx. 2), shots quase na ordem | **C LuckiestGuy** | `CLIMA LINDO.m4a` (ou `no signal (slowed)`) −22 dB | `thud-sound-effect` −7 dB (+ `RIZZ` 0 dB se abre com o galã) |

Exceção: `kiumaz seaven heavens` (12/11) usa Bangers `#FFF700`, escala 2,2, y 0,45, contorno 7 (perto do
Kiumaz v1 do Levi) e gancho de 1 cena ("Mano!"): é um vídeo no estilo do Levi, não o padrão do Ajk.

### Gancho

- **Curiosidade: 2–3 cenas de ~1,3 s** (gancho de 2,5–4,5 s). **Recap AniPoison: 4–7 cenas mais
  rápidas (~0,9 s)**: o gancho dele é uma frase longa com reticências ("Ela bebeu uma poção do amor e
  confessou tudo… mas depois foi ele que não conseguiu mais parar de pensar nela.").
- Sempre clipe do anime. A 1ª cena é **quem a frase cita** (Lihua, Jinshi, Rebecca, Yami); a última
  mostra **a coisa literal**: *Capri* "no seu computador?!" = o trailer real da Capri; *Rebecca* "um
  garoto chamado Kyle?" = a imagem da versão masculina no mangá.
- No recap, o gancho é **o clímax do episódio em shots seguidos** (*Harij*: 0351 → 0352 → 0353;
  *Lorna*: 0271 → 0272 → 0293 → 0313 → 0314).
- Entrada no gancho: costuma pular o começo do clipe (*Lihua* 6,2 s, *Shisui* 12,9 s, *Minato* 4,0 s).
- Efeito: o do rodízio (zoom-in, zoom-out, pan-left…); às vezes a 1ª vira `zoom-out`. *Lucy*: o mesmo
  clipe em duas cenas, sem efeito.
- `SETA.mov` em 5 de 19 (fora o kiumaz), ~1–1,2 s, **uma vez, no começo do vídeo** (0,6 s no gancho da
  *Ela descobriu*; 6,5–6,8 s, logo depois do gancho, em *Yami*, *Harij*, *Minato*; 2,5 s e 20,9 s na
  *Rebecca*), apontando o personagem que a fala cita. **O `Ping` (−3 dB) entra 0,28 s antes da seta**, sempre.
- Texto: "Você sabia que …?", "Por que …?" ou afirmação com "!" (Focus HUB); "Ela/Ele … … mas …"
  (AniPoison). Dois recaps recentes com o gancho **TODO EM CAIXA ALTA** (*Minato*, *ELE TERMINOU*).

### Transição (assinatura dele)

- **Um `light` onde a introdução acaba e a história começa** em **11 de 11** projetos longos
  (Cyberpunk/BC + AniPoison): quase sempre a 2ª ou 3ª frase, logo depois do gancho ("Depois de tanto
  trabalho,", "Durante uma viagem para a praia,", "Quando Lorna chega…"); na *Capri* e na *Lucy*, depois
  de 2–4 linhas de introdução ("Um fã chamado Overyx…", "David conhece Lucy…"). Às vezes um 2º `light`
  na virada da história ou na troca de música (*Lucy* 39,4 s, *Rebecca* 37,5 s, *Essa princesa* "Harij
  nega." 64,3 s). O resto é **corte seco**. Nunca `zoom-in`, whip ou crossfade.
- Curiosidade curta da Apotecária: **nenhuma** transição.

### Som

- **Riser + stinger levando ao corte**: `sharp-riser-327342` (1,9 s, 0 dB) começa ~1,9 s antes do
  corte, `StingerCameraShut SDT012601` (0 dB) entra ~0,25 s antes; no corte entra o `light` (e a música
  nova, quando troca). *Rebecca*: riser 1,78 → stinger 3,41 → light 3,66. *Essa princesa*: 1,98 →
  3,61 → 3,86. *Lucy*: 37,49 → 39,13 → 39,37 (troca de música). Nos curtos da Apotecária não tem.
- **Riser no fim**: `sharp-riser` terminando junto com o vídeo, nos 20.
- **Música** sem ducking e sem fade: Apotecária `Pensando` −20; Cyberpunk/BC `GONE TOO FAR` −15 na
  introdução e a mesma faixa em −20/−22 a partir do `light` (duas peças na trilha), às vezes outra faixa
  −20 na metade; AniPoison `CLIMA LINDO` −20/−22 o vídeo todo (*Harij* troca para `no signal (slowed)` com stinger).
- **Poucos SFX de reação** (0–3 por vídeo): `ES_Camera Shutter 7` (0 dB) num corte forte, `RIZZ`
  (0 dB) no galã/charme, `Suspense 3` (−7) em revelação, `Click` (0), `awkward-moment` (0) no
  constrangimento, `Ping` (−3, 0,28 s antes da seta). Nada de meme aleatório.
- Faixas: música numa (A1, às vezes A3), SFX nas outras; não tem A fixo.

### Legenda — 3 presets, pelo tipo de vídeo

| preset | fonte | cor | escala | y | animação | curva | marca | contorno | sombra (dist/desf/opac/âng) |
|---|---|---|---|---|---|---|---|---|---|
| **A rosa** (Apotecária) | padrão (`captionFont` vazio) | `rosa` | 1,4 | 0,385 | elástica 8 quadros | 8 pontos: 0,6 → 1,048 (t 0,4) → 1 | palavra | 5 | 2 / 0 / 1 / 90° |
| **B amarelo** (Cyberpunk/BC) | padrão | `amarelo` | 1,3 | 0,385 | elástica 8 quadros | 0,584 → 0,97 (t 0,157) → 1 | palavra | 5 | 3 / 0 / 1 / 90° |
| **C LuckiestGuy** (AniPoison) | `LuckiestGuy-Regular.ttf` | `#FCFF00` | 1,4 | 0,47 | elástica 8 quadros | 0,519 → 1,006 (t 0,157) → 1 | tudo | 12 | 2 / 4 / 1 / 90° |

Pontuação `limpar` (onde o campo existe), ~1,4 palavras por bloco, nunca edita o texto da legenda à mão.
Não é o do Fabinho (6 quadros, contorno 7, ângulo 71) nem o do Levi (Kiumaz v1, Bangers 2,1).

### Cor

Uma **camada de ajuste** no vídeo todo, a mesma nos 20 (no Dangai: "Cor: Anime vivo"): exposição +0,25,
brilho +0,23, contraste +0,05, temperatura +0,14, saturação +0,3, vibrance +0,5, nitidez +0,26.

### Enquadramento, entrada e efeito (fazer por ele)

- Rosto no recorte 9:16: arraste o `focusX` até o rosto/ação; não aceite o centro quando o personagem
  está no canto (ele mexe em 42% das cenas).
- `sourceStart` no melhor momento do clipe, pulando o começo parado/borrado.
- Rodízio com intensidade 0,1, mas troque `zoom-in` por `zoom-out` e `pan-up` por `pan-down` quando
  cortaria o rosto, e deixe `nenhum` em cena que já tem muito movimento (motivo provável, pelas trocas
  que ele faz; não confirmado com ele).

### Fechamento e repetição

- **Não volta à cena do gancho** no fim (só 1 de 20) e repete pouco (0–4 clipes por vídeo; *Capri* 21
  por causa do trailer). Diferente do Fabinho.
- Apotecária: CTA "Me segue…" (*Lihua*, *Jinshi*, *Shisui*) ou a revelação final ("Jinshi é filho dos
  dois."). AniPoison: acaba no último acontecimento do episódio, sem CTA. Cyberpunk/BC: o fato mais curioso.

### Confirmar com o Ajk (não dá para medir no `.dangai`)

- se os presets A/B/C estão salvos com nome no Dangai (`presets_de_legenda`);
- a velocidade padrão da narração hoje (110% ou 120%);
- se o `Firefly Wedding S01E07` (Gerar recap, 20/11) foi só um teste.

## Scripts desta skill (`scripts/`)

Os `.py` (`folhas.py`, `recortes.py`, `janela*.py`) precisam de Python com `numpy` e `pillow` e o
`janela-cena.py` lê `G:/ClaudeEditor/...` por padrão: **só no PC do Levi** (ou instale `numpy pillow`).
Os `.mjs`/`.js` de CDP rodam em qualquer PC com o Dangai aberto na porta.

**No PC do Ajk** (testado 20/11/2026: Python 3.14 + numpy 2.4 + pillow 12, ffmpeg 8.1, Node 24 no PATH):
rodam direto `folha-final.py`, `recortes.py`, `nitidez.py`, `movimento.py`, `fabinho/folhas-do-projeto.cjs`,
`fabinho/medir-projetos.cjs` e `ajk/comparar-com-a-biblioteca.ts`. `janela-cena.py` precisa do 4º
argumento (o `planos.json`; sem ele lê `G:/...`). `rostos-cenas.py` precisa de `DANGAI_MOTOR` = a pasta
`modulos/recap/motor` de um clone do Dangai + o python do `%LOCALAPPDATA%\Dangai\recap\motor-runtime`
(não testado no PC do Ajk). `dados-das-folhas.js`/`folhas.py` e `reconhecer.mjs` são do Gerar recap: o
Ajk não usa.

| script | o que faz |
|---|---|
| `cdp.mjs js <f.js>` / `foto <png>` | JS e print no Dangai (`PORTA=9353` = dev; padrão 9354 = instalado) |
| `soltar.mjs x y <arq...>` | solta arquivos na janela |
| `clicarxy.mjs x y`, `tecla.mjs <tecla> [n]` | clique e teclas |
| `c.sh "<texto>"` (+ `clicar.js`) | clica no botão com o texto |
| `dados-das-folhas.js <rascunho> <episodio> [take]` → `folhas.py` | folhas de candidatas por frase (*Gerar recap; só no PC do Levi*) |
| `recortes.py <projeto.dangai> <saida>` | recorte 9:16 no começo/fim de cada cena (Levi; roda também no PC do Ajk) |
| `janela.py <projeto.dangai> <saida>` | quadro inteiro com a janela 9:16 desenhada (*só no PC do Levi*) |
| `folha-final.py <projeto.dangai> <saida>` | **conferência final**: todas as cenas como o Dangai mostra (focusX/câmera + zoom do efeito), 1º e último quadro |
| `rostos-cenas.py <projeto.dangai> <pasta>` | **rosto no centro**: detector do motor em 3 instantes por cena → `faces.json` + folhas `fc_N.jpg` (rostos verdes, janela rosa). Rodar com o python do `motor-runtime`, de dentro de `modulos/recap/motor` (*só no PC do Levi*) |
| `reconhecer.mjs <iniciar/ver/confirmar/cancelar>` + `folha-grupos.py <pasta>` | **Reconhecer na mão** pelo Claude (episódio cortado pelo motor do Dangai): agrupa os rostos, folhas dos grupos e do elenco, grava os nomes |
| `nitidez.py <projeto.dangai>` | **borrão**: cenas com trecho < 45% da nitidez do clipe (foco mudando, fade) |
| `mcp.py <ferramenta> '<json>' [prefixo]` | chama o MCP do Dangai direto (senha em `DANGAI_MCP_SENHA`); salva as imagens do `ver_cenas`/`ver_clipe` |
| `seguir-rostos.mjs <lista>` / `ctrlz.mjs` | Seguir o rosto em lote (clica embaixo do bloco) / desfazer |
| `janela-cena.py <projeto.dangai> <saida> 3,10,26` | cenas escolhidas: 3 quadros com a janela + 3 do resto do clipe (achar `focusX`/`sourceStart`) (*só no PC do Levi*) |
| `fabinho/folhas-do-projeto.cjs <lista.txt> <saida>` | **qualquer PC (Node + ffmpeg)**: tabela frase a frase (fala, clipe, foco, entrada, efeito, transição) + folha com 1 quadro de cada cena no recorte 9:16 |
| `fabinho/medir-projetos.cjs <lista.txt> <saida.json>` | números de cada projeto: ritmo, gancho, foco, entrada, efeitos, legenda, faixas de som, cor |
| `fabinho/comparar-com-a-biblioteca.mts <lista.txt>` | o que a Biblioteca montaria (contas do `shared/trecho.ts`) × o que ficou: cortes iguais/movidos, efeitos trocados (`npx tsx`, `DANGAI_REPO` = clone do Dangai) |
| `ajk/comparar-com-a-biblioteca.ts <lista.txt> <saida.json>` | **qualquer PC com Node 22.6+ (sem tsx, sem npm)**: o mesmo, por projeto, + foco auto/centro/mão, entrada, transições com a fala e o gancho cena a cena. `DANGAI_REPO` = clone do Dangai (só lê o `shared/trecho.ts`) |

`lista.txt` = um caminho de `.dangai` por linha. Tudo só **lê** os projetos.

No repo do Dangai (fora da skill, `_medida/`, ignorado pelo git): `rostos-diag.ts` (decisão de
rosto da Edição rápida contra um foco de referência) e o estudo do corte em
`G:\ClaudeEditor\_capturas\corte-v3\cont` (`regra.py`, régua do gabarito) — *só no PC do Levi*.
