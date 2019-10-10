punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '–', '…', '-']

def strip_punctuation(x):
    for i in punctuation_chars:
        x = x.replace(i,"")
    return x

# list of positive words to use

positive_words = []

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(pos):
    count = 0
    for i in positive_words:
        if i in pos.split():
            count += 1
    return count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(neg):
    count = 0
    for i in negative_words:
        if i in neg.split():
            count += 1
    return count

def strip_punctuation(x):
    for i in punctuation_chars:
        x = x.replace(i," ")
    return x

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_pos(y):
    count = 0
    for i in y:
        if i in positive_words:
            count += 1
    return count

def get_neg(neg):
    count = 0
    for i in negative_words:
        if i in neg:
            count += 1
    return count

def classifier():
    with open("project_twitter_data.csv", "r") as source:
        retweets = []
        replies = []
        neg = []
        pos = []
        net = []

        for i in source.readlines():
            string = strip_punctuation(i).strip()
            word_lists = string.split()
            neg.append(get_neg(word_lists))
            pos.append(get_pos(word_lists))

            if word_lists[-2:-1][0] != "retweet_count":
                retweets.append(word_lists[-2:-1])

            if word_lists[-1:][0] != "reply_count":
                replies.append(word_lists[-1:])

        neg.remove(0)
        pos.remove(0)
        with open("resulting_data.csv","w") as result:
            result.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n'.format())
            j = 0
            for i in retweets:
                retweet = ''.join(i)
                reply = ''.join(replies[j])
                retweet = int(retweet)
                reply = int(reply)
                net = pos[j] + (-neg[j])
                result.write('{}, {}, {}, {}, {}\n'.format(retweet, reply, pos[j], neg[j], net))
                j+=1
        
classifier()
