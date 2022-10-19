import matplotlib.pyplot as plt
import pandas as pd
plt.figure(figsize=(15,9))
def wordcount(string):
    frequency=dict()
    #splits the entire sentence into chuncks of word
    words=string.split()
    for i in range (len(string)):
        if(string[i].isalpha()):
            if string[i] in frequency:
                frequency[string[i]]+=1
            else:
                frequency[string[i]]=1
    return frequency
file=open('constitution.txt','r')
sentence=file.read()
pd.Series(wordcount(sentence)).plot.bar()
