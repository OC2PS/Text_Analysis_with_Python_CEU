#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Naive Bayes and Text Analysis
@author: ariedamuco
"""

# ONLY RUN THIS CELL IF YOU NEED 
# Uncomment the code below and run:


# !conda install nltk #This installs nltk
# import nltk # Imports the library
# nltk.download() #Download the necessary datasets
#STOPWORDS



#########################
#DATA
#########################

import os
os.chdir("/Users/ariedamuco/Dropbox (CEU Econ)/TextAnalysisCEU")

#UC Irvine datasets on ML. https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection 


#open the data as we learned yesterday
file=open('Input/smsspamcollection/SMSSpamCollection', encoding='utf-8')

#read the lines
data = file.readlines()
    
#check how many messages
len(data)

#read the first fice messages
for line in range(0,5):
    print (line ,  data[line])
    
#now open the same file in pandas
import pandas as pd
messages = pd.read_csv('Input/smsspamcollection/SMSSpamCollection', sep='\t',
                           names=["label", "message"])
messages.head()
messages.info()
messages.describe()

messages.groupby('label').describe()
messages['length'] = messages['message'].apply(len)

import seaborn as sns
sns.set_style('whitegrid')

messages['length'].plot(bins=50, kind='hist',color='red')
#skewed distribution
messages.length.describe()
#910 characters, let's see how this looks like, use .iloc[0] to show full message
messages[messages['length'] == 910]['message'].iloc[0]
messages.hist(column='length', by='label',color='red', bins=50,figsize=(10,4))

#it seems that the length of the message is a good predictor of spam, skewed distribution


#lets plot them on the same scale
messages.hist(column='length', by='label',color='red', bins=50,figsize=(10,4), range=[0, 250])

#########################
#TEXT PRE-PROCESS
#########################

"""
The classification algorithms need numerical feature vector in order to perform the classification task. 
There are actually many methods to convert a corpus to a vector format. 
The simplest is the the bag-of-words approach, where each unique word in a text 
will be represented by one number. (As in the Barcelona example)
Similarly we will convert these messages sequences of numbers.
Exactly as yesterday we will split a message into its individual words and return a list.
Moreover, we also remove very common words, ('that', 'on', 'the'). 
To do so, we will use the NLTK library (downloaded earlier). 
It's pretty much the standard library in Python for processing
 text and has a lot of useful features. We'll only use some of the basic ones here.
Let's create a function that will process the string in the message column, 
then we can just use apply() in pandas do process all the text in the DataFrame.
First removing punctuation. 
We can just take advantage of Python's built-in string library to get a quick
list of all the possible punctuation:
"""


"""
The bag-of-words model is a simplifying representation used in natural language processing 
and information retrieval (IR). In this model, a text (such as a sentence or a document)
is represented as the bag (multiset) of its words, disregarding grammar and even word order but keeping multiplicity. 
The bag-of-words model has also been used for computer vision.
The simplest is the the bag-of-words approach, where each unique word in a text will be represented by one number.
"""


from nltk.corpus import stopwords
stopwords.words('english')# Show the vector of stop words


#In here we can use the same processing that we did in previous classes
"""
def remove_junk_in_vec(text):
    junck_free="" 
    punc=[",", ".", ";","'", "?", "&", "!", "-"]
    for i in range(len(text)):
        if text[i] not in punc:
            word=text[i].lower()
            junk_free=junk_free+word
    vec=junk_free.split()               
    return vec
"""
#or alternatively
import string

def remove_junk_in_vec(text):
    junk_free="" 
    for i in text:
        if i.lower() not in string.punctuation:
            junk_free=junk_free+i.lower()
    vec=junk_free.split()               
    return vec

    
#########################
#NORMALIZATION
#########################
"""
NORMALIZE THE TEXT BY DROPPING COMMON WORDS, OR STOPWORDS
There are a lot of ways to continue normalizing this text. 
I.E Stemming or distinguishing by part of speech (http://www.nltk.org/book/ch05.html)

"""


def text_preprocess(text):
    new_vec=[]
    for word in remove_junk_in_vec(text):
        if word not in stopwords.words('english'):
            new_vec.append(word)
    return(new_vec)
        
# Check to make sure its working (TOKENIZATION)
messages['message'].head(9).apply(text_preprocess)

#show original message

messages['message'].head()


#########################
#VECTORIZATION
#########################
"""
Count how many times does a word occur in each message (Known as term frequency)
Weigh the counts, so that frequent tokens get lower weight (inverse document frequency)
Normalize the vectors to unit length, to abstract from the original text length (L2 norm)


Let's begin the first step:
Each vector will have as many dimensions as there are unique words in the SMS corpus.
 We will first use SciKit Learn CountVectorizer. This model will convert a collection 
 of text documents to a matrix of token counts.
We can imagine this as a 2-Dimensional matrix. 
Where the 1-dimension is the entire vocabulary (1 row per word) 
and the other dimension are the actual documents, in this case a column per text message.

Since there are so many messages, we can expect a lot of zero counts for the 
presence of that word in that document. Because of this, SciKit Learn will output a Sparse Matrix.

"""


from sklearn.feature_extraction.text import CountVectorizer

#CountVectorizer Will convert text into token counts
bow_transformer = CountVectorizer(analyzer=text_preprocess).fit(messages['message'])

# Print total number of vocab words
print (len(bow_transformer.vocabulary_))

#let's take a spam message
message9 = messages['message'][8]
print (message9)

#see the vector representation
bow9 = bow_transformer.transform([message9])
print (bow9)
print (bow9.shape)
#this means that after doing the string transformation, none of the words is repeated


#Only one word has been repeated twice, by seeing the email it seems to be "claim"
#let's check if this is the case
print (bow_transformer.get_feature_names()[1544])

#check out feature 9060
print (bow_transformer.get_feature_names()[9060])

#maybe we should have removed also symbols of currency such as pounds or maybe we
#shouldn't as spams usually advertise stuff for sale or prize winning


#transform now all dataset
messages_bow = bow_transformer.transform(messages['message'])

"""
print ('Shape of Sparse Matrix: ', messages_bow.shape)
print ('Amount of Non-Zero occurences: ', messages_bow.nnz)
print ('sparsity: %.2f%%' % (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1])))
"""

#now scikit learn

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer().fit(messages_bow)
tfidf9 = tfidf_transformer.transform(bow9)
print (tfidf9)
print (tfidf_transformer.idf_[bow_transformer.vocabulary_['claim']])



messages_tfidf = tfidf_transformer.transform(messages_bow)
print (messages_tfidf.shape)


from sklearn.naive_bayes import MultinomialNB
#why naive bayes?
#http://www.inf.ed.ac.uk/teaching/courses/inf2b/learnnotes/inf2b-learn-note07-2up.pdf
spam_detect_model = MultinomialNB().fit(messages_tfidf, messages['label'])

print ('predicted:', spam_detect_model.predict(tfidf9)[0])
print ('expected:', messages.label[9])


all_predictions = spam_detect_model.predict(messages_tfidf)
print (all_predictions)

true_val=messages['label']


from sklearn.metrics import classification_report
print (classification_report(messages['label'], all_predictions))




from sklearn.model_selection import train_test_split

msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size=0.2, random_state=1)



from sklearn.pipeline import Pipeline
#create pipeline
pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_preprocess)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])

#Now we can directly pass message text data and the pipeline will do our pre-processing for us! We can treat it as a model/estimator API:
    
    
pipeline.fit(msg_train,label_train)
predictions = pipeline.predict(msg_test)

print (classification_report(predictions,label_test))
