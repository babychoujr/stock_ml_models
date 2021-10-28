import requests

### get keys from twitter/ stock market websites
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKfIVAEAAAAAlqx5hk3BXvnfaQg1BTfrN2f5oO4%3DEFya4NBhHbz8sxjc1U3Xm6IS4TsslJkv32dqHaw7CpzHbS3C43'

params = {
    'q': 'tesla',
    'tweet_mode': 'extended',
    'lang': 'en',
    'count': '100'
}

response = requests.get(
    'https://api.twitter.com/1.1/search/tweets.json?q=tesla',
    params = params,
    headers={
        'authorization': 'Bearer '+BEARER_TOKEN
})
tweet = response.json()
print(response.json())