
import re




def print_menu():
    print("Please enter your choice:\n1.Add new word\n2.Translate english to persian\n3.Translate Persian to English\n4.Exit")
words=[]
def load():
    print("loading")
    file=open('database.txt','r')
    rows=file.read().split('\n')

    for i in range(len(rows)):
        info=rows[i].split(",")
        words.append({
            'english':info[0],
            'persian':info[1]
        })
    print("Program is ready to use")
    file.close()


load()


def normalize_whitespace(string):
    return re.sub(r'(\s)\1{1,}', r'\1', string)
def add_word():

    while True:
        pass_parameter = 0
        new_pass = 0
        newword_en=str(input("Please enter your word in english"))
        newword_per = str(input("Please enter your word in persian"))
        for i in range(len(words)):
            if words[i]['english']==newword_en:
                print("That word is already exist")
                pass_parameter=1
                break
        for i in range(len(words)):
            if pass_parameter==1:
                new_pass=1
                break
            if words[i]['persian']==newword_per:
                print("That word is already exist")
                new_pass=1
                break
        if new_pass==1:
            pass
        else:
            words.append({'english':newword_en,'persian':newword_per})
            break


def search_word_english(search):
    correctcounter = 0
    for i in range(len(words)):
        if search==words[i]['english']:
            return words[i]['persian']
            correctcounter = 1
    if correctcounter==0:
        return "*"

def search_word_persian(search):
    correctcounter=0
    for i in range(len(words)):
        if search==words[i]['persian']:
            return words[i]['english']
            correctcounter = 1
            break
    if correctcounter==0:
        return "*"

def e2p():
    inpt=input("please enter your sentence in english:( \"*\" this is means that your word is not in our database)")
    inpt = re.sub('[ \t]+', ' ', inpt)
    searchwords=inpt.strip().split(' ')
    translation=[]
    for j in range(len(searchwords)):
        translation.append(search_word_english(searchwords[j]))
    for i in range(len(translation)):
        print(translation[i],end=" ")

def p2e():
    inpt=input("Please enter your word in persian:( \"*\" this is means that your word is not in our database)")
    inpt = re.sub('[ \t]+', ' ', inpt)
    searchword=inpt.strip().split(' ')
    translation=[]
    for j in range (len(searchword)):
        translation.append(search_word_persian(searchword[j]))
    for i in range(len(translation)):
        print(translation[i], end=" ")

def exxit():
    file=open('database.txt','w')
    for i in range(len(words)):
        if len(words)-1==i:
            rows=words[i]['english']+','+words[i]['persian']
            file.write(rows)
        else:
            rows=words[i]['english']+','+words[i]['persian']+'\n'
            file.write(rows)
    file.close()
    exit()


while True:
    print("\n")
    print_menu()
    choice=int(input("choice:"))
    if choice==1:
        add_word()
    if choice == 2:
        e2p()
    if choice ==3:
        p2e()
    if choice==4:
        exxit()










