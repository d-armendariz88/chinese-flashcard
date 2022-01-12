import pandas
import random

class WordList:
    def __init__(self, words_possible = 1000):
        self.words = pandas.read_csv("data/1000 chinese words and phrases - Sheet1.csv")
        self.words_list = []
        for index, rows in self.words.iterrows():
            my_list = {"Chinese": rows["Chinese"], "Pinyin": rows["Pinyin"], "Definition": rows["Definition"],
                       "Sentence_Chinese": rows["Sentence 1 - Chinese"], "Sentence_pinyin": rows["Sentence 1 - Pinyin"],
                       "Sentence_english": rows["Sentence 1 - English"], "is_correct": False, "sample_used": False}
            self.words_list.append(my_list)

        self.available_list = self.words_list
        if words_possible < len(self.words_list):
            self.available_list = self.get_limited_group(words_possible)
        self.finished_list = []
        self.current_word = None
        self.get_random_word()
        self.is_pinyin_shown = False

    def reset_program(self, words_possible = 1000):
        self.available_list = self.words_list
        if words_possible < len(self.words_list):
            self.available_list = self.get_limited_group(words_possible)
        self.finished_list = []
        self.get_random_word()

    def show_pinyin(self):
        self.is_pinyin_shown = not self.is_pinyin_shown

    def get_limited_group(self, words_possible):
        word_possible_list = self.words_list
        save_list = []
        for x in range(words_possible):
            random_index = random.randint(0, len(word_possible_list) - 1)
            save_list.append(word_possible_list.pop(random_index))
        return save_list

    def get_random_word(self):
        if(len(self.available_list)==0):
            self.current_word = None
            return
        random_index = random.randint(0, len(self.available_list) - 1)
        self.current_word = None
        new_word = self.available_list.pop(random_index)
        self.current_word = new_word

    def set_word_to_finished(self, is_correct):
        self.current_word["is_correct"] = is_correct
        self.finished_list.append(self.current_word)
        self.get_random_word()