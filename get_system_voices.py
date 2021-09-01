import pyttsx3

index = -1

converter = pyttsx3.init()

voices = converter.getProperty('voices')

for voice in voices:
    index += 1
    print(f"Index {index}")
    print("Voice:")
    print(f"ID: {voice.id}")
    print(f"Name: {voice.name}")
    print(f"Age: {voice.age}")
    print(f"Gender: {voice.gender}")
    print(f"Languages Known: {voice.languages}\n")
