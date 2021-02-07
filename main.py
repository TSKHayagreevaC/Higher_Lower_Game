from art import logo, vs
from game_data import data
import random

def form_data(account):
    """ Format The Accoount Data Into Printable Format. """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, From {account_country}"

def check_answer(guess, a_followers, b_followers):
    """ Takes The User Guess And Follower Counts And Returns If They Got It Right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display Art
print(logo)

score = 0

game_should_continue = True

account_b = random.choice(data)

# Make The Game Repeatable.

while game_should_continue:

    # Generate A Random Account From The Game Data.
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {form_data(account_a)}")
    print(vs)
    print(f"Compare B: {form_data(account_b)}")

    # Ask For The Guess.
    guess = input("Who Are Having More Followers Type A Or B :\n").lower()

    # Check If The User Is Correct.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give User Feedback On Their Guest.
    if is_correct:
        score += 1
        print(f"You Are Right, Current Score : {score}.")
    else:
        game_should_continue = False
        print(f"Sorry That Is Wrong, Final Score : {score}.")