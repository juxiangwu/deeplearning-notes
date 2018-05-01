# #coding:utf-8
# import sys
# import os.path
# import vlc
# from PyQt5 import QtGui, QtCore

# class Player(QtGui.QMainWindow):
#     """A simple Media Player using VLC and Qt
#     """
#     def __init__(self, master=None):
#         QtGui.QMainWindow.__init__(self, master)
#         self.setWindowTitle("Media Player")

#         # creating a basic vlc instance
#         self.instance = vlc.Instance()
#         # creating an empty vlc media player
#         self.mediaplayer = self.instance.media_player_new()

#         self.createUI()
#         self.isPaused = False

#     def createUI(self):
#         """Set up the user interface, signals & slots
#         """
#         self.widget = QtGui.QWidget(self)
#         self.setCentralWidget(self.widget)

#         # In this widget, the video will be drawn
#         if sys.platform == "darwin": # for MacOS
#             self.videoframe = QtGui.QMacCocoaViewContainer(0)
#         else:
#             self.videoframe = QtGui.QFrame()
#         self.palette = self.videoframe.palette()
#         self.palette.setColor (QtGui.QPalette.Window,
#                                QtGui.QColor(0,0,0))
#         self.videoframe.setPalette(self.palette)
#         self.videoframe.setAutoFillBackground(True)

#         self.positionslider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
#         self.positionslider.setToolTip("Position")
#         self.positionslider.setMaximum(1000)
#         self.connect(self.positionslider,
#                      QtCore.SIGNAL("sliderMoved(int)"), self.setPosition)

#         self.hbuttonbox = QtGui.QHBoxLayout()
#         self.playbutton = QtGui.QPushButton("Play")
#         self.hbuttonbox.addWidget(self.playbutton)
#         self.connect(self.playbutton, QtCore.SIGNAL("clicked()"),
#                      self.PlayPause)

#         self.stopbutton = QtGui.QPushButton("Stop")
#         self.hbuttonbox.addWidget(self.stopbutton)
#         self.connect(self.stopbutton, QtCore.SIGNAL("clicked()"),
#                      self.Stop)

#         self.hbuttonbox.addStretch(1)
#         self.volumeslider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
#         self.volumeslider.setMaximum(100)
#         self.volumeslider.setValue(self.mediaplayer.audio_get_volume())
#         self.volumeslider.setToolTip("Volume")
#         self.hbuttonbox.addWidget(self.volumeslider)
#         self.connect(self.volumeslider,
#                      QtCore.SIGNAL("valueChanged(int)"),
#                      self.setVolume)

#         self.vboxlayout = QtGui.QVBoxLayout()
#         self.vboxlayout.addWidget(self.videoframe)
#         self.vboxlayout.addWidget(self.positionslider)
#         self.vboxlayout.addLayout(self.hbuttonbox)

#         self.widget.setLayout(self.vboxlayout)

#         open = QtGui.QAction("&Open", self)
#         self.connect(open, QtCore.SIGNAL("triggered()"), self.OpenFile)
#         exit = QtGui.QAction("&Exit", self)
#         self.connect(exit, QtCore.SIGNAL("triggered()"), sys.exit)
#         menubar = self.menuBar()
#         filemenu = menubar.addMenu("&File")
#         filemenu.addAction(open)
#         filemenu.addSeparator()
#         filemenu.addAction(exit)

#         self.timer = QtCore.QTimer(self)
#         self.timer.setInterval(200)
#         self.connect(self.timer, QtCore.SIGNAL("timeout()"),
#                      self.updateUI)

#     def PlayPause(self):
#         """Toggle play/pause status
#         """
#         if self.mediaplayer.is_playing():
#             self.mediaplayer.pause()
#             self.playbutton.setText("Play")
#             self.isPaused = True
#         else:
#             if self.mediaplayer.play() == -1:
#                 self.OpenFile()
#                 return
#             self.mediaplayer.play()
#             self.playbutton.setText("Pause")
#             self.timer.start()
#             self.isPaused = False

#     def Stop(self):
#         """Stop player
#         """
#         self.mediaplayer.stop()
#         self.playbutton.setText("Play")

#     def OpenFile(self, filename=None):
#         """Open a media file in a MediaPlayer
#         """
#         if filename is None:
#             filename = QtGui.QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser('~'))
#         if not filename:
#             return

