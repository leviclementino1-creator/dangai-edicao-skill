// RECONHECER NA MAO pelo Claude (o "Reconhecer na mao" / "Revisar personagens" do Gerar recap).
// Precisa do Dangai aberto com --remote-debugging-port (PORTA, padrao 9354) e do motor instalado.
//
//   node reconhecer.mjs iniciar <episodioId> <pasta>      agrupa os rostos (minutos) e baixa:
//        <pasta>/grupos.json (key, cenas, sugestoes, conhecido, figurante, n de rostos)
//        <pasta>/g<key>_<i>.jpg (ate 8 rostos por grupo) e <pasta>/elenco/<n>.jpg (fotos do elenco)
//   node reconhecer.mjs ver <episodioId> <pasta>          o mesmo, sem iniciar (descoberta ja pronta)
//   node reconhecer.mjs confirmar <jobId> <decisao.json>  grava os nomes:
//        {"nomes":{"0":"Lily Flambert"},"ignorados":[5],"juntar":[[1,4]],"removidos":{"0":[2]}}
//        nome EXATAMENTE como no elenco (grupos.json -> elenco); grupo sem nome = ignorado.
//   node reconhecer.mjs cancelar <jobId>
//
// Depois rode folha-grupos.py <pasta> para a folha de rostos por grupo.
const PORTA = process.env.PORTA || 9354
const fs = await import('node:fs')
const path = await import('node:path')
const alvos = await (await fetch(`http://127.0.0.1:${PORTA}/json/list`)).json()
const ws = new WebSocket(alvos.find((t) => t.type === 'page').webSocketDebuggerUrl)
await new Promise((r) => ws.addEventListener('open', r, { once: true }))
let seq = 0
const pend = new Map()
ws.addEventListener('message', (e) => {
  const m = JSON.parse(e.data)
  const p = pend.get(m.id)
  if (p) {
    pend.delete(m.id)
    p(m)
  }
})
const enviar = (method, params = {}) => new Promise((res) => { const id = ++seq; pend.set(id, res); ws.send(JSON.stringify({ id, method, params })) })
const avaliar = async (x) => {
  const r = await enviar('Runtime.evaluate', { expression: `(async () => { ${x} })()`, awaitPromise: true, returnByValue: true })
  if (r.result?.exceptionDetails) throw new Error(JSON.stringify(r.result.exceptionDetails).slice(0, 400))
  return r.result?.result?.value
}
const R = 'window.dangai.modulos.recap'
const [, , acao, a, b] = process.argv
const espera = (ms) => new Promise((r) => setTimeout(r, ms))

async function baixar(url, arquivo) {
  const b64 = await avaliar(`const r = await fetch(${JSON.stringify(url)}); const b = new Uint8Array(await r.arrayBuffer()); let s=''; for (const x of b) s += String.fromCharCode(x); return btoa(s)`)
  fs.writeFileSync(arquivo, Buffer.from(b64, 'base64'))
}

async function ver(episodioId, pasta) {
  for (let k = 0; k < 400; k++) {
    const r = await avaliar(`return await ${R}.descobertaAtual(${JSON.stringify(episodioId)})`)
    const ev = r?.ok ? r.value : null
    const st = ev?.estado?.status
    if (st === 'pronta' && ev.pronta) {
      const p = ev.pronta
      fs.mkdirSync(path.join(pasta, 'elenco'), { recursive: true })
      for (const g of p.grupos) for (const [i, u] of g.rostos.entries()) await baixar(u, path.join(pasta, `g${g.key}_${i}.jpg`))
      const elenco = []
      for (const [i, e] of p.elenco.entries()) {
        if (e.foto) await baixar(e.foto, path.join(pasta, 'elenco', `${i}.jpg`)).catch(() => {})
        elenco.push({ i, nome: e.nome, foto: Boolean(e.foto) })
      }
      const grupos = p.grupos.map((g) => ({ key: g.key, cenas: g.cenas, rostos: g.rostos.length, totalDeRostos: g.totalDeRostos, sugestao: g.sugestao, sugestoes: g.sugestoes.slice(0, 4), conhecido: g.conhecido, figurante: g.figurante }))
      fs.writeFileSync(path.join(pasta, 'grupos.json'), JSON.stringify({ jobId: p.jobId, anime: p.anime, online: p.online, grupos, elenco, decisaoSalva: ev.decisaoSalva ?? null }, null, 1))
      console.log(`pronta: job ${p.jobId}, ${grupos.length} grupos, elenco ${elenco.length} -> ${pasta}`)
      return
    }
    if (st === 'falhou' || st === 'cancelada') throw new Error(`descoberta ${st}: ${ev.estado.erro ?? ''}`)
    if (k % 6 === 0) console.log(`${st ?? 'sem descoberta'} ${ev?.estado?.mensagem ?? ''}`)
    await espera(5000)
  }
  throw new Error('demorou demais')
}

try {
  if (acao === 'iniciar') {
    const r = await avaliar(`return await ${R}.iniciarDescoberta({ episodioId: ${JSON.stringify(a)} })`)
    if (!r?.ok) throw new Error(JSON.stringify(r).slice(0, 400))
    await ver(a, b)
  } else if (acao === 'ver') await ver(a, b)
  else if (acao === 'confirmar') {
    const decisao = JSON.parse(fs.readFileSync(b, 'utf8'))
    const r = await avaliar(`return await ${R}.confirmarDescoberta(${JSON.stringify(a)}, ${JSON.stringify({ ignorados: [], juntar: [], removidos: {}, ...decisao })})`)
    console.log(JSON.stringify(r, null, 1).slice(0, 3000))
  } else if (acao === 'cancelar') console.log(JSON.stringify(await avaliar(`return await ${R}.cancelarDescoberta(${JSON.stringify(a)}, false)`)))
  else console.log('uso: iniciar|ver <episodioId> <pasta> | confirmar <jobId> <decisao.json> | cancelar <jobId>')
} catch (e) {
  console.error(String(e))
  process.exitCode = 1
}
setTimeout(() => process.exit(), 100)
