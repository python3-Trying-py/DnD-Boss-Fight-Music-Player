class MainController:
    def __init__(self, model, viewers, audio_service):
        self.model = model
        self.viewers = viewers
        self.audio = audio_service

        self.connect_signals()

    def connect_signals(self):
        self.viewers.play_button.clicked.connect(self.handle_play)
        self.viewers.stop_button.clicked.connect(self.handle_stop)
        self.viewers.music_input.returnPressed.connect(self.load_music)

    def handle_play(self):
        self.model.play()
        self.audio.play()
        print("Playing...")

    def handle_stop(self):
        self.model.stop()
        self.audio.stop()
        print("Stopped.")

    def load_music(self):
        self.model.set_song(self.viewers.music_input.text())
        self.audio.load(self.viewers.music_input.text())
