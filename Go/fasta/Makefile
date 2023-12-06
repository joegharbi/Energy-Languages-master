compile:
	go build fasta.go-3.go
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f fasta-25000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	./fasta.go-3.exe 25000000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	./fasta.go-3.exe 25000000
clean:
	del /Q *.json *.exe