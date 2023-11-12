from plyer import notification
import pygame
import time
import serial
# notification.notify(
#     title = "Alert",
#     message = "GET BACK TO WORK",
#     timeout = 10
# )

def noti():
    arduino = serial.Serial('/dev/cu.usbmodem14201',115200,timeout=1)
    window = pygame.display.set_mode((700, 700))
    TEXTCOLOUR = (0, 0, 0)
    pygame.display.set_caption("STOP BEING DISTRACTED")
    fontObj = pygame.font.Font(None, 50)
    textSufaceObj = fontObj.render("STOP BEING DISTRACTED", True, TEXTCOLOUR, None)
    running = True
    numtimesran = 0
    while running:
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running = False
        
        window.fill((238, 75, 43))
        window.blit(textSufaceObj, (100, 100))
        pygame.display.flip()
        if(numtimesran>500):
            arduino.write(b'f')
            pygame.display.quit()
            break
        numtimesran+=1
        #print(numtimesran)

def play_mp3(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    noti()
    # try:
    #     pygame.mixer.music.load(file_path)
    #     pygame.mixer.music.play()
    #     noti()
    # finally:
    #     pygame.mixer.music.stop()
    #     pygame.mixer.quit()
    #     pygame.quit()

# # Replace 'your_file.mp3' with the path to your MP3 file
# file_path = 'alarm_sound_effect.mp3'

# # Set the duration in seconds
# duration = 10
# play_mp3(file_path, duration)