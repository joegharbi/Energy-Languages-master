compile:
	copy mandelbrot.java-2.java mandelbrot.java
	javac -d . mandelbrot.java
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f mandelbrot.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	java   mandelbrot 16000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	java   mandelbrot 16000
clean:
	del /Q *.json *.class