# ChessMaster Bot

ChessMaster Bot is a simple yet powerful chess bot that plays against a human opponent using the Stockfish chess engine. It allows users to play chess in the command line while receiving moves calculated by the AI.

## Features
- Play against Stockfish, a world-class chess engine.
- Simple command-line interface.
- Supports UCI move format (e.g., `e2e4`).
- Detects game over conditions (checkmate, stalemate, etc.).

## Installation

1. Install Python (if not already installed). 
2. Install the required Python package: 
   ```sh   
   pip install chess      
   ```
3. Download and install [Stockfish](https://stockfishchess.org/download/).
4. Ensure Stockfish is accessible from your system's PATH.

## Usage   

Run the bot with: 
```sh
python chessmaster_bot.py 
```

Enter your moves in UCI format (e.g., `e2e4`) and let the bot respond.

## Example Gameplay
```
Welcome to ChessMaster Bot! Enter moves in UCI format (e.g., e2e4). Type 'quit' to exit.
  a b c d e f g h
8 r n b q k b n r 8
7 p p p p p p p p 7
6 . . . . . . . . 6
5 . . . . . . . . 5
4 . . . . . . . . 4
3 . . . . . . . . 3
2 P P P P P P P P 2
1 R N B Q K B N R 1
  a b c d e f g h
Your move: e2e4
Bot is thinking...
```

## License
This project is open-source and available under the MIT License.

## Contributing
Pull requests and improvements are welcome! Feel free to enhance the bot or add features.

