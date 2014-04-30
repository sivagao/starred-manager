# Let's just use the local mongod instance. Edit as needed.
#
# # Please note that MONGO_HOST and MONGO_PORT could very well be left
# # out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'misc'

API_VERSION = 'v1'
URL_PREFIX = 'api'
DOMAIN = {
    'css_tricks_articles': {},
    'a_list_apart': {},
    'github_starred': {}
}

# ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

X_DOMAINS = '*'

PAGINATION = False
PAGINATION_LIMIT = 50
PAGINATION_DEFAULT = 25

CACHE_CONTROL = 'max-age=1000,must-revalidate'
CACHE_EXPIRES = 1000


