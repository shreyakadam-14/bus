from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QStackedWidget, QListWidget, QListWidgetItem,
    QStatusBar, QMenuBar, QMenu, QToolBar, QAction, QFrame,
    QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView,
    QMessageBox, QLineEdit, QComboBox, QDateEdit, QSpinBox,
    QDoubleSpinBox, QTextEdit, QGroupBox, QTabWidget, QApplication
)
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt, QTimer, QDate
import datetime
import sys

# Import the management modules
from bus_management import BusManagementPage  # Add this line
from driver_management import DriverManagementPage  # Add this line

class MainApplication(QMainWindow):
    """
    Main Application Window - Shows after successful login
    """
    
    def __init__(self, username="Admin", role="User"):
        super().__init__()
        self.username = username
        self.user_role = role
        
        # Setup window
        self.setWindowTitle(f"Bus Management System - Welcome {username}")
        self.setGeometry(100, 50, 1000, 600) #100, 50, 1400, 800
        
        # Setup all UI components
        self.setup_menu_bar()
        self.setup_toolbar()
        self.setup_main_content()
        self.setup_status_bar()
        
    def setup_menu_bar(self):
        """Setup the menu bar"""
        menubar = self.menuBar()
        
        # File Menu
        file_menu = menubar.addMenu("File")
        
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        save_as_action = QAction("Save As...", self)
        print_action = QAction("Print", self)
        logout_action = QAction("Logout", self)
        exit_action = QAction("Exit", self)
        
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(print_action)
        file_menu.addSeparator()
        file_menu.addAction(logout_action)
        file_menu.addAction(exit_action)
        
        # Edit Menu
        edit_menu = menubar.addMenu("Edit")
        
        cut_action = QAction("Cut", self)
        copy_action = QAction("Copy", self)
        paste_action = QAction("Paste", self)
        
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        
        # View Menu
        view_menu = menubar.addMenu("View")
        
        toolbar_action = QAction("Toolbar", self, checkable=True)
        toolbar_action.setChecked(True)
        statusbar_action = QAction("Status Bar", self, checkable=True)
        statusbar_action.setChecked(True)
        
        view_menu.addAction(toolbar_action)
        view_menu.addAction(statusbar_action)
        
        # Tools Menu
        tools_menu = menubar.addMenu("Tools")
        
        calculator_action = QAction("Calculator", self)
        calendar_action = QAction("Calendar", self)
        backup_action = QAction("Backup Database", self)
        restore_action = QAction("Restore Database", self)
        
        tools_menu.addAction(calculator_action)
        tools_menu.addAction(calendar_action)
        tools_menu.addSeparator()
        tools_menu.addAction(backup_action)
        tools_menu.addAction(restore_action)
        
        # Help Menu
        help_menu = menubar.addMenu("Help")
        
        help_action = QAction("User Guide", self)
        about_action = QAction("About", self)
        
        help_menu.addAction(help_action)
        help_menu.addAction(about_action)
        
        # Connect actions
        exit_action.triggered.connect(self.close)
        logout_action.triggered.connect(self.logout)
        about_action.triggered.connect(self.show_about)
        
    def setup_toolbar(self):
        """Setup the toolbar with quick actions"""
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        
        # Dashboard button
        dashboard_btn = QPushButton("Dashboard")
        dashboard_btn.clicked.connect(lambda: self.switch_module("Dashboard"))
        toolbar.addWidget(dashboard_btn)
        
        toolbar.addSeparator()
        
        # Reports button
        reports_btn = QPushButton("Reports")
        reports_btn.clicked.connect(lambda: self.switch_module("Reports"))
        toolbar.addWidget(reports_btn)
        
        # Users button (only for admins)
        if self.user_role in ["Super Admin", "Admin"]:
            users_btn = QPushButton("Users")
            users_btn.clicked.connect(lambda: self.switch_module("Users"))
            toolbar.addWidget(users_btn)
        
        toolbar.addSeparator()
        
        # Print button
        print_btn = QPushButton("Print")
        print_btn.clicked.connect(self.print_current)
        toolbar.addWidget(print_btn)
        
        # Export button
        export_btn = QPushButton("Export")
        export_btn.clicked.connect(self.export_data)
        toolbar.addWidget(export_btn)
        
        toolbar.addSeparator()
        
        # Help button
        help_btn = QPushButton("Help")
        help_btn.clicked.connect(self.show_help)
        toolbar.addWidget(help_btn)
        
    def setup_main_content(self):
        """Setup the main content area with sidebar and central widget"""
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create sidebar
        self.sidebar = self.create_sidebar()
        main_layout.addWidget(self.sidebar)
        
        # Create central work area
        self.central_work_area = self.create_central_work_area()
        main_layout.addWidget(self.central_work_area, 1)
        
    def create_sidebar(self):
        """Create the sidebar navigation"""
        sidebar = QFrame()
        sidebar.setFixedWidth(220)
        sidebar.setFrameStyle(QFrame.Box | QFrame.Raised)
        
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        
        # Sidebar title with user info
        user_frame = QFrame()
        user_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        user_layout = QVBoxLayout(user_frame)
        
        user_label = QLabel(self.username)
        user_label.setFont(QFont("Arial", 12, QFont.Bold))
        user_label.setAlignment(Qt.AlignCenter)
        
        role_label = QLabel(self.user_role)
        role_label.setFont(QFont("Arial", 10))
        role_label.setStyleSheet("color: #7f8c8d;")
        role_label.setAlignment(Qt.AlignCenter)
        
        user_layout.addWidget(user_label)
        user_layout.addWidget(role_label)
        
        # Add separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        
        # Navigation list
        self.nav_list = QListWidget()
        self.nav_list.setFont(QFont("Arial", 11))
        
        # Add navigation items based on user role
        nav_items = [("📊 Dashboard", "Dashboard")]
        
        # Add role-based items
        if self.user_role in ["Super Admin", "Admin", "Manager"]:
            nav_items.extend([
                ("🚌 Buses", "Buses"),
                ("👨‍✈️ Drivers", "Drivers"),
                ("🏫 Schools", "Schools"),
                ("💰 Invoices", "Invoices"),
            ])
        
        nav_items.append(("📈 Reports", "Reports"))
        
        if self.user_role in ["Super Admin", "Admin"]:
            nav_items.extend([
                ("⚙️ Settings", "Settings"),
                ("👥 Users", "Users"),
                ("🗄️ Database", "Database"),
                ("📝 Activity Logs", "Activity Logs"),
            ])
        
        nav_items.extend([
            ("🔍 Search", "Search"),
            ("📅 Calendar", "Calendar"),
            ("🔔 Notifications", "Notifications"),
            ("❓ Help", "Help")
        ])
        
        for text, module in nav_items:
            item = QListWidgetItem(text)
            item.setData(Qt.UserRole, module)
            self.nav_list.addItem(item)
        
        # Connect item click
        self.nav_list.itemClicked.connect(self.on_nav_item_clicked)
        
        # Select dashboard by default
        self.nav_list.item(0).setSelected(True)
        
        sidebar_layout.addWidget(user_frame)
        sidebar_layout.addWidget(separator)
        sidebar_layout.addWidget(self.nav_list)
        
        # Logout button at bottom
        logout_btn = QPushButton("🚪 Logout")
        logout_btn.setFont(QFont("Arial", 10))
        logout_btn.clicked.connect(self.logout)
        sidebar_layout.addWidget(logout_btn)
        
        return sidebar
        
    def create_central_work_area(self):
        """Create the central work area with stacked widgets"""
        # Create stacked widget for different modules
        self.stacked_widget = QStackedWidget()
        
        # Create all module pages
        self.dashboard_page = self.create_dashboard_page()
        self.bus_management_page = self.create_bus_management_page()
        self.driver_management_page = self.create_driver_management_page()  # Add this line
        self.reports_page = self.create_reports_page()
        self.users_page = self.create_users_page()
        self.settings_page = self.create_settings_page()
        self.help_page = self.create_help_page()
        self.placeholder_page = self.create_placeholder_page()
        
        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.addWidget(self.bus_management_page)
        self.stacked_widget.addWidget(self.driver_management_page)  # Add this line
        self.stacked_widget.addWidget(self.reports_page)
        self.stacked_widget.addWidget(self.users_page)
        self.stacked_widget.addWidget(self.settings_page)
        self.stacked_widget.addWidget(self.help_page)
        self.stacked_widget.addWidget(self.placeholder_page)
        
        # Set default page
        self.stacked_widget.setCurrentIndex(0)
        
        return self.stacked_widget
        
    def create_dashboard_page(self):
        """Create dashboard page"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Statistics section
        stats_label = QLabel("System Overview")
        stats_label.setFont(QFont("Arial", 16, QFont.Bold))
        stats_label.setStyleSheet("color: #2c3e50; margin-top: 20px;")
        layout.addWidget(stats_label)
        
        # Statistics cards in grid
        stats_grid = QGridLayout()
        
        stats_data = [
            ("Total Buses", "25", QColor(52, 152, 219)),
            ("Active Drivers", "18", QColor(46, 204, 113)),
            ("Registered Schools", "12", QColor(155, 89, 182)),
            ("Pending Invoices", "8", QColor(231, 76, 60)),
            ("Insurance Expiring", "3", QColor(241, 196, 15)),
            ("Due Salaries", "5", QColor(230, 126, 34))
        ]
        
        for i, (title, value, color) in enumerate(stats_data):
            card = self.create_stat_card(title, value, color)
            stats_grid.addWidget(card, i // 3, i % 3)
        
        layout.addLayout(stats_grid)
        
        # Recent activity section
        activity_label = QLabel("Recent Activity")
        activity_label.setFont(QFont("Arial", 16, QFont.Bold))
        activity_label.setStyleSheet("color: #2c3e50; margin-top: 20px;")
        layout.addWidget(activity_label)
        
        # Activity table
        self.activity_table = QTableWidget()
        self.activity_table.setColumnCount(4)
        self.activity_table.setHorizontalHeaderLabels(["Time", "User", "Activity", "Details"])
        self.activity_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Add sample data
        self.activity_table.setRowCount(5)
        sample_data = [
            ["10:30 AM", self.username, "Login", "Successful login to system"],
            ["11:15 AM", "Manager", "Added Bus", "Bus No: BUS-025 added"],
            ["02:45 PM", "Admin", "Generated Report", "Monthly financial report"],
            ["04:20 PM", "Accountant", "Processed Invoice", "Invoice #INV-1023 paid"],
            ["05:10 PM", "Admin", "Updated Settings", "Tax rate updated to 18%"]
        ]
        
        for row, data in enumerate(sample_data):
            for col, text in enumerate(data):
                item = QTableWidgetItem(text)
                self.activity_table.setItem(row, col, item)
        
        layout.addWidget(self.activity_table)
        
        # Quick actions
        actions_label = QLabel("Quick Actions")
        actions_label.setFont(QFont("Arial", 16, QFont.Bold))
        actions_label.setStyleSheet("color: #2c3e50; margin-top: 20px;")
        layout.addWidget(actions_label)
        
        actions_layout = QHBoxLayout()
        
        actions = ["Generate Report", "Add New Bus", "Process Salary", "Create Invoice"]
        
        for action in actions:
            btn = QPushButton(action)
            btn.setFont(QFont("Arial", 10))
            btn.setFixedHeight(40)
            actions_layout.addWidget(btn)
        
        layout.addLayout(actions_layout)
        
        layout.addStretch()
        
        return page
        
    def create_bus_management_page(self):
        """Create bus management page"""
        page = BusManagementPage()
        return page
        
    def create_driver_management_page(self):
        """Create driver management page"""
        page = DriverManagementPage()
        return page
        
    def create_stat_card(self, title, value, color):
        """Create a statistics card"""
        card = QFrame()
        card.setFrameStyle(QFrame.Box | QFrame.Raised)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Title
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 11))
        title_label.setAlignment(Qt.AlignCenter)
        
        # Value
        value_label = QLabel(value)
        value_label.setFont(QFont("Arial", 24, QFont.Bold))
        value_label.setAlignment(Qt.AlignCenter)
        
        # Set color
        value_label.setStyleSheet(f"color: rgb({color.red()}, {color.green()}, {color.blue()});")
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        
        return card
        
    def create_reports_page(self):
        """Create reports page"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Page header
        header = QLabel("📊 Reports Module")
        header.setFont(QFont("Arial", 20, QFont.Bold))
        header.setStyleSheet("color: #2c3e50;")
        layout.addWidget(header)
        
        # Add separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)
        
        layout.addWidget(QLabel("Reports functionality will be implemented here"))
        layout.addStretch()
        
        return page
        
    def create_users_page(self):
        """Create users management page"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Page header
        header = QLabel("👥 User Management")
        header.setFont(QFont("Arial", 20, QFont.Bold))
        header.setStyleSheet("color: #2c3e50;")
        layout.addWidget(header)
        
        # Add separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)
        
        layout.addWidget(QLabel("User management functionality will be implemented here"))
        layout.addStretch()
        
        return page
        
    def create_settings_page(self):
        """Create settings page"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Page header
        header = QLabel("⚙️ System Settings")
        header.setFont(QFont("Arial", 20, QFont.Bold))
        header.setStyleSheet("color: #2c3e50;")
        layout.addWidget(header)
        
        # Add separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)
        
        layout.addWidget(QLabel("System settings functionality will be implemented here"))
        layout.addStretch()
        
        return page
        
    def create_help_page(self):
        """Create help page"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Page header
        header = QLabel("❓ Help & Support")
        header.setFont(QFont("Arial", 20, QFont.Bold))
        header.setStyleSheet("color: #2c3e50;")
        layout.addWidget(header)
        
        # Add separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)
        
        # Help content
        help_text = QTextEdit()
        help_text.setReadOnly(True)
        help_text.setFont(QFont("Arial", 11))
        help_text.setPlainText(f"""
