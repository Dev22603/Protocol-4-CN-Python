class Frame:
    def __init__(self, seq, ack, data):
        self.seq = seq
        self.ack = ack
        self.data = data