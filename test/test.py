import webbrowser;
import lfm.lfm, lfm.auth, lfm.album

app = lfm.lfm.App("b07bfe5accc130311e9256ae3bd6d67c", "88ea86c8bbbece2613d99744ab1fc9cc")
app.activate()

# Last.fm username: lfm333333
# last.fm password: lfm333333
# Email: lfm333333@gmx.com
# Email password: lfm333333
session = lfm.auth.get_mobile_session("lfm333333", "lfm333333")
app.sk = session["key"]

# token = lfm.auth.get_token()
# webbrowser.open(token.get_url())
# input()
# session = lfm.auth.get_session(token.token)
# print(session["key"])

input()
