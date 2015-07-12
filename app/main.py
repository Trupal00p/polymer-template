from rest_gae import RESTHandler, PERMISSION_ANYONE, PERMISSION_LOGGED_IN_USER, PERMISSION_OWNER_USER, PERMISSION_ADMIN
from rest_gae.users import UserRESTHandler
import webapp2
import data

config = {
    'webapp2_extras.auth': {
        'user_model': 'data.User',
        'user_attributes': [
            'email',
            'is_admin',
        ]
    },
    'webapp2_extras.sessions': {
        'secret_key': '6&kf5f6M9fb6e2jpc$RXQouhx@n6X7j^xJDji*Lk'
    }
}

app = webapp2.WSGIApplication([
    # Wraps MyModel with full REST API (GET/POST/PUT/DELETE)
    RESTHandler(
        '/api/mymodel',  # The base URL for this model's endpoints
        data.MyModel,  # The model to wrap
        permissions={
            'GET': PERMISSION_OWNER_USER,
            'POST': PERMISSION_LOGGED_IN_USER,
            'PUT': PERMISSION_OWNER_USER,
            'DELETE': PERMISSION_OWNER_USER
        },

        # Will be called for every PUT, right before the model is saved (also
        # supports callbacks for GET/POST/DELETE)
        put_callback=lambda model, data: model
    ),

    # Optional REST API for user management
    UserRESTHandler(
        '/api/users',
        # You can extend it with your own custom user class
        user_model=data.User,
        user_details_permission=PERMISSION_OWNER_USER,
        verify_email_address=True,
        verification_email={
            'sender': 'John Doe <john@doe.com>',
            'subject': 'Verify your email address',
            'body_text': 'Click here {{ user.full_name }}: {{ verification_url }}',
            'body_html': '<a href="{{ verification_url }}">Click here</a> {{ user.full_name }}'
        },
        verification_successful_url='/verification_successful',
        verification_failed_url='/verification_failed',
        reset_password_url='/reset_password',
        reset_password_email={
            'sender': 'John Doe <john@doe.com>',
            'subject': 'Please reset your password',
            'body_text': 'Reset here: {{ verification_url }}',
            'body_html': '<a href="{{ verification_url }}">Click here</a> to reset'
        },
    )
], debug=True, config=config)
