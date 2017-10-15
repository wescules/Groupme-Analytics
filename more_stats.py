import json, re, collections, sys
from collections import defaultdict


# Changes the ordering of the output, 
# e.g. from alphabetical order to likes
by_2nd = lambda x: x[-1]

def num_images(data):
    """
    Prints the total number of images sent to the group
    Note: only counts attached images in its current state
    """
    num_images = sum(msg['picture_url'] is not None for msg in data)
    print("{} images".format(num_images))

def num_images_by_user(data, sorting='name', reverse=False):
    """
    Prints the number of images each user has sent
    
    Keywork arguments:
    sorting -- how the output should be sorted (default by name)
    reverse -- reverse the ordering (default False)
    """
    d = defaultdict(int)
    for msg in data:
        if msg['picture_url'] is not None:
            d[msg['name']] += 1
    if sorting == 'likes':
        print("{}".format(str(sorted(d.items(), key=by_2nd, reverse=reverse))))
    else:
        print("{}".format(str(sorted(d.items(), reverse=reverse))))

def msgs_by_likes(data):
    """Prints the number of posts that have a number of likes (0, 1, ...)"""
    d = defaultdict(int)
    for msg in data:
        d[len(msg['favorited_by'])] += 1
    print(sorted(d.items()))

def likes_received(data, sorting='name', reverse=False, ignore_self=False):
    """
    Prints the number of likes each user has received
    
    Keyword arguments:
    sorting -- how the output should be sorted (default by name)
    reverse -- reverse the ordering (default False)
    ignore_self -- ignore self likes (default False)
    """
    d = defaultdict(int)
    for msg in data:
        d[msg['name']] += len(msg['favorited_by'])
    if sorting == 'likes':
        print("{}".format(str(sorted(d.items(), key=by_2nd, reverse=reverse))))
    else:
        print("{}".format(str(sorted(d.items(), reverse=reverse))))

def likes_per_message(data, sorting='name', reverse=False, ignore_self=False):
    """
    Prints user, total likes received, total messages sent, 
    and ratio of likes to messages
    
    Keyword arguments:
    sorting -- how the output should be sorted (default by name)
    reverse -- reverse the ordering (default False)
    ignore_self -- ignore self likes (default False)
    """
    likes = defaultdict(int)
    msgs  = defaultdict(int)
    for msg in data:
        likes[msg['name']] += len(msg['favorited_by'])
        if ignore_self:
            if msg['name'] in msg['favorited_by']:
                likes[msg['name']] -= 1
        msgs[msg['name']] += 1

    print("Username\tLikes\tMessages\tRatio")
    for x in zip(sorted(likes.items()), sorted(msgs.items())):
        print("{}\t{}\t{}\t{}".format(x[0][0], x[0][1], x[1][1], x[0][1]/x[1][1]))


def set_of_ids(data):
    """
    Returns a set of all user ids
    Will be useful for relating messages to ids rather than names, 
    which users can change on a whim
    """
    s = set()
    for message in data:
        if message['user_id'] not in s:
            s.add(message['user_id'])
    return s

def num_messages(data):
    """Returns the total number of messages sent to the group"""
    return len(data)

def main():
    """
    Main program
    
    Reads a filename from standard input, opens it, and does analysis 
    on the contents
    """
    
    #funcs = ['num_images', 'num_images_by_user', 'likes_received', 
    #         'likes_per_message', 'set_of_ids', 'num_messages']
    
    with open('temp-transcript-21636980.json') as data_file:    
        data = json.load(data_file)
    pprint(data)
   
        
if __name__ == "__main__":
    main()
    sys.exit(0)
