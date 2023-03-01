# APTGen
A simple .exe GUI tool to create random Aptamer DNA sequences of specified length and GC content (Windows executable available)

I made this as a quick side project to help anyone who wants a head start on making a random library of aptamers.
Please feel free to use my code and improve it any way you like.

To create an executable file from this code, you can use a tool like PyInstaller. Here are the steps to do it:

1) Install PyInstaller: pip install pyinstaller < type this in cmd (im assuming you have a version on python installed, if not get the latest one)
2) Download the APTGen.py file to a directory
3) Open a command prompt or terminal window and navigate to the directory containing APTGen.py
4) Run the following command to create the executable file:
pyinstaller --onefile random_seq_gui.py
5) PyInstaller will create a new directory called dist, which will contain the executable file. TaDaaaa you created an executable program.
Note: that the executable file will not include the Python interpreter, so it can be run on a computer without Python installed. However, the file may be flagged as potentially harmful by some antivirus software, since it is an executable file generated from Python code.
6) Tinker with my code and add anything you like to it.

viva la Science
