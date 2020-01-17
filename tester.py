class bakery(): 
    def __init__(self, name):
        self.name = name
        self.cookies = 0
    def newCookie(self, flavor):
        cookie = Cookie(flavor)
        self.cookies += 1 
        return cookie
    def countCookies(self):
        print(self.cookies)

class Cookie():
    def __init__(self, flavor):
        self.flavor = flavor
    def getFlavor(self):
        return("Mmm... %s"%self.flavor)
