import tkinter.scrolledtext
from tkinter import *
from WordList import WordList

FONT_NAME = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"

def start_review():
    card_numbers = card_slider.get()
    word_list.reset_program(card_numbers)
    main_menu_frame.pack_forget()
    card_front_frame.pack(padx=1,pady=1)
    set_card()

def flip():
    card_front_frame.pack_forget()
    card_back_frame.pack(padx=1,pady=1)

def next_card():
    if word_list.current_word is not None:
        card_back_frame.pack_forget()
        card_front_frame.pack(padx=1, pady=1)
        set_card()
    else:
        card_back_frame.pack_forget()
        load_results()

def front_to_results():
    card_front_frame.pack_forget()
    load_results()

def back_to_results():
    card_back_frame.pack_forget()
    load_results()

def load_results():
    word_list.examine_results()
    correct_number["text"] = str(len(word_list.correct_list))
    help_number["text"] = str(len(word_list.correct_needed_help))
    wrong_number["text"] = str(len(word_list.wrong_words))
    overview_frame.pack(padx=1, pady=1)

def back_to_menu():
    overview_frame.pack_forget()
    main_menu_frame.pack(padx=1,pady=1)


def correct_selected():
    word_list.set_word_to_finished(True)
    next_card()

def wrong_selected():
    word_list.set_word_to_finished(False)
    next_card()

def show_sample():
    word_list.current_word["sample_used"] = True
    card_front_canvas.itemconfig(front_sample, text=word_list.current_word["Sentence_Chinese"])
    if word_list.is_pinyin_shown:
        card_front_canvas.itemconfig(front_sample_pinyin, text=word_list.current_word["Sentence_pinyin"])


def set_card():
    card_front_canvas.itemconfig(word_text, text=word_list.current_word["Chinese"])
    card_back_canvas.itemconfig(back_chinese,text=word_list.current_word["Chinese"])
    card_back_canvas.itemconfig(back_pinyin, text=word_list.current_word["Pinyin"])
    card_back_canvas.itemconfig(back_definition, text=word_list.current_word["Definition"])
    card_back_canvas.itemconfig(back_sample, text=word_list.current_word["Sentence_Chinese"])
    card_back_canvas.itemconfig(back_sample_pinyin, text=word_list.current_word["Sentence_pinyin"])
    card_back_canvas.itemconfig(back_sample_english, text=word_list.current_word["Sentence_english"])
    display_pinyin()
    card_front_canvas.itemconfig(front_sample, text="")
    card_front_canvas.itemconfig(front_sample_pinyin, text="")

def set_overview():
    word_list.examine_results()


def show_pinyin_pressed():
    word_list.show_pinyin()
    display_pinyin()

def display_pinyin():
    pinyin_data_string = ""
    pinyin_sentence_string = ""
    if word_list.is_pinyin_shown:
        pinyin_data_string = word_list.current_word["Pinyin"]
    card_front_canvas.itemconfig(pinyin_text, text=pinyin_data_string)
    if word_list.current_word["sample_used"] and word_list.is_pinyin_shown:
        pinyin_sentence_string = word_list.current_word["Sentence_pinyin"]
    card_front_canvas.itemconfig(front_sample_pinyin, text=pinyin_sentence_string)

#get data
word_list = WordList(1000)
window = Tk()
window.title("Flashcard")
# window.minsize(width=300,height=300)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

#main menu
main_menu_frame = Frame(window, bg=BACKGROUND_COLOR,width=1000,height=725)
Label(main_menu_frame, text="1000 Mandarin Phrases Flashcards", background=BACKGROUND_COLOR, font=(FONT_NAME, 60, "bold")).grid(column=1,row=0)
card_slider = Scale(main_menu_frame, from_=1, to=1000, background=BACKGROUND_COLOR, highlightthickness=0, orient=HORIZONTAL, length=500)
card_slider.grid(column=0, row=1, columnspan=3)
start_button = Button(main_menu_frame, text="Start", command=start_review).grid(column=1,row=2)
main_menu_frame.pack(padx=1,pady=1)

#card_front_frame
card_front_frame = Frame(window, bg=BACKGROUND_COLOR,width=1000,height=725)

#card back frame
card_back_frame = Frame(window, bg=BACKGROUND_COLOR,width=1000,height=725)

