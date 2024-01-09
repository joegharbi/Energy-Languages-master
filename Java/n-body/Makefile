compile:
	copy nbody.java-4.java nbody.java
	javac -d .  nbody.java
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f nbody.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	java nbody 50000000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	java   nbody 50000000
clean:
	del /Q *.json *.class