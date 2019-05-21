

import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import os
os.chdir("/Users/ariedamuco/Dropbox (CEU Econ)/TextAnalysisCEU")

def preprocessing(text):
    words = word_tokenize(text)
    tokens = [w for w in words if w.lower() not in string.punctuation]
    stopw = stopwords.words('english')
    tokens = [token for token in tokens if token not in stopw]
    # remove words less than three letters
    tokens = [word for word in tokens if len(word)>=3]
    # lemmatize
    lemma = WordNetLemmatizer()
    tokens = [lemma.lemmatize(word) for word in tokens]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text 


text1 = open('Input/105-extracted-date/105-ford-ky.txt', encoding='latin1').read()
text2 = open('Input/105-extracted-date/105-mcconnell-ky.txt', encoding='latin1').read()
text3 = open('Input/105-extracted-date/105-breaux-la.txt', encoding='latin1').read()
text4 = open('Input/105-extracted-date/105-landrieu-la.txt', encoding='latin1').read()

list1 = [text1, text2, text3, text4]
word_list = []
for line in list1:
    word_list.append(preprocessing(line))
word_list

vectorizer = TfidfVectorizer()
doc_vector = vectorizer.fit_transform(word_list)

df = pd.DataFrame(doc_vector.toarray().transpose(), index=vectorizer.get_feature_names())
df.columns = ['text1', 'text2', 'text3', 'text4']


from sklearn.metrics.pairwise import cosine_similarity

txt1 = df['text1'].values.reshape(1, -1)
txt2 = df['text2'].values.reshape(1, -1)
txt3 = df['text3'].values.reshape(1, -1)
txt4 = df['text4'].values.reshape(1, -1)

print("Similarity txt1 and txt2:", cosine_similarity(txt1, txt2))
#http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html


