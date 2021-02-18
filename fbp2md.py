#!/usr/bin/env python3

# Import Beautiful soup and open Facebook posts file
from bs4 import BeautifulSoup
import datetime
import re
import os
import shutil

hugo_dir = "/home/jack/bjfc"
facebook_dir = "/home/jack/code/projects/bjfc"
os.mkdir(hugo_dir + "/content/post")
# hugo_dir = "/PATH/TO/HUGO/DIRECTORY"
# facebook_dir = "/PATH/TO/FACEBOOK/EXPORT/DATA"

if hugo_dir == "/PATH/TO/HUGO/DIRECTORY":
    print("Please change your Hugo directory in fbp2md.py")
    exit()
if facebook_dir == "/PATH/TO/FACEBOOK/EXPORT/DATA":
    print("Please change your Facebook directory in fbp2md.py")
    exit()

today = datetime.date.today()
mention = re.compile("@\[(\d+):(\d+):([a-zA-Z0-9_ \-]*)\]")
pattern = r"\3"
post_number = 0

def write_post(post_number, filename, title, date, figure, contents):
    with open(filename, 'a') as file_object:
        file_object.write("+++" + "\n")
        file_object.write('title = "' + title + '"' + "\n")
        file_object.write('publishDate = ' + date)
        file_object.write("\n")
        file_object.write("draft = false" + "\n")
        file_object.write("+++" + "\n" + "\n")
        if figure is not None:
            file_object.write(figure)
        if contents is not None:
            file_object.write(contents)
        print(filename)

# This produces an albums.md file with links to all the albums
def write_album_post(post_number):
    date = str(today)
    filename = hugo_dir + "/content/post/albums.md"
    title = 'Albums' + '"\nmenu = "main'
    figure = None
    contents = ""
    write_post(post_number, filename, title, date, figure, contents)

# Format timeline
def format_timeline(post_number, soup, rel, title, figure, contents):
    posts = soup.find_all(class_="pam _3-95 _2pi0 _2lej uiBoxWhite noborder")
    for post in posts:
        post_number += 1
        filename = hugo_dir + rel + str(post_number) + '.md'
        if post.find("video") is not None:
            filename = hugo_dir + "/content/post/video/post" + str(post_number) + '.md'

        if post.find("img") is not None:
            figure = ""
            images = post.find_all('img')
            for image in images:
                img = image['src']
                figure += '{{< figure src="/images/' + str(img) + '" >}}\n'
        else:
            figure = ""

        # The timeline post uses the class "_2pin" to show files including line breaks
        # In album files the only class is "_3-95"
        # In this section, the code formats the text nicely by introducing line breaks and replacing @ symbols
        if post.find("div", {"class": "_3-95"}) is not None:
            u = post.find_all("div", {"class": "_3-95"})[-1]
            u2 = u.getText()
            uu = re.sub("  ", "\n\n", u2)
            contents = re.sub(mention, pattern, uu)
        else:
            u = ""

        dd = post.find(class_="_3-94 _2lem").text
        d = datetime.datetime.strptime(dd, '%d %b %Y, %H:%M')
        date = d.strftime('%Y-%m-%d')
        write_post(post_number, filename, title, date, figure, contents)


def format_album(post_number, soup, figure, contents):
    title = soup.find("title").text
    if title == "Timeline Photos":
        pass
    else:
        figure = None
        contents = None
        out_dir = title.replace(" ", "_").lower()
        rel = "/content/" + out_dir + "/post"
        full_path = hugo_dir + "/content/" + out_dir
        os.mkdir(full_path)
        album_file = hugo_dir + "/content/post/albums.md"
        with open(album_file, 'a') as file_object:
            file_object.write('[' + title + ']({{< ref "/' + out_dir + '" >}} "' + title + '")\n')
            file_object.write('\n')
        format_timeline(post_number, soup, rel, title, figure, contents)

fb = facebook_dir + "/posts/posts_1.html"
rel = "/content/post/post"
title = "TITLE"
figure = ""
contents = ""
soup = BeautifulSoup (open(fb), features="lxml")
os.mkdir(hugo_dir + "/content/post/video")
format_timeline(post_number, soup, rel, title, figure, contents)

write_album_post(post_number)

fb = facebook_dir + "/photos_and_videos/album"
post_number = 0
for album in os.listdir(fb):
    if album.endswith(".html"):
        soup = BeautifulSoup (open(fb + "/" + album), features="lxml")
        format_album(post_number, soup, figure, contents)

print("Conversion completed")
