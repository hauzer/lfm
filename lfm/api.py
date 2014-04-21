import requests

from abc import ABCMeta, abstractmethod
from functools import wraps
import inspect
import xml.etree.ElementTree as XmlElementTree
import hashlib

import lfm.info as info


USER_AGENT  = "{}/{}".format(info.NAME, info.VERSION)

ROOT                    = "https://ws.audioscrobbler.com/2.0/"
REQUEST_RATE_PERIOD     = 300
REQUEST_RATE_INTERVAL   = 5
MAX_REQUESTS            = REQUEST_RATE_PERIOD / REQUEST_RATE_INTERVAL
MAX_USERNAME_LENGTH     = 15

KEY     = "312a23775128fd0f9a6d8d3e7a87a4b4"
SECRET  = "d03bece4e91f9a25b0b2b78c75c7c327"


# Errors as shown across Last.fm API pages
class RequestError(Exception): pass
class InvalidServiceError(RequestError): pass
class InvalidMethodError(RequestError): pass
class AuthenticationFailedError(RequestError): pass
class InvalidFormatError(RequestError): pass
class InvalidParametersError(RequestError): pass
class InvalidResourceSpecifiedError(RequestError): pass
class OperationFailedError(RequestError): pass
class InvalidSessionKeyError(RequestError): pass
class InvalidApiKeyError(RequestError): pass
class ServiceOfflineError(RequestError): pass
class SubscribersOnlyError(RequestError): pass
class InvalidMethodSignatureError(RequestError): pass
class TokenNotAuthorizedError(RequestError): pass
class TokenExpiredError(RequestError): pass
class TemporaryErrorError(RequestError): pass
class TrialExpiredError(RequestError): pass
class NotEnoughContentError(RequestError): pass
class NotEnoughMembersError(RequestError): pass
class NotEnoughFansError(RequestError): pass
class NotEnoughNeighboursError(RequestError): pass
class SuspendedApiKeyError(RequestError): pass
class StationDeprecatedError(RequestError): pass
class GeoRestrictedError(RequestError): pass
class RateLimitExceededError(RequestError): pass

error_codes = {
    2: InvalidServiceError,              # 2 : Invalid service - This service does not exist
    3: InvalidMethodError,               # 3 : Invalid Method - No method with that name in this package
    4: AuthenticationFailedError,        # 4 : Authentication Failed - You do not have permissions to access the service
    5: InvalidFormatError,               # 5 : Invalid format - This service doesn't exist in that format
    6: InvalidParametersError,           # 6 : Invalid parameters - Your request is missing a required parameter
    7: InvalidResourceSpecifiedError,    # 7 : Invalid resource specified
    8: OperationFailedError,             # 8 : Operation failed - Something else went wrong
    9: InvalidSessionKeyError,           # 9 : Invalid session key - Please re-authenticate
    10: InvalidApiKeyError,              # 10 : Invalid API key - You must be granted a valid key by last.fm
    11: ServiceOfflineError,             # 11 : Service Offline - This service is temporarily offline. Try again later.
    12: SubscribersOnlyError,            # 12 : Subscribers Only - This station is only available to paid last.fm subscribers
    13: InvalidMethodSignatureError,     # 13 : Invalid method signature supplied
    14: TokenNotAuthorizedError,         # 14 : This token has not been authorized
    15: TokenExpiredError,               # 15 : This token has expired
    16: TemporaryErrorError,             # 16 : There was a temporary error processing your request. Please try again
    18: TrialExpiredError,               # 18 : Trial Expired - This user has no free radio plays left. Subscription required
    20: NotEnoughContentError,           # 20 : Not Enough Content - There is not enough content to play this station
    21: NotEnoughMembersError,           # 21 : Not Enough Members - This group does not have enough members for radio
    22: NotEnoughFansError,              # 22 : Not Enough Fans - This artist does not have enough fans for for radio
    23: NotEnoughNeighboursError,        # 23 : Not Enough Neighbours - There are not enough neighbours for radio
    26: SuspendedApiKeyError,            # 26 : Suspended API key - Access for your account has been suspended, please contact Last.fm
    27: StationDeprecatedError,          # 27 : Deprecated - This station is no longer available
    28: GeoRestrictedError,              # 28 : Geo Restricted - This station is not available with this client/country combination
    29: RateLimitExceededError,          # 29 : Rate limit exceeded - Your IP has made too many requests in a short period
    }


def request(key, secret, package, method, params = {}, session = None, name = None, version = None):
    params = forge_params(params, key, secret, package, method, session)
    resp = requests.post(ROOT, params, headers = forge_headers(name, version)).text
    
    return resp
    
    
