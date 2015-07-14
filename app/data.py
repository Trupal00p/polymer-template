from google.appengine.ext import ndb
from rest_gae.users import User as RESTUser


class User(RESTUser):

    """Our own user class"""
    organization = ndb.KeyProperty(kind='Organization')
    role = ndb.KeyProperty(kind='Role', repeated=True)

    # # This is optional, but if we use a RESTMeta - we must inherit it (and not
    # # run over the original properties)
    # class RESTMeta(RESTUser.RESTMeta):
    # When a new instance is created, this property will be set to the
    # logged-in user's organization if defined
    # user_organization_property = 'organization'
    # When a new instance is created, this property will be set to the
    # logged-in user's role if defined
    # user_role_property = 'role'


class Organization(ndb.Model):

    '''An organization grouping of users'''
    name = ndb.StringProperty()
    owner = ndb.KeyProperty(kind='User')

    class RESTMeta:
        # When a new instance is created, this property will be set to the
        # logged-in user
        user_owner_property = 'owner'


class Role(ndb.Model):

    '''A security role at an organization'''
    name = ndb.StringProperty()
    owner = ndb.KeyProperty(kind='User')
    organization = ndb.KeyProperty(kind='Organization')

    class RESTMeta:
        # When a new instance is created, this property will be set to the
        # logged-in user
        user_owner_property = 'owner'
        # When a new instance is created, this property will be set to the
        # logged-in user's organization if defined
        user_organization_property = 'organization'

        # excluded_output_properties = ['owner']


class MyModel(ndb.Model):
    property1 = ndb.StringProperty()
    property2 = ndb.StringProperty()
    owner = ndb.KeyProperty(kind='User')
    organization = ndb.KeyProperty(kind='Organization')
    role = ndb.KeyProperty(kind='Role', repeated=True)

    class RESTMeta:
        # When a new instance is created, this property will be set to the
        # logged-in user
        user_owner_property = 'owner'
        # When a new instance is created, this property will be set to the
        # logged-in user's organization if defined
        user_organization_property = 'organization'
        # When a new instance is created, this property will be set to the
        # logged-in user's role if defined
        user_role_property = 'role'
        # Only include these properties for output
        include_output_properties = ['property1']
