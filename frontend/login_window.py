from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QCheckBox, QMessageBox, QFrame, QApplication
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QSize

class LoginWindow(QWidget):
    """Simple Login Window without CSS"""
    
    login_successful = pyqtSignal(str, str)  # username, role
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OM SAI TRAVELS - Login")
        
        # Set window size
        self.setFixedSize(450, 350)  # Fixed size for login window
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup UI using only PyQt widgets, no CSS"""
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Application title
        title_label = QLabel("OM SAI TRAVELS")
        title_font = QFont("Segoe UI", 16, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        
        # Subtitle
        subtitle_label = QLabel("Administration Portal")
        subtitle_font = QFont("Segoe UI", 10)
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setAlignment(Qt.AlignCenter)
        
        # Separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        
        # Login form frame
        form_frame = QFrame()
        form_frame.setFrameStyle(QFrame.Box | QFrame.Raised)
        
        form_layout = QVBoxLayout(form_frame)
        form_layout.setSpacing(10)
        
        # Username section
        username_layout = QHBoxLayout()
        username_label = QLabel("Username:")
        username_font = QFont("Segoe UI", 10)
        username_label.setFont(username_font)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")
        self.username_input.setMinimumHeight(30)
        
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        
        # Password section
        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        password_label.setFont(username_font)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(30)
        
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        
        # Remember me checkbox
        self.remember_check = QCheckBox("Remember me")
        self.remember_check.setFont(username_font)
        
        # Login button
        self.login_button = QPushButton("Login")
        login_font = QFont("Segoe UI", 11, QFont.Bold)
        self.login_button.setFont(login_font)
        self.login_button.setMinimumHeight(35)
        self.login_button.clicked.connect(self.authenticate)
        
        # Status label
        self.status_label = QLabel("")
        self.status_label.setFont(QFont("Segoe UI", 9))
        self.status_label.setAlignment(Qt.AlignCenter)
        
        """# Demo credentials label
        demo_label = QLabel("Demo: admin / admin123")
        demo_font = QFont("Segoe UI", 8)
        demo_label.setFont(demo_font)
        demo_label.setAlignment(Qt.AlignCenter)"""
        
        # Add widgets to form layout
        form_layout.addLayout(username_layout)
        form_layout.addLayout(password_layout)
        form_layout.addWidget(self.remember_check)
        form_layout.addWidget(self.login_button)
        form_layout.addWidget(self.status_label)
        """form_layout.addWidget(demo_label)"""
        
        # Add all to main layout
        main_layout.addWidget(title_label)
        main_layout.addWidget(subtitle_label)
        main_layout.addWidget(separator)
        main_layout.addWidget(form_frame)
        
        # Add copyright label at bottom
        copyright_label = QLabel("© 2026 Bus Management System")
        copyright_label.setFont(QFont("Segoe UI", 8))
        copyright_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(copyright_label)
        
        self.setLayout(main_layout)
        
        # Set focus to username field
        self.username_input.setFocus()
        
    def authenticate(self):
        """Authenticate user"""
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            self.show_error("Please enter both username and password")
            return
            
        # Show loading state
        self.login_button.setText("Authenticating...")
        self.login_button.setEnabled(False)
        
        # Mock authentication
        valid_users = {
            "admin": {"password": "admin123", "role": "Super Admin", "name": "System Administrator"},
            "manager": {"password": "manager123", "role": "Manager", "name": "Bus Manager"},
            "viewer": {"password": "viewer123", "role": "Viewer", "name": "Read Only User"}
        }
        
        if username in valid_users and valid_users[username]["password"] == password:
            self.show_success(f"Welcome, {valid_users[username]['name']}!")
            
            # Simulate loading delay
            from PyQt5.QtCore import QTimer
            QTimer.singleShot(1000, lambda: self.login_successful.emit(
                username, valid_users[username]["role"]))
        else:
            self.show_error("Invalid username or password")
            self.login_button.setText("Login")
            self.login_button.setEnabled(True)
        
    def show_error(self, message):
        """Show error message"""
        self.status_label.setText(f"Error: {message}")
        
    def show_success(self, message):
        """Show success message"""
        self.status_label.setText(f"Success: {message}")
        
    def keyPressEvent(self, event):
        """Handle Enter key for login"""
        if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            self.authenticate()
        super().keyPressEvent(event)