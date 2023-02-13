def kittyHat(howManyCats: int, rounds: int):
    cats = []
    cat_counter = 1
    while cat_counter <= howManyCats + 1:
        cats.append(0)
        cat_counter += 1

    cat_counter = 1
    while cat_counter < rounds + 1:
        for index, cat in enumerate(cats):
            if index % cat_counter == 0:
                if cat == 0:
                    cats[index] += 1
                else:
                    cats[index] = 0
# print(f'Cats after round {cat_counter}', cats)
        cat_counter += 1

    del cats[0]

    for index, cat in enumerate(cats):
        if cat == 0:
            cats[index] = 'no hat'
        else:
            cats[index] = 'a hat'
        cat_counter = index + 1
        print(f'Cat {cat_counter} has {cats[index]}')


kittyHat(100, 100)
