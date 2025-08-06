import pygame

# Inicializa o mixer e o pygame
pygame.init()
pygame.mixer.init()

# Carrega a música
pygame.mixer.music.load('ex021.mp3')

# Toca a música
pygame.mixer.music.play()

# Mantém o programa aberto até o usuário apertar ENTER
input('Pressione ENTER para encerrar...')
