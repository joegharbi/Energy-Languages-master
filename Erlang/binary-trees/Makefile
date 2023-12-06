compile:
	copy binarytrees.hipe-2.hipe binarytrees.erl
	erlc binarytrees.erl
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f binarytrees-main-21.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run  binarytrees main 21
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	erl -smp enable -noshell -run  binarytrees main 21
clean:
	del /Q *.json *.beam *.erl *.dump

