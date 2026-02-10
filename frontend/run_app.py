import sys
from PyQt5.QtWidgets import QApplication

# Import your classes
from login_window import LoginWindow
from main_application import MainApplication
from application_controller import ApplicationController

if __name__ == "__main__":
    # Set application style
    QApplication.setStyle("Fusion")
    
    # Start application
    controller = ApplicationController()
    controller.start()