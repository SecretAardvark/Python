#! python3

import webbrowser as wb

socials = [ "https://www.facebook.com/", 
 "https://www.reddit.com/",
"https://www.twitter.com/" ]

for site in socials:
    wb.open(site)
        