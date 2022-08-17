from ._devstage_bridge import *

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sleekforum_db',
        'USER': 'sleekforum_user',
        'PASSWORD': 'sleekforum_password',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

COUNTRYLAYER_X_API_KEY = '6a164cdb3a16bcfda296865470089b7f'

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_AUTO_SIGNUP = True

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
        'APP': {
            'client_id': '422722b1aba578ef6b09',
            'secret': 'a8c478f14ac268d90376e649d5adf66870645e25'
        }
    },
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '703093368866-9v6u7govmij0ipauajtjv8a0h2i6v556.apps.googleusercontent.com',
            'secret': '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',
            'key': 'AIzaSyBw1HykUd4UShKsAxdefASiiawfooznCtk',
        },
        'SCOPE': [
            'profile',
            'email',
            'openid',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    }
}

ACCOUNT_AUTHENTICATION_METHOD = "username_email"

SOCIALACCOUNT_FORMS = {
    'signup': 'sleekapps.allauth.forms.socialaccount.SignupForm'
}
