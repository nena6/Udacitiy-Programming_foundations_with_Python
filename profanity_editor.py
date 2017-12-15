import urllib.request

from builtins import print


def read_text(file):
    quotes = open(file)
    content = quotes.read()
    quotes.close()
    print(content)
    check_profanity(content)


def check_profanity(text):
    #full_url = "http://www.wdylike.appspot.com/?q=" + text
    connection = urllib.request.urlopen("https://www.google.com")
    print(text)
    output = connection.read()
    print(output)


read_text(r"C:\Users\enevvid\Desktop\Self-learning\Projects\Udacity-Programming Foundations with Python\movie_quotes.txt")
