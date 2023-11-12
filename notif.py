from plyer import notification
import pygame
import time

notification.notify(
    title = "Alert",
    message = "GET BACK TO WORK",
    timeout = 10
)

def play_mp3(file_path, duration):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        time.sleep(duration)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

# Replace 'your_file.mp3' with the path to your MP3 file
file_path = 'alarm_sound_effect.mp3'

# Set the duration in seconds
duration = 3

play_mp3(file_path, duration)