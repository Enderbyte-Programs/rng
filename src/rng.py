#!/usr/bin/python3
VERSION="0.1"
import sys
import random
DOCUMENTATION = """
DOCUMENTATION

Unless -r is specified, 0 is good and -1 is bad

--help          Show help menu
--version       Show version info

-c              Coin-Flip: Returns heads or tails or 0 (heads)/1(tails) if -r is specified
-i int,int      Generate a random number between the two provided ints. There must NOT be a space between them, only a comma.
-z              Generate a classic C-style random number between 0 and 2^32
-y              Generate a classic C-style random float between 0 and 1

-h              Print out in a human-readable format
-r              Result, if numerical will be given as an exit code.
"""

args = sys.argv[1:]
if len(args) == 0:
    print("Please provided some command line arguments or run with --help for more options")
    sys.exit(-1)

if "--help" in args:
    print(DOCUMENTATION)
    sys.exit()

elif "--version" in args:
    print(f"Command Line RNG v{VERSION}")
    sys.exit()


HUMANREADABLE = "-h" in args
NUMERARETURN = "-r" in args

if HUMANREADABLE and NUMERARETURN:
    print("Error! -h and -r are conflicting arguments")
    sys.exit(-1)

#Check for conflicting args
command_args = ["-c","-i","-z","-y"]
if len([ss for ss in args if ss in command_args]) > 1:
    print("Error! Please provide only one command.")
    sys.exit(-1)

if "-c" in args:
    retr = random.randint(0,1) == 1
    if NUMERARETURN:
        sys.exit(int(retr))
    else:
        if HUMANREADABLE:
            print(f"The Result Is: {['Tails' if retr else 'Heads'][0]}")
        else:
            if retr:
                print("tails")
            else:
                print("heads")
    sys.exit()

elif "-i" in args:
    try:
        ix = args[args.index("-i")+1]
        i0 = int(ix.split(",")[0])
        i1 = int(ix.split(",")[1])
    except:
        print("Error! There was an error in the provided input")
        sys.exit(-1)
    else:
        rn = random.randint(i0,i1)
        if NUMERARETURN:
            sys.exit(rn)
        if HUMANREADABLE:
            print("The generated number is",rn)
            sys.exit()
        else:
            print(rn)
            sys.exit()
elif "-z" in args:
    rn = int(random.random()*(2**32))
    if NUMERARETURN:
        sys.exit(rn)
    if HUMANREADABLE:
        print("The generated number is",rn)
        sys.exit()
    else:
        print(rn)
        sys.exit()

elif "-y" in args:
    rn = random.random()
    if NUMERARETURN:
        sys.exit(rn)
    if HUMANREADABLE:
        print(f"The generated number is {rn:.20f}")
        sys.exit()
    else:
        print(f"{rn:.20f}")
        sys.exit()