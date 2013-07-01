#
# Errors as shown on Last.fm API pages.
#
# 2 : Invalid service - This service does not exist
# 3 : Invalid Method - No method with that name in this package
# 4 : Authentication Failed - You do not have permissions to access the service
# 5 : Invalid format - This service doesn't exist in that format
# 6 : Invalid parameters - Your request is missing a required parameter
# 7 : Invalid resource specified
# 8 : Operation failed - Something else went wrong
# 9 : Invalid session key - Please re-authenticate
# 10 : Invalid API key - You must be granted a valid key by last.fm
# 11 : Service Offline - This service is temporarily offline. Try again later.
# 12 : Subscribers Only - This station is only available to paid last.fm subscribers
# 13 : Invalid method signature supplied
# 14 : This token has not been authorized
# 15 : This token has expired
# 16 : There was a temporary error processing your request. Please try again
# 18 : Trial Expired - This user has no free radio plays left. Subscription required
# 20 : Not Enough Content - There is not enough content to play this station
# 21 : Not Enough Members - This group does not have enough members for radio
# 22 : Not Enough Fans - This artist does not have enough fans for for radio
# 23 : Not Enough Neighbours - There are not enough neighbours for radio
# 26 : Suspended API key - Access for your account has been suspended, please contact Last.fm
# 27 : Deprecated - This station is no longer available
# 28 : Geo Restricted - This station is not available with this client/country combination
# 29 : Rate limit exceeded - Your IP has made too many requests in a short period
#


class RequestError(Exception):
    pass

class InvalidService(RequestError):
    pass

class InvalidMethod(RequestError):
    pass

class AuthenticationFailed(RequestError):
    pass

class InvalidFormat(RequestError):
    pass

class InvalidParameters(RequestError):
    pass

class InvalidResourceSpecified(RequestError):
    pass

class OperationFailed(RequestError):
    pass

class InvalidSessionKey(RequestError):
    pass

class InvalidApiKey(RequestError):
    pass

class ServiceOffline(RequestError):
    pass

class SubscribersOnly(RequestError):
    pass

class InvalidMethodSignature(RequestError):
    pass

class TokenNotAuthorized(RequestError):
    pass

class TokenExpired(RequestError):
    pass

class TemporaryError(RequestError):
    pass

class TrialExpired(RequestError):
    pass

class NotEnoughContent(RequestError):
    pass

class NotEnoughMembers(RequestError):
    pass

class NotEnoughFans(RequestError):
    pass

class NotEnoughNeighbours(RequestError):
    pass

class SuspendedApiKey(RequestError):
    pass

class StationDeprecated(RequestError):
    pass

class GeoRestricted(RequestError):
    pass

class RateLimitExceeded(RequestError):
    pass


codes = {
        2: InvalidService, 
        3: InvalidMethod,
        4: AuthenticationFailed,
        5: InvalidFormat,
        6: InvalidParameters,
        7: InvalidResourceSpecified,
        8: OperationFailed,
        9: InvalidSessionKey,
        10: InvalidApiKey,
        11: ServiceOffline,
        12: SubscribersOnly,
        13: InvalidMethodSignature,
        14: TokenNotAuthorized,
        15: TokenExpired,
        16: TemporaryError,
        18: TrialExpired,
        20: NotEnoughContent,
        21: NotEnoughMembers,
        22: NotEnoughFans,
        23: NotEnoughNeighbours,
        26: SuspendedApiKey,
        27: StationDeprecated,
        28: GeoRestricted,
        29: RateLimitExceeded,
        }
