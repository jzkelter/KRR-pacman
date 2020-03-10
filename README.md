# KRR-pacman
Class project for KRR, using Companions to control Pac-man implemented in NetLogo.
Maryam Hedayati, Jacob Kelter, Nick LaGrassa


######Table of Contents#######
#1. High-level walkthrough
#2. Test companions-side implementation (without NetLogo and Pythonian)
#3. Run full implementation (companions, NetLogo, Pythonian)
#####End Table of Contents####



#1. High-level walkthrough
This system is comprised of three principle components:
- A PacMan (from here forward called PacPerson) game, implemented in NetLogo
- An intelligent agent implemented in Companions that takes as input state information about the PacPerson game board, reasons about the optimal next move for PacPerson, and returns either the direction(s) that PacPerson should move next. The direction options are None, Left, Right, Up, and Down. None is returned only when no such move will allow PacPerson to continue playing without losing the game.
- Pythonian - code that facilitates the communication between the NetLogo PacPerson game and the Companion agent.

Our Companions code houses the ontology we have created for the PacPerson game. This includes entities such as ghosts, walls, and pellets (the dots that PacPerson eats) and other predicates like blocked (which indicates that the direction for a tile adjacent to PacPerson is invalid because either a wall or a ghost is located on that tile). For a more detailed list of the elements of our ontology, please refer to the section labeled "Ontology" in the file rules.krf (instructions below on how to access).

Our companions code also contains the rules that govern the appropriate behavior of PacPerson given the state of the game board at each 'tick', or decision-making moment. NetLogo sends facts such as the directional location of any adjacent walls, ghosts, or nearest pellets, as well as the directions of nearby ghosts. Our rules take these facts and reason about which direction(s) are most ideal to travel. As will be evident in the code, these rules are numbered and structured in a hierarchy, where lower-number rules (example: Rule 1) are prioritized over higher-number rules (example: Rule 4). Higher-number rules are only used for reasoning about the direction to travel in if the lower-level rules fail to generate a viable direction for PacPerson to move.


#2. Test Companions-side implementation

Note: For setup, we assume that the reader is familiar with the Companions software and has it installed on their machines already.


#2.1. First, access our Companions code in our GitHub
- #steps to get our code go here#


#2.2. To test our Companions code for the first time, follow Steps 1-13 below:

1. Start up Companions
2. Right click 'session-reasoner'
3. Click 'Load Flatfile'
4. Load 'rules.krf'
5. Right click 'session-reasoner'
6. Click 'Load Flatfile'
7. Load a test file of your choice
(Tests are found in the top-level folder "KRR-pacman" and are organized by the number of entities that the tests consider. For example, the file 'test1_allBlocked.krf' in the sub-folder "Tests_oneEntity" contains the facts needed to test our code's response to the case where all four directions surrounding PacPerson are blocked.)
8. Right click 'session-reasoner'
9. Click 'Browse Agent'
10. Click 'Query' tab
11. Type '(directionToFace ?dir)' into query window.
12. Change context to 'PacPersonMt'
13. Click 'Query using fire:query'

***Note on EXPECTED OUTPUTS: ***
Each test file contains a comment on Line 4 that begins "Expected output:" followed by some subset of directions from the set {None, Up, Down, Left, Right}. The result of your query from Step 13 should match the directions listed on Line 4 of your chosen test file.


#2.3. To test our Companions code on a different test file, follow Steps 14-18 below:

14. Navigate to Session Manager (original Companions tab in your browser)
15. Click 'Commands' tab
16. In send>>, enter (doForgetKBMt PacPersonFactsMt)
17. In send>>, enter (doClearWorkingMemory)
18. Steps 5-13 above.



#3. Run full implementation (companions, NetLogo, Pythonian)

#3.1. Setup

#3.1.1. Install Pythonian
- This project used the zipped version of Pythonian supplied in class.  

#3.1.2. Install NetLogo
- Download for free from https://ccl.northwestern.edu/netlogo/download.shtml


#3.1.3. Load NetLogo PacPerson model code
Simply add the pac_agent.py file to the pythonian directory as well as KRR-Pac-Man.nlogo
and pacmap1.csv to the same directory (and the other pacmap*.csv files if you want other levels).
Simply opening KRR-Pac-Man.nlogo from that folder should run everything.


#3.2. Run
Once KRR-Pac-Man.nlogo is open and Companions is running, click the "New" button and then "Play."
Due to a Pythonian issue, sometimes on the first time step nothing is returned from Companions
and NetLogo throws an error. Just dismiss this and click play again and it should work. However,
also due to a Pythonian issue, when running in real time either updating the world-facts in Companions
or quering the next direction to face doesn't work. This makes "Play" behavior buggy. Moving one move
at a time with the "play once" button seems to work better. However, this may also have Pythonian issues. We then will click the "send-companion-world-state" and "ask-companion-direction-to-face" buttons until the correct options are being returned and then press "play-once" again. 

#3.3. Expected output
You should expect to see PacPerson travers the game board in NetLogo. PacPerson should be making directional choices based on the state of the world around them. These choices are laid out in greater detail in our companions code, but the high-level order of priority for choosing a direction follows this general progression:
1. Choose the direction that is
	(a) unblocked (no immediate ghost or wall),
	(b) contains the nearest pellet, and
	(c) not the direction of the nearest ghost
2. Choose the direction that is
	(a) unblocked and
	(b) the same as PacPerson is currently facing
3. Choose the direction that is
	(a) unblocked and
	(b) contains the nearest pellet
4. Choose the direction that is
	(a) unblocked and
	(b) not the direction of the nearest ghost
5. Choose the direction that is
	(a) unblocked
Reminder, each rule contains a condition that the previous rules produce an uninferred sentence.
