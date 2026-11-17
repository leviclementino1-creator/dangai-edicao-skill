// Tabela frase a frase + folha de quadros 9:16 de cada projeto. So LE os .dangai.
// Uso: node folhas-do-projeto.cjs <lista.txt> <saida-dir> [--sem-quadros] [--descricoes=<arquivo.json>]
//   lista.txt: um caminho de .dangai por linha. Precisa de ffmpeg no PATH (menos com --sem-quadros).
//   Saida: <id>.md (tabela + roteiro) e <id>.png (10 quadros por linha, cena 0 no canto, recorte
//   9:16 no focusX/focusY de cada clipe, no meio da cena a partir do sourceStart).
//   --descricoes: { "<id>": ["o que aparece na cena 0", ...] } vira a coluna "o que aparece".
const fs = require('fs')
const path = require('path')
const crypto = require('crypto')
const { spawnSync } = require('child_process')
const opcoes = process.argv.slice(4)
const semQuadros = opcoes.includes('--sem-quadros')
const arqDesc = opcoes.find((o) => o.startsWith('--descricoes='))?.slice(13)
const descricoes = arqDesc ? JSON.parse(fs.readFileSync(arqDesc, 'utf8')) : {}
const lista = fs.readFileSync(process.argv[2], 'utf8').split(/\r?\n/).filter(Boolean)
const SAIDA = process.argv[3]
fs.mkdirSync(SAIDA, { recursive: true })
const TW = 144, TH = 256, COLS = 10
// Nome legivel + 6 letras do caminho: dois projetos de nome parecido ("... (versao longa)") nao
// dividem a mesma pasta de quadros.
const slug = (s, f) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^A-Za-z0-9]+/g, '-').slice(0, 50).replace(/-+$/, '') +
  '-' + crypto.createHash('sha1').update(f).digest('hex').slice(0, 6)
const fmt = (n) => (Math.round(n * 100) / 100).toFixed(2)
const indice = []
for (const f of lista) {
  let p
  try { p = JSON.parse(fs.readFileSync(f, 'utf8')) } catch { continue }
  const sc = p.plan?.scenes ?? []
  if (sc.length < 3) continue
  const nome = path.basename(f, '.dangai')
  const id = slug(nome, f)
  const dir = path.join(SAIDA, id)
  if (!semQuadros) fs.mkdirSync(dir, { recursive: true })
  const desc = descricoes[id] ?? []
  const imgs = p.images
  const words = p.transcript?.words ?? []
  const blocos = p.biblioteca?.blocos ?? []
  const linhas = []
  sc.forEach((s, k) => {
    const im = imgs[s.imageIndex] ?? {}
    const d = s.end - s.start
    const ws = words.filter((w) => w.start >= s.start - 0.02 && w.start < s.end - 0.02)
    const texto = ws.map((w) => w.text).join(' ')
    const bloco = blocos.findIndex((b) => s.start >= b.start - 0.15 && s.start < b.end)
    const frase = bloco >= 0 ? blocos[bloco].sentence : ''
    const inicioDeFrase = bloco >= 0 && Math.abs(blocos[bloco].start - s.start) < 0.15
    const ehVideo = /\.(mp4|mkv|mov|webm)$/i.test(im.path || '')
    const t = ehVideo ? (s.sourceStart || 0) + Math.min(d / 2, 3) : 0
    const fx = im.focusX ?? 0.5, fy = im.focusY ?? 0.5
    const png = path.join(dir, String(k).padStart(3, '0') + '.png')
    if (!semQuadros && !fs.existsSync(png) && im.path && fs.existsSync(im.path)) {
      const rot = s.rotation === 90 ? ',transpose=1' : s.rotation === 270 ? ',transpose=2' : ''
      const vf = `${rot ? rot.slice(1) + ',' : ''}crop='min(iw,ih*9/16)':'min(ih,iw*16/9)':'(iw-min(iw,ih*9/16))*${fx}':'(ih-min(ih,iw*16/9))*${fy}',scale=${TW}:${TH}`
      const args = ['-v', 'error', ...(ehVideo ? ['-ss', t.toFixed(3)] : []), '-i', im.path, '-frames:v', '1', '-vf', vf, '-y', png]
      spawnSync('ffmpeg', args)
    }
    // Clipe que nao existe mais no disco vira quadro vermelho.
    if (!semQuadros && !fs.existsSync(png)) spawnSync('ffmpeg', ['-v', 'error', '-f', 'lavfi', '-i', `color=c=red:s=${TW}x${TH}`, '-frames:v', '1', '-y', png])
    const fonte = im.path ? im.path.replace(/^.*\\(Animes|Mang[aá]s|Filmes)\\/i, '').replace(/\\shots\\/i, ' #') : '?'
    linhas.push({ k, ini: s.start, d, frase, inicioDeFrase, texto, fonte, fx: im.focusAuto ? `auto ${fmt(fx)}` : Math.abs(fx - 0.5) < 0.01 ? 'centro' : `mão ${fmt(fx)}`, ss: s.sourceStart || 0, ef: s.effect, tr: s.transitionIn, b: s.imageIndexB != null })
  })
  // folha: COLS por linha, na ordem das cenas
  const n = sc.length
  const rows = Math.ceil(n / COLS)
  const args = ['-v', 'error', '-framerate', '1', '-i', path.join(dir, '%03d.png'), '-vf', `pad=${TW + 4}:${TH + 4}:2:2:white,tile=${COLS}x${rows}`, '-frames:v', '1', '-y', path.join(SAIDA, id + '.png')]
  if (!semQuadros) spawnSync('ffmpeg', args)
  const comDesc = desc.length > 0
  const md = [`# ${nome}`, '', `salvo ${p.savedAt?.slice(0, 10)} · ${fmt(sc.at(-1).end)} s · ${n} cenas` + (semQuadros ? '' : ` · folha: ${id}.png (${COLS} por linha, cena 0 no canto)`), '',
    'frase = nº da frase do roteiro (`+` = a cena começa no meio do trecho, não na vírgula); foco: `auto` = rosto que o app achou, `mão` = ele arrastou, `centro` = 0,5; entrada = `sourceStart` (s).', '',
    `| # | início | dur | frase | fala na cena (1ª palavra = onde cortou) |${comDesc ? ' o que aparece (no 9:16) |' : ''} clipe | foco | entrada | efeito | trans |`,
    `|---|---|---|---|---|${comDesc ? '---|' : ''}---|---|---|---|---|`]
  for (const l of linhas) md.push(`| ${l.k} | ${fmt(l.ini)} | ${fmt(l.d)} | ${l.frase}${l.inicioDeFrase ? '' : '+'} | ${l.texto.replace(/\|/g, '/')} |${comDesc ? ` ${desc[l.k] ?? ''} |` : ''} ${l.fonte}${l.b ? ' (+B)' : ''} | ${l.fx} | ${l.ss ? fmt(l.ss) : ''} | ${l.ef} | ${l.tr === 'cut' ? '' : l.tr} |`)
  md.push('', '## Roteiro', '', '```', (p.script || '').trim(), '```')
  fs.writeFileSync(path.join(SAIDA, id + '.md'), md.join('\n'))
  indice.push(`${p.savedAt?.slice(0, 10)} ${id} ${n}`)
  console.log('ok', id, n)
}
fs.writeFileSync(path.join(SAIDA, 'indice.txt'), indice.sort().join('\n'))
