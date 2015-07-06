from google.appengine.ext import ndb
from rest_gae.users import User


class MyUser(User):

    """Our own user class"""
    prop1 = ndb.StringProperty(required=True)
    prop2 = ndb.StringProperty()

    # This is optional, but if we use a RESTMeta - we must inherit it (and not
    # run over the original properties)
    class RESTMeta(User.RESTMeta):
        excluded_output_properties = User.RESTMeta.excluded_output_properties + \
            ['prop2']


class MyModel(ndb.Model):
    property1 = ndb.StringProperty()
    property2 = ndb.StringProperty()
    owner = ndb.KeyPropertyProperty(kind='User')

    class RESTMeta:
        # When a new instance is created, this property will be set to the
        # logged-in user
        user_owner_property = 'owner'
        # Only include these properties for output
        include_output_properties = ['property1']