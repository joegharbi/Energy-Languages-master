compile:
	copy revcomp.java-3.java revcomp.java
	javac -d .  revcomp.java
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f nbody.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	java   revcomp 0 < ../../revcomp-input25000000.txt
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	java   revcomp 0 < ../../revcomp-input25000000.txt
clean:
	del /Q *.json *.class