import praw
import time


YESTERDAY = time.time() - 86400  # 60*60*24 seconds before right now
search_term = 'i'


def main():

    r = praw.Reddit('orangebot')
    sub = r.subreddit('sailing')

    count = 0

    for post in get_todays(sub):
        for comment in post.comments.list():
            count += comment.body.count(search_term)

    print(count)


def get_todays(subreddit):
    result = []
    for post in subreddit.new(limit=None):
        if post.created_utc > YESTERDAY:
            result.append(post)
        else:
            continue
    return result

if __name__ == "__main__":
    main()
