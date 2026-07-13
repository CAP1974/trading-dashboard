@echo off
cd /d "%~dp0"
set LOG=%~dp0corrigir_log.txt
echo ---- CORRIGIR DIA 13 %date% %time% ---- > "%LOG%"
echo A aplicar a correcao (Swiss Life + caixa EUR 0.39)...
call node scripts\patch_2026-07-13.js >> "%LOG%" 2>&1
if errorlevel 1 goto fail
echo A regenerar (regen + NAV)...
call node scripts\_regen.js >> "%LOG%" 2>&1
call node scripts\nav.mjs >> "%LOG%" 2>&1
echo A validar...
call node scripts\validate.js >> "%LOG%" 2>&1
if errorlevel 1 goto failval
if exist .git\index.lock del /f .git\index.lock
echo A guardar e publicar...
git add -A >> "%LOG%" 2>&1
git commit -m "correcao dia 13: entrada Swiss Life + caixa EUR 0.39" >> "%LOG%" 2>&1
git push >> "%LOG%" 2>&1
if errorlevel 1 goto failpush
echo. >> "%LOG%"
echo RESULTADO: CORRECAO PUBLICADA COM SUCESSO. Site atualiza em 1-2 minutos. >> "%LOG%"
goto fim
:fail
echo. >> "%LOG%"
echo RESULTADO: PATCH FALHOU - nada alterado. Ler acima. >> "%LOG%"
goto fim
:failval
echo. >> "%LOG%"
echo RESULTADO: VALIDACAO FALHOU - NADA PUBLICADO. Ler os erros acima. >> "%LOG%"
goto fim
:failpush
echo. >> "%LOG%"
echo RESULTADO: PUSH FALHOU - correcao guardada localmente, site NAO atualizou. >> "%LOG%"
:fim
start notepad "%LOG%"
