// alvo: o texto do botao (o c.sh troca "Abrir no editor")
const alvo = "Abrir no editor"
const els = [...document.querySelectorAll('button, [role=button], a')].filter(e => e.offsetParent !== null && e.textContent.trim().includes(alvo))
if (!els.length) return 'nao achei: ' + alvo
els[0].click(); return 'cliquei: ' + els[0].textContent.trim().slice(0, 80)

