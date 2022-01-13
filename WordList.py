import csv
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
        self.correct_list = []
        self.correct_needed_help = []
        self.wrong_words = []
        self.current_word = None
        self.get_random_word()
        self.is_pinyin_shown = False

    def reset_program(self, words_possible = 1000):
        self.available_list = self.words_list
        if words_possible < len(self.words_list):
            self.available_list = self.get_limited_group(words_possible)
        self.finished_list = []
        self.correct_list = []
        self.correct_needed_help = []
        self.wrong_words = []
        self.get_random_word()
        self.is_pinyin_shown = False

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
        self.is_pinyin_shown = False
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

    def examine_results(self):
        self.correct_list = []
        self.correct_needed_help = []
        self.wrong_words = []
        for word in self.finished_list:
            if word["is_correct"]:
                if word["sample_used"]:
                    self.correct_needed_help.append(word)
                else:
                    self.correct_list.append(word)
            else:
                self.wrong_words.append(word)
        keys =self.finished_list[0].keys()

        with open('data/correct.csv', 'w', newline='',encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.correct_list)


        with open('data/correct_with_help.csv', 'w', newline='',encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.correct_needed_help)


        with open('data/wrong.csv', 'w', newline='',encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.wrong_words)