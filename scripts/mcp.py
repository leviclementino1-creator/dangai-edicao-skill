"""Chama uma ferramenta do MCP do Dangai direto (sem o Claude Code ter o MCP carregado).
uso: python mcp.py <ferramenta> '<json args>' [prefixo_das_imagens]
senha: variavel DANGAI_MCP_SENHA (a da secao "Claude (MCP)" do Dangai). Imagens vao para <prefixo>N.jpg.
NAO montar o JSON-RPC em bash com ${2:-{}}: o "}" quebra os argumentos e a ferramenta recebe {} calada."""
import json, sys, os, base64, urllib.request
nome = sys.argv[1]; args = json.loads(sys.argv[2] if len(sys.argv) > 2 else '{}'); pre = sys.argv[3] if len(sys.argv) > 3 else 'mcp_img'
porta = os.environ.get('DANGAI_MCP_PORTA', '47321')
corpo = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": nome, "arguments": args}}).encode()
rq = urllib.request.Request(f'http://127.0.0.1:{porta}/mcp', data=corpo, headers={'Authorization': 'Bearer ' + os.environ['DANGAI_MCP_SENHA'], 'Content-Type': 'application/json'})
d = json.loads(urllib.request.urlopen(rq, timeout=300).read())
if 'error' in d: print(d['error']); sys.exit(1)
k = 0
for c in d['result']['content']:
    if c['type'] == 'image':
        open(f'{pre}{k}.jpg', 'wb').write(base64.b64decode(c['data'])); print('img', f'{pre}{k}.jpg'); k += 1
    else: print(c['text'])
