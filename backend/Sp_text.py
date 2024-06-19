import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import string
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi


def yt_transcript(url: str):
    # yt = YouTube(url)
    text = ''
    try:
        video_id = url.split("/")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        for i in transcript:
            text += ' ' + i['text']

    except Exception as e:
        print(f"An exception occurred: {e}")
        print("video too long!!!!")

    words = text.lower().split()
    # Convert the list of words to a tuple
    word_tuple = tuple(words)
    return word_tuple

# 1. main text matching

# def match_text(word_tuple):
#     search_text = word_tuple
#     count = 0
#     stop_words = set(stopwords.words('english'))
#     search_text = tuple(word for word in search_text if word not in stop_words)

#     grt_acc = 0
#     count = 0
#     # main_link = "https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=friends"
#     # response = requests.get(main_link)
#     # html_content = response.text
#     # soup = BeautifulSoup(html_content, 'html.parser')
#     # links = [a['href'] for a in soup.find_all('a', href=True)]

#     # for link in links:
#     #     if "friends" in link and "view_episode_scripts" in link:
#     #         link = "https://www.springfieldspringfield.co.uk/" + link
#     frS1_links = ["https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=07-ghost-2009&episode=s01e01","https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=friends&episode=s01e01","https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=big-bang-theory&episode=s01e07", "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=friends&episode=s01e03","https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=friends&episode=s01e02","https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=big-bang-theory&episode=s01e07", "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=big-bang-theory&episode=s01e01","https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=big-bang-theory&episode=s09e23"]
#     for link in frS1_links:
#         response = requests.get(link)
#         html_content = response.text

#             # Convert the HTML content to a single string
#         soup = BeautifulSoup(html_content, 'html.parser')
#         text = soup.get_text()
#         text_t = text.translate(str.maketrans("", "", string.punctuation))
#         words_t = text_t.lower().split()
#         word_tuple_t = tuple(words_t)
#         word_tuple_t = tuple(word for word in word_tuple_t if word not in stop_words)
#         matched = tuple(x for x in search_text if x in word_tuple_t)
#         count = count + 1
#         accuracy = (len(matched) / len(search_text)) * 100
#         if accuracy > grt_acc:
#             grt_acc = accuracy
#             max_link = link

#     if count == 0:
#         return "Could not find the search text."
#     else:
#         show, episode = get_show_and_episode(max_link)
#         # return f"Found the search text in:\n{show} - {episode}\nAccuracy: {grt_acc:.2f}%"
#         return show, episode


# 2. main text matching


def match_text(word_tuple):
    search_text = word_tuple
    count = 0
    stop_words = set(stopwords.words('english'))
    search_text = tuple(word for word in search_text if word not in stop_words)

    grt_acc = 0
    count = 0
    with open("@doctype.txt", "r") as f:
        for line in f:
            line = line.strip()  # remove the newline character at the end
            # do something with the link, e.g. print it
            response = requests.get(line)
            html_content = response.text
                # Convert the HTML content to a single string
            soup = BeautifulSoup(html_content, 'html.parser')
            text = soup.get_text()
            text_t = text.translate(str.maketrans("", "", string.punctuation))
            words_t = text_t.lower().split()
            word_tuple_t = tuple(words_t)
            word_tuple_t = tuple(word for word in word_tuple_t if word not in stop_words)
            matched = tuple(x for x in search_text if x in word_tuple_t)
            count = count + 1
            accuracy = (len(matched) / len(search_text)) * 100
            if accuracy > grt_acc:
                grt_acc = accuracy
                max_link = line

    if count == 0:
        return "No match could be found."
    else:
        show, episode = get_show_and_episode(max_link)
        # return f"Found the search text in:\n{show} - {episode}\nAccuracy: {grt_acc:.2f}%"
        return show, episode


# def get_show_and_episode(link):
#     parts = link.split("=")
#     show = parts[1].split("&")[0].replace("-", " ")
#     episode = parts[-1]
#     return show, episode

def get_show_and_episode(link):
    # import pdb
    # pdb.set_trace()
    parts = link.split("=")
    show = ''
    if len(parts) < 2:
        return None, None
    show = parts[1].split("&")[0]
    if len(parts) < 1:
        return show, None
    episode = parts[-1]
    return show, episode


