import time

lyrics = [
    "I was scared to take a breath, didn't want you to move your head",
    "How can we go back to be friends",
    "when we just shared a bed?",
]

def typing_animation(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() 

def show_lyrics(lyrics):
    for line in lyrics:
        typing_animation(line)
        time.sleep(1.5)
    print()

if __name__ == "__main__":
    show_lyrics(lyrics)
