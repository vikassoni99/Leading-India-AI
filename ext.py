import pandas as pd
import nltk

train = pd.read_csv('extraction.csv')

##Number of words
'''
train['word_count'] = train['Title'].apply(lambda x: len(str(x).split(" ")))
train[['Title','word_count']].head()
print(train['word_count'])
'''

##Number of characters
'''
train['char_count'] = train['Title'].str.len()
train[['Title','char_count']].head()
print(train['char_count'])
'''

#Average word length
'''
def avg_word(sentence):
  words = sentence.split()
  return (sum(len(word) for word in words)/len(words))

train['avg_word'] = train['Title'].apply(lambda x: avg_word(x))
train[['Title','avg_word']].head()
print(train['avg_word'])
'''

#Number of stop words
'''
from nltk.corpus import stopwords
stop = stopwords.words('english')

train['stopwords'] = train['Title'].apply(lambda x: len([x for x in x.split() if x in stop]))
train[['Title','stopwords']].head()
'''

#Number of stopwords
'''
train['special_char'] = train['Title'].apply(lambda x: len([x for x in x.split() if x.startswith('#')]))
train[['Title','special_char']].head()
print(train['special_char'])
'''

#Number of numerics
'''
train['numerics'] = train['Title'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
train[['Title','numerics']].head()
print(train['numerics'])
'''

#Number of Upper-case words
'''
train['upper'] = train['Title'].apply(lambda x: len([x for x in x.split() if x.isupper()]))
train[['Title','upper']].head()
print(train['upper'])
'''