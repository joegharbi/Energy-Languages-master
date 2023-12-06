compile:
	go build nbody.go
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f nbody-50000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	nbody.exe 50000000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	nbody.exe 50000000
clean:
	del /Q *.json *.exe