class Twitter:
    def __init__(self):
        self.posts = {}
        self.followers = {}
        self.timeline = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[tweetId] = userId
        self.timeline.append(tweetId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        final = []
        if len(self.timeline) == 0:
            return []
        p = len(self.timeline) - 1
        while len(final) < 10 and p >= 0:
            post = self.timeline[p]
            poster = self.posts[post]

            #if following add to timeline
            if poster == userId:
                final.append(post)
            elif self.followers.get(userId) is not None and poster in self.followers[userId]:
                final.append(post)

            p-=1
        print(final)
        return final

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.followers:
            self.followers[followerId] = {followeeId}
        else:
            self.followers[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)
        
