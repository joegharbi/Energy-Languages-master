compile:
	copy spectralnorm.hipe-2.hipe spectralnorm.erl
	erlc spectralnorm.erl
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f spectralnorm-main-5500.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run  spectralnorm main 5500
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe

run:
	erl -smp enable -noshell -run  spectralnorm main 5500
clean:
	del /Q *.json *.beam *.erl *.dump