#         # create the media
#         if sys.version < '3':
#             filename = unicode(filename)
#         self.media = self.instance.media_new(filename)
#         # put the media in the media player
#         self.mediaplayer.set_media(self.media)

#         # parse the metadata of the file
#         self.media.parse()
#         # set the title of the track as window title
#         self.setWindowTitle(self.media.get_meta(0))

#         # the media player has to be 'connected' to the QFrame
#         # (otherwise a video would be displayed in it's own window)
#         # this is platform specific!
#         # you have to give the id of the QFrame (or similar object) to
#         # vlc, different platforms have different functions for this
#         if sys.platform.startswith('linux'): # for Linux using the X Server
#             self.mediaplayer.set_xwindow(self.videoframe.winId())
#         elif sys.platform == "win32": # for Windows
#             self.mediaplayer.set_hwnd(self.videoframe.winId())
#         elif sys.platform == "darwin": # for MacOS
#             self.mediaplayer.set_nsobject(self.videoframe.winId())
#         self.PlayPause()

#     def setVolume(self, Volume):
#         """Set the volume
#         """
#         self.mediaplayer.audio_set_volume(Volume)

#     def setPosition(self, position):
#         """Set the position
#         """
#         # setting the position to where the slider was dragged
#         self.mediaplayer.set_position(position / 1000.0)
#         # the vlc MediaPlayer needs a float value between 0 and 1, Qt
#         # uses integer variables, so you need a factor; the higher the
#         # factor, the more precise are the results
#         # (1000 should be enough)

#     def updateUI(self):
#         """updates the user interface"""
#         # setting the slider to the desired position
#         self.positionslider.setValue(self.mediaplayer.get_position() * 1000)

#         if not self.mediaplayer.is_playing():
#             # no need to call this function if nothing is played
#             self.timer.stop()
#             if not self.isPaused:
#                 # after the video finished, the play button stills shows
#                 # "Pause", not the desired behavior of a media player
#                 # this will fix it
#                 self.Stop()

# if __name__ == "__main__":
#     app = QtGui.QApplication(sys.argv)
#     player = Player()
#     player.show()
#     player.resize(640, 480)
#     if sys.argv[1:]:
#         player.OpenFile(sys.argv[1])
#     sys.exit(app.exec_())

# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QPushButton, QMessageBox
#from pprint import pprint
import subprocess
import argparse

