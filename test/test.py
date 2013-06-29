import webbrowser;
import lfm.lfm, lfm.api.auth, lfm.api.album, lfm.api.library

app = lfm.lfm.App("b07bfe5accc130311e9256ae3bd6d67c", "88ea86c8bbbece2613d99744ab1fc9cc")
lfm.lfm.app = app

# Last.fm username: lfm333333
# last.fm password: lfm333333
# Email: lfm333333@gmx.com
# Email password: lfm333333
session = lfm.api.auth.get_mobile_session("lfm333333", "lfm333333")
app.sk = session["key"]

# token = lfm.auth.get_token()
# webbrowser.open(token.get_url())
# input()
# session = lfm.auth.get_session(token.token)
# print(session["key"])

#lfm.api.library.add_album({("Metallica", "Metallica"), ("Kansas", "Masque"), ("Kansas", "Freaks of Nature")})
#lfm.api.library.add_artist({"Gentle Giant", "Ludwig van Beethoven", "Riverside"})
lfm.api.library.get_albums("hauzzer", "Kansas")

input()
