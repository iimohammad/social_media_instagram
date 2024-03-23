import requests

# Assuming the ID of the post you want to like is 1
post_id = 1

# Define the URL for liking the post
url = f'http://127.0.0.1:8000/content/FollowingPosts/{post_id}/react/'

# Assuming you have an authentication token or session cookie to authenticate the request
headers = {
    'Authorization': '485623930fe785e472a21a2d9911e0e5ce4159c3',  # Replace with your actual token
    # Other headers if required (e.g., content type)
}

# Assuming the API expects a POST request with certain data to indicate a like
data = {
    'reaction_type': 'like',  # This might vary based on your API design
}

# Send the POST request to like the post
response = requests.post(url, headers=headers, data=data)

# Check the response
if response.status_code == 200:
    print("Post liked successfully!")
else:
    print(f"Failed to like post. Status code: {response.status_code}, Response: {response.text}")
