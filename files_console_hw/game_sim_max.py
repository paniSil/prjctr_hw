import csv

with open('game_score.csv', mode = 'r') as file:
    reader = csv.reader(file)
    next(reader)
    scores = {}
       
    for row in reader:
        name, score = row
        
        if name not in scores:
            scores[name] = score
        else:
            scores[name] = max(int(scores[name]), int(score))

max_scores = sorted(scores.items(), key = lambda item: item[1], reverse = True)

with open('high_scores.csv', mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['Player', 'Highest score'])
    
    for name, score in max_scores:
        writer.writerow([name, score])

