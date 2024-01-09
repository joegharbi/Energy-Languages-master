compile:
	gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -std=c99 -mfpmath=sse -msse3 -fopenmp fasta.gcc-2.c -o a.exe 
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f fasta-25000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	./a.exe 25000000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	./a.exe 25000000
clean:
	del /Q *.json *.exe
