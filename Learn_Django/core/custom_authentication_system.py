from rest_framework.authentication import TokenAuthentication
from logging import Logger

logger = Logger('authentication')

class CustomTokenAuth(TokenAuthentication):
    def auth_using_cookies(self, req):
        cookies = req.COOKIES

        token = cookies['token']
        logger.info(f'Token: {token}')
        return self.authenticate_credentials(token)