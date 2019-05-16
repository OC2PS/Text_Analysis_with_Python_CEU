#pip install nltk
#python -m install nltk

import nltk
#nltk.download()
paragraph="""Mr. ABRAHAM. Mr. President, I rise to register serious concern over a provision in the Omnibus Appropriations bill, included as I understand it over the protest of the Senate. This is a legislative provision appended to the Commerce, Justice, State Appropriations portion of the bill that subjects federal prosecutors and other `attorneys for the Government' to State laws and rules governing attorneys `to the same extent and in the same manner as other attorneys in that State.' 
Now please understand, Mr. President. I think I am as much of a believer in federalism as anyone here. But federalism does not mean that control of all matters should be ceded to the States. One area where I think it is pretty clear that the national government should be the principal source of law is in setting rules of professional conduct for its own officers. To leave that question to the States, it seems to me, is to cede a very large portion of the control for how federal law is to be enforced to the States. That power can then be used to frustrate the enforcement of federal law. The risk that this will happen is significantly greater where the power is being turned over not to the States' elected representatives, but to bar associations vested with the States' powers, but without the accountability to the people of the States that elections generate. 
I believe that we can be pretty sure that this provision imposing State laws and rules on federal prosecutors will be used to frustrate federal law simply by looking at the rules the State bars already have adopted that will have this effect. I believe this trend will only accelerate once those opposed to certain aspects of federal law know, as a result of our adoption of this provision, that they have this new tool at their disposal. """
 
sentences=nltk.sent_tokenize(paragraph)
words = nltk.word_tokenize(paragraph)

"""
remember that we did  these tokenizations even without the use of nltk library.
We can use the split() function for this as follows:

words_split = paragraph.split(" ")
print(words_split)
"""

#remove punctuation
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

result = tokenizer.tokenize(paragraph)
words_remove_punc=" ".join(result)


# Stemming
from nltk.stem import PorterStemmer
stemmer=PorterStemmer() 
 

stemmed_words = [stemmer.stem(word) for word in words]

# Lemmatize

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemma_words = [lemmatizer.lemmatize(word) for word in words]


nltk.download('stopwords')
from nltk.corpus import stopwords
remove_stopwords = [word for word in words if word not in stopwords.words('english')]
#sentences = ' '.join(remove_stopwords)

#stopwords_spanish=nltk.corpus.stopwords.words('spanish')


