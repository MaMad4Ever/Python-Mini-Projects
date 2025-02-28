import pyshorteners

link = "Paste your long link"

s = pyshorteners.Shortener()
short_url = s.tinyurl.short(link)
