
import twitter


TWITTER_CONSUMER_KEY = '3FfZwcDPP3c4cenLoITvGZTkV'
TWITTER_CONSUMER_SECRET = '5PvcbZp16IKQsw548CssRRdmtWfwoKlqm1cmJZnroAyhGkXzvM'
TWITTER_ACCESS_TOKEN_KEY = '427131356-hvRXLoZXLPItSRX4Sb7WvkzBjFbznHkURUTVL68N'
TWITTER_ACCESS_TOKEN_SECRET = 'bBeWyuTd65zfsodlBLMAE7bIRGzGr0ShnIXF04BoB0WHY'

twitter_api = twitter.Api(
    consumer_key=TWITTER_CONSUMER_KEY,
    consumer_secret=TWITTER_CONSUMER_SECRET,
    access_token_key=TWITTER_ACCESS_TOKEN_KEY,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

if __name__ == '__main__':
    follower_ids = twitter_api.GetFollowerIDs()
    print follower_ids
    print "*************"
    following_ids = twitter_api.GetFriendIDs()
    friends =twitter_api.GetFriends()
    print([u.name for u in friends])
    print "************"
    print following_ids
    print(twitter_api.VerifyCredentials())
    zombie_follows = [following_id for following_id in
                      following_ids if following_id not in follower_ids]

    confirm = raw_input(
        "Are you sure you want to unfollow {0} tweeps [y|n]? ".format(
            (len(zombie_follows))))
    if confirm.lower() == 'y':
        for id in zombie_follows:
            user = twitter_api.DestroyFriendship(user_id=id)
            print("Unfollowed {0}".format(user.screen_name))