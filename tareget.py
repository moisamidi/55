from typing import List
import random
import sys

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    boardlist=[]
    for i in range(3):
        boardlist.append([chr(random.choice(range(65,90))),
        chr(random.choice(range(65,90))),
        chr(random.choice(range(65,90)))])
    print (boardlist)
    return boardlist

def letters_list(boardlist: List[List[str]]) -> List[str]:
    """
    Generate list from board
    """
    letters=[]
    for i in boardlist:
        for j in i:
            letters+=j.lower()
    return letters


def get_words(file: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    check1=[]
    check2=[]
    with open(file,'r',encoding='utf-8') as file:
        lines=file.readlines()
    for i in lines:
        firstx=i.strip()
        firsty=firstx.lower()
        if len(firstx)>=4 and letters[4] in firsty:
            check1.append(firsty)
    check0=set(check1)

    for i in check0:
        check2bool=0
        for j in i:
            if j in letters:
                check2bool+=1
            else:
                check2bool-=1
        if check2bool==len(i):
            check2.append(i)

    tuplee=[]
    check3=[]
    for word in check2:
        check3bool=0
        for element in word:
            num1=word.count(element)
            for i in letters:
                num=letters.count(i)
                tuplee+=[(i,num)]
                if element==i and num1<=num:
                    check3bool+=1
                    break
        if check3bool==len(word):
            check3.append(word)
    return check3
def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_words = []
    words = sys.stdin.readlines()
    for i in words:
        for word in i.split():
            if word:
                user_words.append(word)
    return user_words
def get_pure_user_words(user_words: List[str], letters: List[str],\
     words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    check1=[]
    check2=[]
    check4=[]
    for i in user_words:
        if len(i)>=4 and letters[4] in i:
            check1.append(i)
    check0=set(check1)
    for i in check0:
        check2bool=0
        for j in i:
            if j in letters:
                check2bool+=1
            else:
                check2bool-=1
        if check2bool==len(i):
            check2.append(i)

    tuplee=[]
    check3=[]
    for word in check2:
        check3bool=0
        for element in word:
            num1=word.count(element)
            for i in letters:
                num=letters.count(i)
                tuplee+=[(i,num)]
                if element==i and num1<=num:
                    check3bool+=1
                    break
        if check3bool==len(word):
            check3.append(word)
        for element in check3:
            if element not in words_from_dict:
                check4+=element

    return check4
def results_file(check3,user_words,check4):
    """
    save results to file
    """
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(f'all possible words from dictionary:\n\t{" ".join(check3)}\n')
        file.write(f'Words that the player entered :\n\t{", ".join(user_words)}\n')
        file.write(f'Words that are not in the dictionary:\n\t{", ".join(check4)}\n')




def results():
    """
    results
    """
    grid = generate_grid()
    print(grid)
    user_words = get_user_words()
    letters = letters_list(grid)
    wordsdict = get_words('en.txt', letters)
    pure = get_pure_user_words(user_words, letters, wordsdict)
    results_file(wordsdict,user_words, pure)
    

results()
