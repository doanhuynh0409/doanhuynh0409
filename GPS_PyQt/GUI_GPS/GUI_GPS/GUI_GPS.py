import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QFont
import serial
import time
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle('GPS')
        self.setGeometry(500, 100, 400, 150)
        
        font = QFont("Arial", 12)
        self.setFont(font)  # Set the font for the entire application
        # Set up the QLineEdit widgets to display the latitude and longitude values
        self.lat_edit = QLineEdit(self)
        self.lat_edit.setGeometry(50, 25, 300, 25)
        self.lon_edit = QLineEdit(self)
        self.lon_edit.setGeometry(50, 75, 300, 25)
        self.show()
        # Set up the serial connection to the GPS device
        self.serial = serial.Serial('COM1', 9600)

        # # Start reading in GPS data
        self.read_gps_data()

    def read_gps_data(self):
        # Read in GPS data from the serial connection

        gps_data = self.serial.readline().decode()
        print(gps_data)
                
                    
        element_in_gps = gps_data.split(',')
        lat = float(element_in_gps[0].split(':')[1])
        lon = float(element_in_gps[1].split(':')[1])
       
        self.update_edit_fields(lat, lon)
        
        time.sleep(2)
        
        self.read_gps_data()

         
         

    def update_edit_fields(self, lat, lon):
        # Update the latitude and longitude QLineEdit widgets with the new values
        self.lat_edit.setText(str(lat))
        self.lon_edit.setText(str(lon))

if __name__ == '__main__':
    # Create the PyQt application and main window
    app = QApplication(sys.argv)
    main_window = MainWindow()
    #main_window.show()

    # Start the PyQt event loop
    sys.exit(app.exec_())