# TRADING DASHBOARD — Triple Seven Capital
# Instruções para Claude Code

## PROJECTO
- Dashboard: https://cap1974.github.io/trading-dashboard/
- Pasta local: C:\Users\Utilizador\trading-dashboard\
- Stack: HTML estático + data.js + Chart.js

## COMANDO DIÁRIO — "processa watched"
Quando o utilizador disser "processa watched" ou "processa hoje":

PASTA WATCHED (sempre aqui):
C:\Users\Utilizador\trading-dashboard\watched\

PASSOS:
1. Lista ficheiros em ./watched/ — procura eur_DD_MM.png + usd_DD_MM.png
2. Determina a data: DD_MM → YYYY-MM-DD (ano actual 2026)
3. Verifica se existe eventos_DD_MM.txt
4. Corre extract.js:
   node scripts/extract.js --date YYYY-MM-DD --eur ./watched/eur_DD_MM.png --usd ./watched/usd_DD_MM.png
   (adiciona --eventos ./watched/eventos_DD_MM.txt se existir)
5. Corre deploy.js:
   node scripts/deploy.js
6. Move ficheiros processados:
   ./watched/processados/YYYY-MM-DD/

## REGRAS CRÍTICAS
- NUNCA ler o trading_data.json completo
- NUNCA substituir dados existentes — sempre acumular
- NUNCA fazer push sem validação passar
- Backup automático antes de qualquer escrita
- Realizados SEMPRE acumulados (nunca substituir)

## BASES DO FUNDO (não alterar sem ordem explícita)
EUR · 8MSN: capital_base = 58.41€
USD · OMV: capital_base = 213.83$
Meta mensal: 10% da base do início do mês

## MESES ACTIVOS
2026-04: FECHADO · saldo_fim_eur 58.89 · saldo_fim_usd 209.87
2026-05: EM CURSO · base_eur 58.89 · base_usd 213.83 · base_aj_usd 272.28 (aportes 35.14+23.31$)

## REALIZADOS ACUMULADOS MAIO 2026
REAL_EUR_MAIO = +10.55€  (SMSN +10.55)
REAL_USD_MAIO = +8.15$   (FTI -0.52 + VOYA -0.77 + AMZN +0.23 + DELL +3.86 + GOOGL +2.75 + NVDA +2.60)
(actualizar a cada fecho com realizados)

## FORMATO EVENTOS_DD_MM.TXT
Ver modelo completo em: watched/MODELO_eventos.txt

DATA: DD/MM/YYYY

EUR:
SAIDA  | TICKER | Nome | +/-X.XX€ | saida:PRECO | entrada:PRECO | vol:N | Setup | Nota
ENTRADA| TICKER | Nome | entrada:PRECO | vol:N | Setup | Nota
APORTE | TICKER | Nome | +/-X.XX€ | preco:PRECO | vol:N | Nota
CAIXA  | X.XX€                          ← obrigatório, valor exacto screenshot

USD:
SAIDA  | TICKER | Nome | +/-X.XX$ | saida:PRECO | entrada:PRECO | vol:N | Setup | Nota
ENTRADA| TICKER | Nome | entrada:PRECO | vol:N | Setup | Nota
APORTE | TICKER | Nome | +/-X.XX$ | preco:PRECO | vol:N | Nota
TRANSFERENCIA | EUR→USD | -X.XX€ | +X.XX$ | Nota
CAIXA  | X.XX$                          ← obrigatório, valor exacto screenshot

DIARIO:
Texto livre com nota do dia

CAMPOS CRÍTICOS:
• SAIDA  → lucro + saida + entrada + vol  (para lucro_pct e REAL_MAIO)
• ENTRADA→ entrada + vol                  (base para deltas futuros)
• CAIXA  → SEMPRE presente, valor exacto  (actualiza display HTML)

## RATING CTM (automático)
≥30% → 5★
20-29.9% → 4★
10-19.9% → 3★
5-9.99% → 2★
0-4.99% → 1★
qualquer perda → 0★

## INÍCIO DE NOVO MÊS
Quando utilizador disser "início de [Mês]":
Base EUR = saldo XTB conta EUR
Base USD = saldo XTB conta USD
Cria novo entry em meses com base e meta (base × 0.10)
Reset realizados acumulados do mês para 0

## EFICIÊNCIA DE TOKENS
- Thinking budget: mínimo
- Zero explicações intermédias
- Zero leitura de ficheiros grandes
- Executar scripts em vez de processar JSON manualmente
- Um commit com tudo — nunca commits parciais
