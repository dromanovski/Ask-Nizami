"""

The greatest romantic epic poet in Persian literature Nizami Ganjvi
will answer any question that is on your mind

"""

import tkinter
import random
from PIL import ImageTk
from PIL import Image
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer


WIDTH = 800
HEIGHT = 600

def main():


    # print greetings
    print('')
    print('                                           Ask Nizami anything! ')
    print('')

    # Get an imput and transfer into random image
    question = input('Type your question: ')
    random_image = get_file()

    mixer.init()
    mixer.music.load("audio.wav")
    mixer.music.set_volume(0.2)
    mixer.music.play()
    mixer.music.fadeout(10000)

    # Create a canvas with the image
    canvas = make_canvas(WIDTH, HEIGHT, 'Your Answer')
    image = ImageTk.PhotoImage(Image.open(random_image))
    canvas.create_image(0, 0, anchor="nw", image=image)

    # Extract random quote
    random_quote = get_quote()
    first_part, second_part = adjust_length(random_quote)

    # Create two black placeholder canvases for question and answer
    canvas.create_rectangle(0, 0, 799, 80, fill = 'black')
    canvas.create_rectangle(0, 520, 799, 600, fill='black')

    # Input question and answer on black canvases
    canvas.create_text(10, 20, anchor='w', font='system 15', fill = 'yellow', text= 'You asked Nizami: ')
    canvas.create_text(10, 50, anchor='w', font='Arial 15', fill = 'white', text= question)
    canvas.create_text(90, 530, anchor='w', font='system 15', fill = 'gray', text= 'Nizami answers: ')

    # Add a picture of Nizami and picture of a question mark on black canvases
    nizami = ImageTk.PhotoImage(Image.open('images/nizami.jpg'))
    canvas.create_image(0, 520, anchor="nw", image=nizami)
    question = ImageTk.PhotoImage(Image.open('images/question.png'))
    canvas.create_image(720, 0, anchor="nw", image=question)



    # Create a canvas for an animated line resembling typing for the first line of an answer
    canvas_text1 = canvas.create_text(90, 550, font='Arial 15', fill='white', text='', anchor=tkinter.NW)
    animated1 = first_part
    delta = 50
    delay = 0
    for i in range(len(animated1) + 1):
        s = animated1[:i]
        update_text = lambda s=s: canvas.itemconfigure(canvas_text1, text=s)
        canvas.after(delay, update_text)
        delay += delta

    # Play Prince of Persia 8-bit intro

    # Create a canvas for an animated line resembling typing for the first line of an answer
    canvas_text2 = canvas.create_text(90, 575, font='Arial 15', fill='white', text='', anchor=tkinter.NW)
    animated2 = second_part
    delta = 50
    delay = 5000
    for i in range(len(animated2) + 1):
        s = animated2[:i]
        update_text = lambda s=s: canvas.itemconfigure(canvas_text2, text=s)
        canvas.after(delay, update_text)
        delay += delta


    canvas.mainloop()

# Extract a random quote from a text file
def get_quote():
    random_num2 = random.randint(1, 2224)
    with open('book2.txt', 'rt') as file:
       for i, line in enumerate(file):
           if i == random_num2:
               return line
    file.close()

# Break the quote into two lines if its two long to fit the image
def adjust_length(quote):
    if len(quote) >= 114:
        first_part = quote[0:len(quote) // 2]
        second_part = quote[len(quote) // 2:]
        return first_part, second_part
    else:
        return quote, ''

# Get a random picture from a collection
def get_file():
    random_num = random.randint(1, 565)
    filename = 'images/_' + str(random_num) + '.jpg'
    return filename

# Create a new canvas
def make_canvas(width, height, title=None):
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width, height=height)
    canvas.pack()
    return canvas

    # give back an image
    # give back a quote
    # give back an image on a quote
    # repeat the loop asking user for new questions




if __name__ == '__main__':
    main()