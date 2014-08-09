AUTHOR = 'Rushi Agrawal'
SITENAME = 'Sense, and Simplicity'
TIMEZONE = 'Asia/Kolkata'

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

DISQUS_SITENAME = 'rushiagr'

SEARCHBOX = True

TWITTER_USER = 'reeshi_india'
TWITTER_TWEET_BUTTON = True
GOOGLE_PLUS_ONE = True
FACEBOOK_LIKE = True

SOCIAL = (('twitter', 'http://twitter.com/reeshi_india'),
          ('github', 'http://github.com/rushiagr'),
         )

STATIC_PATHS = [
    'test',
    ]
