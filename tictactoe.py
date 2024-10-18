X = 'X'
O = 'O'
EMPTY = None


def initial_state():
  """
  Returns starting state of the board.
  """
  return [[EMPTY for _ in range(3)] for _ in range(3)]


def player(board):
  """
  Returns player who has the next turn on a board.
  """
  # Conta o número de peças X e O para determinar o próximo jogador
  x_count = sum(row.count(X) for row in board)
  o_count = sum(row.count(O) for row in board)
  return X if x_count == o_count else O


def actions(board):
    # Gera uma lista de todas as posições vazias como tuplas
    return [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == EMPTY]




def result(board, action):
    # Desempacota a ação em linha e coluna
    i, j = action  

    # Verifica se a posição está vazia
    if board[i][j] != EMPTY:
        raise ValueError("Essa posição já está ocupada.")

    # Cria uma cópia do tabuleiro atual
    new_board = [row[:] for row in board]

    # Define a jogada do jogador atual
    new_board[i][j] = player(board)

    return new_board


def winner(board):
  """
  Returns the winner of the game, if there is one.
  """
  # Check rows
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
      return board[i][0]
  # Check columns
  for j in range(3):
    if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
      return board[0][j]
  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
    return board[0][2]
  # No winner yet
  return None


def terminal(board):
  """
  Returns True if game is over, False otherwise.
  """
  return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
  """
  Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
  """
  if winner(board) == X:
    return -1  # X perdeu
  elif winner(board) == O:
    return 1   # O ganhou
  else:
    return 0   # Empate


def minimax(board, depth=0, maximizing_player=True):
    if terminal(board):
        return utility(board), None  # Retorna valor e nenhuma ação se for terminal

    if player(board) == O:
        best_value = float('-inf')
        best_move = None
        for action in actions(board):
            value, _ = minimax(result(board, action), depth + 1, False)
            if value > best_value:
                best_value = value
                best_move = action
        return best_value, best_move  # Retorna melhor valor e melhor ação
    else:
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            value, _ = minimax(result(board, action), depth + 1, True)
            if value < best_value:
                best_value = value
                best_move = action
        return best_value, best_move  # Retorna melhor valor e melhor ação
