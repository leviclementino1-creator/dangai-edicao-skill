// O que a Biblioteca montaria x o que ficou no .dangai (so LE os projetos).
// Uso (Node 22.6+ roda .ts direto; sem tsx, sem npm install):
//   set DANGAI_REPO=<clone do Dangai>  &&  node comparar-com-a-biblioteca.ts <lista.txt> <saida.json>
// Por projeto: cortes iguais/movidos/novos/tirados, efeito trocado do rodizio, foco (auto/centro/mao),
// entrada (sourceStart), transicoes com a fala, e o gancho cena a cena (fala, clipe, efeito, foco, entrada).
import { readFileSync, writeFileSync } from 'node:fs'
import { pathToFileURL } from 'node:url'
const REPO = process.env.DANGAI_REPO
if (!REPO) { console.error('Defina DANGAI_REPO = pasta de um clone do Dangai (https://github.com/faahpla/dangai)'); process.exit(1) }
const { slotsDoTrecho, palavrasDoTrecho, spansDoTrecho } = await import(pathToFileURL(REPO + '/shared/trecho.ts').href)

const KB = ['zoom-in', 'zoom-out', 'pan-left', 'pan-right', 'pan-up', 'pan-down']
const lista = readFileSync(process.argv[2], 'utf8').split(/\r?\n/).filter(Boolean)
const out: any[] = []
const med = (a: number[]) => { if (!a.length) return null; const s = [...a].sort((x, y) => x - y); return +s[Math.floor(s.length / 2)].toFixed(2) }

