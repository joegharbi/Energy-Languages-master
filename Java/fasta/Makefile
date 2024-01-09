compile:
	copy fasta.java-5.java fasta.java
	javac -d .  fasta.java
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f fannkuchredux-12.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	java   fasta 25000000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	java   fasta 25000000
clean:
	del /Q *.json *.class

