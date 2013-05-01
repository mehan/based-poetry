import pytumblr
from BeautifulSoup import BeautifulSoup 
Soup = BeautifulSoup
import random
from time import sleep
import sys
import urllib
import re
import chopper_class

<<<<<<< HEAD
# enter your Tumblr API credentials below
client = pytumblr.TumblrRestClient(
    '<consumer_key>',
    '<consumer_secret>',
    '<oauth_token>',
    '<oauth_secret>',
=======
client = pytumblr.TumblrRestClient(
    'XXX',
>>>>>>> bb9628afca4cef27678f06d5f169b36cae805a09
)

urls = list()
lyrics_list = list()
url_file = open("urls.txt")

<<<<<<< HEAD
# create fake user agent with urllib
class FakeMozillaOpener(urllib.FancyURLopener):
	version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31'
urllib._urlopener = FakeMozillaOpener()


=======
# here's how to fake a user agent string with urllib
class FakeMozillaOpener(urllib.FancyURLopener):
  version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31'
urllib._urlopener = FakeMozillaOpener()

>>>>>>> bb9628afca4cef27678f06d5f169b36cae805a09
for line in url_file:
	line = line.strip()
	urls.append(line)

<<<<<<< HEAD
# loop through list of urls in urls.txt, scape each page, put lyrics in 'content'
=======
# print urls	
>>>>>>> bb9628afca4cef27678f06d5f169b36cae805a09

for url in urls:
	data = urllib.urlopen(url).read()
	soup = Soup(data)
	content = soup.find('div', attrs={'class': 'lyrics'})
<<<<<<< HEAD
	if content is None:
		continue
	for a_tag in content.findAll('a', attrs={'href': True, 'class': True}):
		lyric = str(a_tag.string).strip()  
		if lyric not in lyrics_list: 
			lyrics_list.append(lyric)
	sleep(1.0)

# use the chopper_class module to grep lines containing the keyword, randomize them and generate the poem
=======


	for a_tag in content.findAll('a', attrs={'href': True, 'class': True}):
  		lyric = str(a_tag.string).strip()  
  		if lyric not in lyrics_list: 
 			lyrics_list.append(lyric)
 	sleep(1.0)

# print lyrics_list

>>>>>>> bb9628afca4cef27678f06d5f169b36cae805a09

chopper = chopper_class.Chopper(keyword="based")
chopper.chop_list(text=lyrics_list)
generate = chopper.gen(n=5)
<<<<<<< HEAD


#write the poem to a new tumblr post

client.create_text('based-poetry.tumblr.com', body=generate)
=======
# print generate

#create tumblr text post

client.create_text('based-poetry.tumblr.com', body=generate)
>>>>>>> bb9628afca4cef27678f06d5f169b36cae805a09
