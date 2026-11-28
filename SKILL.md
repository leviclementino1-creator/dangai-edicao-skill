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
4. **Música e efeitos:** onde estão as músicas da pessoa e **o guia dela** (qual música para qual
   clima e onde entrar). É o Levi: o guia dele já está na seção 4. Outra pessoa sem guia: monte com ela
   o `guia-de-musicas.local.md` (nesta pasta, fora do git) seguindo `prompts/guia-de-musicas.md` —
   liste a pasta de músicas, ouça a onda de cada uma (o drop/entrada) e pergunte o clima. Sem guia, a
   Edição rápida escolhe sozinha, mas aí CONFIRA cada música com a pessoa antes de entregar.
5. **Seta e outros overlays:** arquivo da seta + o som dela (o Levi: seta Pngtree + Ping), ou não usar.
6. **Cena ruim que eu achar na conferência:** troco direto (padrão do Levi: "sim ué") ou pergunto antes.
7. **Título, descrição e hashtags:** eu escrevo no fim (`editar.textos`) ou você faz.

Formato do `perfil.local.md` (curto, uma linha por item):
```
quem: Levi | fluxo: gerar-recap | legenda: Kiumaz v1 | favoritas: primeiro
musica: edicao-rapida | seta: <caminho> + Ping | cena-ruim: trocar-direto | textos: eu
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
  cortado lá (`buscar_na_biblioteca {anime}` mostra quais episódios existem). **Peça também os
  arquivos dos episódios que o roteiro cita** (para achar o minuto pela legenda) **e as cenas-chave
  com o minuto**, se a pessoa souber — e monte o MAPA DO ROTEIRO (seção 3) antes de escolher.
  Quem usa o Gerar recap (2.16.2+) pode fazer a curiosidade nele: um episódio principal (o que mais
  aparece) + os outros como **episódios extras** (seção 3, "Episódios extras").

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
- já está cortado na Biblioteca? Use (`buscar_na_biblioteca` pelo anime/episódio). No Gerar recap
  (2.16.2+): ponha como **episódio extra** e escolha a cena lá (seção 3, "Episódios extras");
- não está: diga qual episódio é (se você sabe a história; se não, ofereça pesquisar — wiki/guia
  de episódios) e **peça o arquivo daquele episódio**, ou pergunte se ela prefere seguir só com o
  episódio atual. Não improvise com uma cena parecida do ep atual sem avisar (Laid-Off S01E07:
  "expulso da antiga guilda" é o ep 1; usei uma cena do ep 7 e o Levi notou).

Pode começar a **analisar o episódio** assim que ele chegar (o corte leva ~3–4 min, por trás)
enquanto espera o roteiro e o áudio. Deixe **"Reconhecer personagens" marcado**.

**Confira o reconhecimento de personagens depois do corte** (os nomes por cena no `episodio.json`:
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
- **Cortado pelo AnCut** (cenas em `G:\App Corte Cenas\Output\...`; o Dangai responde "Cenas do
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
| `editar` (lote) | TUDO num pedido: `cenas[]` {cena, clipe, entrada, focoX, efeito, intensidade, zoomFixo, origemDoZoom, **camera:{pontos:[{t,cx,cy,zoom}]}**\|"desligar", **curva** (constante/suave/acelera/freia/chega-rapido), **curvaPontos**, grid:{clipe,entrada,focoX}\|"desligar"}, `sons.adicionar/remover`, `imagens.adicionar/remover` (seta: x/y em % do quadro, escala, rotacao), `legenda` (campos caption*), `textos` {titulos, descricao, hashtags} |
| `listar_faixas` | sons e imagens por cima com id (para remover) |
| `desfazer` | volta o último `editar` |
| `buscar_na_biblioteca` | clipes de qualquer episódio por texto/personagem/episódio/anime; `favoritas: true` = só as da estrela; `episodio` + `perto: "mm:ss"` (+ `raio`) = só as cenas daquele trecho |
| `presets_de_legenda` (aplicar) | os presets de legenda salvos, qual bate com o projeto (`diferencas`) e `aplicar: "<nome>"` |
| `ver_varios` (caminhos, momento) | **IMAGEM** do quadro inteiro de até 48 clipes lado a lado, numerados: escolher por expressão/ação (seção 9, "Expressões e ações") |
| `buscar_fala` (texto, pasta/arquivos, idioma) | acha o momento pelas LEGENDAS dos episódios (`.mkv` ou `.ass/.srt`): episódio + segundo + a fala (curiosidade, seção 3) |
| `listar_episodios` | os episódios do Gerar recap (`ep_...`, título, passo) |
| `reconhecer_personagens` (acao, episodio, jobId, decisao) | o **Reconhecer na mão**: `iniciar`/`ver` → folhas dos grupos de rostos + do elenco; `confirmar` com os nomes; `cancelar` (seção 01) |
| `episodios_extras` (episodio, definir) | **Gerar recap**: os episódios EXTRAS do recap (2.16.2+). Sem `definir`: principal, extras e os que dá pra adicionar; `definir: [ep_...]` troca a lista |
| `cenas_do_recap` (episodio, frase, de, perto, personagem, busca) | **Gerar recap**, passo Cenas: sem `frase` = as frases e as cenas escolhidas; com `frase` = sugestões/perto/outras do principal ou do extra `de`, com o `arquivo` (mp4) de cada uma |
| `escolher_cenas_do_recap` (episodio, frase, cenas) | **Gerar recap**: grava as cenas de UMA frase (travada). `cenas: [{planoIds, episodio, inSec, outSec, palavra}]` copiadas do `cenas_do_recap` |
| `abrir_projeto` (caminho) | abre um `.dangai` |

Regras de uso:
- **Um lote por rodada** (cada `editar` valida, grava e REABRE o projeto: ~8–10 s). Junte todas as
  mudanças; depois `ver_cenas` das cenas mexidas para conferir. Lote com erro (cena que não existe,
  arquivo que não existe, campo inválido) não grava nada.
- O checklist da seção 3 continua valendo: `ver_clipe` para achar o melhor momento, `ver_cenas`
  para conferir rosto/centro, `buscar_na_biblioteca` para curiosidade (cenas de outros episódios).
- **Seta + Ping juntos** no mesmo lote (seta do Levi + Ping −10 dB, ver seção 3).
  - **x/y da imagem por cima = deslocamento a partir do CENTRO, em %** (−50…50; o Levi usa x 25, y −12). x 68 joga a seta pra fora da tela, e foi assim que ela sumiu no Nia E08 (24/11).
  - A seta aponta pra direita em 0°, e a rotação é no sentido horário.
  - Caminho com "—" (o da seta): mande o JSON com `—` (ensure_ascii). Pelo bash ele vira "�" e a imagem some do render sem aviso.
  - Confira a seta num quadro do MP4.
- **Título, descrição e hashtags: escreva você** no `textos` do `editar` ao terminar (não precisa do
  Gemini). A thumbnail ainda é pelo módulo Thumbnail.
- O MCP **não** cobre o Gerar recap (roteiro/voz/aba Cenas): esses passos continuam pela ponte
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
2. **Roteiro**: *Meu roteiro* cola o texto dele (linha em branco = parte; agrupe pelas seções dele).
   Depois de colar, o app chama o Gemini pra "Ler" o episódio e "Ligar" as frases (5+ min no
   Laid-Off S01E07, 17/11). Quando EU escolho as cenas, **Cancelar** na hora: o texto já está
   gravado, *Aprovar roteiro* funciona e a sugestão de cenas é local. O app ainda escreve que o gancho "vira 2 ou 3 cenas no passo Cenas", mas a regra é a da seção 9: ~1 corte por segundo de gancho (4 s = 4 cortes).
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
fala de coisas espalhadas pela série: a cena certa pode estar em OUTRO episódio.

**O jeito certo (20/11): MAPA DO ROTEIRO antes de escolher cena.** O erro típico é escolher "uma
cena com o personagem" em vez de "a cena em que aquilo acontece". Então:
1. **Peça** (seção 01): o anime, os **episódios que o roteiro cita** (os `.mkv`, ou a pasta deles) e,
   se a pessoa souber, as **cenas-chave com o minuto** ("ep 49, 12:30, o Grimmjow morde") — é o
   sinal mais forte que existe.
2. **Monte o mapa**: para cada frase, de qual episódio e de que minuto ela é. Ferramentas:
   - `buscar_fala {texto, pasta | arquivos}` — procura nas LEGENDAS dos episódios (portugues
     primeiro) e devolve episódio + segundo + a fala. Use as palavras-chave da frase ou o que o
     personagem diz naquele momento ("cinco folhas", "empresto 500 milhões"). ~0,5 s por episódio.
   - não achou pela fala: o que você sabe da história, ou ofereça pesquisar (wiki/guia de episódios).
   - frase genérica ("ele é o mais forte"): sem minuto; aí vale personagem + checklist.
3. **Mostre o mapa à pessoa** (tabela curta: frase → episódio, minuto, o que acontece) e espere o
   OK ou as correções. Quem escreveu o roteiro sabe de onde tirou cada frase.
4. **Ache a cena exata**: `buscar_na_biblioteca {anime, episodio, perto: "mm:ss", raio: 15}` →
   só as cenas daquele trecho, da mais perto para a mais longe → `ver_clipe` nas candidatas e o
   checklist de sempre (rosto, ação, corpo inteiro, nada borrado). O episódio não está cortado
   na Biblioteca? Corte (Gerar recap > Analisar, ou o AnCut) antes.
5. Personagem citado sem minuto: reconhecimento em dia (seção 01) e `buscar_na_biblioteca
   {anime, personagem}` + favoritas primeiro.

Detalhes:
- A **Biblioteca** do Dangai (desde a 2.10.1 = a pasta do AnCut, `G:\App Corte Cenas\Output`, +
  a raiz do recap `G:\Dangai Recap\Biblioteca`) tem todos os episódios já cortados da série:
  busque por personagem/episódio (Ctrl+B, filtro de personagem) e use cena de qualquer um.
- No `.dangai`, uma cena de outro episódio é só o `path` do shot dele em `images[]`
  (`<saida do AnCut>\<anime>\SxxEyy\shots\<numero>.mp4`); os planos de cada episódio estão no
  `metadata/shots.json` do AnCut (personagem, tempo) ou no `episodio.json` do recap.
- Faltou o episódio que tem o momento? Corte ele (Gerar recap > Analisar, ou o AnCut) — ele entra
  na Biblioteca — e pegue a cena de lá.
- **Gerar recap com vários episódios (2.16.2+): EPISÓDIOS EXTRAS.** O rascunho tem um episódio
  principal (roteiro e voz) e uma lista de extras; a aba Cenas tira cena de qualquer um deles e o
  *Abrir no editor* monta cada cena do episódio dela. Use em curiosidade e em frase que cita outro
  episódio. Ver "Episódios extras" abaixo. (Dangai mais velho: monte pelo principal e troque as
  cenas dos outros no editor com `editar {cena, clipe}`.)

#### Episódios extras no Gerar recap (como fazer)

1. **O extra precisa estar ABERTO no Dangai**: a lista mostra os episódios que este Dangai já abriu
   (Gerar recap > Novo recap > soltar o `.mkv` e analisar, ou o AnCut + *Reconhecer agora*). Sem
   cenas cortadas ele aparece apagado.
2. **Adicionar**: pelo MCP, `episodios_extras {episodio: <principal>}` → `podeAdicionar` →
   `episodios_extras {episodio, definir: [<extras>]}` (a lista INTEIRA: manda os que já estavam
   junto). Na tela: aba Cenas, barra "Episódio" > **+ Episódios extras** > marcar.
3. **Achar a cena**: o mapa do roteiro (acima) diz de que episódio e minuto é cada frase →
   `cenas_do_recap {episodio, frase, de: <extra>, perto: "mm:ss"}` (a faixa `perto` = as cenas
   daquele minuto) ou `personagem`/`busca`. Olhe com `ver_varios {caminhos: [<arquivo>...]}` e passe
   o checklist de sempre. Na tela: seletor "Episódio" + "Perto do minuto" (12:30 + Enter).
4. **Gravar**: `escolher_cenas_do_recap {episodio, frase, cenas: [{planoIds, episodio, inSec, outSec,
   palavra}]}` copiando a cena como o `cenas_do_recap` devolveu (o id do extra vem com prefixo,
   `91831777c5~0075`: não mexa). Várias cenas na frase = `palavra` crescente (a 1ª é 0). Entra
   travada. Com a aba Cenas aberta, reabra o passo para ver.
5. **O que NÃO faz**: o *Sugerir* sugere só do principal (frase que cita outro episódio é você quem
   escolhe); as faixas "Sugestões" da tela continuam as do principal. Tirar um extra da lista faz as
   frases com cena dele voltarem para o Sugerir.

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
6b. **ANTES de escolher, veja o episódio INTEIRO por assunto** (Levi 25/11, Nia E08: "tinha MUITAS
   CENAS MELHORES do espadachim, da luta, da espada"). Eu escolhia frase por frase perto do momento
   e perdia os melhores planos (olhos sob o chapéu, golpes com rastro, corpo a corpo, salto).
   Faça `scripts/folhas-ep.py` (todas as cenas, marcando as usadas) e separe por assunto com
   `scripts/categorias.py <pasta> <cats.json>` (ex.: personagem principal / arma / luta). Escolha
   pelas folhas de assunto, e cena de outro momento do ep vale se bate com a palavra (fora de
   ordem ok). Ação com movimento > close parado.
   **Os 6 erros que achei revendo o Nia E08 inteiro (25/11, 23 de 59 cenas trocáveis):**
   (1) close parado onde havia ação (c21 "habilidades" = rosto; havia o golpe 0147);
   (2) a frase cita um e mostrei outro (c35 "a Nia não era normal" com o espadachim; c34 "o
   espadachim percebe" com mãos sem rosto); (3) cena escura/estilizada ilegível no 9:16 (c15 vermelho
   borrado); (4) plano aberto com gente minúscula (c10, c41); (5) repetir o mesmo plano (c14 e c26
   com o ataque da Rinokis); (6) perder a cena LITERAL da palavra ("espada mágica" tinha a espada
   roxa brilhando 0143; "pega uma garrafa" tinha a mão pegando 0131; "entre os dois" tinha os dois
   no quadro 0163). Confira cada cena contra esses 6 antes de gravar.
   **E toda candidata passa pelo recorte 9:16 ANTES de ser proposta** (`scripts/vertical.py <saida.jpg>
   <lista.json>`: 3 quadros de cada clipe já recortados pelo rosto). Das 23 que propus no Nia E08
   olhando o 16:9, só ~12 ficaram boas no vertical. Caem no 9:16: espada/golpe na HORIZONTAL (0143,
   0147), dois personagens afastados (0163 "entre os dois", 0119 Nia + lâmina, 0115 Nia + espadachim
   — só com câmera livre), mão/ombro sem rosto (0014), vermelho borrado (0113). Ficam bons:
   um assunto só, composição em pé (lâmina na vertical 0118, olho pelo rasgo 0146, olhos com aura
   0278), plano médio. Clipe que só fica bom no fim pede `entrada` perto do fim (0167, 0164).
   **Mas dois personagens lado a lado NÃO é descarte: anima a câmera** (Levi 25/11: "se tiverem 2
   personagens um do lado do outro, dá pra animar a câmera na vertical"). Câmera livre de um pro
   outro (Nia com a garrafa → espadachim 0115; Nia → lâmina descendo 0119; cara a cara 0129) e
   espada deitada = câmera correndo pela lâmina (0143). Prévia no 9:16 antes de gravar:
   `scripts/camera-previa.py <saida.jpg> <lista.json>` ([cena, clipe, entrada, duração, cxDe, cxAté,
   nota], cx = posição na largura da fonte; no .dangai x = (0,5 − cx) × 100). Só não salva quando
   os dois estão embolados/de costas no meio do movimento (0163).
7. **Enquadramento** `focusX` no rosto/ação (motor de rostos, fx=(cx−0,158)/0,684).
   **No GRID a conta é outra** (cada metade 1080x960 pega 0,633 da largura do 16:9):
   **fx = (cx − 0,316) / 0,367**. A Edição rápida já calcula certo nas duas metades; não "corrija"
   com a fórmula da tela cheia (Kikansha E08, 25/11: errei 4 grids assim e voltei). O
   `foco-certo.py` marca `GRID(cima)` nessas cenas: ali o "fx certo" dele NÃO vale. Se o
   personagem anda: Câmera livre > Seguir o rosto — e confira (seção 4).
   **(23/11, Goblin S01E08) CÂMERA LIVRE É PADRÃO, não exceção:**
   - Use câmera livre em toda cena em que o assunto se mexe (personagem andando, dragão virando, golpe, voo), **de qualquer duração, até as curtas do gancho** (Levi: "tem cenas menores que as vezes precisam também de movimento"). Também nas cenas com vários personagens, indo de um pro outro. O tempo da cena não é critério; o que vale é ter movimento pra acompanhar ou mais de um assunto.
   - **Como se escreve (MCP, 2.13.2+):** `editar {cenas:[{cena, camera:{pontos:[{t:0, cx:0.25}, {t:1, cx:0.6}]}, curva:"chega-rapido"}]}`.
     Você diz ONDE O ASSUNTO ESTÁ no quadro 16:9 original (`cx` 0 = esquerda, 1 = direita; `cy` 0 = topo,
     1 = base; `zoom` 1–3) em cada momento `t` da cena (0 = começo, 1 = fim). Pontos no meio (0<t<1)
     seguem quem anda (ex.: `[{t:0,cx:.3},{t:.5,cx:.55},{t:1,cx:.4}]`). O MCP converte para o `x/y` do
     núcleo (x = (0,5 − cx) × 100) e **prende na borda** — "ponto parado na borda" no retorno = o
     assunto está fora do alcance naquele zoom (aumente o zoom ou aceite). `listar_cenas` devolve a
     câmera na mesma língua (`camera.pontos` com cx/cy/zoom) e a `curva`. Sem MCP: o `.dangai`
     (`camera:{from,to,source:true,keys:[]}`, x positivo mostra o que está à esquerda) + `abrir_projeto`.
   - **O gráfico (ritmo) da cena** = `curva`: `constante` (linear: pan contínuo, bom em quem anda),
     `suave` (acelera e freia — o padrão), `acelera`, `freia`, **`chega-rapido`** (o pan do Levi:
     `[0,0,0.052,0.964]`, chega rápido e assenta — use no pan de um personagem pro outro) ou
     `curvaPontos: [x1,y1,x2,y2]` para desenhar. A curva vale para a câmera livre E para o efeito.
   - Pra o que não é rosto (dragão, monstro, objeto), o detector não ajuda: meça a posição no quadro.
   - **Como o Levi faz o pan** (Nia E08 24/11, cena do ataque): começa no assunto mais longe (x −25), termina no centro (x 0), com `curvePoints: [0,0,0.052,0.964]`: chega rápido e assenta (ease-out). Copie essa curva.
   - **Cenas seguidas com o mesmo plano/ângulo do mesmo personagem = "são iguais"** (Nia E08: 0116 e 0102). Troque uma por outra ação (ajoelhada, de lado, com outro personagem).
   - **Confira a câmera no `ver_cenas`** (2.13.2+): cena com câmera livre sai com **3 quadros** (começo,
     meio e fim do caminho, com o ritmo da curva, o x E o y e o zoom). Medido contra o preview real no
     Laid-Off (25/11): mesmo enquadramento, ~2–3% de diferença na altura. Antes (até a 2.13.1) ele
     mostrava só as pontas e sem o y — foi assim que errei a cena 5 três vezes. Depois do render,
     ainda vale o `centro-render.py` (abaixo) para o rosto no meio.
   - **POR QUE EU DESCENTRALIZAVA (medido 24/11, Nia E08, 59 cenas):** o app e a conta estão
     CERTOS — o rosto previsto pelo focusX bate com o render com 1–4% de erro. O erro era MEU:
     ajustei o focoX "no olho" e na direção errada (cenas 5, 7, 18, 57: certos 0,27/0,34/0,19/0,60,
     eu pus 0,18/0,42/0,08/0,45; na 5 e na 57 o valor automático já estava certo e eu estraguei),
     e disse que tinha conferido sem medir. Câmera livre com ponta chutada também (cena 53 termina
     com a Nia em 0,71). **Regras:** (1) nunca empurrar focoX no olho: CALCULE do rosto medido na
     fonte no meio da cena — `scripts/foco-certo.py <.dangai> <pasta>` dá o "fx certo" de cada cena;
     lembre: focoX MENOR leva o rosto para a DIREITA da tela; (2) depois de todo render, rode
     `scripts/centro-render.py <.dangai> <mp4> <pasta>` (python do motor, de dentro de
     `modulos/recap/motor`): mede o rosto em 3 instantes de cada cena e faz folhas com a linha do
     meio; tudo fora de 0,42–0,58 é refeito; (3) as cenas sem rosto detectado (perfil, costas,
     close extremo, objeto) eu olho nas folhas, uma por uma; (4) antes de renderizar, dá para
     conferir no preview da Edição (mesmo recorte do render — dica do Levi).
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

**AS 12 CORREÇÕES DO KIKANSHA S02E20 (25/11) — conferir TODAS antes da 1ª entrega.** O Levi pediu
"analisa e anota pra nunca mais errar". Cada uma ele teve que pedir:
1. **Episódio em baixa resolução**: baixei 480p e só ele notou. Antes de cortar, `ffprobe` a resolução;
   < 720p → avise e peça o 1080p. O corte novo sai igual: reaproveite as escolhas pelo TEMPO (`start` do
   plano), não pelo número (a numeração anda).
2. **Música que troca a cada parte** ("estranhas, em momentos errados"): uma música depois do gancho.
3. **Música entrando DEPOIS da batida principal**: medi RMS em janela de 0,25 s e entrei 0,5 s atrasado.
   Ache a pancada pela **onda** (`showwavespic` do trecho + RMS de 40 ms) e ponha `inicioSec` = pancada − 0,02.
4. **Clima errado na virada**: a parte sentimental/épica (corpo no limite, lembranças, magia final) pedia
   MY HERO IS OUR HERO. Entrada boa em **1:45,4** (volta com tudo depois da pausa), na virada com riser +
   impacto. Não voltar pra música do começo no fechamento ("não combina"): a mesma segue até o fim.
5. **Gancho com cena demais**: 6 cortes em 4 s. ~1 corte por segundo, só os melhores.
6. **Close extremo no gancho** (rosto gritando enchendo a tela + zoom-in): plano médio, zoom-out.
7. **Cena abstrata sozinha** (dragão de luz em "magia humana": "n entendo nada"): troque por REAÇÃO de
   personagem (grid Zod sorrindo × Priscilla surpresa).
8. **Cena feia no grid** (só os olhos da Priscilla: "mt grande", "tem q ser cenas bonitas"): a metade do
   grid também é plano médio bonito (luz, cabelo ao vento).
9. **Metade de baixo do grid descentralizada**: o `ver_cenas` não desenha a de baixo e a minha simulação
   com ffmpeg não bateu com o app. Confira a de baixo **num quadro do MP4** (ou no preview) e corrija.
10. **Último quadro do clipe é a cena seguinte** (apareceu céu no fim do grid): `entrada + duração ≤
    clipe − 0,1 s`; olhe o último quadro de cada cena no MP4.
11. **Sem seta e sem SFX** ("n tem seta pra colocar? efeito sonoro?"): a 1ª entrega já vai com a seta
    dele + Ping num detalhe que a fala cita e SFX nas ações visíveis (magia, impacto). Biblioteca Eagle
    Kiumaz/efeitos sonoros (Sparkling Spell, Telekinesis Blast, Ping, Explosion...). SFX longo (>3 s) não
    entra pelo MCP sem cortar.
12. **SFX baixo demais**: os risers/impactos da Edição rápida ficaram ~14 dB abaixo da voz (sumiam).
    Meça o LUFS de cada arquivo e ponha o efeito ~6–8 dB abaixo da voz (`gainDb` = alvo − LUFS do arquivo).
Também: no 2.13 o corte do "Analisar" vai para `G:\Dangai Recap\Biblioteca\<anime>\SxxEyy` (não a pasta
do AnCut), e o painel "Vídeo pronto" aberto engole o clique em Renderizar: feche (Fechar) antes.

**AS CORREÇÕES DO FOOL NIGHT S01E01 (26/11) — também antes da 1ª entrega.** Levi: "com base em todas
as mudanças que fizemos nesse vídeo anota". Cada uma ele teve que pedir:
1. **Gancho impactante desde o 1º quadro** ("lembra de melhorar o hook! deixar impactante!"). A 1ª cena é
   o protagonista com **EXPRESSÃO forte em PLANO MÉDIO** (choque, grito, choro), nunca close de rosto ("a
   primeira cena tá mt perto, frame ruim"). Ficou o Toshiro chocado de boca aberta, do peito pra cima.
2. **Cada cena do gancho conta a frase sozinha e é a imagem MAIS FORTE do assunto.** "Flor no peito" foi
   recusada ("não gostei, bota uma cena impactante de um esqueleto planta"). Símbolo pequeno < a coisa
   inteira e bizarra (o esqueleto virando planta dentro da cápsula).
3. **Olhe o ÚLTIMO quadro de cada cena do gancho**: o clipe do corpo brotando terminava na mão ("no final,
   trocar pra um outro frame"). Corte antes, ou divida a cena e emende outro plano.
4. **Use a ABERTURA (e outros episódios) quando ela tem o plano mais forte** (o Levi liberou: "se tiver
   cenas melhores nos outros eps, na opening pode usar"). O episódio 1 costuma não ter abertura; a do 2
   tinha o corpo explodindo em plantas. Como fazer:
   - corte o outro episódio em *Cortar episódios* > "Só cortar". No 2.13 ele vai para `G:\App Corte Cenas\Output`;
   - desde a 2.16.2 o outro episódio entra como **extra** do recap (seção 3, "Episódios extras") e a cena
     dele vai direto na frase. Dangai mais velho: grave um clipe do próprio episódio como substituto e, depois
     do *Abrir no editor*, troque pelo MCP: `editar {cena, clipe: <shots/NNNN.mp4 do outro ep>}`;
   - confira o recorte: a abertura tem créditos em japonês por cima de muitos planos. Escolha um trecho limpo
     ou desloque o focoX para tirar o texto.
5. **A imagem LITERAL da frase existe no episódio: procure.** O próprio Levi achou:
   - "transformar pessoas em plantas": o homem na TV com a árvore crescendo da cabeça (`entrada` no trecho
     em que a árvore cresce, zoom fixo 1,2 para tirar a borda da TV);
   - "pagar as contas e os medicamentos da mãe": a farmacêutica pegando o dinheiro no balcão, no lugar
     do Toshiro curvado de perto.
   Tela de TV, flashback, documento e balcão contam a frase melhor que um rosto qualquer.
6. **O Levi mexe no projeto entre um pedido e outro** ("arrumei o timming do hook!"). Antes de editar:
   `estado` (naoSalvo false) e `listar_cenas` para ler o que ele mudou. Edite só as cenas pedidas, pelo MCP
   ou num `.dangai` relido na hora, e confirme depois que os tempos dele ficaram iguais.
7. **A Edição rápida pôs 3 músicas de novo** (MENTE MÁ, River's End e ATLXS). Troque. No Fool Night ficou:
   - gancho com a Batchi slowed;
   - contexto com a instrumental, entrando na pancada (19,20 s);
   - River's End a partir da virada para o drama, com a SUBIDA dela (1:20) caindo num momento-chave
     ("acaba passando pelo procedimento"). Calcule `inicioSec` = 80 − (momento − at).
8. **Música baixa no começo** ("a segunda música é bem baixa no começo"). Faixa com dinâmica longa, como
   a River's End (−21 LUFS antes da subida e −17,5 depois): meça o LUFS de cada trecho usado e, se a
   diferença passar de ~2 dB, **divida a trilha em duas no `.dangai`, com ganhos diferentes**. Piano entra
   ~1 dB acima do phonk que vinha antes.
9. **Seta escondida atrás da legenda.** A legenda Kiumaz fica no meio (y 0,45), então a seta vai ACIMA ou
   ABAIXO da faixa da legenda (y entre −30 e −15, ou entre +15 e +30). Confira num quadro do MP4.
10. **SFX:**
    - o `sons.adicionar` do MCP põe o ARQUIVO INTEIRO. Efeito longo (magia de 49 s, relógio de 8 s) entra
      pelo `.dangai` com `usarSec` e `fadeOutSec`;
    - dois sons na MESMA `faixa` com tempos que se cruzam se atropelam. Use outra `faixa` (confira a
      sobreposição por faixa);
    - o que funcionou: magia de planta no corpo brotando, caixa registradora no dinheiro, relógio em
      "dois anos" e Ping junto da seta. Os marcadores ficam 6–8 dB abaixo da voz.
11. **Dividir uma cena** (o MCP não divide): no `.dangai`, copie o objeto da cena, mude `start`/`end`/
    `sourceStart`, copie a entrada de `images` trocando `path` e `fileName` (e `rel`, se existir), aponte
    o `imageIndex` para ela e faça `abrir_projeto`. Guarde backup em `G:	mp-medida\` antes.
12. **Thumbnail com as imagens que o Levi melhora** (já em pé, 1122x1402):
    - em cima, a figura com as plantas aproximada (135%) e subida até o peito ficar logo acima do texto;
    - embaixo, o rosto aproximado (170%) até o cabelo encostar no texto;
    - mantenha o texto, a seta "apontando" e o rasgo com brilho na cor original;
    - salve e suba no Drive quando ele pedir ("upa tudo no drive").
Também ficou valendo:
- nada de corpo ensanguentado caído (o beco com sangue saiu);
- close extremo só dentro de grid;
- 2 grids na discussão (Yomiko × Toshiro).

**BLACK CLOVER S02E09 (28/11): a v1 contra a final** (Levi: "compara a v1 com a final e vê como podia ter
acertado de primeira"). Das 57 cenas da v1, só 15 ficaram iguais. Quase tudo que ele pediu JÁ ESTAVA nesta
skill; o erro foi não aplicar antes da 1ª entrega. Diff medido: `antes-som.dangai` × o `.dangai` final.
1. **Animação primeiro.** As 3 cenas que ele mesmo achou ("cena boa pra krl q tu n usou": Morris com
   os tentáculos 0419; Yuno com a coroa em 8:10 0191; Morris "SINISTRA" em 14:30 0367) estavam no topo do
   ranking de movimento e eu não usei. Antes de escolher, rode
   `python scripts/ranking-animacao.py "<pasta do ep>" 0.5` (o python com cv2). Depois faça um `ver_varios`
   dos ~40 primeiros e reserve os melhores para: o gancho, a 1ª vez que um personagem aparece ("quando for
   falar do cara" = o plano mais sinistro dele) e as frases de poder ("magia das estrelas" = o Yuno de coroa,
   não uma estrela abstrata).
2. **Outros episódios logo na v1** (seção 01). O roteiro citava o Yami preso (ele quase não aparece no
   ep), o Lucifero (não aparece), a "Tríade derrotada" (a luta foi no E05) e os "magos rejeitados/família".
   A final usa o E05 (Yami de braços de osso 0212, Magna vencendo 0576+0577, Touros andando pra luz
   0444/0446/0449, grid 0452+0447), o E04 (a silhueta gigante do Lucifero 0188, zoomFixo 1,35) e o E08
   (Luck sorrindo × Asta em "nenhum deles se importava"). Na v1 tudo era do E09.
3. **Frase que cita um fato mostra o fato** (Fool Night item 5, de novo): "Tríade derrotada" = o vilão
   apanhando (Magna vencendo); "Morris indignado" = o Morris de pé, revoltado, não caído; "aquele
   esquadrão" = a galera toda, em grid.
4. **Close só em grid.** A v1 tinha rosto de tela cheia nas cenas 8, 17, 26, 29, 45 e 57. Na final viraram
   grid (cima e baixo com pessoas DIFERENTES), e ficaram 11 grids no vídeo.
5. **Cena parada e longa = 2 cenas.** A 2 do gancho (0404 por 1,45 s) e a 50 (1,46 s) ele mandou dividir.
   Gancho: nenhum clipe em 2 cenas seguidas. Fora do gancho, cena ≥ 1,4 s com movimento < 10 vira duas,
   cortando numa palavra.
6. **Seta + Ping na v1**: a final tem 3 setas animadas (gancho no Yami, Vanessa, "o homem que deu uma
   família"), todas com o Ping.
7. **Música (o que o Levi deixou na final):**
   - Black Clover = **Haruka Mirai do 0 até a virada (52,6 s), uma faixa só** (`inicioSec` 9,9, −20 dB,
     ducking 6). A v1 trocava 4 vezes: Haruka, Haruka, NO BATIDÃO e Kaikai Kitan;
   - a virada emocional ("todos se reúnem… o homem que deu uma família pra eles") = **MY HERO IS OUR HERO
     entrando JÁ NA SUBIDA** (`inicioSec` 22,55, onde a faixa explode de −22 para −9 dB RMS), **−17 dB**,
     até o fim. Eu tinha feito uma introdução baixinha (de 8,6 s, com +7 dB) subindo até a pancada; ele
     tirou. Música emocional entra com tudo no corte, sem preparar;
   - ganho: a MY HERO ficou ~2 dB acima da Haruka (orquestra soa mais baixa que a OP no mesmo RMS).
8. **SFX no volume certo já na v1** (Kikansha item 12, de novo). Final: Riser Metallic −10,5, sharp riser
   −3, deep sub impact −12, impact −10, Ping −10. Na v1 estavam 5–8 dB mais baixos. Magia visível ganhou
   som: Sparkling Spell na Grey neutralizando (35,6 s) e Telekinesis Blast na gravidade (44,6 s).
9. **Câmera livre e ritmo do Levi (o que ele mexeu à mão).** Ele pôs câmera livre em 4 cenas, sempre um
   **pan horizontal só em x**, sem zoom (`scale` 1), atravessando o quadro 16:9 (±34 = de uma borda à outra):
   | cena | plano | o que tem | câmera (x de → até) | ritmo (`curvePoints`) |
   |---|---|---|---|---|
   | 10 "o Yuno finalmente consegue" (1,24 s) | 0293 | golpe largo, Yuno × Zenon | −34 → +28 | `[0, 0.375, 0.008, 1]` |
   | 12 "Só que, mesmo com todos os membros da" (1,58 s) | 0338 | plano largo com mais de um | +22 → −12 | `[0.192, 0.594, 0, 0.92]` |
   | 21 "Só que, nesse momento," (0,95 s) | 0401 | assunto saindo do centro | 0 → +25 | linear |
   | 54 "Todos aqueles magos que um dia" (1,31 s) | 0348 | vários personagens lado a lado | +34 → −31 | linear |
   Como repetir:
   - **onde:** plano largo com ação ou com várias pessoas lado a lado, até em cena de 1 s. Close e
     rosto centrado ficam no efeito comum;
   - **câmera:** `editar {cena, camera:{pontos:[{t:0,cx:<início>},{t:1,cx:<fim>}]}}`, varrendo quase o quadro
     todo (uma borda até perto da outra) e seguindo a direção da ação;
   - **ritmo:** golpe ou impacto = curva que dispara e assenta, `curvaPontos [0, 0.375, 0.008, 1]` (a dele,
     igual à "chega rápido" do Nia E08). Plano de grupo ou de passagem = constante (linear);
   - o resto das cenas ficou com zoom-in/zoom-out a 0,1 e sem curva. Ele também puxou o focoX à mão em
     7 cenas (6, 21, 22, 27, 46, 48 e 59). A pior era a 48 da v1: com fx 0, o rosto ficava fora da tela.
     Por isso, depois de render, rodar `centro-render.py`.
10. **Bug meu:** dividir cena à mão sem `"rel": null` na imagem nova corrompeu o `.dangai`. Valide com o
    schema (`projectFileSchema.safeParse`, via `npx tsx --tsconfig tsconfig.node.json`) antes de abrir, e
    divida também `biblioteca.blocos`, deslocando as chaves de `porBloco`.

**TRAVA ANTES DE ENTREGAR: gancho, música e SFX** (Levi 22/11, Overgeared S01E09: "errou colocando pouca
cena no hook, errou na música e nos efeitos sonoros, isso nunca mais pode acontecer"). O vídeo saiu
com 1,9 mil views contra 45 mil do Black Clover. Só entrega com os três itens conferidos com número:
- **Gancho**:
  - conte as cenas até a saída do gancho: **~1 corte por segundo** (4 s = 4 cortes, 6 s = 5–6), cada um ~0,7–1,5 s e equilibrado. Mais que isso vira picotado: Kikansha E20 (25/11) tinha 6 cortes em 4 s (0,5–1 s) e o Levi pediu "pega as melhores, balanceia mais". Menos que isso vira parado (Overgeared: 3 em 5,6 s);
  - cada cena ≤ 1,2 s e a 1ª ≤ 1 s;
  - só plano com movimento/ação (nada de grupo posando ou rosto parado);
  - 3 cenas em 5,6 s foi o erro;
  - **FORTE: cenas impactantes e bem animadas** (Levi 25/11, Nia E08): golpe com rastro, aura, olhos
    brilhando, espada acesa, salto, impacto, corpo a corpo. Procure nas folhas por assunto o
    momento MAIS animado do episódio, mesmo de outro trecho (no Nia E08: o espadachim com aura roxa
    e olhos vermelhos da luta de noite, 0278/0301/0280/0287). Close parado e plano calmo ficam
    pro meio do vídeo.
- **Música**:
  - **nunca aceitar a música da Edição rápida sem conferir**: troque pela do guia (seção 4, "MÚSICA — como escolher": a tabela do Levi ou o `guia-de-musicas.local.md` da pessoa), conforme o clima de cada parte;
  - ação/progressão = Montagem Batchi no gancho → instrumental na virada;
  - **uma música só depois do gancho**, sem trocar a cada parte (Levi 25/11, Kikansha: a Edição rápida pôs 3 músicas, uma por parte, e ele achou "estranhas, em momentos errados"). Se a faixa não cobre o vídeo, **recomece a mesma faixa no drop** numa virada de parte, onde já tem o riser e o impacto.
  - ELSE PARIS e Afternoon of Konoha num vídeo de ação foi o erro;
  - nível ~−26 LUFS efetivo (medido), gancho com música audível (sem ducking, sem fade longo), drop no riser.
- **SFX**:
  - liste com `listar_faixas` e passe **um por um**;
  - zero "som do sino", zero meme;
  - cada efeito ligado a uma ação visível (dinheiro = MONEY, seta = Ping);
  - abertura = pop, gancho→contexto = riser, troca de música = sharp riser + impact.mp3.

**Conferência final obrigatória**: `scripts/folha-final.py <projeto.dangai> <saida>` (ou o
`ver_cenas` do MCP) — o recorte do focusX (1º e último quadro) ou da câmera livre (começo, meio e
fim, desde a 2.13.2). Olhe TODAS antes de entregar; o Levi não pode ser quem acha. O `folha-final.py`
NÃO mostra a câmera livre: para ela, o `ver_cenas` ou quadros do MP4 renderizado (item 7).

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
- **Gancho**: conte pelo TEMPO, não pelo número (Levi 22/11, Overgeared: 3 cenas em 5,6 s = "muito tempo
  parado"):
  - cada cena ~0,6–1,2 s, a 1ª no máximo ~1 s;
  - um gancho de ~4–6 s tem **4 a 6 cortes** (~1 por segundo, só os MELHORES planos);
  - **"MANO," no começo tem uma cena SÓ PRA ELE** (Levi 26/11): um corte curto, de 0,3 a 0,6 s, só na palavra "Mano" — um rosto/reação forte de impacto — e o resto da frase começa na cena seguinte ("esse cara..."). Não juntar "Mano, esse cara aceitou" num plano só;
  - a 1ª cena mostra quem a frase cita;
  - ação e movimento; nada de plano parado (grupo posando, rosto quieto);
  - **variedade**: em "cada vez mais fortes", mostre a PROGRESSÃO (Goblin 23/11: três cenas do mesmo dragão = "é o mesmo dragão").
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

- **MÚSICA — como escolher (o jeito do Levi, 22–25/11; ele: "depois que eu expliquei você está aplicando bem")**.
  A Edição rápida já tenta seguir isto, mas **nunca aceite a música dela sem conferir** (no Overgeared
  ela pôs ELSE PARIS e Afternoon of Konoha num vídeo de ação, baixas, e o vídeo flopou). Passo a passo:
  1. **Leia o clima de cada parte do roteiro** (gancho, contexto, virada, clímax, fechamento): ação /
     progressão, épico ("tudo dando certo do nada"), emocional / história triste, romance, suspense,
     comédia / slice of life, curiosidade neutra.
  2. **Escolha pela tabela do guia** (abaixo, ou o `guia-de-musicas.local.md` da pessoa — seção 00).
     Música específica (ELSE PARIS, Naruto) só no clima EXATO e num trecho de 15 s ou mais.
  3. **Gancho**: a música já entra **audível** desde o 0 s — sem ducking, sem fade-in longo
     (`fadeInSec` 0,05), um pouco mais alta que o resto. Em ação/progressão, o combo da Batchi.
  4. **O drop cai no fim do riser** (a saída do gancho): `inicioSec` = segundo do drop no arquivo −
     saída do gancho. Ache o drop OUVINDO A ONDA (RMS de 0,2 s: o primeiro bumbo/grave forte depois
     da subida), não confie cego no detector (`entradas.ts` adiantava na Batchi: 16,9 s × 19,2 s).
  5. **Troque de música quando o clima mudar** (ex.: a história fica triste no meio): a nova entra
     no ponto bom dela (a coluna "onde entrar"), com **sharp riser + impact.mp3** no corte da troca.
     Não troque sem mudança de clima — **uma música só no vídeo todo é ok** (o Levi tirou a 2ª no Laid-Off).
  6. **Volume**: ~−26 LUFS efetivos no mix (≈12 LU abaixo da voz). Meça com ebur128 no trecho usado
     (gainDb = −26 − LUFS do trecho). A Edição rápida antiga deixava ~−30 ("muito baixa").
  7. **Confira ouvindo** o começo (gancho → riser → drop) e cada troca antes de entregar.

  **O BÁSICO (vale para qualquer pessoa, com ou sem guia):** classifique as músicas da pasta dela
  ouvindo a onda (energia, batida, subida → drop) e use esta tabela. O guia pessoal só afina (qual
  arquivo, que segundo).

  | clima da parte | que música | como entrar |
  |---|---|---|
  | **gancho** (os 5 s que decidem o alcance) | a mais forte do vídeo: batida marcada, phonk/trap/rock, ou a OP do anime instrumental | audível desde o 0 s; o drop/refrão bate no fim do riser |
  | **ação, luta, progressão, "aura"** | phonk, trap, rock/OP de anime de ação: grave forte, altos e baixos | entrar no drop ou na parte mais cheia |
  | **épico, virada, "tudo dando certo do nada"** | orquestral/OST épica ou OP crescendo | entrar já no pico ("com tudo"), não na intro |
  | **emocional, história triste, passado do personagem** | piano/cordas, OST lenta, instrumental de balada | pular a intro vazia; entrar onde a melodia começa |
  | **romance** | instrumental de pop/balada, lo-fi suave | trecho melódico, sem batida pesada |
  | **suspense, mistério** | drone, batida lenta, pad grave | só se o suspense durar (15 s+); senão não troca |
  | **comédia, slice of life** | leve, ukulele/piano saltitante, lo-fi animado | qualquer trecho alegre; evitar em vídeo de ação |
  | **curiosidade / explicação neutra** | lo-fi, instrumental neutra, sem drama | pular silêncio do começo; volume constante |

  Regras de bolso: **uma música por clima, não por frase** (trocar demais cansa); a do **gancho é a
  melhor** do vídeo; música muito específica (tema de um anime, meme) só no anime/clima dela; nunca
  música com voz cantada brigando com a narração (prefira instrumental); nada de silêncio — o vídeo
  inteiro tem música.

  **Guia de músicas do Levi** (pastas no PC dele: G: = `G:\App Resumo\music\`, D: = `D:\Downloads\Kiumaz\2. assets\music\`):

  | música (arquivo) | pasta | quando usar | onde entrar |
  |---|---|---|---|
  | **MONTAGEM BATCHI (Super Slowed + Reverb) [BRAZILIAN PHONK].m4a** → **MXZI, Rushex - Montagem Batchi (Instrumental HQ).m4a** | D: → G: | a preferida dele, ação/progressão: o gancho na slowed e, na virada gancho→contexto, troca para a instrumental | corta em ~0:25 da slowed e emenda em ~0:19 da instrumental |
  | ATLXS - PASSO BEM SOLTO instrumental.mp3 | G: | pós-gancho genérico; cabe em quase tudo, até no vídeo todo | — |
  | Black Clover - Haruka Mirai (OP1 - Filtered Instrumental).mp3 | G: | gancho e pós-gancho, **só em Black Clover** | o refrão em ~0:14, junto com o contexto |
  | Boku No Hero Academia Movie OST - MY HERO IS OUR HERO - Futari No Hero.mp3 | G:/D: | emocional, história de personagem de shounen | o começo; ~1:44 para épico/emocionante no meio |
  | CLIMA LINDO.m4a | G: | curiosidade, slice of life, comédia (neutra: nada emocional/épico) | ~0:10 |
  | ELSE PARIS (MUSICA DE SUSPENSE DO TIKTOK).mp3 | G: | só suspense que dure o bastante (raro) | — |
  | GLICHERY, MXCCREE, DJ GLICHEKY - X-GALACTICO (SLOWED) (1).m4a | G: | começo de vídeo de ação, se pegar a parte certa (mais da Kizuni); nunca romance | — |
  | Jujutsu Kaisen Season 2 Opening 2 King Gnu - SPECIALZ (Instrumental).mp3 | G: | ação, muitos altos e baixos; boa entrada no meio do vídeo | — |
  | Naruto - Afternoon of Konoha.mp3 | G: | MUITO específica: só comédia bem slice of life (raro) | — |
  | no signal (slowed).m4a | G: | curiosidade e romance (neutra) | — |
  | We Don't Talk Anymore Instrumental - Mighty Seven (youtube).mp3 | G: | romance e partes emocionais | — |
  | Where Our Blue Is (Instrumental).mp3 | G: | épico, ação, aventura, "tudo dando certo do nada" | ~0:46 (já entra com tudo) |
  | Echoes of the Eye Soundtrack - River’s End.mp3 | D: | histórias tristes e emocionais (é mais baixa) | ~1:20 |
  | Kaikai Kitan - Eve (Instrumental).mp3 | D: | ação, mas situacional | — |
  | MENTE MÁ (Instrumental).mp3 | D: | genérica, historinha mais animada; também no meio | ~0:07 |
  | NO BATIDÃO - ZXKAI Instrumental.mp3 | D: | animadíssima, "aura" | ~0:15 |

  Resumo por clima: **ação/progressão** = Batchi no gancho → SPECIALZ, Where Our Blue Is (0:46) ou
  Kaikai Kitan nas partes épicas; **emocional** = MY HERO IS OUR HERO, River's End (1:20) ou We Don't
  Talk Anymore; **curiosidade/romance neutro** = no signal ou CLIMA LINDO (0:10); **Black Clover** =
  Haruka Mirai. Outra pessoa: o guia dela (seção 00), nunca o do Levi com arquivos que ela não tem.
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

**Black Clover S02E08 (21/11) — o que ficou de regra:**
- **Legenda**: a Edição rápida põe o "estilo salvo", que NÃO é o Kiumaz v1. Logo depois de abrir no
  editor: `presets_de_legenda {aplicar:"Kiumaz v1"}` e conferir `igualAoProjeto: true` (Levi cobrou).
- **Cena boa mas curta**: em vez de trocar, emende o plano seguinte — o candidato aceita
  `planoIds` CONSECUTIVOS (`["0298","0299"]`, `inSec` do 1º, `outSec` do último) e vira uma cena
  só, mais longa (Levi: "pôr a cena seguinte e aumentar o número de cenas, se aquela era boa").
- **Faixa preta (letterbox) nas memórias/flashback**: muitas cenas de memória vêm com ~15% de faixa
  em cima e embaixo. Meça (linhas pretas no quadro) e ponha `zoomFixo: 1/(1-2×faixa)` (15% → 1,45)
  com `origemDoZoom {0,5; 0,5}`: o efeito (zoom-in/out) continua animando por cima do zoom fixo.
  **MAS o zoom total = fixo × efeito**: 1,45 com zoom-in 1,1 chega a 1,6x e o Levi reclamou ("tem
  cena com muito zoom!", 21/11). Com zoom fixo, o efeito é **zoom-out** (ou nenhum), nunca zoom-in,
  e meça o zoom TOTAL de cada cena. Opções a oferecer: 1,43 + zoom-out (sem faixa, máx. 1,43x),
  1,25 + zoom-out (fio de faixa no fim) ou deixar a faixa (flashback).
  Com o zoom, rosto que já era close fica perto demais → troque essas, e re-meça o centro do rosto
  (`rostos-cenas.py`), porque a janela fica mais estreita.
- **"Muito zoom" = plano de OLHO** (Levi 21/11: "olho do Yuno, olho do Zenon"): o detector NÃO acha
  rosto em plano só de olho/meio rosto (sai vazio, não "grande"), então `rostos-cenas.py` sozinho
  deixa passar. Olhe a folha do `ver_cenas` procurando olho/boca enchendo a tela (também no ÚLTIMO
  quadro: clipe que começa médio e fecha no olho, ex. 0239) e troque por plano médio/corpo inteiro.
  Clipe novo mais curto que a cena mostra o quadro seguinte (saiu um quadro branco): `ffprobe` a
  duração e use clipe ≥ cena.
- **Drop da música**: o detector ainda erra em música com PAUSA antes da pancada (ATLXS – Passo Bem
  Solto: silêncio 60,0–60,6 s, pancada 60,75 s; o detector marcou 62,05 s, 1,3 s atrasado).
  Conferir SEMPRE pela onda do grave e, se precisar, mexer na trilha direto no `.dangai`
  (`inicioSec` = pancada − saída do gancho; a volta da música no começo de uma parte) e
  `abrir_projeto` para recarregar (o MCP ainda não edita trilha).
- **Porta do MCP**: se a 47321 estiver ocupada, o Dangai sobe na 47322 (veja
  `window.dangai.modulos.claude.estado()` → `url`); o `claude mcp add` registrado aponta para a 47321,
  então use `mcp.py` com `DANGAI_MCP_PORTA`.
- **Thumbnail (módulo Thumbnail, por CDP)**: botão "Thumbnail" no editor → 2 imagens (cima/baixo):
  "Quadro do projeto" + clicar na régua no tempo da cena + "Usar este quadro"; "Enquadrar sozinho"
  tira o rosto das faixas proibidas do TikTok; aba Texto: Linha 1/2 + estilo **Kiumaz**; "Salvar PNG"
  abre a janela "Salvar a thumbnail" (WScript.Shell `AppActivate` + `SendKeys` %n, ^a, caminho,
  ENTER). **Nunca esquecer o CORTE NO MEIO** (aba **Divisor**: o rasgo entre as duas imagens; no
  estilo Kiumaz, o "Brilho dentro", com **"Brilho fora" ~30–40** desde a 2.16.1 — o Levi quer um pouco de halo por fora também; confira a emenda no PNG salvo e suba o brilho se ela sumir em imagens escuras) — a do Zenon saiu sem e o Levi cobrou. E **escolha quadros
  BONITOS** para a thumb, não só legíveis: rosto no melhor desenho do episódio, cor forte, luz,
  expressão marcante (ver_varios nas candidatas antes de escolher). Fórmula que o Levi gostou: **vilão em cima × quem ele perdeu embaixo** (Zenon com o rosto
  de osso / Allen criança sorrindo) + "MATOU O / MELHOR AMIGO?!" + a seta.
  **Padrão medido na thumb que o Levi arrumou (21/11):** divisor **Rasgo com brilho, cor Original
  (rasgo escuro), brilho mínimo** (o branco sumiu nas nuvens); zoom **pelo quadro, sem exagero**: no Black Clover,
  144% em cima e 128% embaixo; no Overgeared, 112% (com a imagem dele já recortada); no Goblin (23/11:
  "vc dá muito zoom!"), 144% em cima e **101% embaixo**. Com as imagens que ele melhora (já em pé),
  comece perto de 100% e mostre o personagem inteiro; só aproxime se ficar pequeno. O aviso de rosto
  nas faixas do TikTok ele ignora. Seta: modo **"Apontando o rosto"**.
  **Nia S01E08 (24/11), o que o Levi arrumou na minha:** os DOIS rostos encostados no texto (o
  texto fica entre os rostos, não entre chapéu/cenário): em cima 100% mas descido (cy 0,58) até a
  boca ficar logo acima do texto; embaixo **146%** (eu tinha posto 122%: Nia pequena) com o rosto
  logo abaixo do texto, sorriso no meio e a garrafa ainda no quadro. Seta GRANDE e visível: base na
  borda esquerda na altura do texto, curva subindo até o rosto de cima (base ~(40,920), ponta
  ~(315,640) em 1080x1920), nunca escondida atrás do texto. Regra: medir o ROSTO — rosto pequeno
  no painel = aproxime; corpo inteiro só quando o rosto ainda fica grande.
  seta pequena da esquerda apontando o rosto do vilão. Imagem de fora: soltar SÓ com a thumb no modo
  **"De um projeto"** — no painel "Vídeo pronto" (pós-render) o soltar cai na TIMELINE como cenas novas
  (desfazer com Ctrl+Z depois de clicar num lugar neutro e conferir `estado`).
  **Imagem de fora no painel "Vídeo pronto"** (22/11, Overgeared): aba Imagens > slot > "Do computador"
  > **Colar (Ctrl+V)** com a imagem na área de transferência (PowerShell:
  `[System.Windows.Forms.Clipboard]::SetImage([System.Drawing.Image]::FromFile(...))`). Quadro em
  resolução cheia: `ffmpeg -ss <t> -i <episodio.mkv> -frames:v 1`. Texto: os campos "PODER/SUPREMO"
  são PLACEHOLDER (valor vazio): preencha pelo `placeholder`. Seta escondida atrás do texto: Seta >
  **Livre** e arraste com `scripts/arrastar.mjs x1 y1 x2 y2`. Salvar de novo pede "Substituir".
- **Frase que cita outro episódio** ("depois de ser expulso da antiga guilda" = a expulsão do
  ep 1): a cena certa é a DAQUELE episódio. No Gerar recap: ponha o episódio como **extra** e
  escolha lá (seção 3, "Episódios extras"); fora dele, `buscar_na_biblioteca` (anime/episódio).
  Se o episódio não está cortado, **peça o arquivo ao Levi** antes de improvisar com o que o ep
  atual tem (no Laid-Off S01E07 usei o Rein gritando "você me expulsou?!" do ep 7 e ele notou).
- **Tela de status/sistema** (Levi 22/11, Overgeared): só fica se mostra algo claro e ligado à fala
  ("Lv:95" no "nível 95", "Lv:251" no "acima do nível 200"). Só texto japonês sem número que importe
  ("derrotou o Malaxus", ficha de item, entrar na guilda): **tira** ou põe em **grid** com um personagem.
- **Entrega no Drive: PERGUNTE antes** (Levi 23/11). Terminou o vídeo e a thumb, pergunte "quer que eu suba no Drive?" e só suba com o sim. Como subir: vídeo + thumb no Google Drive dele (conta leviclementino1, montada no K: desde 22/11) = copiar pra `K:\Meu Drive\Dangai\<anime SxxEyy>\`, esperar sincronizar (id da nuvem no `metadata_sqlite_db` do DriveFS) e compartilhar a PASTA com `share_file {permissionId:"anyoneWithLink"}`
  (Google Drive para desktop sincroniza). Thumb: ele melhora os 2 quadros — mande o de CIMA e o de BAIXO
  separados (quadro 1920x1080 do .mkv), espere ele devolver e cole nos slots.
- Cena que não mostra QUEM a frase cita é cena errada, mesmo bonita ("a própria mestre tava
  tentando acabar com ela" com a Lily chocada → errado; é a Elsie sorrindo no "Essa guilda acabou!").

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
- **EXPRESSÕES E AÇÕES da frase** (Levi 20/11: "ele odeia" = cara de bravo, "empurrado" = o
  empurrão). A cena mostra o SENTIMENTO ou o VERBO, no rosto/corpo de quem a frase cita, na
  palavra dele — nunca um rosto neutro "do personagem":

  | a frase diz | procure |
  |---|---|
  | odeia, raiva, furioso, "não aceita", irritado | cara brava: sobrancelha franzida, dente cerrado, grito, punho fechado (chibi vale no tom de zoeira) |
  | medo, apavorado, "tremeu" | olhos arregalados, recuando, tremendo, suor |
  | chora, triste, arrasada, sofre | lágrima, cabeça baixa, de costas/sozinha na janela |
  | choque, "descobre", "do nada", "não acredita" | boca aberta, olhos arregalados, close de reação |
  | feliz, comemora, "deu certo" | sorriso aberto, braços erguidos, pulando |
  | promete, decide, "vai conseguir" | olhar firme pra frente, punho, apontando |
  | vergonha, gosta de alguém | corada, olhando pro lado, mão no rosto |
  | se acha, humilha, despreza | olhar de cima, sorriso de canto, braços cruzados |
  | cansou, enjoou, tédio | olhar vazio, suspiro, apoiada na mão |
  | empurra, expulsa, joga fora | o empurrão / alguém sendo jogado / a porta batendo, no impacto |
  | bate, soca, apanha | o golpe no quadro do impacto; "apanha" = quem leva |
  | corre, foge, persegue | corpo inteiro correndo (perseguir = os dois no quadro) |
  | cai, desmaia | o corpo caindo |
  | abraça, segura a mão, beija | o gesto, de perto |
  | come, bebe | o gesto (copo na boca, mordida) |
  | mata, morre | reação ou o momento antes — sem sangue em destaque (regra da plataforma) |

  **Como achar:** junte as candidatas — `buscar_na_biblioteca {anime, personagem}` (as cenas
  dele), `{episodio, perto}` (o trecho do momento) ou `buscar_fala` com as palavras da emoção na
  fala ("odeio", "maldito", "socorro", "obrigado": o momento da fala carrega a cara) — e passe
  tudo no **`ver_varios {caminhos}`** (até 48 quadros inteiros lado a lado, numerados): escolha a
  expressão MAIS forte e depois `ver_clipe` nela para o melhor momento (o pico da cara, não o
  começo). No Laid-Off, 12 candidatas de "bravo" saíram numa folha em 0,7 s.
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
| `rostos-cenas.py <projeto.dangai> <pasta>` | **rosto no centro**: detector do motor em 3 instantes por cena → `faces.json` + folhas `fc_N.jpg` (rostos verdes, janela rosa). Rodar com o python do `motor-runtime`, de dentro de `modulos/recap/motor` (*só no PC do Levi*) |
| `reconhecer.mjs <iniciar/ver/confirmar/cancelar>` + `folha-grupos.py <pasta>` | **Reconhecer na mão** pelo Claude (episódio cortado pelo motor do Dangai): agrupa os rostos, folhas dos grupos e do elenco, grava os nomes |
| `nitidez.py <projeto.dangai>` | **borrão**: cenas com trecho < 45% da nitidez do clipe (foco mudando, fade) |
| `mcp.py <ferramenta> '<json>' [prefixo]` | chama o MCP do Dangai direto (senha em `DANGAI_MCP_SENHA`); salva as imagens do `ver_cenas`/`ver_clipe` |
| `seguir-rostos.mjs <lista>` / `ctrlz.mjs` | Seguir o rosto em lote (clica embaixo do bloco) / desfazer |
| `janela-cena.py <projeto.dangai> <saida> 3,10,26` | cenas escolhidas: 3 quadros com a janela + 3 do resto do clipe (achar `focusX`/`sourceStart`) (*só no PC do Levi*) |
| `fabinho/folhas-do-projeto.cjs <lista.txt> <saida>` | **qualquer PC (Node + ffmpeg)**: tabela frase a frase (fala, clipe, foco, entrada, efeito, transição) + folha com 1 quadro de cada cena no recorte 9:16 |
| `fabinho/medir-projetos.cjs <lista.txt> <saida.json>` | números de cada projeto: ritmo, gancho, foco, entrada, efeitos, legenda, faixas de som, cor |
| `fabinho/comparar-com-a-biblioteca.mts <lista.txt>` | o que a Biblioteca montaria (contas do `shared/trecho.ts`) × o que ficou: cortes iguais/movidos, efeitos trocados (`npx tsx`, `DANGAI_REPO` = clone do Dangai) |

`lista.txt` = um caminho de `.dangai` por linha. Tudo só **lê** os projetos.

No repo do Dangai (fora da skill, `_medida/`, ignorado pelo git): `rostos-diag.ts` (decisão de
rosto da Edição rápida contra um foco de referência) e o estudo do corte em
`G:\ClaudeEditor\_capturas\corte-v3\cont` (`regra.py`, régua do gabarito) — *só no PC do Levi*.
