class GuessError(Exception):
    pass

class GuessTooHighError(GuessError):
    pass

class GuessTooLowError(GuessError):

    pass

class GuessCorrectError(GuessError):
    pass

def guess_number():
    secret_number = 42
    while True:
        try:
            guess = int(input("Guess the secret number: "))
            if guess > secret_number:
                raise GuessTooHighError
            elif guess < secret_number:
                raise GuessTooLowError
            else:
                raise GuessCorrectError
        except GuessTooHighError:
            print("Your guess is too high!")
        except GuessTooLowError:
            print("Your guess is too low!")
        except GuessCorrectError:
            print("Congratulations, you guessed the secret number!")
            break

guess_number()
