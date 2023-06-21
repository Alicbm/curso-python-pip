import random


def all_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('Piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('This option not is available')
    return None, None

  computer_option = random.choice(options)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Ganaste!!!')
      user_wins += 1
    else:
      print('Perdiste...')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'piedra':
      print('Perdiste...')
      computer_wins += 1
    else:
      print('Ganaste!!!')
      user_wins += 1
  elif user_option == 'papel':
    if computer_option == 'tijera':
      print('Perdiste...')
      computer_wins += 1
    else:
      print('Ganaste!!!')
      user_wins += 1
  return user_wins, computer_wins


def check_winner(user_wins, computer_wins):
  if user_wins == 2:
    print('You are the real Winner')
    return user_wins, computer_wins

  if computer_wins == 2:
    print('The computer is the real Winner')

  return user_wins, computer_wins


def run_game():
  round = 1
  user_wins = 0
  computer_wins = 0

  while True:

    print('*' * 20)
    print('ROUND ', round)
    print('*' * 20)

    print('User => ', user_wins)
    print('Computer => ', computer_wins)
    round += 1

    user_option, computer_option = all_options()
    user_wins, computer_wins = check_rules(user_option, computer_option,
                                           user_wins, computer_wins)

    if user_wins >= 2 or computer_wins >= 2:
      user_wins, computer_wins = check_winner(user_wins, computer_wins)
      break


run_game()
