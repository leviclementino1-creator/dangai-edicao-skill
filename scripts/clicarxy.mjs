const [, , x, y] = process.argv
const alvos = await (await fetch(`http://127.0.0.1:${process.env.PORTA || 9354}/json/list`)).json()
const ws = new WebSocket(alvos.find((t) => t.type === 'page').webSocketDebuggerUrl)
await new Promise((r) => ws.addEventListener('open', r, { once: true }))
let seq = 0; const pend = new Map()
ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); const p = pend.get(m.id); if (p) { pend.delete(m.id); p(m) } })
const enviar = (method, params = {}) => new Promise((res) => { const id = ++seq; pend.set(id, res); ws.send(JSON.stringify({ id, method, params })) })
for (const type of ['mousePressed', 'mouseReleased']) await enviar('Input.dispatchMouseEvent', { type, x: +x, y: +y, button: 'left', clickCount: 1 })
console.log('ok'); setTimeout(() => process.exit(0), 100)
