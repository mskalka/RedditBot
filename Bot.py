import praw
import time


YESTERDAY = time.time() - 86400  # 60*60*24 seconds before right now
search_term = 'GGG'


def main():

    r = praw.Reddit('orangebot')
    sub = r.subreddit('pathofexile')

    count = 0

    for post in get_todays(sub):
        for comment in post.comments:
            if search_term in comment.body:
                count += 1

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
