from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

from mopidy import backend
from mopidy.models import Playlist
from mopidy.models import Track

import os
import fnmatch
import glob

def find_files(path):
    matches = glob.glob(os.path.join(path,'*.mp3'))
    return matches

def find_files2(path):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.mp3'):
            matches.append(os.path.join(root, filename))
    return matches

class USBPlaylistProvider(backend.PlaylistsProvider):
    def create(self, name):
        pass
    
    def delete(self, uri):
        pass
    
    def lookup(self, uri):
        path=self.backend.config['usbplaylist']['path']

        for playlist in self.playlists:
            if playlist.uri == uri:
                files=find_files2(path)
                tracks =[]
                for file in files:
                    tracks.append(Track(uri='file:'+file, name="USB-File"))
                return playlist.copy(tracks=tracks)
        
    def refresh(self):
        playlists=[]
        uri="usb://playall"
        playlist = Playlist(uri=uri, name="USB")
        playlists.append(playlist)
        self.playlists = playlists
        backend.BackendListener.send('playlists_loaded')
        
    def save(self, playlist):
        pass
    
    

        
