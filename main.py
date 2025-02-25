import chess
import chess.engine

def main():
    board = chess.Board()
    engine_path = "stockfish"  # Убедись, что Stockfish установлен и доступен в PATH
    
    try:
        engine = chess.engine.SimpleEngine.popen_uci(engine_path)
    except FileNotFoundError:
        print("Stockfish not found. Make sure it's installed and accessible.")
        return

    print("Welcome to ChessMaster Bot! Enter moves in UCI format (e.g., e2e4). Type 'quit' to exit.")
    
    while not board.is_game_over():
        print(board)
        user_move = input("Your move: ")
        
        if user_move.lower() == "quit":
            break

        if chess.Move.from_uci(user_move) in board.legal_moves:
            board.push_uci(user_move)
        else:
            print("Invalid move. Try again.")
            continue

        if board.is_game_over():
            break

        print("Bot is thinking...")
        result = engine.play(board, chess.engine.Limit(time=1.0))
        board.push(result.move)

    print("Game over!")
    print("Result:", board.result())
    engine.quit()

if __name__ == "__main__":
    main()
