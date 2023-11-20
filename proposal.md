---

## Final Project Proposal

**Team**: Muhammad Farooq Memon, Ansh Singhal, Atharv Tekurkar, Zuhair AlMassri  
**Team Name**: Bhupendra JogAI

---

### Ultimate Tic Tac Toe

**Project Description:**  
We aim to develop a Python interface for the game Ultimate Tic Tac Toe, akin to the Konane game, and test various heuristics for an adversarial search. The interface will offer multiple difficulty modes for an AI opponent by adjusting the depth of the search algorithm. Our end goal is to create a playable interface with varying AI difficulty levels.

**What is Ultimate Tic Tac Toe:**  
Ultimate Tic Tac Toe features nine boards arranged in a 3x3 grid, where players engage in Tic Tac Toe on each smaller board. The game begins in the centermost board, with X making the first move. The next valid board for O depends on X's move within the current mini-board. Once a board is won, subsequent moves on that board don't affect the game. If a player is directed to a full board, they can choose any spot on the larger board to continue.

**Exact Rules:**

- Initial play starts on the centermost board with X going first.
- The next board available for play depends on the position of the last move.
- Players continue on the decided board unless it's already decided or full.
- If directed to a full board, the player can choose any spot on the larger board.

**Progress So Far:**

- Obtained an intuitive understanding by playing amongst the team.
- Conducted research on the game's NP-completeness and discussed potential runtime and branching factor.
- Discussed implementation strategies for board states, favoring a nested matrix structure.

---
