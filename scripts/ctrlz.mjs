// node ctrlz.mjs : manda Ctrl+Z (desfazer) na janela do Dangai.
const alvos = await (await fetch(`http://127.0.0.1:${process.env.PORTA || 9354}/json/list`)).json()
const ws = new WebSocket(alvos.find((t) => t.type === 'page').webSocketDebuggerUrl)
await new Promise((r) => ws.addEventListener('open', r, { once: true }))
let seq = 0; const pend = new Map()
ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); const p = pend.get(m.id); if (p) { pend.delete(m.id); p(m) } })
const enviar = (method, params = {}) => new Promise((res) => { const id = ++seq; pend.set(id, res); ws.send(JSON.stringify({ id, method, params })) })
for (const type of ['keyDown', 'keyUp']) await enviar('Input.dispatchKeyEvent', { type, key: 'z', code: 'KeyZ', windowsVirtualKeyCode: 90, modifiers: 2 })
console.log('ok'); setTimeout(() => process.exit(0), 100)
