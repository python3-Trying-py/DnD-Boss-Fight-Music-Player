import logging

logger = logging.getLogger(__name__)

class MainController:
    def __init__(self, model, viewers, audio_service):
        self.model = model
        self.viewers = viewers
        self.audio = audio_service
        self.tracks = []
        self.current_track_index = 0
        self.audio.on_intro_done = self.play_next_track

        self.connect_signals()
        self.update()

    def connect_signals(self):
        self.viewers.PB_play_button.clicked.connect(self.handle_play)
        self.viewers.PB_stop_button.clicked.connect(self.handle_stop)
        self.viewers.PB_fight_select.clicked.connect(self.load_fight)
        self.viewers.Ti_music_timer.timeout.connect(self.check_music)
        self.audio.intro_finished.connect(self.play_next_track)
        self.audio.fight_finished.connect(self.handle_stop)

    def handle_play(self):
        self.model.play()
        self.audio.play()
        self.viewers.Ti_music_timer.start()
        logger.info("Playing...")

    def handle_stop(self):
        self.model.stop()
        self.audio.stop()
        self.viewers.Ti_music_timer.stop()
        logger.info("Stopped")

    def load_fight(self):
        self.current_track_index = 0
        self.viewers.La_current_fight.setText(self.viewers.CB_fight_selection.currentText())
        self.tracks = self.model.grab_tracks(self.viewers.CB_fight_selection.currentText())
        self.viewers.La_current_track.setText(self.tracks[0])
        self.audio.load(f"{self.viewers.CB_fight_selection.currentText()}/{self.tracks[0]}")

    def load_music(self):                     
        self.viewers.La_current_track.setText()
        #self.model.set_song(self.viewers.music_input.text())
        #self.audio.load(self.viewers.music_input.text())

    def check_music(self):
        self.audio.check_music()
        self.viewers.Ti_music_timer.start()
    
    def play_next_track(self):
        self.current_track_index += 1
        if self.current_track_index < len(self.tracks):
            next_track = self.tracks[self.current_track_index]
            self.viewers.La_current_track.setText(next_track)
            self.audio.load(f"{self.viewers.CB_fight_selection.currentText()}/{next_track}")
            self.audio.play()
        else:
            logger.info("No more tracks")

    def update(self):
        self.viewers.CB_fight_selection.clear()
        for fight_title in self.model.grab_fights():
            self.viewers.CB_fight_selection.addItem(fight_title)
