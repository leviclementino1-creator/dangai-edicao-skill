const alvos = await (await fetch(`http://127.0.0.1:${process.env.PORTA || 9354}/json/list`)).json()
const pagina = alvos.find((t) => t.type === 'page')
const ws = new WebSocket(pagina.webSocketDebuggerUrl)
await new Promise((r) => ws.addEventListener('open', r, { once: true }))
let seq = 0; const pend = new Map()
ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); const p = pend.get(m.id); if (p) { pend.delete(m.id); p(m) } })
const enviar = (method, params = {}) => new Promise((res) => { const id = ++seq; pend.set(id, res); ws.send(JSON.stringify({ id, method, params })) })
const avaliar = async (x) => (await enviar('Runtime.evaluate', { expression: `(async () => { ${x} })()`, awaitPromise: true, returnByValue: true })).result?.result?.value
const [, , acao, arg] = process.argv
const fs = await import('node:fs')
if (acao === 'js') console.log(JSON.stringify(await avaliar(fs.readFileSync(arg, 'utf8')), null, 1))
if (acao === 'foto') { const r = await enviar('Page.captureScreenshot', { format: 'png' }); fs.writeFileSync(arg, Buffer.from(r.result.data, 'base64')); console.log('ok') }
setTimeout(() => process.exit(0), 100)
