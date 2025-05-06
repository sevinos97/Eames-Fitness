# simple UI_Element class parent
class UI_Element:
    def scroll(self, dy):
        self.pos = self.pos[0], self.pos[1] + dy
    
    def draw(self, surf):
        raise NotImplementedError("Obj draw not implemented")
    
    def handleEvent(self, event):
        return None
    
    def updatePos(self):
        raise NotImplementedError("Obj updatepos not implemented")

    def update(self):
        return None