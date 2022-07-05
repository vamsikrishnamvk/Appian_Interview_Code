import random
def shuffle1(list_52):
    # print(list_52)
    if(len(list_52)<2):
        return None
    else:
        for i in range(len(list_52)-1,0,-1):
            j = random.randint(0, i + 1)
            list_52[i], list_52[j] = list_52[j], list_52[i]

def dealacard(list_52):
    pickone = random.randint(0,len(list_52)-1)
    # print(pickone)
    return pickone

dict_of_cards= {1:'Hearts_Ace',2:'Hearts_2',3:'Hearts_3',4:'Hearts_4',5:'Hearts_5',6:'Hearts_6',7:'Hearts_7',8:'Hearts_8',9:'Hearts_9',10:'Hearts_10',11:'Hearts_Jack',
12:'Hearts_King',13:'Hearts_Queen',14:'Clubs_Ace',15:'Clubs_2',16:'Clubs_3',17:'Clubs_4',18:'Clubs_5',19:'Clubs_6',20:'Clubs_7',
21:'Clubs_8',22:'Clubs_9',23:'Clubs_10',24:'Clubs_Jack',25:'Clubs_King',26:'Clubs_Queen',27:'Spades_Ace',28:'Spades_2',
29:'Spades_3',30:'Spades_4',31:'Spades_5',32:'Spades_6',33:'Spades_7',34:'Spades_8',35:'Spades_9',36:'Spades_10',
37:'Spades_Jack',38:'Spades_King',39:'Spades_Queen',40:'Diamonds_Ace',41:'Diamonds_2',42:'Diamonds_3',43:'Diamonds_4',
44:'Diamonds_5',45:'Diamonds_6',46:'Diamonds_7',47:'Diamonds_8',48:'Diamonds_9',49:'Diamonds_10',50:'Diamonds_Jack',
51:'Diamonds_King',52:'Diamonds_Queen'}
# print(dict_of_cards[1])

list_52=[]
for i in range(1,53):
    list_52.append(i)
shuffle1(list_52)
# print(list_52)
jj=0
for k in range(0, len(list_52)):
    #print(len(list_52))
    if(len(list_52)==0 or len(list_52)>52):
        print("Deck Empty")
    else:
        #list_52.remove(list_52[dealacard(list_52)])
        if(len(list_52)!=0):
            # print("kk",len(list_52))
            # print(list_52)
            temp = dealacard(list_52)
            print(dict_of_cards[list_52[temp]])
            list_52.remove(list_52[temp])
        #shuffle1(list_52)
        jj+=1
print("total deck count",jj)