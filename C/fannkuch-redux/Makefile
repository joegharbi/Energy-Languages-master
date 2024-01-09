compile:
	gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -std=c99 -fopenmp fannkuchredux.gcc-5.c -o a.exe 
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f fannkuchredux-12.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	./a.exe 12
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	./a.exe 12
clean:
	del /Q *.json *.exe
