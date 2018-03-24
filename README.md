# runcpp.py
A simple python script to compile a c++ source file and run the executable, all with one command.

Usage:
```
$ python runcpp.py --help
runcpp.py -i <filename> (without .cpp extension)
```

This statement on the command line will compile and run a file called hello.cpp in the same folder.
```
$ python runcpp.py -i hello
Hello, World!
```

I found that I wrote programs in python faster because how quickly I could switch to a terminal and run the script. With C++, I would have to compile, and then run the program and it was quite repetitive.

So I decided to make writing C++ a little bit more fun by reducing that two-step process down to one. If there are any compile errors, then they will be displayed on the terminal and the script will end. The executable will only run if the compiler has no complaints.

For the time being, the script runs only on windows machines and compilation treats all warnings as errors. 

I intend to add features to this script to be cross-platform, support header files and linking with other source files and being able to process g++ operations and arguments. 
Feel free to customize the code to your liking.
