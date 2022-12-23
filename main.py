from data import words
import random

words_list = [word for word in words.split('\n')[:-1]]
word = random.choice(words_list)
