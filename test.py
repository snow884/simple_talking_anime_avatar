from simple_talking_anime_avatar import get_image_speaking, get_speaker_video

image_avatat_speaking_u = get_image_speaking("u")


import pyttsx3

engine = pyttsx3.init()

engine.save_to_file("Hello World", "test.wav")
engine.runAndWait()

get_speaker_video("test.mp4", "test.wav", 30)
