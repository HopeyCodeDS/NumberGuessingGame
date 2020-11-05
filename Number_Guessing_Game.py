from random import randint

#Maximum number of trial
max_trial = 5
print('You only have 7 chances')

#Initializing the number of guesses
count = 0

random_number = randint(1,11)

while count < max_trial:
    count += 1    

    #Users guessed number between 1 and 10
    guess = int(input('Guess any number between 1 and 10: '))    

    if guess == random_number:
        print('Congratulations, you guessed right at the ', count,'try')
        #Once guessed right, the loop will break
        break
    elif guess > random_number:
        print('Incorrect! Your guess is high!')
        print('Try again!')
    elif guess < random_number:
        print('Incorrect Your guess is low!')
        print('Try again!')
     
if count >= max_trial:
    print('The number is {}'.format(random_number))
    print('Try your luck next time')
