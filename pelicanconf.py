AUTHOR = 'Rushi Agrawal'
SITENAME = 'Sense, and Simplicity'
TIMEZONE = 'Asia/Kolkata'


# Alchemy theme options
PAGES_ON_MENU=True
SITE_SUBTEXT="On interactions between softwares and humans. Rushi Agrawal's blog."
GITHUB_ADDRESS = 'https://github.com/rushiagr'
TWITTER_ADDRESS = 'https://twitter.com/rushiagr'
DEFAULT_PAGINATION = 10


# Comment the following line to generate locally-viewable blog. Run
# 'python3 -m http.server' to view the blog at localhost:8000
SITEURL = 'http://rushiagr.github.io'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

FEED_DOMAIN = 'http://rushiagr.github.io'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

GITHUB_USER = 'rushiagr'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

GOOGLE_ANALYTICS = 'UA-37074962-1'
GOOGLE_ANALYTICS_ID = 'UA-37074962-1'

DISQUS_SITENAME = 'rushiagr'

SEARCHBOX = True

TWITTER_USER = 'rushiagr'
TWITTER_TWEET_BUTTON = True
GOOGLE_PLUS_ONE = True
FACEBOOK_LIKE = True

SOCIAL = (('twitter', 'http://twitter.com/rushiagr'),
          ('github', 'http://github.com/rushiagr'),
         )

STATIC_PATHS = [
    'test',
    ]
