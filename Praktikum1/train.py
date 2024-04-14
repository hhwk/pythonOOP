class Train:
    def __init__(self):
        self.vagon = []
        self.cargo_info = ""

    def attach_vagon(self, vagon):
        self.vagon.append(vagon)

    def detach_vagon(self, vagon):
        self.vagon.remove(vagon)

    def get_vagon(self):
        return self.vagon

    def print_cargo_info(self):
        print(self.cargo_info)