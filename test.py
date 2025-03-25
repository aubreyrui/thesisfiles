from facebook_scraper import get_posts
import lxml

for post in get_posts('nintendo', pages=1):
     print(post['text'][:50])