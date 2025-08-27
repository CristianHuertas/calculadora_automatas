Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Calculadora de Lenguajes Formales" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Iniciando la aplicación..." -ForegroundColor Green
Write-Host "La aplicación se abrirá automáticamente en tu navegador web" -ForegroundColor Yellow
Write-Host ""
Write-Host "URL: http://localhost:8501" -ForegroundColor Blue
Write-Host ""
Write-Host "Para detener la aplicación, presiona Ctrl+C en esta ventana" -ForegroundColor Red
Write-Host ""

try {
    # Intentar usar streamlit desde PATH
    streamlit run app.py
} catch {
    Write-Host "Intentando con la ruta completa de Python..." -ForegroundColor Yellow
    # Usar la ruta completa si no está en PATH
    & "$env:USERPROFILE\AppData\Local\Programs\Python\Python313\Scripts\streamlit.exe" run app.py
}

Write-Host ""
Write-Host "Presiona cualquier tecla para cerrar..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