def forge_params(params, key, secret, package, method, session = None):
    params["api_key"] = key
    params["method"] = "{}.{}".format(package, method)
    try: params["sk"] = session.key
    except AttributeError: pass
    params["api_sig"] = sign_params(params, secret)
    
    return params
    
    
def sign_params(params, secret):
    # Parameters are alphabetically sorted by their key, and then concatenated
    # in a keyvalue manner. The application's secret is appended afterwards,
    # the whole thing is UTF-8 encoded, and then md5() hashed, hex digest of it
    # being the signature. Some parameters mustn't be included in the calculation.

    # Keys excluded from the calculation
    excluded_keys = ["format"]

    concat_params = ""
    for key in sorted(list(params)):
        if key not in excluded_keys:
            concat_params += key + params[key]
    concat_params += secret
    
    sig = hashlib.md5(concat_params.encode("utf-8")).hexdigest()
    
    return sig
    
    
def forge_headers(name, version):
    user_agent = "{}/{} {}".format(name, version, USER_AGENT)
    return {
        "User-Agent": user_agent,
        }
        
        
def response_to_xml(response):
    return XmlElementTree.fromstring(response)
    
    
def check_xml_for_errors(xml):
    if xml.attrib["status"] == "failed":
        error = xml.find("error")
        error_code = int(error.attrib["code"])
        message = error.text.strip()
        raise error_codes[error_code](message)
    

class App:
    def __init__(self, key = KEY, secret = SECRET, session = None, name = "unknown", version = "unknown"):
        self.key = key
        self.secret = secret
        self.session = session
        self.name = name
        self.version = version
        
        
    def request(self, package, method, params = {}):
        return request(self.key, self.secret, package, method, params,  \
                        session = self.session, name = self.name,   \
                        version = self.version)


class PackageMetaclass(type):
    def __init__(cls, name, bases, attrs):
        api_package_name = name.lower()
        api_methods = [(k, v) for k, v in cls.__dict__.items()  \
                        if not k.startswith("__") and callable(v) and not hasattr(v, "_is_helper")]
                        
        for api_method_func_name, api_method in api_methods:
            try:
                api_method_name = api_method._name
            except AttributeError:
                api_method_name = api_method_func_name.replace("_", "").lower()
                
            api_method_params = [x.rstrip('_') for x in inspect.signature(api_method).parameters if x != "self"]
            
            try:
                api_method_returns = api_method._returns
            except AttributeError:
                api_method_returns = None
            
            @wraps(api_method)
            def wrapper(api_method, api_method_name, api_method_params, api_method_returns):
                @wraps(wrapper)
                def wrapper2(self, *args, **kwargs):
                    params = dict(zip(api_method_params, args))
                    
                    custom_params = api_method(self, *args, **kwargs)
                    try: params.update(custom_params)
                    except TypeError: pass
                    
                    for k, v in params.items():
                        if isinstance(v, bool):
                            if v: params[k] = "1"
                            else: params[k] = "0"
                        else:
                            try: param = v.as_parameter()
                            except AttributeError:
                                params[k] = str(v)
                            else:
                                params[k] = None
                                params.update(param)
                    
                    params = dict((k, v) for k, v in params.items() if v is not None)
                    
                    response = self.app.request(api_package_name, api_method_name, params)
                    if api_method_returns is not None:
                        return api_method_returns.from_xml(response, self.app)
                    else:
                        return response
                    
                return wrapper2

            w = wrapper(api_method, api_method_name, api_method_params, api_method_returns)
            setattr(cls, api_method_func_name, w)
            
        return super().__init__(name, bases, attrs)

        
class Package(metaclass = PackageMetaclass):
    def __init__(self, app):
        self.app = app
    

def name(which):
    def decorator(func):
        func._name = which
        return func
    
    return decorator


def returns(what):
    def decorator(func):
        func._returns = what
        return func
    
    return decorator
    

def helper(func):
    func._is_helper = True
    return func
    

class DataMetaclass(ABCMeta):
    def __new__(cls, name, bases, attrs):
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        from_xml = cls.from_xml
        
        @wraps(from_xml)
        def wrapper(response, app):
            xml = response_to_xml(response)
            check_xml_for_errors(xml)
            return from_xml(xml, app)
            
        cls.from_xml = wrapper

        return super().__init__(name, bases, attrs)
    
    
class Data(metaclass = DataMetaclass):
    @staticmethod
    @abstractmethod
    def from_xml(xml, app):
        pass

    @abstractmethod
    def as_parameter(self):
        pass
        