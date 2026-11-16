import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        # user_id -> list of (timestamp, tweet_id), most recent last
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        # user_id -> set of followed user_ids
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """User posts a new tweet."""
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Return the 10 most recent tweet IDs from the user and
        users they follow, ordered from most recent to least recent.
        """
        # Collect all relevant users (self + following)
        users = self.following[userId] | {userId}

        # Use a max-heap to merge tweets from all followed users
        # Python has a min-heap, so negate timestamps
        heap: list[tuple[int, int, int, int]] = []

        for uid in users:
            user_tweets = self.tweets[uid]
            if user_tweets:
                idx = len(user_tweets) - 1
                ts, tid = user_tweets[idx]
                # (neg_timestamp, tweet_id, user_id, index)
                heapq.heappush(heap, (-ts, tid, uid, idx))

        result: list[int] = []
        while heap and len(result) < 10:
            neg_ts, tid, uid, idx = heapq.heappop(heap)
            result.append(tid)

            # Push the next older tweet from this user
            if idx > 0:
                idx -= 1
                ts, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-ts, tid, uid, idx))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """Follower starts following followee."""
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Follower stops following followee."""
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)