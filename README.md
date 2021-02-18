# fbp2my

fbp2md is a tool for converting an export of a Facebook Page from HTML files into markdown files ready to be used with a static site generator.
This tool was designed to be used with hugo as a static site generator, but it should be possible to support other file structures.

The "p" in fbp2md stands for page as this script is specifically designed for public pages, i.e it's not designed for personal profiles.
If you're interested in that check out [ditchbook](https://github.com/cleverdevil/ditchbook).
It is also a python script that converts an exported personal profile froma JSON file to a micropub format.

# What is the point?

I ran a successful Facebook page for several years and my friends and I poured so much time and effort into the page, that when I deleted my Facebook account in 2018, it was the only thing I missed on the platform.

I wanted to set up a website with all the posts we made on Facebook.
Obviously, it will still need some manual work as short Facebook posts don't make good posts on an independent website.
A lot of the techniques we used to find our "reach" were used to manipulate Facebook's algorithm and have our posts shown to more people.

The ultimate reason, however, for me writing this short script is because I believe that a web without Facebook is a better web.
If people own their own content, they can still share the content to whatever platforms they want.

# Dependencies

- Python
- virtualenv (optional, but recommended)
  - BeautifulSoup4
  - lxml
- Hugo (or static site generator of your choice)

# How to use
Install hugo on your system following these [instructions ](https://gohugo.io/getting-started/quick-start/)

Clone this repository with the following command or by installing it manually and then open the directory.
``` sh
git clone https://github.com/jiewawa/fbp2md.git
cd fbp2md
```

Copy album directories from `facebook_dir/photos_and_videos` ignoring album, thumbnails and video directories

Paste into `hugo_dir/static/images/photos_and_videos`

Open `fbp2md.py` in the text editor of your choice

Change the `hugo_dir` and `facebook_dir` files near the top of the file

``` sh
virtualenv -p python3.9 venv
. venv/bin/activate
pip install BeautifulSoup4 lxml
python fbp2md.py
deactivate
```

# Future plans

I could probably and probably should add a way of automatically copying the image stucture over to the Hugo directory.
The reason that I didn't is that I downloaded and unzipped the archive I used as a template a long time ago and can't remember if I deleted anything.

I would like to add options for exporting to other static site generators.
I don't have experience with any others, but the metadata in the head of the markdown files should follow the same format, so the only thing that needs to change is directory structures.

There is probably a better way for me to handle video.
I decided that I didn't want to host it myself, and I didn't want to put them on Youtube, effectively moving between two platforms that I don't want to be involved in.

Rework this README file.
I can't remember reading many other README files written in the first person.

# Things I'm not sure about

The archive I downloaded from Facebook was downloaded over a year ago, so I'm not sure how much has changed.

I don't know if class references are consistent across all downloads, or if they have changed in the last year, or even if they are randomly generated.

# How can you help

If you have a Facebook page that you would like to host as its own website, you can try the script and let me know if everything works out.
The goal of this project was to let people get off Facebook, so if I can help even one person, I will have accomplished my goal.

This is my first time publishing code on the internet, and I'm sure that there are things I'm doing that are not best practices.
Feel free to look over the file and give feedback.
It's only 121 lines of code as of the time of writing.
