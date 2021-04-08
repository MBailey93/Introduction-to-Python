#!/usr/bin/env python
#-- coding:UTF-8 -- 

import text_stats

def word_choices(text):
    word_dict = {}
    for i in range(len(text)-1):
        cur_word = text[i]
        next_word = text[i+1]
        if cur_word in word_dict:
            if next_word in word_dict[cur_word]:
                word_dict[cur_word][next_word] += 1
            else:
                word_dict[cur_word][next_word] = 1
        else:
            word_dict[cur_word] = {next_word: 1}
    return word_dict


def next_word(word_dict, word):
    if word in word_dict:    
        from random import randint
        total_successors = sum(list(word_dict[word].values()))
        rand_number = randint(1, total_successors)
        cumul_sums = 0
        for key, value in word_dict[word].items():
            if value + cumul_sums >= rand_number:
                return key
            else:
                cumul_sums += value
    else:
        return None 


def check_args(arg):
    try:
        input_file = arg[1]
        if len(arg) < 4:
            print('Arguments must be a .txt file, initial word, max words and (optionally) a file to write to')
        elif len(arg) > 5:
            print('Arguments must be a .txt file, initial word, max words and (optionally) a file to write to')
        elif '.txt' != input_file[-4:]:
            print('Arguments must be a .txt file, initial word, max words and (optionally) a file to write to')
        elif len(arg) == 4:
            return arg[1:4] + [0]
        else:
            return arg[1:5]          
    except:
       print('The file does not exist!')


def generate_text(text, initial_word, max_words):
        cur_word = initial_word
        msg = cur_word
        text = text_stats.read_text(text)
        text = text.split()
        word_dict = word_choices(text)
        for i in range(int(max_words)):
            cur_word = next_word(word_dict, cur_word)
            if cur_word == None:
                break
            msg = msg + " " + cur_word        
        return print(msg)

def output_generated(args):
    if args[3] == 0:
        generate_text(args[0],args[1],args[2])
    else:
        import sys
        original_stdout = sys.stdout
        with open(args[3], 'w') as f:
            sys.stdout = f
            generate_text(args[0],args[1],args[2])
            sys.stdout = original_stdout

if __name__ == '__main__':
    import sys  
    checked_args = check_args(sys.argv)
    if checked_args:
        output_generated(checked_args)     
        