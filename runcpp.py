# Script that compiles and executes a .cpp file
# Usage:
# python runcpp.py -i <filename> (without .cpp extension)

import getopt, subprocess, sys

def main(argv):
    cpp_file = ''
    exe_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:",["help",'ifile=']) # This parses the arguments into lists
    except getopt.GetoptError as err:
        # print help information and exit
        print(err)      
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--ifile"):
            cpp_file = a + '.cpp'
            exe_file = a + '.exe'
            run(cpp_file, exe_file)
            

def usage():
    print('runcpp.py -i <filename> (without .cpp extension)')

def run(cpp_file, exe_file):
    x = subprocess.run('g++ ' + cpp_file + ' -o ' + exe_file + ' -Werror -Wall') # Compile & treat warnings as errors and list all warnings 
    if x.returncode == 0:                                                        # If compiled without errors
        subprocess.run(exe_file)                        
    

if __name__=='__main__':
    main(sys.argv[1:])


