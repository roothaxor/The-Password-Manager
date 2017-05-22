@echo off
color 17
mode con:cols=70 lines=14
title Military Grade Password Generation v.4.0
call :CurDir
python %Curnt%\nsa_gen
goto :EOF
:CurDir
pushd %~dp0
set Curnt=%CD%
popd
goto :EOF
REM pipe for py
