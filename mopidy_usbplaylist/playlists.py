from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

from mopidy import backend
from mopidy.models import Playlist

class USBPlaylistProvider(backend.PlaylistProvider):
    def create(self, name):
        pass
    
    def delete(self, uri):
        pass
    
    def lookup(self, uri):
        path=self.backend.config['usbplaylist']['path']
        
    
    def refresh(self):
        playlists=[]
        uri="usb://playall"
        playlist = Playlist(uri=uri, name="USB")
        playlists.append(playlist)
        self.playlists = playlists
        backend.BackendListener.send('playlists_loaded')
        
    def safe(self. playlist):
        pass