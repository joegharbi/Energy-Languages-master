compile:
	go build knucleotide.go-6.go
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f knucleotide-6.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	knucleotide.go-6.exe 0 < ../../knucleotide-input25000000.txt	timeout /T 5 /NOBREAK > NUL
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	knucleotide.go-6.exe 0 < ../../knucleotide-input25000000.txt
clean:
	del /Q *.json *.exe