Welcome to Bus Management System, {self.username}!

Quick Guide:

1. DASHBOARD
   - View system statistics
   - Monitor recent activities
   - Access quick actions

2. BUS MANAGEMENT
   - Manage bus fleet
   - Track insurance details
   - Renew insurance policies

3. DRIVER MANAGEMENT
   - Manage driver details
   - Track license expiry
   - Process salary payments

4. REPORTS
   - Generate various reports
   - Export to PDF/Excel
   - Schedule automatic reports

5. SETTINGS
   - Configure system preferences
   - Manage database backups
   - Customize application settings

6. USER MANAGEMENT
   - Add/Edit/Delete users
   - Assign roles and permissions
   - Reset user passwords

Need Help?
- Check the user guide for detailed instructions
- Contact support for technical issues
- Visit our website for updates

Contact Information:
Email: support@busmgmt.com
Phone: +91 9876543210
Hours: 9:00 AM - 6:00 PM (Monday to Friday)
        """)
        
        layout.addWidget(help_text)
        
        layout.addStretch()
        
        return page
        
    def create_placeholder_page(self):
        """Create a placeholder page for modules not implemented"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Coming soon message
        message = QLabel("🚧 Module Under Development")
        message.setFont(QFont("Arial", 24, QFont.Bold))
        message.setStyleSheet("color: #e74c3c;")
        message.setAlignment(Qt.AlignCenter)
        
        info = QLabel("This module is currently being developed.\nIt will be available in the next update.")
        info.setFont(QFont("Arial", 14))
        info.setAlignment(Qt.AlignCenter)
        
        layout.addStretch()
        layout.addWidget(message)
        layout.addWidget(info)
        layout.addStretch()
        
        # Back to dashboard button
        back_btn = QPushButton("← Back to Dashboard")
        back_btn.setFont(QFont("Arial", 12))
        back_btn.clicked.connect(lambda: self.switch_module("Dashboard"))
        layout.addWidget(back_btn)
        
        return page
        
    def setup_status_bar(self):
        """Setup the status bar"""
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        
        # Add status labels
        statusbar.showMessage("Ready")
        
        # Add permanent widgets
        user_label = QLabel(f"👤 {self.username} ({self.user_role})")
        user_label.setFont(QFont("Arial", 9))
        
        time_label = QLabel()
        time_label.setFont(QFont("Arial", 9))
        
        # Update time every second
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(lambda: time_label.setText(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.status_timer.start(1000)
        
        statusbar.addPermanentWidget(user_label)
        statusbar.addPermanentWidget(time_label)
        
    def on_nav_item_clicked(self, item):
        """Handle navigation item click"""
        module = item.data(Qt.UserRole)
        self.current_module = module
        
        # Update status bar
        self.statusBar().showMessage(f"Switched to {module}")
        
        # Switch to appropriate page
        module_map = {
            "Dashboard": 0,
            "Buses": 1,
            "Drivers": 2,  # Add this line for Drivers
            "Reports": 3,
            "Users": 4,
            "Settings": 5,
            "Help": 6
        }
        
        if module in module_map:
            self.stacked_widget.setCurrentIndex(module_map[module])
        else:
            # Show placeholder for other modules
            self.stacked_widget.setCurrentIndex(7)  # Placeholder page (increased to 7)
            QMessageBox.information(self, "Coming Soon", 
                                  f"The {module} module is under development.")
            
    def switch_module(self, module_name):
        """Switch to a specific module"""
        # Find and select the navigation item
        for i in range(self.nav_list.count()):
            item = self.nav_list.item(i)
            if item.data(Qt.UserRole) == module_name:
                self.nav_list.setCurrentItem(item)
                self.on_nav_item_clicked(item)
                break
                
    def print_current(self):
        """Print current page"""
        QMessageBox.information(self, "Print", 
                              "Print functionality would be implemented here.")
        
    def export_data(self):
        """Export current data"""
        QMessageBox.information(self, "Export", 
                              "Export functionality would be implemented here.")
        
    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(self, "About Bus Management System",
                         f"Bus Management System v1.0.0\n"
                         f"Logged in as: {self.username} ({self.user_role})\n"
                         f"Developed with PyQt5\n"
                         f"© 2024 All rights reserved")
        
    def show_help(self):
        """Show help"""
        self.switch_module("Help")
        
    def logout(self):
        """Logout from application"""
        reply = QMessageBox.question(self, "Logout", 
                                    "Are you sure you want to logout?",
                                    QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.close()
            # In a real app, you would restart the login window here
            QMessageBox.information(None, "Logged Out", 
                                  "You have been logged out successfully.")