#Based Poetry#

Based Poetry is a Python script for creating poems from lyrics scraped from the web and then posting them to a Tumblr account. To see it in action [visit the Based Poetry Tumblr blog](http://based-poetry.tumblr.com/). 

A few notes on how this works:

* The script is set up to scrape pages from *a certain rap lyrics website*, iterate through lines from those lyrics looking for a keyword (i.e. "based"), select a certain number of lines that contain that keyword (n=5) and then assemble them into a short poem that is then posted to Tumblr.

* To use this program, you'll need the [python-oauth2](https://github.com/simplegeo/python-oauth2) and [pytumblr](https://github.com/tumblr/pytumblr) modules.

* To post to a Tumblr account, you'll need to [register your app to use the Tumblr API](http://www.tumblr.com/docs/en/api/v2). You'll then need to go through the OAuth flow to grant your app credentials to post to your Tumblr blog. I used [this three-legged OAuth example](https://github.com/simplegeo/python-oauth2#twitter-three-legged-oauth-example) (just replac all the Twitter stuff with Tumblr stuff).

* Put the URLs of all the pages you want to scrape in url.txt, with each seperated by a line break.

* If you want to automate the app, you'll need to use something like a cron job. I simply deployed the app to Heroku and used [the Heroku scheduler](https://addons.heroku.com/scheduler) in order to schedule it to run daily.

Developed by [Mehan Jayasuriya](http://mehan.info) at [NYU ITP](http://itp.nyu.edu) in [Adam Parrish](http://www.decontextualize.com/)'s course "Reading and Writing Electronic Text". Based in part on [Adam's code examples](https://github.com/aparrish/rwet-examples) for the class. Shoutout to [the cat force](https://www.facebook.com/CatForceProtectLilBAndKekeAtAllCost), protect Lil B at all cost. 




