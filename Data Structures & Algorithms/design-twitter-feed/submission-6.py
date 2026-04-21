class Twitter:

    def __init__(self):
        self.follows = {}
        self.posts = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        if userId in self.posts:
            tweets.extend(self.posts[userId])
        if userId in self.follows:
            for user in self.follows[userId]:
                if user in self.posts:
                    tweets.extend(self.posts[user])
        tweets = [(-index, value) for index, value in tweets]
        heapq.heapify(tweets)
        nlargest = heapq.nsmallest(10, tweets)
        print(nlargest)
        return [value for index, value in nlargest]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set([])
        if followerId == followeeId:
            return
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
