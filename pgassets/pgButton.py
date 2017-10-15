from pgassets.pgTextPanel import pgTextPanel


class pgButton(pgTextPanel):
    def __init__(self, pos: tuple, size: tuple, text="", transparent=False, color=(255, 255, 255), borderwidth=2, fontsize=20):
        pgTextPanel.__init__(self, pos, size, text, transparent, borderwidth, color, fontsize=fontsize)
