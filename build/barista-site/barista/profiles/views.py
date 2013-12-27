from urllib import urlencode
from uuid import uuid4
from django.contrib.sites.models import get_current_site
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.views.generic import View
import requests

from barista.profiles.constants import SESSION_STATE_KEY, FACEBOOK_APPLICATION_ID, FACEBOOK_APPLICATION_SECRET, FACEBOOK_ACCESS_RESOURCE, FACEBOOK_USER_INFO_RESOURCE
from barista.profiles.models import ConnectedAccount


class WebLoginFacebookView(View):
    """
    Login view for Facebook
    """

    def get(self, request):
        """
        Directs the flow in 3 directions;
            1. Ask the user for permission
                2. Acquire permission and do additional work on login_with_facebook_auth
                3. Get denied permission and redirect back to the original url
        """
        if request.GET.get('error'):
            # return to next_url without vote
            HttpResponseRedirect('ERROR')
        if request.GET.get('code'):
            return self.login_with_facebook_auth(request)
        else:
            return self.login_via_facebook(request)

    def login_via_facebook(self, request):
        """
        Ask the user for permission and go to login_via_facebook_auth
        """
        state_key = request.session.get(SESSION_STATE_KEY)
        if state_key is None:
            state_key = uuid4().hex
            request.session[SESSION_STATE_KEY] = state_key
        site = get_current_site(request)
        redirect_uri = "http://%s%s" % (site, reverse("web_login_facebook"))
        url_params = {'app_id' : FACEBOOK_APPLICATION_ID,
                      'redirect_uri' : redirect_uri,
                      'state': state_key,
                      # 'scope': 'email',
                      }
        facebook_login_url = 'https://www.facebook.com/dialog/oauth?' + urlencode(url_params)
        return HttpResponseRedirect(facebook_login_url)

    def login_with_facebook_auth(self, request):
        """
        Check if the token is fresh, if not re-acquire it.
        Then get access token and enter user into model with ConnectedAccount
        """
        if request.session.get(SESSION_STATE_KEY) != request.GET.get('state'):
            return HttpResponseRedirect(reverse('web_login')+("?error=There was a problem authenticating you. Please connect with Facebook or Twitter to vote."))
        site = get_current_site(request)
        redirect_uri = "http://%s%s" % (site, reverse("web_login_facebook"))
        facebook_code_response = QueryDict.dict(request.GET).get('code')
        access_token_params = { 'client_id' : FACEBOOK_APPLICATION_ID,
                                'redirect_uri' : redirect_uri,
                                'client_secret' : FACEBOOK_APPLICATION_SECRET,
                                'code' : facebook_code_response,
                                }
       # Get Access from facebook to reach user data
        facebook_access_token_resource = FACEBOOK_ACCESS_RESOURCE + '?' + urlencode(access_token_params)
        user_access_token = requests.get(facebook_access_token_resource)

        # create a dictionary of user info
        response_dict = {}
        if user_access_token.status_code == 200:
            response_list = user_access_token.content.split('&')
            # decoded_response_url = urlparse.parse_qs(twitter_user_access_info.content)
            # The above line is also usable, it creates the same thing that the below 2 lines do. Maybe faster
            for item in response_list:
                key = item.split('=')[0]
                value = item.split('=')[1]
                response_dict[key] = value
        elif user_access_token.status_code == 400:
            # If the token has expired then the user will be prompted to authorize again and
            # therefore forcing a new token to be created.
            return self.login_via_facebook(request)

        facebook_user_info=requests.get(FACEBOOK_USER_INFO_RESOURCE + '?' + user_access_token.content)

        name = facebook_user_info.json().get('name').split()
        user_defaults = {'name': name
                         }
        try:
            user = ConnectedAccount.objects.get(identifier=facebook_user_info.json()['id'])
        except:
            user = None
        if user is None:
            # Ask facebook for user data to create a new user
            user, user_is_created = ConnectedAccount.objects.get_or_create(identifier=facebook_user_info.json()['id'],
                                                                  defaults=user_defaults)
        request.session['user_id'] = user.id
        return HttpResponseRedirect(reverse("home"))
