# Checkers

A checkers (draughts) game written in Python with Pygame. Play against a friend on the same computer, play against a minimax-based CPU, or watch two CPUs play each other.

## Features

- 8x8 board with a graphical Pygame interface
- Mandatory captures and multi-jump chains
- Kings, shown with a gold dot
- **CPU opponent** using minimax with alpha-beta pruning and iterative deepening
- CPU vs CPU mode for testing and tuning the evaluation
- Game logic, UI and AI are separate modules, so the rules can be tested without Pygame

## Requirements

- Python 3.10 or newer
- [Pygame](https://www.pygame.org/)

## Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install -r requirements.txt
```

## Running the game

```bash
python main.py                    # two players, same computer
python main.py --mode single      # you (red) vs the CPU (blue)
python main.py --mode cpu-battle  # CPU vs CPU
```

## How to play

- Red (Player 1) moves first and players alternate turns.
- Click a piece to select it, then click its destination. Click the selected piece again to deselect.
- If a capture is available you must take it, and a piece that can keep jumping must.
- Reaching the far row promotes a piece to a king.
- You win when your opponent has no pieces or no legal moves.

## How the AI works

The CPU in `ai/minmax.py` searches the game tree with minimax and alpha-beta pruning.

- **Iterative deepening:** it searches depth 1, 2, 3, ... until it reaches the maximum depth (12) or the time limit (8 seconds per move). The best move from each pass is searched first in the next, which improves pruning.
- **Evaluation:** a position's score is the CPU's material minus the opponent's, with kings worth more than regular pieces (default 2 vs 1) and a small bonus for having a larger share of the kings. A win or loss scores +/-100.
- **Multi-jumps:** when a move leaves the same player to move again, the search stays at the same depth rather than consuming a ply.

In CPU vs CPU mode the two sides use different search depths and king values, which makes it easy to compare settings.

## Project structure

| Path | Purpose |
|------|---------|
| `main.py` | Entry point and mode selection |
| `game.py` | Rules: turns, move generation, multi-jumps, win detection |
| `board.py` | Board state, piece movement, capture removal |
| `piece.py` | Piece behaviour: valid moves and promotion |
| `ui.py` | Pygame rendering, mouse input, game loops for each mode |
| `ai/minmax.py` | Minimax search and position evaluation |
| `constants.py` | Shared constants (players, board and window sizes) |

## Configuration

- Board and window sizes: `constants.py`
- AI search limits: `single_player_run()` in `ui.py` (`max_depth`, time limit)
- Evaluation weights: `basic_value` and `king_value` in `ai/minmax.py`
