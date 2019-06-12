def emoji_to_text(emoji):
    lookup = {'👊': 'rock', '✋': 'paper', '✌️': 'scissors'}
    return lookup.get(emoji)

def evaluate(player, computer):
    outcomes = {
        ('rock', 'scissors'): 'win',
        ('rock', 'paper'): 'lose',
        ('paper', 'rock'): 'win',
        ('paper', 'scissors'): 'lose',
        ('scissors', 'rock'): 'lose',
        ('scissors', 'paper'): 'win'
    }
    if player == computer:
        return 'tie'
    return outcomes[player, computer]
