compile:
	gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -funroll-loops -fopenmp revcomp.gcc-6.c -o revcomp.gcc-6.exe 
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f nbody-50000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	revcomp.gcc-6.exe 0 < ../../revcomp-input25000000.txt
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	revcomp.gcc-6.exe 0 < ../../revcomp-input25000000.txt
clean:
	del /Q *.json *.exe

