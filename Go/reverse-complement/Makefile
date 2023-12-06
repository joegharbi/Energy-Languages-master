compile:
	go build revcomp.go-6.go
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f regexredux-5000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	revcomp.go-6.exe 0 < ../../revcomp-input25000000.txt
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	revcomp.go-6.exe 0 < ../../revcomp-input25000000.txt
clean:
	del /Q *.json *.exe