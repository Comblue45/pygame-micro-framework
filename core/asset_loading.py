import pygame
import os

class Assats:

    def __init__(self) -> None:
        self._images = {}
        self._sounds = {}

    def load_image(self, image_path: str, name: str) -> None:
        image = pygame.image.load(image_path)
        self._images[name] = image

    def load_art_folder(self, folder_path: str) -> None:
        EXCEPTIONS = set()

        for file in os.listdir(folder_path):
            if file.endswith(".png") and not any(file.startswith(exception) for exception in EXCEPTIONS):
                self.load_image(f"{folder_path}/{file}", file)

    def get_image(self, name: str) -> pygame.Surface:
        return self._images[name]


    def load_sound(self, sound_path: str, name: str) -> None:
        sound = pygame.mixer.Sound(sound_path)
        self._sounds[name] = sound

    def load_sound_folder(self, folder_path: str) -> None:
        EXCEPTIONS = set()

        for file in os.listdir(folder_path):
            if file.endswith(".wav") and not any(file.startswith(exception) for exception in EXCEPTIONS):
                self.load_sound(f"{folder_path}/{file}", file)

    def get_sound(self, name: str) -> pygame.Surface:
        return self._sounds[name]