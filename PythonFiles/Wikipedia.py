
#pip install Wikipedia

import wikipedia

wikipedia.set_lang("en")
wikipedia.search("Budapest")

BP = wikipedia.page('Budapest')
BP.title
BP.url

BP.links[0]

Barcelona=wikipedia.summary("Barcelona", sentences=10)

import re
regexp = re.compile(r'Founded(.*)tournaments')
matched=regexp.search(Barcelona)
if matched:
    print (matched.group())
  
  
section = wikipedia.WikipediaPage('Barcelona').section('Names')

content = wikipedia.WikipediaPage('Barcelona').content
content = content.replace('\n',' ').replace('\'',' ')

#https://pypi.org/project/wikipedia/
#https://medium.com/@Alexander_H/scraping-wikipedia-with-python-8000fc9c9e6c
#print(wikipedia.WikipediaPage(title = 'Metropolis (1927 film)').summary)