from httpx2_auth._authentication import (
    Basic,
    HeaderApiKey,
    QueryApiKey,
    SupportMultiAuth,
)
from httpx2_auth._aws import AWS4Auth
from httpx2_auth._errors import (
    AuthenticationFailed,
    GrantNotProvided,
    HttpxAuthException,
    InvalidGrantRequest,
    InvalidToken,
    StateNotProvided,
    TimeoutOccurred,
    TokenExpiryNotProvided,
)
from httpx2_auth._oauth2.authorization_code import (
    OAuth2AuthorizationCode,
    OktaAuthorizationCode,
    WakaTimeAuthorizationCode,
)
from httpx2_auth._oauth2.authorization_code_pkce import (
    OAuth2AuthorizationCodePKCE,
    OktaAuthorizationCodePKCE,
)
from httpx2_auth._oauth2.browser import DisplaySettings
from httpx2_auth._oauth2.client_credentials import (
    OAuth2ClientCredentials,
    OktaClientCredentials,
)
from httpx2_auth._oauth2.common import OAuth2
from httpx2_auth._oauth2.implicit import (
    AzureActiveDirectoryImplicit,
    AzureActiveDirectoryImplicitIdToken,
    OAuth2Implicit,
    OktaImplicit,
    OktaImplicitIdToken,
)
from httpx2_auth._oauth2.resource_owner_password import (
    OAuth2ResourceOwnerPasswordCredentials,
    OktaResourceOwnerPasswordCredentials,
)
from httpx2_auth._oauth2.tokens import JsonTokenFileCache, TokenMemoryCache

__all__ = [
    "AWS4Auth",
    "AuthenticationFailed",
    "AzureActiveDirectoryImplicit",
    "AzureActiveDirectoryImplicitIdToken",
    "Basic",
    "DisplaySettings",
    "GrantNotProvided",
    "HeaderApiKey",
    "HttpxAuthException",
    "InvalidGrantRequest",
    "InvalidToken",
    "JsonTokenFileCache",
    "OAuth2",
    "OAuth2AuthorizationCode",
    "OAuth2AuthorizationCodePKCE",
    "OAuth2ClientCredentials",
    "OAuth2Implicit",
    "OAuth2ResourceOwnerPasswordCredentials",
    "OktaAuthorizationCode",
    "OktaAuthorizationCodePKCE",
    "OktaClientCredentials",
    "OktaImplicit",
    "OktaImplicitIdToken",
    "OktaResourceOwnerPasswordCredentials",
    "QueryApiKey",
    "StateNotProvided",
    "SupportMultiAuth",
    "TimeoutOccurred",
    "TokenExpiryNotProvided",
    "TokenMemoryCache",
    "WakaTimeAuthorizationCode",
    "__version__",
]

# Version number as Major.Minor.Patch
# The version modification must respect the following rules:
# Major should be incremented in case there is a breaking change. (eg: 2.5.8 -> 3.0.0)
# Minor should be incremented in case there is an enhancement. (eg: 2.5.8 -> 2.6.0)
# Patch should be incremented in case there is a bug fix. (eg: 2.5.8 -> 2.5.9)
# NOTE: Using major version 2 as of releasing `httpx2-auth`.
__version__ = "2.0.0"
