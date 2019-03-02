#!/usr/bin/env python3
import zlib
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import base64_decode, URLSafeTimedSerializer


class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
    # NOTE: Override method
    def get_signing_serializer(self, secret_key):
        signer_kwargs = {
            'key_derivation': self.key_derivation,
            'digest_method': self.digest_method
        }
        return URLSafeTimedSerializer(
            secret_key,
            salt=self.salt,
            serializer=self.serializer,
            signer_kwargs=signer_kwargs
        )


class FlaskSessionCookieManager:
    @classmethod
    def decode(cls, secret_key, cookie):
        sscsi = SimpleSecureCookieSessionInterface()
        signingSerializer = sscsi.get_signing_serializer(secret_key)
        return signingSerializer.loads(cookie)

    @classmethod
    def encode(cls, secret_key, session):
        sscsi = SimpleSecureCookieSessionInterface()
        signingSerializer = sscsi.get_signing_serializer(secret_key)
        return signingSerializer.dumps(session)


if __name__ == '__main__':
    secret_key = 'super-secret'
    cookie = 'eyJ1c2VybmFtZSI6ImFkbWluIn0.D1uQvg.w7LiHs3S_zjX-U-RaeUX9am5buI'
    print(FlaskSessionCookieManager.decode(secret_key, cookie))

    session = { 'username': 'admin' }
    print(FlaskSessionCookieManager.encode(secret_key, session))