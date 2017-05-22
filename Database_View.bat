@echo off
color 07
mode con:cols=85 lines=35
title SECURE VAULT- LEVEL 6 ACCESS
call :CurDir
python %Curnt%\nsa_view
pause
:CurDir
pushd %~dp0
set Curnt=%CD%
popd