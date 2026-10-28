from random import shuffle
cpu_side = 1
counter = 0


def evaluate(game, basic_value, king_value): # Returns integer evaluate
    evaluation = 0
    king_counts = [0,0]
    if game.check_win_condition() is not None:
        if game.check_win_condition() == cpu_side:
            return 100
        else:
            return -100

    for piece_details in game.find_all_piece_details():
        if piece_details[0] == cpu_side:
            if piece_details[1]:
                evaluation += king_value
                king_counts[0] += 1
            else:
                evaluation += basic_value
        else:
            if piece_details[1]:
                evaluation -= king_value*1
                king_counts[1] += 1
            else:
                evaluation -= basic_value
    total_kings = king_counts[0] + king_counts[1]
    if total_kings != 0:
        evaluation += (king_counts[0] / total_kings) * 0.5

    return evaluation



def find_move(game, depth, maximizing, alpha = -102, beta = +102, previous_best = None, basic_value = 1, king_value = 2): # Returns integer evaluate
    if depth == 0 or game.check_win_condition() is not None:
        return evaluate(game, basic_value, king_value), None

    moves = game.generate_moves()
    if len(moves) == 1:
        return evaluate(game, basic_value, king_value), moves[0]

    shuffle(moves)
    best_move = None
    if previous_best is not None and previous_best[1] in moves:
        moves.remove(previous_best[1])
        moves.insert(0, previous_best[1])

    if maximizing:
        best = -101
        for move in moves:
            new_game = game.copy()
            new_game.handle_move(move[1], move[2])
            if cpu_side == new_game.current_player:
                score = find_move(new_game, depth, True, alpha, beta)[0]
            else:
                score = find_move(new_game, depth - 1, False, alpha, beta)[0]
            if score > best:
                best = score
                best_move = move

            alpha = max(alpha, best)
            if alpha >= beta:
                break

        return best, best_move

    else:
        best = 101
        for move in moves:
            new_game = game.copy()
            new_game.handle_move(move[1], move[2])
            if cpu_side != new_game.current_player:
                score = find_move(new_game, depth, False, alpha, beta)[0]
            else:
                score = find_move(new_game, depth - 1, True, alpha, beta)[0]
            if score < best:
                best = score
                best_move = move

            beta = min(beta, best)
            if beta <= alpha:
                break
        return best, best_move


