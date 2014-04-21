import lfm.api as api


class Album(api.Data):
    def __init__(self, artist, name):
        self.name = name
        self.artist = artist
        
    def as_parameter(self, key):
        return {
            "artist": self.artist,
            "album": self.name,
            }


class List(api.Data, list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def as_parameter(self, key):
        param = ""
        for x in self:
            param = "{},{}".format(param, x)
        param = param.lstrip(",")
        
        return {
            key: param,
            }

            
class Nothing(api.Data):
    @staticmethod
    def from_xml(xml, app):
        pass
            

class Session(api.Data):
    @staticmethod
    def from_xml(xml, app):
        session = xml.find("session")
        key = session.find("key").text
        user = User(session.find("name").text, bool(int(session.find("subscriber").text)))

        return Session(key, user)
        
    def __init__(self, key, user):
        self.key = key
        self.user = user
        
    def as_parameter(self, key):
        return {
            "sk": self.key,
            }

            
class Tag(api.Data):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def as_parameter(self, key):
        return {
            key: str(self),
            }

        
class Token(api.Data):
    @staticmethod
    def from_xml(xml, app):
        return Token(app, xml.find("token").text)
        
    def __init__(self, app, id):
        self.app = app
        self.id = id
        
    def as_parameter(self, key):
        return {
            "token": self.id,
            }
        
    @property
    def auth_url(self):
        return r"http://www.last.fm/api/auth/?api_key=" + self.app.key + r"&token=" + self.id
        
           
class User(api.Data):
    @staticmethod
    def from_xml(xml, app):
        pass
        
    def __init__(self, name, is_subscriber = None):
        self.name = name
        self.is_subscriber = is_subscriber
        
    def as_parameter(self, key):
        return {
            "username": self.name,
            }
