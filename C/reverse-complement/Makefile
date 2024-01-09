compile:
	gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -funroll-loops -fopenmp revcomp.gcc-6.c -o a.exe 
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f revcomp.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	a.exe 0 < ../../revcomp-input25000000.txt
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	a.exe 0 < ../../revcomp-input25000000.txt
clean:
	del /Q *.json *.exe

