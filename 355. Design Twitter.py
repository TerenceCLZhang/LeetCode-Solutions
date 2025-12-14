class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.following[userId].add(userId)
        for user in self.following[userId]:
            if user in self.user_tweets:
                index = len(self.user_tweets[user]) - 1
                time, tweet_id = self.user_tweets[user][index]
                heapq.heappush(heap, (time, tweet_id, user, index))

        while heap and len(res) < 10:
            _, tweet_id, user, index = heapq.heappop(heap)
            res.append(tweet_id)
            index -= 1
            if index >= 0:
                time, tweet_id = self.user_tweets[user][index]
                heapq.heappush(heap, (time, tweet_id, user, index))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
