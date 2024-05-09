import requests
import re

def count_words(subreddit, word_list, after=None, counter={}):
    if after is None and counter:
        sorted_words = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    response = requests.get(url, headers={"User-Agent": "Counting bot"})
    if response.status_code != 200:
        return

    data = response.json()
    for post in data["data"]["children"]:
        title = post["data"]["title"]
        for word in word_list:
            word = word.lower()
            pattern = r"\b" + re.escape(word) + r"\b"
            count = len(re.findall(pattern, title, re.IGNORECASE))
            if count > 0:
                counter[word] = counter.get(word, 0) + count

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counter)
count_words("learnprogramming", ["java", "javascript", "python"])
