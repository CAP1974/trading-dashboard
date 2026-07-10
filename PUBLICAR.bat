@echo off
cd /d "%~dp0"
set LOG=%~dp0publicar_log.txt
echo ---- PUBLICAR %date% %time% ---- > "%LOG%"
echo A validar os dados...
call node scripts\validate.js >> "%LOG%" 2>&1
if errorlevel 1 goto fail
if exist .git\index.lock del /f .git\index.lock
echo A guardar... 
git add -A >> "%LOG%" 2>&1
git commit -m "atualizacao dashboard" >> "%LOG%" 2>&1
echo A publicar no site...
git push >> "%LOG%" 2>&1
if errorlevel 1 goto failpush
echo. >> "%LOG%"
echo RESULTADO: PUBLICADO COM SUCESSO. O site atualiza em 1-2 minutos. >> "%LOG%"
goto fim
:fail
echo. >> "%LOG%"
echo RESULTADO: VALIDACAO FALHOU - NADA FOI PUBLICADO. Ler os erros acima. >> "%LOG%"
goto fim
:failpush
echo. >> "%LOG%"
echo RESULTADO: O PUSH FALHOU - guardado localmente, site NAO atualizou. >> "%LOG%"
:fim
start notepad "%LOG%"
