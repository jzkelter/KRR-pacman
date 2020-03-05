# KRR-pacman
Class project for KRR, using Companions to control Pac-man implemented in NetLogo

To test code (first time, or if changes made to board):
1. <Start up companions>
2. Right click 'session-reasoner'
3. Click 'Load Flatfile'
4. Load 'board.krf'
5. Right click 'session-reasoner'
6. Click 'Load Flatfile'
7. Load 'facts.krf'
8. Right click 'session-reasoner'
9. Click 'Browse Agent'
10. Click 'Query' tab
11. Type '(directionToFace ?dir)' into query window.
12. Change context to 'PacPersonMt'
13. Click 'Query using fire:query'

To continue testing (where only facts are changed):
Navigate to Session Manager (original Companions tab in your browser)
14. Click 'Commands' tab
15. In send>>, enter (doForgetKBMt PacPersonFactsMt)
16. In send>>, enter (doClearWorkingMemory)
17. Steps 5-13 above.
