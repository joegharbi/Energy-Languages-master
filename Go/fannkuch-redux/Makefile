compile:
	go build -o a.exe fannkuchredux.go
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f fannkuchredux-12.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	a.exe 12
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	a.exe 12
clean:
	del /Q *.json *.exe