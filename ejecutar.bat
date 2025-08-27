@echo off
echo ===================================
echo Calculadora de Lenguajes Formales
echo ===================================
echo.
echo Iniciando la aplicacion...
echo La aplicacion se abrira automaticamente en tu navegador web
echo.
echo URL: http://localhost:8501
echo.
echo Para detener la aplicacion, presiona Ctrl+C en esta ventana
echo.

"%USERPROFILE%\AppData\Local\Programs\Python\Python313\Scripts\streamlit.exe" run app.py

pause
