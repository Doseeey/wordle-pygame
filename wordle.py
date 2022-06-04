import pygame
from constants import Constants as C
from random import choice

pygame.init()
pygame.display.set_caption("Wordle game clone")
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30

def get_word():
    wordlist = [word.replace("\n", "") for word in list(open("wordlist.txt"))]
    word = choice(wordlist)
    assert(len(word) == C.LETTER_LENGTH)
    assert(word.islower())

def main(): 
    clock = pygame.time.Clock()
    guess_word = get_word()
    while True:
        

if __name__ == "__main__":
    main()