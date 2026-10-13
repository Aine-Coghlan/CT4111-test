def guess_checker(guess, secret):
    if guess < secret:
        return "Too high"
    elif guess > secret:
        return "Too low"
    return "Correct"
