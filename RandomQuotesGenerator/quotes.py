import random

QUOTES = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, don’t waste it living someone else’s life. - Steve Jobs",
    "Be the change that you wish to see in the world. - Mahatma Gandhi",
    "In the middle of every difficulty lies opportunity. - Albert Einstein"
]

def get_random_quote():
    """Return a random quote from the list."""
    return random.choice(QUOTES)
