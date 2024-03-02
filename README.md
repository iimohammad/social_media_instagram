# Social Media Platform

This is a social media platform similar to Instagram, developed using Python frameworks for the backend. It allows users to share posts, stories, send direct messages, comment on posts, like posts, follow/unfollow other users, and view activity logs.

## Features

- **Content Management**: Users can share various types of content including images, videos, and text posts. Stories feature is also available.
- **User Area**: Users can have public or private profiles. They can register, login, edit their profile, view other profiles, follow/unfollow other users.
- **User Activities**: Users can interact with posts by commenting on them, liking them, or deleting their own comments. They can also delete their likes.
- **Logs**: Activity logs are automatically recorded including content viewed and profiles visited.
- **Direct Messaging**: Users can send text, audio, and image messages to each other.

## Models

The project includes the following models:

- **Users**: Stores information about users including their profiles, registration details, and authentication.
- **Posts**: Stores information about posts including images, videos, and text content along with details such as the user who posted it and the timestamp.
- **Stories**: Similar to posts but with a shorter lifespan, stories disappear after a certain period of time.
- **Comments**: Stores user comments on posts along with the post they're commenting on and the timestamp.
- **Logs**: Records user activities such as viewing content and visiting profiles.
- **Messages**: Stores direct messages between users, including text, audio, and image messages.

## Endpoints

The following endpoints are implemented:

- **Content**: 
  - Create post (single and multi-slide)
  - Mention users
  - Fetch posts from followed users
  
- **User Area**: 
  - User registration
  - User login
  - Edit profile
  - View profile
  - Follow/unfollow users
  
- **User Activities**: 
  - Comment on posts
  - Like posts
  - Unlike posts
  
- **Logs**: 
  - Automatically records content viewed and profiles visited
  
- **Direct Messaging**: 
  - Send messages
  - Receive messages

## Setup

To run this project locally, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure database settings in `settings.py`
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests if you have any suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).
