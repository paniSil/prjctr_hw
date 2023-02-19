import random, csv

players = ['Bilbo', 'Frodo', 'Merry', 'Sam', 'Pippin']

with open('game_score.csv', mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['player', 'score'])
    
    for player in players:    
        for game in range(10):
            score = random.randint(0, 100)
            writer.writerow([player, score])