# URL list taken from Wikipedia
STATIONS = [
    ['Radio 1', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_one/format/pls.pls'],
    ['Radio 1Xtra', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_1xtra/format/pls.pls'],
    ['Radio 2', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_two/format/pls.pls'],
    ['Radio 3', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_three/format/pls.pls'],
    ['Radio 4', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_fourfm/format/pls.pls'],
    ['Radio 4Xtra', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_four_extra/format/pls.pls'],
    ['Radio 5 Live', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_five_live/format/pls.pls'],
    #['Radio 5 Live Sports Extra', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_five_live_sports_extra/format/pls.pls'],
    ['Radio 6', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_6music/format/pls.pls'],
    ['Asian Network', 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_asian_network/format/pls.pls'],
    ['Radio Scotland', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_scotland_fm.mpd'],
    [u'Radio nan Gàidheal', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_nan_gaidheal.mpd'],
    ['Radio Wales', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_radio_wales_fm.mpd'],
    ['Radio Cymru', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_radio_cymru.mpd'],
    ['Radio Ulster', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_radio_ulster.mpd'],
    ['Radio Foyle', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_foyle.mpd'],
    ['BBC Berkshire', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_berkshire.mpd'],
    ['BBC Bristol', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_bristol.mpd'],
    ['BBC Cambridgeshire', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_cambridge.mpd'],
    ['BBC Cornwall', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_cornwall.mpd'],
    ['BBC Coventry & Warwickshire', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_radio_coventry_warwickshire.mpd'],
    ['BBC Cumbria', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_cumbria.mpd'],
    ['BBC Derby', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_radio_derby.mpd'],
    ['BBC Devon', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_radio_devon.mpd'],
    ['BBC Essex', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_essex.mpd'],
    ['BBC Gloucestershire', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_gloucestershire.mpd'],
    ['BBC Guernsey', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_guernsey.mpd'],
    ['BBC Hereford & Worcester', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_hereford_worcester.mpd'],
    ['BBC Humberside', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_humberside.mpd'],
    ['BBC Jersey', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_jersey.mpd'],
    ['BBC Kent', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_kent.mpd'],
    ['BBC Lancashire', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_lancashire.mpd'],
    ['BBC Leeds', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_leeds.mpd'],
    ['BBC Leicester', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_leicester.mpd'],
    ['BBC Lincolnshire', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_lincolnshire.mpd'],
    ['BBC London', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_london.mpd'],
    ['BBC Manchester', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_manchester.mpd'],
    ['BBC Merseyside', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_merseyside.mpd'],
    ['BBC Newcastle', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_newcastle.mpd'],
    ['BBC Norfolk', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_norfolk.mpd'],
    ['BBC Northampton', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_northampton.mpd'],
    ['BBC Nottingham', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_nottingham.mpd'],
    ['BBC Oxford', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_oxford.mpd'],
    ['BBC Sheffield', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_radio_sheffield.mpd'],
    ['BBC Shropshire', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_shropshire.mpd'],
    ['BBC Solent', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_solent.mpd'],
    ['BBC Somerset', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_radio_somerset_sound.mpd'],
    ['BBC Stoke', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_radio_stoke.mpd'],
    ['BBC Suffolk', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_radio_suffolk.mpd'],
    ['BBC Surrey', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_surrey.mpd'],
    ['BBC Sussex', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_sussex.mpd'],
    ['BBC Tees', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_tees.mpd'],
    ['BBC Three Counties', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/ak/bbc_three_counties_radio.mpd'],
    ['BBC Wiltshire', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_radio_wiltshire.mpd'],
    ['BBC WM', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnw/bbc_wm.mpd'],
    ['BBC York', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/aks/bbc_radio_york.mpd'],
    ['BBC World Service - Internet Schedule', 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/nonuk/sbr_low/llnw/bbc_world_service.m3u8'],
    ['BBC World Service - English News', 'http://www.bbc.co.uk/worldservice/meta/live/mp3/ennws.pls'],
    ['BBC World Service - Africa', 'http://www.bbc.co.uk/worldservice/meta/live/mp3/enafw.pls'],
    ['BBC Arabic Radio', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/llnws/bbc_arabic_radio.mpd'],
]
WIN_TITLE = "BBC radio"

class Win(QMainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.player = None
        # args
        parser = argparse.ArgumentParser(description='BBC radio player')
        parser.add_argument('-p', '--player', default='vlc')
        parser.add_argument('player_args', nargs='*')
        args = parser.parse_args()
        self.player_prog = args.player
        self.player_args = args.player_args
        # UI
        self.setWindowTitle(WIN_TITLE)
        self.setMinimumSize(300, 600)
        self.scroll_area = QScrollArea()
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.widget)
        self.setCentralWidget(self.scroll_area)
        for name, url in STATIONS:
            button = QPushButton(name.replace('&', '&&'))
            button.args = {
                'name': name,
                'url': url,
            }
            button.clicked.connect(self.listen)
            self.layout.addWidget(button)
        # timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_player)

    def listen(self):
        pressed_button = self.sender()
        for button in self.widget.findChildren(QPushButton):
            if button != pressed_button and not button.isEnabled():
                button.setEnabled(True)
                break
        pressed_button.setEnabled(False)
        # stop the running player instance before starting another one
        if self.player:
            if self.player.poll() is None:
                self.player.terminate()
                self.player.wait()
        cmd = [self.player_prog]
        cmd.extend(self.player_args)
        cmd.append(pressed_button.args['url'])
        try:
            self.player = subprocess.Popen(cmd)
        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setText('Couldn\'t launch\n"%s"' % ' '.join(cmd))
            msg_box.setInformativeText(unicode(e))
            msg_box.exec_()
            pressed_button.setEnabled(True)
        self.setWindowTitle('%s - %s' % (pressed_button.args['name'], WIN_TITLE))
        self.timer.start(200)

    def check_player(self):
        if self.player and self.player.poll() is not None:
            # the player has been stopped
            self.player = None
            self.timer.stop()
            self.setWindowTitle(WIN_TITLE)
            for button in self.widget.findChildren(QPushButton):
                if not button.isEnabled():
                    button.setEnabled(True)
                    break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())