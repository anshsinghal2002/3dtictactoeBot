# Final Project Write-Up

## Bhupendra JogAI - Ultimate Tic Tac Toe AI

**Team:** Muhammad Farooq Memon, Ansh Singhal, Atharv Tekurkar, Zuhair AlMassri  
**Team Name:** Bhupendra JogAI

---

## Summary

The Bhupendra JogAI team embarked on a challenging journey to develop a Python interface for Ultimate Tic Tac Toe, implementing various heuristics for an adversarial search. This write-up documents our process, the heuristics explored, conclusions drawn, and future considerations.

---

## Project Overview

### Ultimate Tic Tac Toe

Ultimate Tic Tac Toe presents a unique twist on the classic game, featuring nine boards within a 3x3 grid. Players engage in Tic Tac Toe on each smaller board, and the game's complexity arises from the interplay between the moves on individual boards.

**Modified Rules:** The team strategically revised the game rules, requiring a player to win on any mini-board to win the game. This alteration significantly shortened the development and playing time while preserving the essence and strategic depth of the game.

The project aimed to create a Python interface for the modified game, offering different difficulty levels by adjusting the depth of the adversarial search algorithm.

---

## Implementation Details

### Data Structures and Interaction

Our implementation utilizes a nested matrix structure to represent the state of the game. Each element of the outer matrix corresponds to a mini-board, and the inner matrices represent the individual Tic Tac Toe boards. User interaction is facilitated through a Python interface that accepts moves and displays the game state.

### Heuristics Explored

#### Evolution of Heuristic Metrics

The heuristic evolution involved exploring various metrics, including:

- **Number of Central Tiles Filled:** Prioritizing moves occupying the center, akin to traditional Tic Tac Toe strategy.
- **Number of Possible Moves for Opponent/Player:** Evaluating strategic moves based on the available options for both players.
- **Number of Mini Boards Won:** Emphasizing control by tallying wins across mini-boards.
- **Number of Symbols on Central Mini Board:** Assessing control and influence on the central mini-board.

#### Iterative Improvement

The team implemented the basic game structure, integrated the initial heuristic, and conducted iterative improvements. We adjusted the depth of the search algorithm, exploring various heuristic possibilities, and collected data on AI performance across different difficulty levels.

### Development Process

The development process commenced with implementing a min-max adversarial search for a normal Tic Tac Toe game. This initial step laid the groundwork for adapting the algorithm to handle the complexities of Ultimate Tic Tac Toe.

---

## Evaluation and Conclusions

### Evaluation Metrics

To evaluate AI performance, we considered win rates, average game length, and user experience. The metrics provided a comprehensive view of the AI's effectiveness and the impact of different heuristics on gameplay.

### Iterative Improvement and Conclusions

Through an iterative process, the team tested and refined heuristics, adjusting hyperparameters to enhance AI decision-making. The corner control and edge occupancy heuristics showed promise in creating more strategic AI moves, while the blocking moves heuristic significantly improved defensive capabilities.

#### Conclusions Drawn

1. **Heuristic Impact:** Different heuristics significantly influenced AI behavior, with corner control and blocking moves proving to be particularly effective.

2. **User Experience:** AI difficulty levels provided engaging gameplay experiences for users of varying skill levels.

3. **Future Considerations:** Future work could explore more advanced AI techniques, incorporate machine learning approaches, and adapt the game for different platforms.

---

## Future Directions

### User Interface Enhancements

Improving the user interface, adding graphical elements, and enhancing visualization could elevate the overall gaming experience.

### Community Engagement

Sharing the project with the open-source community and encouraging contributions could lead to further enhancements and collaborative development.

---

## Acknowledgments

The Bhupendra JogAI team acknowledges the support and collaboration of Hassan Aamir, Alisa Motiwala, Saeed AlSuwaidi, Mohammed Kaid, Siddhant Deka, Ali Kazmi, Joseph Cirksey, Musa Jamil and Eyosyas Achamyeleh, and their enthusiastic participation in the development of the heuristic.

---
