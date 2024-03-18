import random 

def play():
    user = input('Enter your choice - r or p or s ')
    bot = random.choice(['r','p', 's'])

    if user == bot:
        return 'Tie'
    
    if is_win(user, bot):
        return 'U won'
    
    return 'U lost'

def is_win(player, opponent):
    if (player =='r' and opponent == 's') or (player =='s' and opponent == 'p') or (player =='p' and opponent == 'r'):
        return  True
    
print(play())