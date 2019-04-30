#download and manage data with pandas 

import pandas as pd
import os

#change to your own working directory
os.chdir("/Users/ariedamuco/Dropbox (CEU Econ)/TextAnalysisCEU")

data_first= pd.read_csv('Outputs/Barcelona_counter_freq.txt', delimiter=";") 

#with delimiter
data_first.describe()

#check the word with the highest frequency
data_first[data_first['count'] == 13]['word']

#sort the data
data_first= data_first.sort_values('count', ascending=False)
data_head= data_first.head()

#rename columns
new_cols = ["Most Frequent Word", "f2"]
data_head.columns = new_cols
#plot the most common words
fig=data_head.set_index("Most Frequent Word").f2.plot(kind='bar', colormap='PiYG').get_figure()
fig.savefig('Output/most_common.png')

#data_first['count'].hist()
#data_first['count'].min()
#data_first['count'].max()


#get the tables in a wikipedia article such as the Billboard Hot number one singles
data70=pd.read_html("https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1970s")
#get the third line of the data

data70=data70[2]

#explore the data
data70.head()
data70.tail()


# Select every row up to 1
data70=data70.iloc[1:]

# Select the second and third row
#data70.iloc[1:2]


#drop missing values
data70=data70.dropna()


#assign new names to columns

new_cols = ["ranked", "date_s","artist","single","weeks","ref"]
data70.columns = new_cols
data70['length'] = data70['single'].apply(len)


#explore only one variable

data70["artist"].head()
#two variables

data70[["artist", "weeks"]].head()

#count values
data70['length'].value_counts()



#Select a column
data70['artist']

data70.describe()

#data70.sort_values(by="artist")

#some summary statistics
data70["weeks"].mean()    

data70["length"].max()   


# select columns by name
data70.filter(items=['weeks']) 


#contains a certain name or variable
data70[data70['artist'].str.contains(r'Jackson')]


#frequency of how many times each artist appears
data70.artist.value_counts()
data70['artist'].value_counts()

#create a filtered dataset
#df_filtered = data70[data70['weeks'] == 4]

df_filtered = data70[data70['weeks'] == "4"]


#get data from other years
items = ['1980', '1990', '2000']
for item in items:
    data_name="data"+item
    text="https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the__"+item+"s"        
    data=pd.read_html(text)
    data=data[2]
    data=data.iloc[1:]
    new_cols = ["ranked", "date_s","artist","single","record_label", "weeks","ref"]
    data.columns = new_cols
    data=data.dropna()

    data70=data70.append(data)
  
       
#delete column we don't want     
del data70['ref']


#convert to numeric
data70['weeks'] = data70['weeks'].convert_objects(convert_numeric=True)


#or you could do
data70.ranked = data70.ranked.astype(float)


#generate the year number as a column
data70['year']=data70.date_s.str.replace(",", "").str.split(" ").str[2]

#fill missing values with zeros
#data70.ranked = data70.ranked.astype(float).fillna(0.0)

"""
#other example of dataset
players=pd.read_html("http://www.basketball-reference.com/awards/slam_500_greatest.html")
players=players[0]
"""
