# join-channel-api

**How to run script**

> first download the files 
```
1. git clone https://github.com/Abbas-OR/join-channel-api.git
2. cd join-channel-api
3. nano page.py and go to 13 and 14 llne change (can open other code editors)
4. python3 page.py
```
**How can call the api**

> just requset to the your domain or api  like  this 
 
> http:// or https:// your domain or server ip :port /json?token=bot_token&channel=channel_id&user_id=user_id

> can use (@username or id) for channel

**code**
```
if status == 'join':
  print("hi welcome")
elif status == 'left':
  d = ['description'] #show  you reason
  print("you should join the channel")
  print(d)
elif status == 'error':
  print(" call to support for check the api " ) 
```