#overview frame
overview_frame = Frame(window, bg=BACKGROUND_COLOR,width=1000,height=725)
Label(overview_frame, text="Results").grid(column=1,row=0)
#scrollbar correct
Label(overview_frame, text="Correct").grid(column=0,row=2)
correct_number = Label(overview_frame, text="Correct")
correct_number.grid(column=0,row=3)
correct_list = tkinter.scrolledtext.ScrolledText(overview_frame, width = 30, height = 8, font=(FONT_NAME, 10, "normal"))
#scollbar needHelp
Label(overview_frame, text="Need help").grid(column=1,row=2)
help_number = Label(overview_frame, text="Correct")
help_number.grid(column=1,row=3)
help_list = tkinter.scrolledtext.ScrolledText(overview_frame, width = 30, height = 8, font=(FONT_NAME, 10, "normal"))
#scrollbar wrong
Label(overview_frame, text="Wrong").grid(column=2,row=2)
wrong_number = Label(overview_frame, text="Correct")
wrong_number.grid(column=2,row=3)
wrong_list = tkinter.scrolledtext.ScrolledText(overview_frame, width = 30, height = 8, font=(FONT_NAME, 10, "normal"))

Button(overview_frame, text="Back to menu", command=back_to_menu).grid(column=3,row=6)


#images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
correct_button_image = PhotoImage(file="images/right.png")
wrong_button_image =PhotoImage(file="images/wrong.png")

#buttons
example_button = Button(card_front_frame, text="Example Usage",highlightthickness=0, command=show_sample)
example_button.grid(column=2, row=2)
flip_button = Button(card_front_frame, text="Flip",highlightthickness=0, command=flip)
flip_button.grid(column=4, row=2)
front_quit = Button(card_front_frame, text="End Test",highlightthickness=0, command=front_to_results)
front_quit.grid(column=4, row=3)
back_quit = Button(card_back_frame, text="End Test",highlightthickness=0, command=back_to_results)
back_quit.grid(column=3, row=5)
#back frame

correct_button = Button(card_back_frame, image=correct_button_image,highlightthickness=0, command=correct_selected )
correct_button.grid(column=0, row=4)
wrong_button = Button(card_back_frame, image=wrong_button_image,highlightthickness=0, command=wrong_selected)
wrong_button.grid(column=3, row=4)

#canvas
card_front_canvas = Canvas(card_front_frame, width=800,height=525,highlightthickness=0, background=BACKGROUND_COLOR)
card_front_canvas.create_image(400,262, image=card_front_image)
card_front_canvas.grid(column=0,row=1, columnspan=4)
word_text = card_front_canvas.create_text(400,263, text="word", fill="black", font=(FONT_NAME, 60, "bold"))
pinyin_text = card_front_canvas.create_text(400,363, text="pinyin", fill="black", font=(FONT_NAME, 30, "normal"),width=1000)
front_sample = card_front_canvas.create_text(400,413, text="pinyin", fill="black", font=(FONT_NAME, 20, "normal"),width=2000)
front_sample_pinyin = card_front_canvas.create_text(400,450, text="pinyin", fill="black", font=(FONT_NAME, 20, "normal"),width=2000)
#back
card_back_canvas = Canvas(card_back_frame, width=800,height=525,highlightthickness=0, background=BACKGROUND_COLOR)
card_back_canvas.create_image(400,262, image=card_back_image)
card_back_canvas.grid(column=0,row=1, columnspan=4)
back_chinese = card_back_canvas.create_text(400,50, text= "char", fill="black", font=(FONT_NAME, 40, "normal"))
back_pinyin = card_back_canvas.create_text(400,110, text= "pinyin", fill="black", font=(FONT_NAME, 30, "italic"))
back_definition = card_back_canvas.create_text(400,170, text= "def", fill="black", font=(FONT_NAME, 10, "normal"),width=1000)
back_sample = card_back_canvas.create_text(400,250, text= "samp", fill="black", font=(FONT_NAME, 20, "normal"),width=1000)
back_sample_pinyin = card_back_canvas.create_text(400,300, text= "samp_pinyin", fill="black", font=(FONT_NAME, 10, "normal"),width=1000)
back_sample_english = card_back_canvas.create_text(400,330, text= "samp_english", fill="black", font=(FONT_NAME, 10, "normal"),width=1000)

#PinyinFunctions
pinyin_show = False
show_pinyin_button = Button(card_front_frame, text="Show Pinyin", bg=BACKGROUND_COLOR, command=show_pinyin_pressed)
show_pinyin_button.grid(column=1, row=2)

#end of mainloop
window.mainloop()
