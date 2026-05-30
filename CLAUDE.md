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

PASSOS OBRIGATÓRIOS (SEMPRE TODOS):

1. Lista ./watched/ — localiza os 3 ficheiros:
   • eur_DD_MM.png      ← screenshot conta EUR
   • usd_DD_MM.png      ← screenshot conta USD
   • eventos_DD_MM.txt  ← eventos do dia (SEMPRE presente)

2. Determina a data: DD_MM → YYYY-MM-DD (ano actual 2026)

3. LÊ os 3 ficheiros ANTES de qualquer escrita:
   a) Read eur_DD_MM.png   → saldo EUR, caixa EUR, posições abertas EUR
   b) Read usd_DD_MM.png   → saldo USD, caixa USD, posições abertas USD
   c) Read eventos_DD_MM.txt → saídas, entradas, aportes, caixa, diário

4. Corre extract.js (posições abertas):
   node scripts/extract.js --date YYYY-MM-DD --eur ./watched/eur_DD_MM.png --usd ./watched/usd_DD_MM.png

5. Aplica eventos do .txt ao JSON (extract.js NÃO processa o .txt):
   Para cada linha activa (sem #):
   • SAIDA  → adicionar a posicoes_fechadas + eventos[] + actualizar REAL_MAIO
   • ENTRADA→ adicionar a eventos[] (posição já captada pelo extract.js)
   • APORTE → adicionar a eventos[]
   • CAIXA  → actualizar eur.caixa / usd.caixa no dia
   • DIARIO → adicionar diario.nota

6. Corre: node scripts/_regen.js

7. Actualiza index.html:
   • Capital EUR / USD (saldo do screenshot)
   • Caixa EUR / USD
   • Retorno EUR/USD % meta (= (REAL+LUCRO_ABT) / meta × 100)
   • Equity sub (realizado + lucro aberto)
   • AUM (SALDO_EUR + SALDO_USD × 0.92)

8. Move para ./watched/processados/YYYY-MM-DD/:
   eur_DD_MM.png, usd_DD_MM.png, eventos_DD_MM.txt

9. Commit único + push

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
2026-05: FECHADO · saldo_fim_eur 73.10 · saldo_fim_usd 294.09 · real_eur +10.75 · real_usd +12.77 · equity_eur 350.1% · equity_usd 121.6% · 18 trades · WR 50% · PF 3.29
2026-06: EM CURSO · base_eur 73.10 · base_usd 294.09 · meta_eur 7.31 · meta_usd 29.41

## REALIZADOS ACUMULADOS JUNHO 2026
REAL_EUR_JUN = +0.00€
REAL_USD_JUN = +0.00$
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
