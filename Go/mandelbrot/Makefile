compile:
	go build mandelbrot.go-3.go
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f mandelbrot-3.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	mandelbrot.go-3.exe 16000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	mandelbrot.go-3.exe 16000
clean:
	del /Q *.json *.exe