# importing api 
from django.shortcuts import render 
from newsapi import NewsApiClient 

from django.conf import settings
from pprint import pprint
'''
Installation
$ pip install newsapi-python
Usage
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='API_KEY')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/sources
sources = newsapi.get_sources()

'''
# https://newsapi.org/docs/client-libraries/python
# Create your views here. 
def index(request): 
	
	newsapi = NewsApiClient(api_key =settings.API_KEY) 
	
	top_headlines = newsapi.get_top_headlines(sources ='bbc-news,the-verge,techcrunch') 
	
	all_articles = newsapi.get_everything(sources ='bbc-news,the-verge,techcrunch') 
	
	# /v2/sources
	sources = newsapi.get_sources()
	pprint(sources)

	l = top_headlines['articles'] 
	desc =[] 
	news =[] 
	img =[] 

	for i in range(len(l)): 
		f = l[i] 
		news.append(f['title']) 
		desc.append(f['description']) 
		img.append(f['urlToImage']) 
	mylist = zip(news, desc, img) 

	return render(request, 'index.html', context ={"mylist":mylist}) 
