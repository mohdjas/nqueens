DESCRIPTION
-----------

Python program implementing backtracking algorithm with pruning to produce solution and time for the N Queens Problem for N = 4 to 19.

USAGE AND OUTPUT
----------------

usage: python nqueens.py

Output includes the N value, the solution (see BOARD REPRESENTATION below), time taken and the number of boards traversed to arrive at the solution.

Example output: 
n:  15 	[0, 2, 4, 1, 9, 11, 13, 3, 12, 8, 5, 14, 6, 10, 7] []
t:  0:00:00.054228 	4003

Tested on Ubuntu x86 14.04 using Python 2.7.5. Not compatible with Python 3.

BOARD REPRESENTATION
--------------------

The Board is represented as a list of queen positions and possible positions of the remaining queens. The index of the list gives the row number and the value at the index gives the column of the Board.

Example: [1,3][0,2] represents queens at positions (0,1) and (1, 3). The second list represents the next possible queen locations, ie (2, 0), (2, 2), (3, 0) and (3, 2).


PREREQUISITES
-------------

None.


LICENSE
-------

See LICENSE.md for license information.
