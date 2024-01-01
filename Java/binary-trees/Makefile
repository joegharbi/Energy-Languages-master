compile:
	copy binarytrees.java-7.java binarytrees.java
	javac -d .  binarytrees.java
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f fasta-25000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	java binarytrees 21
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	java binarytrees 21

clean:
	del /Q *.json *.class