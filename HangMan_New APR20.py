from random_word import RandomWords
import numpy as np
r = RandomWords()


def word_creator():
    word1=r.get_random_word()
    if word1==None:
        word(word_creator)
    return (word1)

def Convert(string):
    output=[]
    output[:0]=string
    return output

def underscore_creator(randnum,word):
    arrayed_word=Convert(word)
    print (word, "is word")
    answer=[]
    for i in range(len(randnum)):
        answer.append(arrayed_word[randnum[i]])
        arrayed_word[randnum[i]]="_"

    return (answer,arrayed_word)

def randomize_array_of_numbers(word):
    randnums=np.random.randint(0,len(word),len(word)-3)
    return randnums

def array_to_word(targetted_array):
    final_word=''
    for i in range(len(targetted_array)):
        final_word=final_word+targetted_array[i]
    return final_word

def count_the_number_of_attemps(arrayed_word):
    count=0
    for i in range(len(arrayed_word)):
        if arrayed_word[i]=='_':
            count=count+1

    attempt=count+3
    return attempt

def input_user_choice():
    print ("Enter your choice: ")
    choice=input("")
    return choice

def check_choice_in_answer_list(choice,answer):
    answer_match=False
    for i in range(len(answer)):
        if choice==answer[i]:
            answer_match=True
            break
            del answer[i]
    return answer_match

def print_status_formally(status):
    if status==True:
        print ("Great! You guessed the right word.")
    else:
        print ("Sorry! You missed a guess.")

def keeping_the_word_back(choice,arrayed_word,in_array):
    print (choice," is choice ",arrayed_word," is arrayed word ",in_array," is in array")

    for i in range(len(in_array)):
        if choice==in_array[i]:
            req_num=i
            in_array[i]=in_array[i].upper()
            arrayed_word[req_num]=choice
    to_show=array_to_word(arrayed_word)
    return to_show

def validating_choice(choice):
    if len(choice)!=1:
        return False

def main():

    word_range=7

    flag="White"
    print ("")
    print ("Please wait for me to find you a suitable word.. ")
    while flag=="White":

    #creating word on criteria

        word=word_creator()


        if len(word)<=word_range and len(word)>=word_range-2:
             flag="Red"


    #randomizing and creating underscore pattern

    randnum=randomize_array_of_numbers(word)
    answers,arrayed_word=underscore_creator(randnum,word)

    print ("")
    print ("Alright, I found you a word.")
    print (array_to_word(arrayed_word))

    print ("Welcome to the answering section of the game. ")

    #number of attempts
    attempts=count_the_number_of_attemps(arrayed_word)

    in_array=Convert(word)
    inputted_array=[]

    print (answers, " is the answers")
    for i in range(attempts):
        choice=input_user_choice()
        valid_choice=validating_choice(inputted_array,choice)
        if valid_choice==False:
            print ("Please enter a single letter as your choice. For example: 'a', 'b', 'c' e.t.c...")
            attempts=attempts+1
            continue
        status=check_choice_in_answer_list(choice,answers)
        print_status_formally(status)
        print ("Number of attempts remaining is: ",attempts-i-1)
        if status==True:
            print (keeping_the_word_back(choice,arrayed_word,in_array)," is the current status of your Hangman Word")
            print ("")
        if word.lower()==keeping_the_word_back(choice,arrayed_word,in_array).lower():
            print ("Congratulations!!! You saved the Hanging Man.")
            break




def welcome():
    print ("Welcome to Baibhav's Hangman. Press Y to proceed.")
    user_choice=input ("")
    if user_choice=="Y":
        main()
    else:
        print ("Thank you for using Baibhav's Hangman. See you soon.")



welcome()



#almost completed. Just data_inputting and checking is left