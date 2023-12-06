compile:
	copy knucleotide.hipe-3.hipe knucleotide.erl
	erlc knucleotide.erl
measure:
	cmd /C start /B cmd /C "cmd /C start /B scaphandre json -n 100000 -f knucleotide-main-0.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run  knucleotide main 0 < ../../knucleotide-input25000000.txt
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	erl -smp enable -noshell -run  knucleotide main 0 < ../../knucleotide-input25000000.txt
clean:
	del /Q *.json *.beam *.erl *.dump