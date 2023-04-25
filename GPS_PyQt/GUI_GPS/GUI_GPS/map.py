import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl

class MapViewer(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Map Viewer')
        self.map_page = QWebEnginePage(self)
        self.map_page.setHtml("""
            <html>
            <head>
                <style>
                    html, body, #map {
                        margin: 0;
                        padding: 0;
                        height: 100%;
                    }
                </style>
            </head>
            <body>
                <iframe id="map" src="https://www.google.com/maps/embed/v1/place?q=Paris&key=YOUR_API_KEY" allowfullscreen></iframe>
            </body>
            </html>
        """)
        self.map = QWebEngineView(self)
        self.map.setPage(self.map_page)
        self.map.setGeometry(0, 0, 800, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MapViewer()
    sys.exit(app.exec_())
