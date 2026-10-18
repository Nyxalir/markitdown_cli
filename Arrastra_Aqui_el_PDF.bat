@echo off
:: Cambiar el directorio de trabajo a la ubicación del script
cd /d "%~dp0"

:: Verificar si se arrastró un archivo
if "%~1"=="" (
    echo Error: No has arrastrado ningun archivo.
    echo Arrastra un archivo PDF o compatible sobre este icono.
    pause
    exit /b
)

:: Ejecutar el script usando el Python del entorno virtual
call .\venv\Scripts\python.exe conversor.py "%~1"

echo.
echo Proceso finalizado. Presiona cualquier tecla para cerrar.
pause