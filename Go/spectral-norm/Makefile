compile:
	go build spectralnorm.go-4.go
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f regexredux-5000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	spectralnorm.go-4.exe 5500
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	spectralnorm.go-4.exe 5500
clean:
	del /Q *.json *.exe
