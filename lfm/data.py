import lfm.api as api


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
        
    def as_parameter(self):
        return {
            "sk": self.key,
            }

        
class Token(api.Data):
    @staticmethod
    def from_xml(xml, app):
        return Token(app, xml.find("token").text)
        
    def __init__(self, app, id):
        self.app = app
        self.id = id
        
    def as_parameter(self):
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
        
    def as_parameter(self):
        return {
            "username": self.name,
            }
