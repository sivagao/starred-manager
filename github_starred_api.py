import pymongo
db = pymongo.MongoClient().github
# import github star repo script

from github import Github
g = Github('ghlndsl@126.com', '<password>')
u = g.get_usr()
a = u.get_starred()

def dictRepo(repo):
    f = repo
    return dict((name, getattr(f, name)) for name in dir(f) if not name.startswith('__'))
db.test.insert((dictRepo(i) for i in a))


# then cnfig eve to support restful api from mongodb