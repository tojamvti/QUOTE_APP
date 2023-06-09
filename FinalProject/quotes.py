import random

class Quotes:
    def __init__(self):
        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
            "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
        ]

    def get_random_quote(self):
        return random.choice(self.quotes)

    def add_quote(self, quote):
        self.quotes.append(quote)