for (const f of lista) {
  const p = JSON.parse(readFileSync(f, 'utf8'))
  const b = p.biblioteca
  const sc = p.plan?.scenes ?? []
  const imgs = p.images ?? []
  const nome = f.split(/[\\/]/).pop()
  if (!b?.blocos?.length || !Object.keys(b.porBloco ?? {}).length) { out.push({ nome, semBiblioteca: true }); continue }
  const palavras = p.transcript?.words ?? []
  const spans: { start: number; end: number; paths: string[]; frase: number }[] = []
  for (const [i, frase] of b.blocos.entries()) {
    const cenas = b.porBloco[String(i)] ?? []
    if (!cenas.length) continue
    const slots = slotsDoTrecho(cenas, b.pesos?.[String(i)], b.unioes?.[String(i)])
    const pal = palavrasDoTrecho(palavras, frase.start, frase.end)
    const c = b.cortes?.[String(i)]
    const cortes = c?.length === slots.length - 1 ? c : null
    const ds = spansDoTrecho(frase.start, frase.end, slots, pal, cortes)
    slots.forEach((s: any, k: number) => spans.push({ ...ds[k], paths: s.paths, frase: i }))
  }
  // cortes
  const app = spans.slice(1).map((s) => s.start)
  const fim = sc.slice(1).map((s: any) => s.start)
  let iguais = 0, movidos = 0
  const desl: number[] = []
  const usados = new Set<number>()
  for (const t of app) {
    let melhor = -1, d = Infinity
    fim.forEach((u: number, j: number) => { if (!usados.has(j) && Math.abs(u - t) < d) { d = Math.abs(u - t); melhor = j } })
    if (d < 0.05) { iguais++; usados.add(melhor) } else if (d < 0.6) { movidos++; usados.add(melhor); desl.push(+(fim[melhor] - t).toFixed(2)) }
  }
  // ordem das cenas: a sequencia de clipes do app x a final
  const seqApp = spans.map((s) => s.paths[0].toLowerCase())
  const seqFim = sc.map((s: any) => (imgs[s.imageIndex]?.path ?? '').toLowerCase())
  const mesmaSeq = seqApp.length === seqFim.length && seqApp.every((x, i) => x === seqFim[i])
  // efeito (rodizio por indice do bloco)
  const trocas: Record<string, number> = {}
  let comp = 0, trocados = 0
  if (sc.length === spans.length) sc.forEach((s: any, i: number) => {
    if (s.imageIndexB != null) return
    comp++
    const esp = KB[i % KB.length]
    if (s.effect !== esp) { trocados++; const k = `${esp}->${s.effect}`; trocas[k] = (trocas[k] ?? 0) + 1 }
  })
  // foco e entrada, por cena
  const foco = { auto: 0, centro: 0, manual: 0 }
  const fx: number[] = []
  for (const s of sc) {
    const im = imgs[s.imageIndex]; if (!im) continue
    if (im.focusAuto) foco.auto++
    else if (Math.abs(im.focusX - 0.5) <= 0.01) foco.centro++
    else { foco.manual++; fx.push(+im.focusX.toFixed(2)) }
  }
  const ss = sc.filter((s: any) => s.sourceStart > 0.01).map((s: any) => s.sourceStart)
  // gancho detalhado: palavras de cada cena
  const fimG = Math.max(...b.blocos.filter((x: any) => x.sentence === 0).map((x: any) => x.end))
  const gancho = sc.filter((s: any) => s.start < fimG - 0.05).map((s: any) => ({
    dur: +(s.end - s.start).toFixed(2),
    fala: palavras.filter((w: any) => w.start >= s.start - 0.02 && w.start < s.end - 0.02).map((w: any) => w.text).join(' '),
    clipe: (imgs[s.imageIndex]?.path ?? '').split(/[\\/]/).slice(-4).join('/'),
    efeito: s.effect, fx: imgs[s.imageIndex]?.focusAuto ? 'auto' : +(imgs[s.imageIndex]?.focusX ?? 0.5).toFixed(2), entrada: +(s.sourceStart ?? 0).toFixed(2),
  }))
  // palavras por cena
  const ppc = sc.map((s: any) => palavras.filter((w: any) => w.start >= s.start - 0.02 && w.start < s.end - 0.02).length)
  // ultima cena repete o gancho?
  const primeiros = new Set(sc.slice(0, gancho.length).map((s: any) => imgs[s.imageIndex]?.path))
  const fechaNoGancho = primeiros.has(imgs[sc.at(-1)?.imageIndex]?.path)
  // marcas por trecho
  const porTrecho = Object.values(b.porBloco).map((x: any) => x.length)
  out.push({
    nome, cenasApp: spans.length, cenasFim: sc.length, mesmaSeq, iguais, movidos, novos: fim.length - usados.size, tirados: app.length - iguais - movidos,
    deslMed: med(desl), antes: desl.filter((x) => x < 0).length, depois: desl.filter((x) => x > 0).length,
    efeitoComparado: comp, efeitoTrocado: trocados, trocas, foco, fx, entradaN: ss.length, entradaMed: med(ss),
    trans: sc.filter((s: any) => s.transitionIn && s.transitionIn !== 'cut').map((s: any) => ({ t: +s.start.toFixed(2), tipo: s.transitionIn, fala: palavras.filter((w: any) => w.start >= s.start - 0.02 && w.start < s.end - 0.02).map((w: any) => w.text).join(' ') })),
    camera: sc.filter((s: any) => s.camera).length, rot: sc.filter((s: any) => s.rotation).length, curvaEase: sc.filter((s: any) => s.curve !== 'linear').length, nenhum: sc.filter((s: any) => s.effect === 'nenhum').length,
    palavrasPorCena: med(ppc), porTrecho: { med: med(porTrecho), dist: porTrecho.reduce((m: any, k: number) => (m[k] = (m[k] || 0) + 1, m), {}) },
    pesos: Object.keys(b.pesos ?? {}).length, unioes: Object.values(b.unioes ?? {}).flat().length, cortesPuxados: Object.values(b.cortes ?? {}).flat().length,
    gancho, fechaNoGancho,
  })
}
writeFileSync(process.argv[3], JSON.stringify(out, null, 1))
console.log('ok', out.length)
