compile:
	gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -mfpmath=sse -msse3 nbody.gcc-4.c -o a.exe -lm
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f nbody-50000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	./a.exe 50000000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	./a.exe 50000000
clean:
	del /Q *.json *.exe

