from random import randint
# 
welcome_text = 'угадайте число от 1 до 100

number = randint(1, 100)

print(welcome_text))

def main():
    while True:
        guess = int(input('введите число от 1 до 100: '))
        if guess < number:
            print('Ваше число меньше того, что загадано')
        elif guess > number:
            print('Ваше число больше того, что загадано')
        elif guess == number:
            break

main()

print('Отличная интуиция! Вы угадали число :)')
        
 
