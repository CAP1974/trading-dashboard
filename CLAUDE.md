# TRADING DASHBOARD — Triple Seven Capital
# Instruções para Claude Code

## PROJECTO
- Dashboard: https://cap1974.github.io/trading-dashboard/
- Pasta local: C:\Users\Utilizador\trading-dashboard\
- Stack: HTML estático + data.js + Chart.js

## NOTA (2026-07-17)
Houve uma tentativa de automatizar este fluxo com uma app externa ("Fecho do Dia" / CTM PRO)
que gerava `watched/fecho_YYYY-MM-DD.json` e um script `scripts/ingest.js` para o aplicar sem
ler screenshots. Não resultou (validação falhava e exigia correção manual na mesma) e foi
removida em 2026-07-17. O fluxo activo é sempre o "COMANDO DIÁRIO" abaixo — ler sempre os
screenshots e o eventos.txt à mão.

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

4. Escreve o dia YYYY-MM-DD no trading_data.json (posições abertas lidas dos screenshots).
   Um script Python `scripts/tmp_DD_MM.py` por dia é o padrão usado — cria, corre, e mantém
   como registo do que foi escrito.

5. Aplica eventos do .txt ao JSON:
   Para cada linha activa (sem #):
   • SAIDA  → adicionar a posicoes_fechadas + eventos[] + actualizar REAL_MAIO
   • ENTRADA→ adicionar a eventos[] (posição já captada pelo extract.js)
   • APORTE → adicionar a eventos[]
   • CAIXA  → actualizar eur.caixa / usd.caixa no dia
   • DIARIO → adicionar diario.nota

6. Corre: node scripts/_regen.js

6b. Verificação opcional recomendada: node scripts/validate.js
    • Não é bloqueante — algumas regras dão falso positivo em casos legítimos (ex: ativos
      cotados em moeda diferente do EUR/USD como Swiss Life; "atual"=0 fora de horas de
      mercado é normal, não um erro). Ler o resultado com juízo antes de "corrigir" algo
      que na verdade está certo.
    • ⚠️ NOTA schema (confirmado empiricamente 2026-07-15, saldo−Σvalor(posições)==caixa em
      TODOS os dias desde 29/05): `saldo` de cada dia JÁ É o capital total da conta (caixa +
      Σvalor das posições) — é literalmente o que a XTB mostra em "Valor das Minhas Operações"
      no fundo do ecrã, apesar do nome sugerir "só posições". O campo `caixa` é guardado
      também, em separado, só para referência/exibição (ex: tabela XLSX) — NUNCA somar caixa
      a saldo outra vez (AUM, Capital EUR/USD, NAV). Bug cometido e corrigido em 2026-07-15:
      "correcao" da caixa tinha introduzido dupla contagem em index.html, no fecho de Junho/
      base de Julho, e no nav.mjs.

6c. NAV (quotas), opcional: node scripts/nav.mjs — recalcula o NAV unitizado (retorno oficial TWR).
    Usa `saldo` sozinho como capital total (NÃO somar caixa). Corre quando quiseres que a aba
    NAV reflita o dia.
    • Depósito/levantamento/transferência EXTERNOS: registar SEMPRE em fund_metrics
      (usd.aportes / eur.transferencias, com data) — o NAV lê dali. Aportes a posições
      financiados pela caixa NÃO são fluxos externos.

7. Actualiza index.html:
   • Capital EUR / USD = saldo do dia (já é o capital total, NÃO somar caixa outra vez)
   • Retorno EUR/USD % meta (= (REAL+LUCRO_ABT) / meta × 100)
   • Equity sub (realizado + lucro aberto)
   • AUM (saldo_EUR + saldo_USD × fx do dia; fallback 0.92)

8. Move para ./watched/processados/YYYY-MM-DD/:
   eur_DD_MM.png, usd_DD_MM.png, eventos_DD_MM.txt

9. Commit único + push

## REGRAS CRÍTICAS
- NUNCA ler o trading_data.json completo
- NUNCA substituir dados existentes — sempre acumular
- Se CAIXA do eventos.txt divergir do screenshot, PARAR e perguntar ao utilizador antes de processar
- Backup automático antes de qualquer escrita
- Realizados SEMPRE acumulados (nunca substituir)
- Datas SEMPRE no ano corrente (2026) — nunca 2025 (bug corrigido 2026-07-10)
- STOPS: cada posição aberta deve ter campo `stop` (preço). pct ≤ −10% = STOP DURO violado →
  alertar o utilizador no resumo do dia. (CBRS/SpaceX são exceção histórica marcada.)

## BASES DO FUNDO (não alterar sem ordem explícita)
EUR · 8MSN: capital_base = 58.41€
USD · OMV: capital_base = 213.83$
Meta mensal: 10% da base do início do mês

## MESES ACTIVOS
Ver sempre `meses` no trading_data.json — é a fonte única e actual (status FECHADO/EM CURSO,
base, meta, realizado, saldo_fim). Não duplicar esses números aqui, ficam desatualizados.

## REALIZADOS ACUMULADOS DO MÊS EM CURSO
Ver `meses["YYYY-MM"].realizado_eur` / `.realizado_usd` no JSON — actualizar a cada dia
processado com saídas, nunca substituir manualmente aqui.

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
