from pgassets.common.pgImageButton import pgImageButton


class pgToggleButton(pgImageButton):
    def __init__(self, pos, size, img_path_1, img_path_2, color=(255, 255, 255), borderwidth=2, transparent=False):
        pgImageButton.__init__(self, pos, size, img_path_1, color, borderwidth=borderwidth, transparent=transparent)
        self.img_1 = img_path_1
        self.img_2 = img_path_2
        self.state = 1

    def collidepoint(self, pos: tuple):
        if pgImageButton.collidepoint(self, pos):
            if self.state == 1:
                self.set_image(self.img_2)
                self.state = 2
            elif self.state == 2:
                self.set_image(self.img_1)
                self.state = 1
            return True
        return False
