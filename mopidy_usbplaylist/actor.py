from __future__ import unicode_literals

import logging

from mopidy import backend

import pykka

from .playlists import USBPlaylistProvider


logger = logging.getLogger(__name__)


class USBPlaylistBackend(pykka.ThreadingActor, backend.Backend):
    name = 'usbplaylist'

    def __init__(self, config, audio):
        super(USBPlaylistBackend, self).__init__()

        self.config=config
        
        self.playlists = USBPlaylistProvider

    def on_start(self):
        self.playlists.refresh()

    def on_stop(self):
        pass
