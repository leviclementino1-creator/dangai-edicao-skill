// Mede os projetos .dangai (so leitura). Uso: node medir.cjs <lista.txt> <saida.json>
const fs = require('fs')
const path = require('path')
const lista = fs.readFileSync(process.argv[2], 'utf8').split(/\r?\n/).filter(Boolean)
const med = (a) => { if (!a.length) return null; const s = [...a].sort((x, y) => x - y); return +s[Math.floor(s.length / 2)].toFixed(3) }
const avg = (a) => a.length ? +(a.reduce((x, y) => x + y, 0) / a.length).toFixed(3) : null
const cont = (a) => a.reduce((m, k) => (m[k] = (m[k] || 0) + 1, m), {})
const tipo = (p) => {
  const ext = path.extname(p || '').toLowerCase()
  const low = (p || '').toLowerCase()
  if (/\\shots\\/.test(low)) return 'shot'
  if (/mang/.test(low)) return 'manga'
  if (/filme/.test(low)) return 'filme'
  if (['.png', '.jpg', '.jpeg', '.webp'].includes(ext)) return 'print'
  if (['.mp4', '.mkv', '.mov', '.webm'].includes(ext)) return 'video'
  if (ext === '.gif') return 'gif'
  return ext || '?'
}
const out = []
for (const f of lista) {
  let p
  try { p = JSON.parse(fs.readFileSync(f, 'utf8')) } catch (e) { out.push({ f, erro: String(e).slice(0, 80) }); continue }
  const sc = p.plan?.scenes ?? []
  if (sc.length < 3) { out.push({ f: path.basename(f), vazio: true, cenas: sc.length }); continue }
  const imgs = p.images ?? []
  const dur = Math.max(...sc.map((s) => s.end))
  const durs = sc.map((s) => s.end - s.start)
  const blocos = p.biblioteca?.blocos ?? []
  // gancho: primeira frase (sentence 0) do roteiro; senao 1o ponto final nas palavras
  let fimGancho = null
  if (blocos.length) fimGancho = Math.max(...blocos.filter((b) => b.sentence === 0).map((b) => b.end))
  else {
    const w = p.transcript?.words ?? []
    const i = w.findIndex((x) => /[.!?]$/.test(x.text))
    if (i >= 0) fimGancho = w[i].end
  }
  const gancho = fimGancho == null ? [] : sc.filter((s) => s.start < fimGancho - 0.05)
  const usados = new Set(sc.map((s) => s.imageIndex))
  const imgsUsadas = [...usados].map((i) => imgs[i]).filter(Boolean)
  const fx = imgsUsadas.filter((i) => i.focusAuto === false && Math.abs(i.focusX - 0.5) > 0.01)
  const trilhas = (p.trilhas ?? []).map(({ peaks, rms, ...r }) => r)
  const porFaixa = {}
  for (const t of trilhas) {
    const k = 'A' + (t.faixa + 1)
    porFaixa[k] ??= []
    porFaixa[k].push({ nome: t.fileName, db: t.gainDb, at: +t.at.toFixed(2), usa: t.usarSec == null ? +(t.durationSec - t.inicioSec).toFixed(2) : +t.usarSec.toFixed(2), fi: t.fadeInSec, fo: t.fadeOutSec, duck: !!t.ducking })
  }
  // comparacao: o que ele marcou na Biblioteca (porBloco) contra o que ficou na timeline
  let marcadas = 0, foraDasMarcas = 0
  const pb = p.biblioteca?.porBloco ?? {}
  const todasMarcadas = new Set(Object.values(pb).flat().map((x) => x.toLowerCase()))
  if (todasMarcadas.size) {
    for (const s of sc) {
      const im = imgs[s.imageIndex]
      if (!im) continue
      marcadas++
      if (!todasMarcadas.has((im.path || '').toLowerCase())) foraDasMarcas++
    }
  }
  // cortes no meio de frase vs no fim de frase (bloco)
  const fronteiras = new Set(blocos.map((b) => +b.end.toFixed(1)))
  const cortesNoBloco = sc.slice(1).filter((s) => blocos.some((b) => Math.abs(b.start - s.start) < 0.15)).length
  out.push({
    f: path.basename(f), pasta: path.dirname(f), salvo: p.savedAt, formato: p.formato, origem: p.planOrigin, editado: p.planEdited,
    dur: +dur.toFixed(1), cenas: sc.length, segPorCena: { med: med(durs), media: avg(durs), min: +Math.min(...durs).toFixed(2), max: +Math.max(...durs).toFixed(2) },
    frases: blocos.length, cortesNoInicioDeBloco: cortesNoBloco,
    gancho: { fim: fimGancho && +fimGancho.toFixed(2), cenas: gancho.length, tipos: cont(gancho.map((s) => tipo(imgs[s.imageIndex]?.path))), segs: gancho.map((s) => +(s.end - s.start).toFixed(2)), efeitos: gancho.map((s) => s.effect) },
    tipos: cont(sc.map((s) => tipo(imgs[s.imageIndex]?.path))),
    repetidas: sc.length - new Set(sc.map((s) => imgs[s.imageIndex]?.path)).size,
    focoAuto: imgsUsadas.filter((i) => i.focusAuto).length, focoManual: fx.length, focoMeio: imgsUsadas.filter((i) => !i.focusAuto && Math.abs(i.focusX - 0.5) <= 0.01).length,
    focoManualX: fx.map((i) => +i.focusX.toFixed(2)), invertido: imgsUsadas.filter((i) => i.invertido).length,
    sourceStart: { comEntrada: sc.filter((s) => s.sourceStart > 0.01).length, med: med(sc.filter((s) => s.sourceStart > 0.01).map((s) => s.sourceStart)) },
    efeitos: cont(sc.map((s) => s.effect)), intens: cont(sc.map((s) => s.intensity)), curvas: cont(sc.map((s) => s.curve)),
    camera: sc.filter((s) => s.camera).length, cameraKeys: sc.filter((s) => s.camera?.keys?.length).length, rotacao: sc.filter((s) => s.rotation).length,
    divididas: sc.filter((s) => s.imageIndexB != null).length,
    transicoes: cont(sc.map((s) => s.transitionIn)),
    legenda: { on: p.captionsEnabled, editada: p.captionsEdited, fonte: p.captionFont, cor: p.captionColor, escala: p.captionScale, y: p.captionY, anim: p.captionAnimation, quadros: p.captionAnimationFrames, curva: p.captionAnimationCurve, marca: p.captionMark, pont: p.captionPontuacao, contorno: p.captionStroke, sombra: p.captionShadow, palavrasPorBloco: avg((p.captions ?? []).map((c) => c.words?.length ?? 0)) },
    faixas: porFaixa, music: p.music ? { nome: path.basename(p.music.path || p.music), db: p.musicGainDb } : null, sfxAuto: p.sfxEnabled, sfxManual: (p.sfxManual ?? []).length,
    sobre: (p.sobreposicoes ?? []).map((o) => ({ tipo: o.tipo, nome: o.fileName, cor: o.cor ? Object.fromEntries(Object.entries(o.cor).filter(([k, v]) => typeof v === 'number' && v !== 0 && k !== 'intensidade')) : null, efeito: o.efeito, usa: o.usarSec, durationSec: o.durationSec })),
    audio: p.edicaoDeAudio ? { cadeia: Object.fromEntries(Object.entries(p.edicaoDeAudio.cadeia ?? {}).map(([k, v]) => [k, v && typeof v === 'object' ? v.ligado : v])) } : null,
    gancoTexto: p.hookText, fimTexto: p.endText,
    biblioteca: { marcadas: todasMarcadas.size, cenasNaTimeline: marcadas, foraDasMarcas, unioes: Object.values(p.biblioteca?.unioes ?? {}).flat().length, cortesPuxados: Object.values(p.biblioteca?.cortes ?? {}).flat().length },
    modulos: Object.keys(p.modulos ?? {}),
  })
}
fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 1))
console.log('ok', out.length, 'vazios', out.filter((o) => o.vazio).length)
