import pytumblr
from BeautifulSoup import BeautifulSoup 
Soup = BeautifulSoup
import random
from time import sleep
import sys
import urllib
import re
import chopper_class

# enter your Tumblr API credentials below
client = pytumblr.TumblrRestClient(
    '<consumer_key>',
    '<consumer_secret>',
    '<oauth_token>',
    '<oauth_secret>',
)

urls = list()
lyrics_list = list()
url_file = open("urls.txt")

# create fake user agent with urllib
class FakeMozillaOpener(urllib.FancyURLopener):
	version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31'
urllib._urlopener = FakeMozillaOpener()


for line in url_file:
	line = line.strip()
	urls.append(line)

# loop through list of urls in urls.txt, scape each page, put lyrics in 'content'

for url in urls:
	data = urllib.urlopen(url).read()
	soup = Soup(data)
	content = soup.find('div', attrs={'class': 'lyrics'})
	if content is None:
		continue
	for a_tag in content.findAll('a', attrs={'href': True, 'class': True}):
		lyric = str(a_tag.string).strip()  
		if lyric not in lyrics_list: 
			lyrics_list.append(lyric)
	sleep(1.0)

# use the chopper_class module to grep lines containing the keyword, randomize them and generate the poem

chopper = chopper_class.Chopper(keyword="based")
chopper.chop_list(text=lyrics_list)
generate = chopper.gen(n=5)


#write the poem to a new tumblr post

client.create_text('based-poetry.tumblr.com', body=generate)
