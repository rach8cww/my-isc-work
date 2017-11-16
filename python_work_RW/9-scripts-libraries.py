print
print "Scripts and Libraries Exercise"
print

# part 1

import dancing.dance
from dancing. dance import boogie
import sys

"""
made a new directory (mkdir) inside python_work_RW called "dancing" and within
that made a directory called __init__.py.
Then can import dancing
"""

# part 2 - checking what the boogie function does (aka reading the code in file)
"""
with open ('dance.py', 'r') as shoes:
	data = shoes.read()
	print data
"""

# part 3

moves = sys.argv[1:]
# make some new dance moves:
dancing_queen = ["twirl", "jump", "sway", "cartwheel", "backflip"]
boogie(dancing_queen) # calls out the function


print
