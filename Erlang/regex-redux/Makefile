compile:
	copy regexredux.hipe-6.hipe regexredux.erl
	erlc regexredux.erl
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f regexredux-main-0.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run -noinput -run regexredux main 0 < ../../regexredux-input50000.txt
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	erl -smp enable -noshell -run -noinput -run regexredux main 0 < ../../regexredux-input50000.txt
clean:
	del /Q *.json *.beam *.erl *.dump