from pgassets.common.pgObject import pgObject


class pgStructureInput(pgObject):
    def __init__(self, pos, size):
        pgObject.__init__(self, pos, size, transparent=True, borderwidth=2)