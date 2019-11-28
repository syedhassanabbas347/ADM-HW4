#!/usr/bin/env python
# coding: utf-8

# In[10]:


#----------------Build your own implementation of Counting Sort-------#
def countingSort(listelement):
    
    x= max(listelement)+1
    indexList = [0 for i in range(x)]
    
    for i in range(len(listelement)):
        indexList[listelement[i]] +=1 

    RunningSumList =list(indexList)
    for i in range(1,(len(RunningSumList))):
        RunningSumList[i] = RunningSumList[i] + RunningSumList[i-1]

    finalList = [0 for i in range(len(listelement))]
   
    for i in range(len(listelement)):
        finalList[ RunningSumList[listelement[i]] -1] = listelement[i]
        RunningSumList[listelement[i]] = RunningSumList[listelement[i]] -1
    print(finalList)

listelement = [1,4,1,2,7,5,2,3494,11,45]
countingSort(listelement)


#-----------implementation of Counting Sort,that receives in input a list with all the letters of the alphabet-----#
def countingSortForAlphabet(listelement):
    ordSortedList = []
    alphabet ='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    alphabetDic = dict(enumerate(alphabet))
    
    for i in range(len(listelement)):
        for key, value in alphabetDic.items():
            if  listelement[i] == value:
                ordSortedList.append(key)
    x= max(ordSortedList)+1
    indexList = [0 for i in range(x)]


    for i in range(len(ordSortedList)):
        indexList[ordSortedList[i]] +=1 

    RunningSumList =list(indexList)
   
    for i in range(1,(len(RunningSumList))):
        RunningSumList[i] = RunningSumList[i] + RunningSumList[i-1]

    finalList = [0 for i in range(len(ordSortedList))]
   
    for i in range(len(ordSortedList)):
        finalList[ RunningSumList[ordSortedList[i]] -1] = ordSortedList[i]
        RunningSumList[ordSortedList[i]] = RunningSumList[ordSortedList[i]] -1
    
   
    for i in range(len(finalList)):
        for key, value in alphabetDic.items():
            if  finalList[i] == key:
                finalList[i]= value
   
    return(finalList)
NameList = ['b','C','R','r','u','V','G','c','v','W','w','X','x','Y','I','g','H','h','m','S','s','y','Z','z','T','t','U','N','i','J','l','M','D','d','E','e','A','a','B','F','f','j','K','k','L','n','O','o','P','p','Q','q']

countingSortForAlphabet(NameList)


# Time Complexity Theoretically: O()=k+n+k+n=2k+2n=2(n+k)=O(n+k)
# Time Complexity Empirically: In our example 'k' is a small value that's why we can take time complexity as O(n) empirically.

# In[ ]:


#---implementation of Counting Sort, that receives in input a list of length m #
# that contains words with maximum length equal to n, and returns the list ordered according to alphabetical order.---------- #
def countingSortForAlphabet(listelement):
    ordSortedList = []
    alphabet =' AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    alphabetDic = dict(enumerate(alphabet))
    
    for i in range(len(listelement)):
        for key, value in alphabetDic.items():
            if  listelement[i] == value:
                ordSortedList.append(key)
    x= max(ordSortedList)+1
    indexList = [0 for i in range(x)]


    for i in range(len(ordSortedList)):
        indexList[ordSortedList[i]] +=1 

    RunningSumList =list(indexList)
   
    for i in range(1,(len(RunningSumList))):
        RunningSumList[i] = RunningSumList[i] + RunningSumList[i-1]

    finalList = [0 for i in range(len(ordSortedList))]
   
    for i in range(len(ordSortedList)):
        finalList[ RunningSumList[ordSortedList[i]] -1] = ordSortedList[i]
        RunningSumList[ordSortedList[i]] = RunningSumList[ordSortedList[i]] -1
    
   
    for i in range(len(finalList)):
        for key, value in alphabetDic.items():
            if  finalList[i] == key:
                finalList[i]= value
   
    return(finalList)


listOfWords = ['Astronomy','Astrolabe','Baa','Astrophysics','At','Aster','Ataman']
#Aster; Astrolabe; Astronomy; Astrophysics; At; Ataman; Attack; Baa

def count3(listOfWords, k):    
    if len(listOfWords)==1:
        return listOfWords
    else:
        firstLetters=[s[k] for s in listOfWords]
        set_letters=set(firstLetters)

        dict_lect={ch:[w for w in listOfWords if w[k]==ch] for ch in firstLetters}

        sort=countingSortForAlphabet(list(dict_lect.keys()))
        out=[]
        for ch in sort:
            out+=count3(dict_lect[ch], k+1)
        return out
maxlen=0
for w in listOfWords:
    if len(w)>maxlen:
        maxlen=len(w)
maxlen+=1
for i in range(len(listOfWords)):
    if len(listOfWords[i])!=maxlen:
        listOfWords[i]=listOfWords[i]+(' '*(maxlen-len(listOfWords[i])))
final=count3(listOfWords, 0)
f=[w[:w.index(' ')] for w in final]
print(f)


# Time Complexity Theoretically: O()=k+n+k+n=2k+2n=2(n+k)=O(n+k)
# Time Complexity Empirically: It can be change with number of input strings but in our example 'k' is a small value that's why we can take time complexity as O(n) empirically.

# In[ ]:




