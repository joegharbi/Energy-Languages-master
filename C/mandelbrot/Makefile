compile:
	gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -mno-fma -fno-finite-math-only -mfpmath=sse -msse2 -fopenmp mandelbrot.gcc-6.c -o a.exe 
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f mandelbrot-16000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	./a.exe 16000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	./a.exe 16000
clean:
	del /Q *.json *.exe

