import random

capitals = {
    'Ukraine': 'Kyiv',
    'France': 'Paris',
    'Italy': 'Rome',
    'Germany': 'Berlin',
    'Ireland': 'Dublin',
    'Spain': 'Madrid'
        }


def guess_capital():
    countries = list(capitals.keys())
    random.shuffle(countries)

    score = 0
    lives = 3

    for country in countries:
        print(f'What\'s the capital of {country}?')
        while True:
            answer_capital = input().strip().capitalize()

            if answer_capital.lower() == 'exit':
                print(f'Thank you for playing!\nYour score is {score}')
                return

            if answer_capital == capitals[country]:
                score += 1
                print(f'You are correct! Great job! \nYour score is {score}')
                break

            else:
                lives -= 1
                if lives == 0:
                    print(f'You have no more lives!Game over! \nYour score is {score}')
                    return
                elif lives == 2:
                    hint = capitals[country][0]
                    print(f'Wrong! Capital is starting with {hint}. You have {lives} lives left')
                elif lives == 1:
                    hint = capitals[country][0]+capitals[country][1]
                    print(f'Wrong! Capital is starting with {hint}. You have {lives} lives left')


# guess_capital()


def convert_roman(rome_num: str):

    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    digit = 0

    while digit < len(rome_num):
        if digit+1 < len(rome_num):
            if numerals[rome_num[digit]] < numerals[rome_num[digit+1]] and rome_num[digit] not in ['L','D']:
                result += numerals[rome_num[digit+1]] - numerals[rome_num[digit]]
                digit += 2
            else:
                result += numerals[rome_num[digit]]
                digit += 1
        else:
            result += numerals[rome_num[digit]]
            digit += 1
    return result


print(convert_roman('MCMXCIV'))
