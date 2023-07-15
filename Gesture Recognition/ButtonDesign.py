import cv2

class Button():
    def __init__(self, pos, text, size):
        self.pos = pos
        self.size = size
        self.text = text

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.size[0], self.pos[1] + self.size[1]), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, self.text, (self.pos[0] + 15, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN,
                    4, (255, 255, 255), 5)
        return img

    def checkOnClick(self, img, finger_pos):
        clicked = False

        if finger_pos[0] in range(self.pos[0], self.pos[0] + self.size[0]) and finger_pos[1] in range(self.pos[1], self.pos[1] + self.size[1]):
            cv2.rectangle(img, self.pos, (self.pos[0] + self.size[0], self.pos[1] + self.size[1]), (0, 255, 0),
                          cv2.FILLED)
            cv2.putText(img, self.text, (self.pos[0] + 15, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN,
                        4, (255, 255, 255), 5)
            clicked = True

        return img, clicked
