#!/usr/bin/env python
#-- coding:UTF-8 -- 

def read_text(name1):
    import sys
    import string
    with open(sys.path[0] + '/' + name1, 'r', encoding="utf8") as file:
        text = file.read()
    z = string.punctuation
    text = text.lower()
    remove_punc = text.maketrans('', '', z)
    text = text.translate(remove_punc)
    return text 

def letter_stat(text1):
    import string
    z = string.ascii_lowercase
    letters = {}
    for i in z:
        letters[i] = text1.count(i)
    data_stat = sorted(letters.items(), key = lambda item: item[1], reverse = True)
    return data_stat   

def word_stat(text2):
    from collections import Counter
    from functools import reduce
    import string
    new_text2 = text2.split()
    word = Counter(new_text2)
    data = sorted(word.items(), key = lambda x : x[1], reverse = True)
    data_stat = data[0 : 5]
    follow_index = ([i + 1 for i, x in enumerate(new_text2) if x == y[0]] for y in data_stat)
    follow_word = ([new_text2[x] for x in y] for y in follow_index)
    follow_stat = [sorted(Counter(x).items(), key = lambda x : x[1], reverse = True)[0 : 3] for x in follow_word]
    return [data_stat, follow_stat]

def unique_stat(text3):
    new_text1 = text3.split()
    data_stat = len(set(list(new_text1)))
    return data_stat
    
def text_stat(text4):
    import string
    new_text1 = text4.split()
    data = len(list(new_text1))
    return data
    
    
def input_text(arg):
    try:
        input_file = arg[1]
        if len(arg) < 2:
            print('Please input a text file to analyse!')
        elif len(arg) > 3:
            print('Arguments must be a .txt file to analyse and optionally another to write to')
        elif '.txt' != input_file[-4:]:
            print('Arguments must be one or two files in .txt format!')
        elif len(arg) == 2:
            return [read_text(input_file), 0]
        else:
            return [read_text(input_file), arg[2]]          
    except:
        print('The file does not exist!')

def print_stats(text):
    try:
        print('The count of each letter in the text is : \n')
        stat1 = letter_stat(text1 = text)
        for i in range(len(stat1)):
            print('-- {}, {}'.format(stat1[i][0], stat1[i][1]))
        print('\n')
        print('The most commonly occuring words in the text and the words that mostly frequently follow them are: \n')
        stat2 = word_stat(text2 = text)
        for i in range(len(stat2[0])):
            print('{} ({} occurrences)'.format(stat2[0][i][0], stat2[0][i][1]))
            for j in range(len(stat2[1][0])):
                print('-- {},  {}'.format(stat2[1][i][j][0], stat2[1][i][j][1]))
        print('\n')
        stat3 = unique_stat(text3 = text)
        print('The number of unique words without punctuation in the text is : {}'.format(stat3))
        print('\n')
        stat4 = text_stat(text4 = text)
        print('The number of words without punctation in the text is : {}'.format(stat4))
    except Exception as e:
        print(e)

def output_stats(files):
    if files[1] == 0:
        print_stats(files[0])
    else:
        import sys
        original_stdout = sys.stdout
        with open(files[1], 'w') as f:
            sys.stdout = f
            print_stats(files[0])
            sys.stdout = original_stdout
    
if __name__ == '__main__':
    import sys
    text_orig = input_text(sys.argv)    
    if text_orig:
        output_stats(text_orig)



#Additional questions
#1.
#In what way did you "clean up" or divide up the text into words (in the program; the text files should be left
#unaffected)? This does not have to be perfect in any sense, but it should at least avoid counting "lord",
# "Lord" and "lord." as different words？

#First, all the punctuation in the text is removed from the text, because it should not be definied as words.
#Second, splitting the text by a space to generate words, because the content between two space should be definied as words.
#Third, changing all the upper letters into lower letters.

#2.
#Which data structures have you used (such as lists, tuples, dictionaries, sets, ...)? Why does that choice
#make sense? You do not have to do any extensive research on the topics, or try to find exotic modern data
#structures, but you should reflect on which of the standard data types (or variants thereof) make sense. If
#you have tried some other solution and updated your code later on, feel free to discuss the effects!

#First, 'generator' data structure which has highest frequency in this task, because it does not save the whole data, but the formula to generate
#the data. So it can save a lot of memory and increase the running speed.
#Second, 'list' data structure is uesd to be output, because it can save the real data.
#Third, 'dictionary' data structure is used to sort the words and letters by their frequency which is a convenient way to sort.
#Third, 'set' data structure is used to generate unique words.
