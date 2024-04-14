class Way:
    def __init__(self, number):
        self.number = number
        self.vagon = []

    def add_vagon(self, vagon):
        self.vagon.append(vagon)

    def remove_vagon(self, vagon):
        self.vagon.remove(vagon)

    def get_vagon(self):
        return self.vagon