compile:
	gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -std=c99 -fopenmp fannkuchredux.gcc-5.c -o fannkuchredux.gcc-5.exe 
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f fannkuchredux-12.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	./fannkuchredux.gcc-5.exe 12
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	./fannkuchredux.gcc-5.exe 12
clean:
	del /Q *.json *.exe
