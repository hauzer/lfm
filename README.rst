Features
========

- Supports all packages and methods listed at http://www.last.fm/api.

- Methods return plain Python types: dictionaries and lists.

- If the user wishes, the library can make an application comply to the point 4.4 of
  `Last.fm's API ToS <http://www.last.fm/api/tos>`_, which says that the request
  rate of an application must be limited.

- Handles all Last.fm API errors via exceptions.

- Easily extendible.

|

A tutorial
==========

A short introduction
--------------------

*lfm.App*
~~~~~~~~~

Instantiate a Last.fm application::

    from lastfm import lfm
    
    app = lfm.App(API_KEY, SECRET)

The above is self-explanatory. You'll need an API key and the corresponding "secret"
given by Last.fm. If you don't have those handy, you can ommit them for **testing**
purposes, as *lfm* comes with its own. You are expected to provide your own key and
secret in real applications.

If you want your application to comply to Last.fm's request rate limit, you'll need
to provide a third argument, a file in which a sqlite3 database which tracks requests
will be stored.

::
    
    LFM_FILE = "lfm.dat"
    
    app = lfm.App(API_KEY, SECRET, LFM_FILE)

As a fourth argument, you can provide a tuple of your program's name and version,
to be used in the user-agent::

    NAME    = "myprogram"
    VERSION = "1.0.0"
    
    app = lfm.App(API_KEY, SECRET, LFM_FILE, (NAME, VERSION))
    
The user-agent is formatted as "NAME/VERSION lfm/LFMVERSION". If you don't provide
this information, both the name and version will be "unknown".


Methods and packages
~~~~~~~~~~~~~~~~~~~~

API methods are organized like so::

    data = app.package.method_name(...)
    
So, if you wanted to, for example, fetch all recently listened tracks of a user,
you'd do something like this::

    tracks = app.user.get_recent_tracks(user)
    
Note the underscores. Last.fm uses *camelCase* for method names. Such a thing
isn't Pythonic, though, hence the transformation of names to *under_scores*.


Authenticating
--------------

*auth.get_mobile_session()*
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's get a user's session now. There are three ways to do this. The first one
is by supplying a username and a password::

    session = app.auth.get_mobile_session(user, pwd)


*auth.get_session()*
~~~~~~~~~~~~~~~~~~~~
    
The second one is more complicated, but more secure and trustworthy. First,
you need to fetch a token::

    token = app.auth.get_token()
    
Then you have to make the user authenticate the token by pointing him to the
authentication web-page::

    import webbrowser
    
    webbrowser.open(token.url)
    input("Press enter after granting access.")
    
After the user has granted access, all that's left is to fetch the session::

    session = app.auth.get_session(token)


*auth.get_url()*
~~~~~~~~~~~~~~~~~~~~

The third one is for web apps. `auth.get_url()` takes one argument, a callback URL,
and returns an URL which points to the authentication page. When the user
authenticates, the page redirects to the callback URL with the token appended as a
GET parameter.  
For more information, consult the `official Last.fm documentation <http://www.last.fm/api/webauth>`_.


Using the session
~~~~~~~~~~~~~~~~~

Regardless of which of the methods you use, a session needs to be bound to your
app by assigning the session key to the *App*'s *session_key* attribute::

    app.session_key = session["key"]

That's all. You can now call methods which require authentication::

    app.track.remove_tag(artist, track, tag)
    

More
----

For more information on specific methods, consult the `API page <http://www.last.fm/api>`_
on Last.fm.

|

An advanced tutorial
====================

Custom requests
---------------

Say, for example, that Last.fm has added a new method not yet available in
this library. What can be done then? The solution is actually quite straightforward:
use *App.request()*. You can manually specify the API package, method and parameters::

    def playlist_remove(app, playlist_id):
        params = {
                  "playlistID": playlist_id,
                 }
    
        return app.request("playlist", "remove", params)

Simple as that.


Adding new packages
-------------------

*App.request_auto()*
~~~~~~~~~~~~~~~~~~~~~~~~

What if, by some miracle, a whole new package with a bunch of methods was added?
You'd want to use those methods several times in your program. Calling *request()*
every time would be quite cumbersome; very repetitive and error-prone.

Well, an unlikely hero arises: *App.request_auto()*! This function tries
to automate every bit of requesting that can possibly be automated, and generally
succeeds very well! This whole library is built on that one function. Here's an
example from the source itself::

    class Track(Package):
    
        ...
        
        def get_info(self, artist = None, track = None, username = None, autocorrect = None, mbid = None):
            data = self.app.request_auto()
            return data["track"]
        
        ...

What kind of magick is this? Well, without going into too much detail
(open source, remember?), the function cleverly learns all of the three,
if possible: the package, the method, the parameters:

- It assembles the method name from the caller function's name; "getInfo"
  in this case.
  
- The parameters, ignoring *self*, are grabbed from the caller's arguments.
  Parameter names are stripped of trailing underscores, to allow the use of
  parameters such as *from*.
  True to the Python's philosophy of "duck-tape" programming, the function tries
  to accept all kinds of types as parameters. It handles all primitive ones well:
  integers, floats, booleans, and such. Of the more complicated types, it can
  handle lists, but not dictionaries.
  
- The name of the package is learned from the name of the class the function's
  in, but **only** if the class inherits *lfm.Package*.
  
*request_auto()* is not only intelligent and elegant, it's also flexible.
You can override any of the three::

    def get_info(self, artist = None, track = None, username = None, autocorrect = None, mbid = None):
        package = "the_correct_package_name"
        method  = "the_correct_method_name"
        
        params  = {
                   "special" : 0xDEADBEEF,
                   "mbid"    : None,
                  }
        
        data = self.app.request_auto(package, method, params)
        return data["track"]
        
So, we have added a new parameter called *special*, and made *mbid*
always *None*, whatever the user may have passed. Pretty neat, huh?
Note that *params* will be **merged into** the auto-gathered
dictionary of parameters, not overwrite them. 


Inheriting *Package*
~~~~~~~~~~~~~~~~~~~~

Very well, your custom-made Package would look something like this::

    class Forum(Package):
        def post(self, threadid, msg):
            data = self.app.request_auto()
            return data
    
And you'd use it like so::

    forum = Forum(app)
    forum.post("1832723", "Hello folks!")


Inheriting *App*
~~~~~~~~~~~~~~~~

To add the finishing touch, you could extend *App*::

    class App(lfm.App):
        forum = None
        
        def __init__(self, key, secret, db = None, info = None):
            super().__init__(key, secret, db, info)
            
            forum = Forum(self)

And with that::

    app.forum.post("1832723", "Hello folks!")
    
Donations
=========

If you enjoy my work, please consider a donation.

    BTC: BC1QF2G847UQTDY6GAG5D64DSCFVEZ0HHY7AC3PNKX
    
    ETH: 0x61a08C3f8dF5A0507923FcA2ec8597e68e51d6A0
    
    XMR: 48aLGv9rg2Q1edA36PjKbj34SEAViUSGH47QfGDmWuqEDjUE1fA238BMn6z3R79DfKBTgu6TkT4VL5sMeTG6axMaKXytH6F
