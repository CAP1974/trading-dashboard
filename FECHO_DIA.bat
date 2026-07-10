@echo off
cd /d "%~dp0"
set LOG=%~dp0fecho_log.txt
echo ---- FECHO DO DIA %date% %time% ---- > "%LOG%"
echo A aplicar o fecho do dia...
call node scripts\ingest.js >> "%LOG%" 2>&1
if errorlevel 1 goto fail
if exist .git\index.lock del /f .git\index.lock
echo A guardar e publicar...
git add -A >> "%LOG%" 2>&1
git commit -m "diario fecho-dia" >> "%LOG%" 2>&1
git push >> "%LOG%" 2>&1
if errorlevel 1 goto failpush
echo. >> "%LOG%"
echo RESULTADO: DIA PUBLICADO COM SUCESSO. Site atualiza em 1-2 minutos. >> "%LOG%"
goto fim
:fail
echo. >> "%LOG%"
echo RESULTADO: FALHOU (validacao ou sem ficheiro fecho) - NADA PUBLICADO. Ler acima. >> "%LOG%"
goto fim
:failpush
echo. >> "%LOG%"
echo RESULTADO: PUSH FALHOU - dia guardado localmente, site NAO atualizou. >> "%LOG%"
:fim
start notepad "%LOG%"
