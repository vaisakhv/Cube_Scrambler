import random
import argparse
import sys
import subprocess as shell

parser = argparse.ArgumentParser(description='Script options',prefix_chars='-+')
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument('-n','--min', type=str, dest='minRange',help='The min range of the random generator')
requiredNamed.add_argument('-x','--max', type=str, dest='maxRange',help='The max range of the random generator')
arguments = parser.parse_args() # Treat Arguments in your script

#makes sure that all the required parameters has been passed by the user
if arguments.maxRange == None or arguments.minRange == None:
    print("both the arguments -n/--minRange and -x/--maxRange are required")
    cmd = "python "+sys.argv[0]+" -h"
    shell.call(cmd, shell=True)
    sys.exit(2)

moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "F", "F'", "F2", "D", "D'", "D2", "B", "B'", "B2"]

minRange = int(arguments.minRange)
maxRange = int(arguments.maxRange)

nunberMoves = minRange + int(random.random()* (maxRange - minRange))
print("Number of randomly selected moves (between " + str(minRange) + " and " + str(maxRange) + ") : " + str(nunberMoves))

randMoves = []
while len(randMoves) < nunberMoves:
    move = moves[(int)(random.random() * len(moves))] 
    if len(randMoves) == 0 or move[0] != randMoves[-1][0] :
        randMoves.append(move)

print(" ".join([str(x) for x in randMoves]))