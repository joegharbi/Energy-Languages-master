compile:
	javac -d .  fannkuchredux.java
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f fannkuchredux-12.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	java   fannkuchredux 12
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	java   fannkuchredux 12
clean:
	del /Q *.json *.class