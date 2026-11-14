#!/bin/bash
# Clica no 1o botao visivel com o texto $1 (PORTA=9353 para o Dangai de dev).
D=$(dirname "$0")
python -c "import sys,json;print(open(sys.argv[1],encoding='utf8').read().replace('__TEXTO__',json.dumps(sys.argv[2])))" "$D/clicar.js" "$1" > "$D/_c.js"
node "$D/cdp.mjs" js "$D/_c.js"
