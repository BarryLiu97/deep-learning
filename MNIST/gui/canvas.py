from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor, QPainter


class Canvas(QLabel):
    def __init__(self, parent):
        super().__init__()
        pixmap = QPixmap(500, 500)
        # pixmap.fill(Qt.white)
        pixmap.fill(Qt.black)
        self.setPixmap(pixmap)

        # self.pen_color = QColor('#000000')
        self.pen_color = QColor('#ffffff')

        self.last_x, self.last_y = None, None

    def clear(self):
        # self.pixmap().fill(Qt.white)
        self.pixmap().fill(Qt.black)
        self.update()

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        painter = QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(18)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None