// O que a Biblioteca montaria (mesmas contas do app) x o que ficou no .dangai. So LE os projetos.
// Uso (de dentro do clone do Dangai):
//   DANGAI_REPO=E:/Projetos/dangai npx tsx --tsconfig tsconfig.node.json <este arquivo> <lista.txt>
import { readFileSync } from 'node:fs'
import { pathToFileURL } from 'node:url'
const REPO = process.env.DANGAI_REPO ?? 'E:/Projetos/dangai'
const { KEN_BURNS_EFFECTS, CLIP_INTENSITY } = await import(pathToFileURL(`${REPO}/shared/contract.ts`).href)
const { slotsDoTrecho, palavrasDoTrecho, spansDoTrecho } = await import(pathToFileURL(`${REPO}/shared/trecho.ts`).href)

const lista = readFileSync(process.argv[2], 'utf8').split(/\r?\n/).filter(Boolean)
const tot = { proj: 0, slots: 0, cenas: 0, cortesApp: 0, cortesIguais: 0, cortesMovidos: 0, deslocs: [] as number[], cortesNovos: 0, cortesTirados: 0, efeitoTrocado: 0, efeitoComparado: 0, intensTrocada: 0, trocas: {} as Record<string, number>, novoEfeitoAposTroca: {} as Record<string, number> }
const porProj: string[] = []
for (const f of lista) {
  let p: any
  try { p = JSON.parse(readFileSync(f, 'utf8')) } catch { continue }
  const b = p.biblioteca
  const sc = p.plan?.scenes ?? []
  if (!b?.blocos?.length || !Object.keys(b.porBloco ?? {}).length || sc.length < 3) continue
  const palavras = p.transcript?.words ?? []
  const spans: { start: number; end: number }[] = []
  for (const [i, frase] of b.blocos.entries()) {
    const cenas = b.porBloco[String(i)] ?? []
    if (!cenas.length) continue
    const slots = slotsDoTrecho(cenas, b.pesos?.[String(i)], b.unioes?.[String(i)])
    const pal = palavrasDoTrecho(palavras, frase.start, frase.end)
    const c = b.cortes?.[String(i)]
    const cortes = c?.length === slots.length - 1 ? c : null
    spans.push(...spansDoTrecho(frase.start, frase.end, slots, pal, cortes))
  }
  const app = spans.slice(1).map((s) => s.start)
  const fim = sc.slice(1).map((s: any) => s.start)
  let iguais = 0, movidos = 0
  const usados = new Set<number>()
  for (const t of app) {
    let melhor = -1, d = Infinity
    fim.forEach((u: number, j: number) => { if (!usados.has(j) && Math.abs(u - t) < d) { d = Math.abs(u - t); melhor = j } })
    if (d < 0.05) { iguais++; usados.add(melhor) }
    else if (d < 0.6) { movidos++; usados.add(melhor); tot.deslocs.push(+(fim[melhor] - t).toFixed(2)) }
  }
  const novos = fim.length - usados.size
  const tirados = app.length - iguais - movidos
  // efeito: o app gira KEN_BURNS_EFFECTS por indice de bloco
  let trocados = 0, comp = 0, intens = 0
  if (Math.abs(sc.length - spans.length) <= 0) {
    sc.forEach((s: any, i: number) => {
      const esperado = KEN_BURNS_EFFECTS[i % KEN_BURNS_EFFECTS.length]
      if (s.imageIndexB != null) return
      comp++
      if (s.effect !== esperado) { trocados++; const k = `${esperado}->${s.effect}`; tot.trocas[k] = (tot.trocas[k] ?? 0) + 1 }
      if (s.intensity !== CLIP_INTENSITY) intens++
    })
  }
  tot.proj++; tot.slots += spans.length; tot.cenas += sc.length; tot.cortesApp += app.length; tot.cortesIguais += iguais; tot.cortesMovidos += movidos; tot.cortesNovos += novos; tot.cortesTirados += tirados
  tot.efeitoTrocado += trocados; tot.efeitoComparado += comp; tot.intensTrocada += intens
  porProj.push(`${f.split('\\').pop()!.slice(0, 38).padEnd(38)} slots ${spans.length} cenas ${sc.length} | cortes iguais ${iguais} movidos ${movidos} novos ${novos} tirados ${tirados} | efeito trocado ${trocados}/${comp}`)
}
console.log(porProj.join('\n'))
const d = tot.deslocs.sort((a, b) => a - b)
console.log(JSON.stringify({ ...tot, deslocs: undefined, deslocMed: d[Math.floor(d.length / 2)], deslocAbsMed: [...d].map(Math.abs).sort((a, b) => a - b)[Math.floor(d.length / 2)], antes: d.filter((x) => x < 0).length, depois: d.filter((x) => x > 0).length }, null, 1))
