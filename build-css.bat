@echo off
cd /d "%~dp0"
echo Memproses Tailwind CSS...
npx tailwindcss -i input.css -o ventimax-style.min.css --minify
echo Selesai! File ventimax-style.min.css berhasil diperbarui.
pause
