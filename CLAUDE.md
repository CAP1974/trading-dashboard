## FLUXO DIÁRIO — WATCHED FOLDER

Pasta watched: C:\Users\Utilizador\trading-dashboard\watched\

Quando o utilizador disser "processa watched" ou "processa hoje":
1. Procura ficheiros em ./watched/ (relativo à raiz do projecto)
2. Identifica par eur_DD_MM.png + usd_DD_MM.png mais recente
3. Corre: node scripts/extract.js --date YYYY-MM-DD --eur ./watched/eur_DD_MM.png --usd ./watched/usd_DD_MM.png
4. Se existir eventos_DD_MM.txt: adiciona --eventos ./watched/eventos_DD_MM.txt
5. Corre: node scripts/deploy.js
6. Move ficheiros para ./watched/processados/YYYY-MM-DD/

NUNCA procurar em trading-watcher ou outras pastas.
NUNCA ler o trading_data.json completo.

## MODO EFICIÊNCIA — SEMPRE ACTIVO

Tokens:
- Zero narração de processo
- Zero confirmações intermédias
- Zero resumos do que foi feito
- Resultado directo ou erro

Pensamento:
- Thinking budget: mínimo necessário
- Não explicar raciocínio salvo erro crítico
- Uma solução, não alternativas

Código:
- Escrever ficheiro completo de uma vez
- Sem comentários óbvios
- Sem TODO nem placeholders

Git:
- Sempre um único commit com tudo
- Mensagem curta: "feat: X" ou "fix: X"

Erros:
- Reportar só o essencial: ficheiro + linha + causa
- Propor fix imediato sem pedir confirmação

Ficheiros grandes:
- Ler só o necessário (grep/sed em vez de cat completo)
- Editar só as linhas afectadas

## FECHO DIÁRIO — FORMATO OBRIGATÓRIO

Quando o utilizador apresenta fechos do dia, SEMPRE verificar se forneceu caixa EUR e USD.
Se não forneceu, perguntar IMEDIATAMENTE antes de correr o pipeline:
  "Qual o valor de caixa EUR e USD hoje? (senão mantém carry-forward do dia anterior)"

Template completo de fecho diário:
```
Fechos de hoje DD/MM/YYYY:
--eur screenshot/eur_DD_MM.png
--usd screenshot/usd_DD_MM.png
Caixa EUR: X.XX€
Caixa USD: X.XX$
Realizados EUR: [lista: TICKER ±X.XX€ Venda/Compra]
Realizados USD: [lista: TICKER ±X.XX$ Venda/Compra]
Entradas: [lista de novos activos abertos]
```

Comando pipeline com caixa:
```
node scripts/pipeline.js \
  --eur screenshot/eur_DD_MM.png \
  --usd screenshot/usd_DD_MM.png \
  --caixa-eur X.XX \
  --caixa-usd X.XX
```

Caixa carry-forward: se --caixa-eur/usd não fornecido, extract.js usa automaticamente
o valor do dia anterior mais recente. Confirmar no output: "Caixa EUR: X (carry-forward de YYYY-MM-DD)".

## PROTECÇÃO DE DADOS
- NUNCA escrever trading_data.json sem backup prévio (extract.js faz isto automaticamente)
- NUNCA fazer push sem validação passar (deploy.js valida antes do git push)
- Em caso de dados corrompidos: node scripts/restore.js --list
- Backups em data/backups/ — últimos 30 mantidos, ignorados pelo git
