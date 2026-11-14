// Gera frases.json e planos.json (na pasta atual) para o folhas.py.
// node dados-das-folhas.js <rascunho.json> <episodio.json> [takeId]
// rascunho: %APPDATA%\Dangai\modulos\recap\recaps\<id>.json
// episodio: o episodio.json da pasta do episodio (ou <Biblioteca>/_indices/<id>/episodio.json)
const fs = require('fs')
const [, , arqR, arqE, takeId] = process.argv
const r = JSON.parse(fs.readFileSync(arqR, 'utf8'))
const ep = JSON.parse(fs.readFileSync(arqE, 'utf8'))
const ro = r.roteiros.find((x) => x.versao === r.atual) || r.roteiros.at(-1)
const t = takeId ? r.voz.takes.find((x) => x.id === takeId) : r.voz.takes.find((x) => x.id === r.voz.atual) || r.voz.takes.at(-1)
const ev = Object.fromEntries(r.eventos.map((e) => [e.id, e]))
const cues = Object.fromEntries((ep.cues || []).map((c) => [c.id, c]))
const esc = Object.fromEntries(((r.cenas && r.cenas.escolhas) || []).map((e) => [e.fraseId, e]))
const out = []
for (const s of ro.secoes) for (const f of s.frases) {
  const tr = t.trechos.find((x) => x.fraseId === f.id)
  if (!tr) continue
  const e = esc[f.id] || {}
  out.push({
    id: f.id, secao: s.papel, texto: f.texto, intencao: f.intencaoVisual, offset: tr.offset, dur: tr.duracao,
    palavras: t.palavras.filter((p) => p.fraseId === f.id).map((p) => [p.texto, +p.start.toFixed(2)]),
    eventos: (f.eventoIds || []).map((i) => ({ id: i, t0: ev[i]?.t0, t1: ev[i]?.t1, resumo: ev[i]?.resumo })),
    cue: cues[f.cueDoMomento] ? { t: cues[f.cueDoMomento].start, texto: cues[f.cueDoMomento].texto } : null,
    app: (e.cenas || []).map((c) => ({ planos: c.candidato.planoIds, in: c.candidato.inSec, out: c.candidato.outSec, w: c.palavraInicio })),
    fita: (e.fita || []).map((c) => ({ planos: c.planoIds, in: c.inSec, porque: c.porque })),
  })
}
fs.writeFileSync('frases.json', JSON.stringify(out, null, 1))
fs.writeFileSync('planos.json', JSON.stringify(ep.planos.map((p) => ({ id: p.id, s: p.start, e: p.end, kf: p.keyframe, pers: (p.personagens || []).map((x) => x.nome), fal: p.falantes }))))
console.log(out.length, 'frases;', ep.planos.length, 'planos. Agora: python folhas.py')
