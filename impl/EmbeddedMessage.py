class EmbeddedMessage:
    def __init__(self, embed=None, img=None, error=None, sync=False):
        self.embed = embed
        self.img = img
        self.error = error
        self.sync = sync
