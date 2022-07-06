"""
Implementation of rock, paper, scissors by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random

def play():
  user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
  computer = random.choice(['r', 'p', 's'])

  if is_win(user, computer):
    return 'You won!'
  if is_win(computer, user):
    return "You lost!"
  else:
    print("It's a tie!")
    return(play())
    
def is_win(player, opponent):
  #return true if player wins
  
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
      return True

print(play())
