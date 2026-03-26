@echo off
setlocal

:: 배치 파일 위치로 이동
cd /d %~dp0

:: 날짜 생성
for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format Mdd"') do set filename=%%I.md

:: 복사
copy md.txt %filename%

:: VSCode로 열기
code %filename%

endlocal