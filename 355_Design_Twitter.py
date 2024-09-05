class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.following[userId]
        followee_tweets = [self.tweets[follower] for follower in followers]
        followee_tweets.append(self.tweets[userId])
        feed = heapq.merge(*followee_tweets)
        return [tweet[1] for tweet in heapq.nlargest(10, feed)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
