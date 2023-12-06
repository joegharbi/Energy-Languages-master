compile:
	copy pidigits.hipe pidigits.erl
	erlc pidigits.erl
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f pidigits-main-10000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run  pidigits main 10000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	erl -smp enable -noshell -run  pidigits main 10000
clean:
	del /Q *.json *.beam *.erl *.dump