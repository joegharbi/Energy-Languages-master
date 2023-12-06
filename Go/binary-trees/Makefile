compile:
	go build binarytrees.go-2.go
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f binarytrees-21.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	./binarytrees.go-2.exe 21
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	./binarytrees.go-2.exe 21
clean:
	del /Q *.json *.exe
