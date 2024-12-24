# Social Media API

## Project Description
The **Social Media API** simulates the core functionalities of a social media platform. It provides endpoints for user management, post creation and interaction, user relationships (following and followers), and a personalized user feed. The API is built following RESTful principles using Django and Django REST Framework (DRF).

## Features
### User Management
- User registration, authentication, and profile management.
- Secure user data with token-based authentication.

### Post Management
- Create, retrieve, update, and delete posts.
- Add media (optional) to posts.

### Following System
- Follow and unfollow users.
- View followers and following lists.

### User Feed
- Retrieve posts from followed users in reverse chronological order.

### Notifications
- Receive updates about activities such as follows, likes, and comments.

### Messaging
- Send and receive messages between users.

## API Endpoints
### Users
- **POST /api/register/**: Register a new user.
- **POST /api/login/**: Login and get a JWT token.
- **GET /api/user/profile/**: View authenticated user's profile.
- **POST /api/logout/**: Logout and invalidate the token.

### Posts
- **POST /api/posts/**: Create a new post.
- **GET /api/posts/**: Retrieve all posts.
- **POST /api/posts/{post_id}/like/**: Like a specific post.
- **POST /api/posts/{post_id}/comment/**: Add a comment to a post.

### Follow System
- **POST /api/users/{user_id}/follow/**: Follow a user.
- **DELETE /api/users/{user_id}/unfollow/**: Unfollow a user.
- **GET /api/followers/**: List all followers.
- **GET /api/following/**: List all following users.

### Notifications
- **GET /api/notifications/**: View user notifications.

### Messaging
- **POST /api/messages/**: Send a message to another user.

## Technologies Used
- **Backend Framework**: Django
- **API Framework**: Django REST Framework (DRF)
- **Authentication**: DRF Token-based Authentication
- **Database**: SQLite (default) or PostgreSQL for production
- **Version Control**: Git and GitHub

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/project-name.git
   cd project-name
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Development Server:

bash
Copy code
python manage.py runserver
Test Endpoints: Use tools like Postman or cURL to interact with the API.

API Documentation
Refer to the API Documentation for detailed information about all endpoints.

Contribution Guidelines
Fork the repository.
Create a new branch for your feature/bug fix.
Commit your changes and push to your branch.
Create a pull request for review.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or support, feel free to contact:

Name: Abel Erduno Hakenso
Email: hakensoabel@gmail.com
markdown
Copy code

### Next Steps
- Replace `username/project-name` with the actual GitHub repository URL.
- Add any missing details, such as advanced setup instructions or deployment steps.
- Optionally create separate files for API documentation and a license. Let me know if you need templates for those!
