This project came out of an attempt to spoil a friend's habit of playing a certain unnamed game ("f2"). It is a single-player paper-and-pencil game where you have to cross out numbers that are either equal or sum up to ten. (see RULES.txt) This project serves as (1) an interface to play the game and (2) an attempt to find solutions to it.
The files are roughly one year old by now, so this documentation may be sketchy or inaccurate.




########################## THE GAME (F2.PY) ##########################

The f2.py file is the main program for playing the game yourself. You have the following input options:
> 'x y dir'
>>> select a point with the coordinates (x, y) and a neighbour to cross out (see RULES.txt)
>>> dir can either be ['u', 'l', 'd', 'r'] for each cardinal direction respectively
> 'c'
>>> copies field (see RULES.txt)
> 'exit'
>>> exits program
You should try playing it yourself first before reading on. An example of starting moves would be "0 0 d" then "1 2 u" then "8 0 r" then "7 0 r" then "c" since you are out of moves.






############### SOLVING THE GAME (FYEAH.PY; FYEAH2.PY) ###############

The fyeah and tree-related series of files were created in an attempt to find a solution (1) by looking for a solution through random moves [fyeah.py], which worked in the end and (2) by searching all possible moves in the tree [fyeah2.py].
In the end, the [fyeah.py] found a solution within its scope during its first run. This is remarkable since there are less than 100 trials per run. This hints at lots of possible winning paths.
Both programs can be accelerated by commenting out all of the print statements.


fyeah.py:

[fyeah.py] tries a random move and copies the field over with a probability of 1 in 10'000. It could be improved by adapting the probability to the size of the field (greater field -> smaller chance). It could also be improved by ignoring already crossed-out fields for the (x, y)-pick.
[fyeah.py] currently outputs to Solution1.txt. The solution that was found is in SOLUTION.txt.
Uses [f2_file_loader.py] (misnomer?) to get all possible moves,


fyeah2.py:

[fyeah2.py] builds a tree of possible moves depth-first and then checks whether the game has been won. It's looks mostly abandoned but the cause of a great deal of files in here:
[f1.py], [f2_tree_data.py], [f2_tree_handler.py], [f2_file_loader.py]
[this.txt], [to_load.txt], [treetesttt.txt], [treetesttttttttttt.txt]

There is also some unused code for queues: [mylist.py], [game_one.py]
And the individual squares: [mysquare.py]






############################## LICENSE ##############################

What? Licensing/Copyright? Yeah I'd be happy if you fork and improve upon this program! I don't really want to wade through licensing for this little thing, so just point to this paragraph/file if you have the need to.

