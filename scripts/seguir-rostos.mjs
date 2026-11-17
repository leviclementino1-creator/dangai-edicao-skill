// node seguir-rostos.mjs <lista.json>  — lista = [[n, id, x], ...] (x = meio do bloco na régua)
// Para cada bloco: clica na parte de BAIXO do bloco (o "x" de apagar fica em cima!), liga a
// Câmera livre e aperta "Seguir o rosto". Imprime o recado que o Dangai deu.
import fs from 'node:fs'
const lista = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))
const Y = Number(process.env.Y_BLOCO || 762)
const alvos = await (await fetch(`http://127.0.0.1:${process.env.PORTA || 9354}/json/list`)).json()
const ws = new WebSocket(alvos.find((t) => t.type === 'page').webSocketDebuggerUrl)
await new Promise((r) => ws.addEventListener('open', r, { once: true }))
let seq = 0; const pend = new Map()
ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); const p = pend.get(m.id); if (p) { pend.delete(m.id); p(m) } })
const enviar = (method, params = {}) => new Promise((res) => { const id = ++seq; pend.set(id, res); ws.send(JSON.stringify({ id, method, params })) })
const js = async (x) => (await enviar('Runtime.evaluate', { expression: `(async () => { ${x} })()`, awaitPromise: true, returnByValue: true })).result?.result?.value
const espera = (ms) => new Promise((r) => setTimeout(r, ms))
async function clicar(x, y) {
  for (const type of ['mousePressed', 'mouseReleased']) await enviar('Input.dispatchMouseEvent', { type, x, y, button: 'left', clickCount: 1 })
}
const botao = (txt) => js(`const b=[...document.querySelectorAll('button')].find(b=>b.offsetParent&&b.textContent.trim()===${JSON.stringify(txt)});if(!b)return false;b.click();return true`)
const blocos = () => js(`return [...document.querySelectorAll('*')].map(e=>e.children.length===0?e.textContent:'').find(t=>/^\\d+ blocos$/.test(t))`)
const antes = await blocos()
for (const [n, id, x] of lista) {
  await clicar(x, Y); await espera(1200)
  const titulo = await js(`const e=[...document.querySelectorAll('*')].find(e=>/^Bloco \\d+\\s*de \\d+$/.test(e.textContent.trim()));return e?e.textContent.trim().match(/\\d+/)[0]:null`)
  if (titulo !== String(n)) { console.log(n, id, 'PULEI: selecionou', titulo); continue }
  await botao('Câmera livre'); await espera(800)
  const ok = await botao('Seguir o rosto')
  let recado = ''
  for (let i = 0; i < 40 && ok; i++) {
    await espera(1000)
    recado = await js(`return [...document.querySelectorAll('p,div,span')].map(e=>e.children.length===0?e.textContent:'').find(t=>/Rosto encontrado|Não deu|nao deu|Nenhum rosto|rosto em/i.test(t))||''`)
    if (recado) break
  }
  console.log(n, id, ok ? recado || '(sem recado)' : 'sem botão Seguir o rosto')
}
const depois = await blocos()
console.log('blocos antes/depois:', antes, depois)
setTimeout(() => process.exit(0), 100)
