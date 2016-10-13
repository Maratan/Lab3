from uid import *
from friends import *

user = GetID('faynky')
user_id = user.execute()

friends_client = GetFriends(user_id)
friends = friends_client.execute()

for (age, count) in friends:
    print('{} {}'.format(int(age), int(count)))
