from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QLineEdit, QComboBox,
    QDateEdit, QSpinBox, QDoubleSpinBox, QFrame, QGroupBox,
    QTabWidget, QTextEdit, QHeaderView, QMessageBox,
    QCheckBox, QFileDialog, QFormLayout, QDialog, QGridLayout,
    QRadioButton, QButtonGroup, QTextEdit, QListWidget, QListWidgetItem,
    QInputDialog, QTimeEdit, QScrollArea
)
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtCore import Qt, QDate
import datetime

# Mock data for schools
MOCK_SCHOOLS = [
    {
        'id': 1,
        'name': 'Delhi Public School',
        'school_code': 'DPS001',
        'type': 'Private',
        'address': '123 Education Lane, Delhi',
        'city': 'Delhi',
        'phone': '011-23456789',
        'email': 'contact@dpsdelhi.edu.in',
        'principal_name': 'Dr. Ramesh Sharma',
        'contact_person': 'Mr. Anil Kumar',
        'contact_person_phone': '9876543210',
        'student_count': 2500,
        'contract_status': 'Active',
        'contract_start': '2023-01-01',
        'contract_end': '2024-12-31',
        'monthly_fee': 150000,
        'payment_status': 'Paid',
        'assigned_buses': ['BUS-001', 'BUS-002'],
        'pickup_time': '07:30',
        'drop_time': '14:30',
        'billing_address': 'Same as school address',
        'gst_number': '07AABCD1234E1Z5'
    },
    {
        'id': 2,
        'name': 'Kendriya Vidyalaya',
        'school_code': 'KV001',
        'type': 'Government',
        'address': '456 Government Road, Delhi',
        'city': 'Delhi',
        'phone': '011-34567890',
        'email': 'kvdelhi@kvs.gov.in',
        'principal_name': 'Dr. Sunita Verma',
        'contact_person': 'Mr. Rajesh Singh',
        'contact_person_phone': '9876543211',
        'student_count': 1800,
        'contract_status': 'Active',
        'contract_start': '2023-03-01',
        'contract_end': '2025-02-28',
        'monthly_fee': 120000,
        'payment_status': 'Pending',
        'assigned_buses': ['BUS-003', 'BUS-004'],
        'pickup_time': '08:00',
        'drop_time': '15:00',
        'billing_address': 'Kendriya Vidyalaya, Delhi',
        'gst_number': '07BABCD1234E1Z6'
    },
    {
        'id': 3,
        'name': 'Modern Public School',
        'school_code': 'MPS001',
        'type': 'Private',
        'address': '789 Modern Road, Gurgaon',
        'city': 'Gurgaon',
        'phone': '0124-4567890',
        'email': 'info@modernschool.edu.in',
        'principal_name': 'Mrs. Priya Kapoor',
        'contact_person': 'Mr. Vikas Gupta',
        'contact_person_phone': '9876543212',
        'student_count': 3000,
        'contract_status': 'Active',
        'contract_start': '2023-06-01',
        'contract_end': '2024-05-31',
        'monthly_fee': 200000,
        'payment_status': 'Paid',
        'assigned_buses': ['BUS-005'],
        'pickup_time': '07:45',
        'drop_time': '14:45',
        'billing_address': 'Modern School Accounts Dept, Gurgaon',
        'gst_number': '06CABCD1234E1Z7'
    },
    {
        'id': 4,
        'name': 'Little Angels School',
        'school_code': 'LAS001',
        'type': 'Private',
        'address': '101 Children Street, Noida',
        'city': 'Noida',
        'phone': '0120-5678901',
        'email': 'contact@littleangels.edu.in',
        'principal_name': 'Mrs. Anjali Mehta',
        'contact_person': 'Mr. Sanjay Patel',
        'contact_person_phone': '9876543213',
        'student_count': 1200,
        'contract_status': 'Expiring Soon',
        'contract_start': '2022-04-01',
        'contract_end': '2023-12-31',
        'monthly_fee': 80000,
        'payment_status': 'Overdue',
        'assigned_buses': ['BUS-006'],
        'pickup_time': '08:15',
        'drop_time': '15:15',
        'billing_address': 'Little Angels School, Noida',
        'gst_number': '09DABCD1234E1Z8'
    },
    {
        'id': 5,
        'name': 'Government Senior Secondary School',
        'school_code': 'GSSS001',
        'type': 'Government',
        'address': '202 Public Sector, Faridabad',
        'city': 'Faridabad',
        'phone': '0129-6789012',
        'email': 'gsss.fbd@edu.gov.in',
        'principal_name': 'Mr. Harish Yadav',
        'contact_person': 'Mr. Rakesh Kumar',
        'contact_person_phone': '9876543214',
        'student_count': 2200,
        'contract_status': 'Inactive',
        'contract_start': '2022-09-01',
        'contract_end': '2023-08-31',
        'monthly_fee': 100000,
        'payment_status': 'Paid',
        'assigned_buses': ['BUS-007', 'BUS-008'],
        'pickup_time': '07:15',
        'drop_time': '14:15',
        'billing_address': 'GSSS Faridabad',
        'gst_number': '06EABCD1234E1Z9'
    }
]

# Available buses for assignment
AVAILABLE_BUSES = ['BUS-001', 'BUS-002', 'BUS-003', 'BUS-004', 'BUS-005', 'BUS-006', 'BUS-007', 'BUS-008', 'BUS-009', 'BUS-010']

# School types
SCHOOL_TYPES = ['Private', 'Government', 'International', 'CBSE', 'ICSE', 'State Board']
CONTRACT_STATUSES = ['Active', 'Inactive', 'Expiring Soon', 'Negotiation', 'Terminated']
PAYMENT_STATUSES = ['Paid', 'Pending', 'Overdue', 'Partially Paid']


class SchoolManagementPage(QWidget):
    """
    Main School Management Page - To be integrated into the main application
    """
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize the UI"""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Page header
        header_label = QLabel("🏫 School Management")
        header_label.setFont(QFont("Segoe UI", 20, QFont.Bold))
        header_label.setStyleSheet("color: #2c3e50;")
        main_layout.addWidget(header_label)
        
        # Add separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)
        
        # Create tab widget for different school management sections
        self.tab_widget = QTabWidget()
        
        # Create tabs
        self.school_list_tab = SchoolListTab()
        self.school_form_tab = SchoolFormTab()
        self.school_bus_assignment_tab = SchoolBusAssignmentTab()
        
        # Add tabs
        self.tab_widget.addTab(self.school_list_tab, "School List")
        self.tab_widget.addTab(self.school_form_tab, "Add/Edit School")
        self.tab_widget.addTab(self.school_bus_assignment_tab, "Bus Assignment")
        
        main_layout.addWidget(self.tab_widget)
        
        # Add status label at bottom
        self.status_label = QLabel("Ready")
        self.status_label.setFont(QFont("Segoe UI", 9))
        self.status_label.setStyleSheet("color: #7f8c8d;")
        main_layout.addWidget(self.status_label)


class SchoolListTab(QWidget):
    """Tab for listing and managing schools"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_schools()
        
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Search and filter section
        filter_widget = QWidget()
        filter_layout = QHBoxLayout(filter_widget)
        
        # Search input
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name, location, code...")
        self.search_input.setFixedWidth(250)
        self.search_input.textChanged.connect(self.filter_schools)
        filter_layout.addWidget(self.search_input)
        
        # Contract status filter
        filter_layout.addWidget(QLabel("Contract Status:"))
        self.contract_filter = QComboBox()
        self.contract_filter.addItems(["All"] + CONTRACT_STATUSES)
        self.contract_filter.currentTextChanged.connect(self.filter_schools)
        self.contract_filter.setFixedWidth(150)
        filter_layout.addWidget(self.contract_filter)
        
        # School type filter
        filter_layout.addWidget(QLabel("School Type:"))
        self.type_filter = QComboBox()
        self.type_filter.addItems(["All"] + SCHOOL_TYPES)
        self.type_filter.currentTextChanged.connect(self.filter_schools)
        self.type_filter.setFixedWidth(150)
        filter_layout.addWidget(self.type_filter)
        
        # City filter
        filter_layout.addWidget(QLabel("City:"))
        self.city_filter = QComboBox()
        self.city_filter.addItems(["All", "Delhi", "Gurgaon", "Noida", "Faridabad", "Ghaziabad"])
        self.city_filter.currentTextChanged.connect(self.filter_schools)
        self.city_filter.setFixedWidth(120)
        filter_layout.addWidget(self.city_filter)
        
        filter_layout.addStretch()
        
        # Export buttons
        export_excel_btn = QPushButton("Export to Excel")
        export_excel_btn.clicked.connect(self.export_to_excel)
        filter_layout.addWidget(export_excel_btn)
        
        export_pdf_btn = QPushButton("Export to PDF")
        export_pdf_btn.clicked.connect(self.export_to_pdf)
        filter_layout.addWidget(export_pdf_btn)
        
        layout.addWidget(filter_widget)
        
        # School table
        self.school_table = QTableWidget()
        self.school_table.setColumnCount(10)
        self.school_table.setHorizontalHeaderLabels([
            "School Name", "Code", "Type", "Location", 
            "Contact Person", "Phone", "Contract Status", 
            "Monthly Fee", "Assigned Buses", "Students"
        ])
        self.school_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.school_table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        layout.addWidget(self.school_table)
        
        # Action buttons section
        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        
        # Bulk operations
        bulk_label = QLabel("Bulk Operations:")
        action_layout.addWidget(bulk_label)
        
        self.bulk_action = QComboBox()
        self.bulk_action.addItems(["Update Contract Status", "Generate Invoices", "Export Selected", "Print Contracts"])
        action_layout.addWidget(self.bulk_action)
        
        bulk_apply_btn = QPushButton("Apply")
        bulk_apply_btn.clicked.connect(self.apply_bulk_operation)
        action_layout.addWidget(bulk_apply_btn)
        
        action_layout.addStretch()
        
        # Individual action buttons
        view_btn = QPushButton("View Details")
        view_btn.clicked.connect(self.view_details)
        action_layout.addWidget(view_btn)
        
        edit_btn = QPushButton("Edit School")
        edit_btn.clicked.connect(self.edit_school)
        action_layout.addWidget(edit_btn)
        
        assign_bus_btn = QPushButton("Assign Buses")
        assign_bus_btn.clicked.connect(self.assign_buses)
        action_layout.addWidget(assign_bus_btn)
        
        contract_btn = QPushButton("View Contract")
        contract_btn.clicked.connect(self.view_contract)
        action_layout.addWidget(contract_btn)
        
        delete_btn = QPushButton("Delete School")
        delete_btn.clicked.connect(self.delete_school)
        action_layout.addWidget(delete_btn)
        
        layout.addWidget(action_widget)
        
    def load_schools(self):
        """Load schools into the table"""
        self.school_table.setRowCount(len(MOCK_SCHOOLS))
        
        for row, school in enumerate(MOCK_SCHOOLS):
            # School Name
            item = QTableWidgetItem(school['name'])
            self.school_table.setItem(row, 0, item)
            
            # School Code
            item = QTableWidgetItem(school['school_code'])
            self.school_table.setItem(row, 1, item)
            
            # School Type
            item = QTableWidgetItem(school['type'])
            self.school_table.setItem(row, 2, item)
            
            # Location (City)
            item = QTableWidgetItem(school['city'])
            self.school_table.setItem(row, 3, item)
            
            # Contact Person
            item = QTableWidgetItem(school['contact_person'])
            self.school_table.setItem(row, 4, item)
            
            # Phone
            item = QTableWidgetItem(school['phone'])
            self.school_table.setItem(row, 5, item)
            
            # Contract Status with color coding
            contract_item = QTableWidgetItem(school['contract_status'])
            if school['contract_status'] == 'Active':
                contract_item.setBackground(QColor(220, 255, 220))
                contract_item.setForeground(QColor(0, 100, 0))
            elif school['contract_status'] == 'Expiring Soon':
                contract_item.setBackground(QColor(255, 255, 200))
                contract_item.setForeground(QColor(153, 102, 0))
            elif school['contract_status'] == 'Inactive':
                contract_item.setBackground(QColor(255, 220, 220))
                contract_item.setForeground(QColor(139, 0, 0))
            else:
                contract_item.setBackground(QColor(230, 230, 230))
                contract_item.setForeground(QColor(100, 100, 100))
            contract_item.setTextAlignment(Qt.AlignCenter)
            self.school_table.setItem(row, 6, contract_item)
            
            # Monthly Fee
            item = QTableWidgetItem(f"₹ {school['monthly_fee']:,}")
            item.setTextAlignment(Qt.AlignRight)
            self.school_table.setItem(row, 7, item)
            
            # Assigned Buses
            buses_text = ", ".join(school['assigned_buses']) if school['assigned_buses'] else "None"
            item = QTableWidgetItem(buses_text)
            self.school_table.setItem(row, 8, item)
            
            # Students
            item = QTableWidgetItem(f"{school['student_count']:,}")
            item.setTextAlignment(Qt.AlignCenter)
            self.school_table.setItem(row, 9, item)
            
    def filter_schools(self):
        """Filter schools based on search and filter criteria"""
        search_text = self.search_input.text().lower()
        contract_filter = self.contract_filter.currentText()
        type_filter = self.type_filter.currentText()
        city_filter = self.city_filter.currentText()
        
        for row in range(self.school_table.rowCount()):
            show_row = True
            
            # Search filter
            if search_text:
                row_text = ''
                for col in range(self.school_table.columnCount()):
                    item = self.school_table.item(row, col)
                    if item:
                        row_text += item.text().lower() + ' '
                if search_text not in row_text:
                    show_row = False
            
            # Contract status filter
            if contract_filter != 'All':
                contract_item = self.school_table.item(row, 6)
                if contract_item and contract_item.text() != contract_filter:
                    show_row = False
            
            # School type filter
            if type_filter != 'All':
                type_item = self.school_table.item(row, 2)
                if type_item and type_item.text() != type_filter:
                    show_row = False
            
            # City filter
            if city_filter != 'All':
                city_item = self.school_table.item(row, 3)
                if city_item and city_item.text() != city_filter:
                    show_row = False
            
            self.school_table.setRowHidden(row, not show_row)
            
    def get_selected_school(self):
        """Get the currently selected school"""
        selected_items = self.school_table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            return MOCK_SCHOOLS[row] if row < len(MOCK_SCHOOLS) else None
        return None
        
    def view_details(self):
        """View details of selected school"""
        school = self.get_selected_school()
        if school:
            dialog = SchoolDetailsDialog(school)
            dialog.exec_()
        else:
            QMessageBox.warning(self, "No Selection", 
                              "Please select a school first")
            
    def edit_school(self):
        """Edit selected school"""
        school = self.get_selected_school()
        if school:
            # Switch to school form tab with edit mode
            parent = self.parent().parent().parent()  # Get SchoolManagementPage
            if hasattr(parent, 'tab_widget'):
                parent.tab_widget.setCurrentIndex(1)  # Switch to form tab
                parent.school_form_tab.load_school_data(school)
        else:
            QMessageBox.warning(self, "No Selection", 
                              "Please select a school first")
            
    def assign_buses(self):
        """Assign buses to selected school"""
        school = self.get_selected_school()
        if school:
            # Switch to bus assignment tab
            parent = self.parent().parent().parent()  # Get SchoolManagementPage
            if hasattr(parent, 'tab_widget'):
                parent.tab_widget.setCurrentIndex(2)  # Switch to bus assignment tab
                parent.school_bus_assignment_tab.load_school_data(school)
        else:
            QMessageBox.warning(self, "No Selection", 
                              "Please select a school first")
            
    def view_contract(self):
        """View contract of selected school"""
        school = self.get_selected_school()
        if school:
            dialog = ContractDetailsDialog(school)
            dialog.exec_()
        else:
            QMessageBox.warning(self, "No Selection", 
                              "Please select a school first")
            
    def delete_school(self):
        """Delete selected school"""
        school = self.get_selected_school()
        if school:
            reply = QMessageBox.question(self, "Confirm Delete",
                                       f"Delete school {school['name']}?",
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                QMessageBox.information(self, "Success", 
                                      f"School {school['name']} deleted (demo mode)")
        else:
            QMessageBox.warning(self, "No Selection", 
                              "Please select a school first")
            
    def apply_bulk_operation(self):
        """Apply bulk operation"""
        operation = self.bulk_action.currentText()
        
        if operation == "Update Contract Status":
            status, ok = QInputDialog.getItem(self, "Update Contract Status", 
                                            "Select new status:", CONTRACT_STATUSES, 0, False)
            if ok and status:
                QMessageBox.information(self, "Bulk Update", 
                                      f"Updated contract status to {status} for selected schools (demo mode)")
        elif operation == "Generate Invoices":
            month, ok = QInputDialog.getItem(self, "Generate Invoices", 
                                           "Select month:", ["January", "February", "March", "April", 
                                                           "May", "June", "July", "August", 
                                                           "September", "October", "November", "December"], 0, False)
            if ok and month:
                QMessageBox.information(self, "Invoice Generation", 
                                      f"Invoices generated for {month} (demo mode)")
        else:
            QMessageBox.information(self, "Bulk Operation", 
                                  f"{operation} applied to selected schools (demo mode)")
        
    def export_to_excel(self):
        """Export to Excel"""
        QMessageBox.information(self, "Export", 
                              "School data exported to Excel (demo mode)")
        
    def export_to_pdf(self):
        """Export to PDF"""
        QMessageBox.information(self, "Export", 
                              "School data exported to PDF (demo mode)")


class SchoolFormTab(QWidget):
    """Tab for adding/editing school details"""
    
    def __init__(self):
        super().__init__()
        self.current_school = None
        self.init_ui()
        
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Form title
        self.form_title = QLabel("Add New School")
        self.form_title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        layout.addWidget(self.form_title)
        
        # Create scroll area for long form
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        # Create tab widget for form sections
        form_tabs = QTabWidget()
        
        # Basic Information Tab
        basic_tab = self.create_basic_info_tab()
        form_tabs.addTab(basic_tab, "Basic Information")
        
        # Contact Information Tab
        contact_tab = self.create_contact_info_tab()
        form_tabs.addTab(contact_tab, "Contact Information")
        
        # Contract & Billing Tab
        contract_tab = self.create_contract_billing_tab()
        form_tabs.addTab(contract_tab, "Contract & Billing")
        
        # Transportation Details Tab
        transport_tab = self.create_transport_details_tab()
        form_tabs.addTab(transport_tab, "Transportation Details")
        
        scroll_layout.addWidget(form_tabs)
        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)
        
        # Form buttons
        button_layout = QHBoxLayout()
        
        self.save_btn = QPushButton("Save School")
        self.save_btn.clicked.connect(self.save_school)
        button_layout.addWidget(self.save_btn)
        
        clear_btn = QPushButton("Clear Form")
        clear_btn.clicked.connect(self.clear_form)
        button_layout.addWidget(clear_btn)
        
        layout.addLayout(button_layout)
        
        # Status label
        self.status_label = QLabel("")
        self.status_label.setFont(QFont("Segoe UI", 9))
        layout.addWidget(self.status_label)
        
    def create_basic_info_tab(self):
        """Create basic information tab"""
        tab = QWidget()
        layout = QFormLayout(tab)
        layout.setSpacing(10)
        
        # School Name
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter school name")
        layout.addRow("School Name*:", self.name_input)
        
        # School Code
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Enter school code")
        layout.addRow("School Code*:", self.code_input)
        
        # School Type
        self.type_combo = QComboBox()
        self.type_combo.addItems(SCHOOL_TYPES)
        layout.addRow("School Type*:", self.type_combo)
        
        # Address
        self.address_input = QTextEdit()
        self.address_input.setMaximumHeight(60)
        self.address_input.setPlaceholderText("Enter school address")
        layout.addRow("Address*:", self.address_input)
        
        # City
        self.city_input = QComboBox()
        self.city_input.setEditable(True)
        self.city_input.addItems(["Delhi", "Gurgaon", "Noida", "Faridabad", "Ghaziabad", "Other"])
        layout.addRow("City*:", self.city_input)
        
        # Student Count
        self.student_count = QSpinBox()
        self.student_count.setRange(0, 10000)
        self.student_count.setValue(1000)
        self.student_count.setSingleStep(100)
        layout.addRow("Student Count:", self.student_count)
        
        # Establishment Year
        self.establishment_year = QSpinBox()
        self.establishment_year.setRange(1900, datetime.datetime.now().year)
        self.establishment_year.setValue(2000)
        layout.addRow("Establishment Year:", self.establishment_year)
        
        return tab
        
    def create_contact_info_tab(self):
        """Create contact information tab"""
        tab = QWidget()
        layout = QFormLayout(tab)
        layout.setSpacing(10)
        
        # Principal Name
        self.principal_name = QLineEdit()
        self.principal_name.setPlaceholderText("Enter principal name")
        layout.addRow("Principal Name*:", self.principal_name)
        
        # School Phone
        self.school_phone = QLineEdit()
        self.school_phone.setPlaceholderText("Enter school phone number")
        layout.addRow("School Phone*:", self.school_phone)
        
        # School Email
        self.school_email = QLineEdit()
        self.school_email.setPlaceholderText("Enter school email")
        layout.addRow("School Email:", self.school_email)
        
        # Contact Person Name
        self.contact_person = QLineEdit()
        self.contact_person.setPlaceholderText("Enter contact person name")
        layout.addRow("Contact Person*:", self.contact_person)
        
        # Contact Person Phone
        self.contact_phone = QLineEdit()
        self.contact_phone.setPlaceholderText("Enter contact person phone")
        self.contact_phone.setInputMask("9999999999")
        layout.addRow("Contact Person Phone*:", self.contact_phone)
        
        # Contact Person Email
        self.contact_email = QLineEdit()
        self.contact_email.setPlaceholderText("Enter contact person email")
        layout.addRow("Contact Person Email:", self.contact_email)
        
        # Designation
        self.designation = QComboBox()
        self.designation.addItems(["Transport In-charge", "Administrator", "Principal", "Accountant", "Other"])
        layout.addRow("Designation:", self.designation)
        
        return tab
        
    def create_contract_billing_tab(self):
        """Create contract and billing tab"""
        tab = QWidget()
        layout = QFormLayout(tab)
        layout.setSpacing(10)
        
        # Contract Status
        self.contract_status = QComboBox()
        self.contract_status.addItems(CONTRACT_STATUSES)
        layout.addRow("Contract Status:", self.contract_status)
        
        # Contract Start Date
        self.contract_start = QDateEdit()
        self.contract_start.setCalendarPopup(True)
        self.contract_start.setDate(QDate.currentDate())
        layout.addRow("Contract Start Date*:", self.contract_start)
        
        # Contract End Date
        self.contract_end = QDateEdit()
        self.contract_end.setCalendarPopup(True)
        self.contract_end.setDate(QDate.currentDate().addYears(1))
        layout.addRow("Contract End Date*:", self.contract_end)
        
        # Monthly Fee
        self.monthly_fee = QDoubleSpinBox()
        self.monthly_fee.setRange(0, 1000000)
        self.monthly_fee.setPrefix("₹ ")
        self.monthly_fee.setValue(100000)
        self.monthly_fee.setSingleStep(10000)
        layout.addRow("Monthly Fee*:", self.monthly_fee)
        
        # Payment Status
        self.payment_status = QComboBox()
        self.payment_status.addItems(PAYMENT_STATUSES)
        layout.addRow("Payment Status:", self.payment_status)
        
        # Billing Address
        self.billing_address = QTextEdit()
        self.billing_address.setMaximumHeight(60)
        self.billing_address.setPlaceholderText("Enter billing address")
        layout.addRow("Billing Address:", self.billing_address)
        
        # GST Number
        self.gst_number = QLineEdit()
        self.gst_number.setPlaceholderText("Enter GST number")
        layout.addRow("GST Number:", self.gst_number)
        
        # Contract Terms
        self.contract_terms = QTextEdit()
        self.contract_terms.setMaximumHeight(80)
        self.contract_terms.setPlaceholderText("Enter contract terms and conditions")
        layout.addRow("Contract Terms:", self.contract_terms)
        
        return tab
        
    def create_transport_details_tab(self):
        """Create transportation details tab"""
        tab = QWidget()
        layout = QFormLayout(tab)
        layout.setSpacing(10)
        
        # Pickup Time
        self.pickup_time = QTimeEdit()
        self.pickup_time.setTime(datetime.time(7, 30))
        layout.addRow("Morning Pickup Time:", self.pickup_time)
        
        # Drop Time
        self.drop_time = QTimeEdit()
        self.drop_time.setTime(datetime.time(14, 30))
        layout.addRow("Afternoon Drop Time:", self.drop_time)
        
        # Number of Buses Required
        self.buses_required = QSpinBox()
        self.buses_required.setRange(0, 20)
        self.buses_required.setValue(2)
        layout.addRow("Buses Required:", self.buses_required)
        
        # Special Requirements
        self.special_requirements = QTextEdit()
        self.special_requirements.setMaximumHeight(60)
        self.special_requirements.setPlaceholderText("Any special transportation requirements")
        layout.addRow("Special Requirements:", self.special_requirements)
        
        # Route Description
        self.route_description = QTextEdit()
        self.route_description.setMaximumHeight(80)
        self.route_description.setPlaceholderText("Describe pickup/drop routes")
        layout.addRow("Route Description:", self.route_description)
        
        # Notes
        self.notes_input = QTextEdit()
        self.notes_input.setMaximumHeight(60)
        self.notes_input.setPlaceholderText("Additional notes")
        layout.addRow("Notes:", self.notes_input)
        
        return tab
        
    def load_school_data(self, school_data):
        """Load existing school data into form"""
        self.current_school = school_data
        self.form_title.setText(f"Edit School: {school_data['name']}")
        
        # Basic information
        self.name_input.setText(school_data['name'])
        self.code_input.setText(school_data['school_code'])
        self.type_combo.setCurrentText(school_data['type'])
        self.address_input.setPlainText(school_data['address'])
        self.city_input.setCurrentText(school_data['city'])
        self.student_count.setValue(school_data['student_count'])
        
        # Contact information
        self.principal_name.setText(school_data['principal_name'])
        self.school_phone.setText(school_data['phone'])
        self.school_email.setText(school_data['email'])
        self.contact_person.setText(school_data['contact_person'])
        self.contact_phone.setText(school_data['contact_person_phone'])
        
        # Contract & billing
        self.contract_status.setCurrentText(school_data['contract_status'])
        contract_start = QDate.fromString(school_data['contract_start'], 'yyyy-MM-dd')
        self.contract_start.setDate(contract_start)
        contract_end = QDate.fromString(school_data['contract_end'], 'yyyy-MM-dd')
        self.contract_end.setDate(contract_end)
        self.monthly_fee.setValue(school_data['monthly_fee'])
        self.payment_status.setCurrentText(school_data['payment_status'])
        self.billing_address.setPlainText(school_data['billing_address'])
        self.gst_number.setText(school_data['gst_number'])
        
        # Transportation details
        pickup_time = datetime.datetime.strptime(school_data['pickup_time'], '%H:%M').time()
        self.pickup_time.setTime(pickup_time)
        drop_time = datetime.datetime.strptime(school_data['drop_time'], '%H:%M').time()
        self.drop_time.setTime(drop_time)
        self.buses_required.setValue(len(school_data['assigned_buses']))
        
    def clear_form(self):
        """Clear the form"""
        self.current_school = None
        self.form_title.setText("Add New School")
        
        # Clear all fields
        self.name_input.clear()
        self.code_input.clear()
        self.type_combo.setCurrentIndex(0)
        self.address_input.clear()
        self.city_input.setCurrentIndex(0)
        self.student_count.setValue(1000)
        self.establishment_year.setValue(2000)
        
        self.principal_name.clear()
        self.school_phone.clear()
        self.school_email.clear()
        self.contact_person.clear()
        self.contact_phone.clear()
        self.contact_email.clear()
        self.designation.setCurrentIndex(0)
        
        self.contract_status.setCurrentIndex(0)
        self.contract_start.setDate(QDate.currentDate())
        self.contract_end.setDate(QDate.currentDate().addYears(1))
        self.monthly_fee.setValue(100000)
        self.payment_status.setCurrentIndex(0)
        self.billing_address.clear()
        self.gst_number.clear()
        self.contract_terms.clear()
        
        self.pickup_time.setTime(datetime.time(7, 30))
        self.drop_time.setTime(datetime.time(14, 30))
        self.buses_required.setValue(2)
        self.special_requirements.clear()
        self.route_description.clear()
        self.notes_input.clear()
        
        self.status_label.setText("Form cleared")
        
    def save_school(self):
        """Save school data"""
        # Basic validation
        if not self.name_input.text().strip():
            self.status_label.setText("Error: School name is required")
            return
            
        if not self.code_input.text().strip():
            self.status_label.setText("Error: School code is required")
            return
            
        if not self.principal_name.text().strip():
            self.status_label.setText("Error: Principal name is required")
            return
            
        if not self.school_phone.text().strip():
            self.status_label.setText("Error: School phone is required")
            return
            
        # Save logic (in real app, this would save to database)
        if self.current_school:
            action = "updated"
        else:
            action = "added"
            
        QMessageBox.information(self, "Success", 
                              f"School {action} successfully!")
        self.status_label.setText(f"School {action} at {datetime.datetime.now().strftime('%H:%M:%S')}")
        
        # Switch back to school list
        parent = self.parent().parent().parent()  # Get SchoolManagementPage
        if hasattr(parent, 'tab_widget'):
            parent.tab_widget.setCurrentIndex(0)  # Switch to list tab


class SchoolDetailsDialog(QDialog):
    """Dialog to display school details"""
    
    def __init__(self, school_data, parent=None):
        super().__init__(parent)
        self.school_data = school_data
        self.setWindowTitle(f"School Details - {school_data['name']}")
        self.setGeometry(100, 100, 700, 600)
        self.init_ui()
        
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout(self)
        
        # School information display
        info_text = f"""
        <b>School Name:</b> {self.school_data['name']}<br>
        <b>School Code:</b> {self.school_data['school_code']}<br>
        <b>Type:</b> {self.school_data['type']}<br>
        <b>Address:</b> {self.school_data['address']}<br>
        <b>City:</b> {self.school_data['city']}<br>
        <b>Phone:</b> {self.school_data['phone']}<br>
        <b>Email:</b> {self.school_data['email']}<br>
        <b>Principal:</b> {self.school_data['principal_name']}<br>
        <b>Contact Person:</b> {self.school_data['contact_person']}<br>
        <b>Contact Phone:</b> {self.school_data['contact_person_phone']}<br>
        <b>Student Count:</b> {self.school_data['student_count']}<br>
        <b>Contract Status:</b> {self.school_data['contract_status']}<br>
        <b>Monthly Fee:</b> ₹ {self.school_data['monthly_fee']:,}<br>
        <b>Payment Status:</b> {self.school_data['payment_status']}<br>
        <b>Assigned Buses:</b> {', '.join(self.school_data['assigned_buses']) or 'None'}<br>
        <b>GST Number:</b> {self.school_data['gst_number']}
        """
        
        info_label = QLabel(info_text)
        info_label.setWordWrap(True)
        layout.addWidget(info_label)
        
        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn)


class ContractDetailsDialog(QDialog):
    """Dialog to display contract details"""
    
    def __init__(self, school_data, parent=None):
        super().__init__(parent)
        self.school_data = school_data
        self.setWindowTitle(f"Contract Details - {school_data['name']}")
        self.setGeometry(100, 100, 700, 600)
        self.init_ui()
        
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout(self)
        
        # Contract information display
        contract_text = f"""
        <b>School Name:</b> {self.school_data['name']}<br>
        <b>Contract Status:</b> {self.school_data['contract_status']}<br>
        <b>Contract Start Date:</b> {self.school_data['contract_start']}<br>
        <b>Contract End Date:</b> {self.school_data['contract_end']}<br>
        <b>Monthly Fee:</b> ₹ {self.school_data['monthly_fee']:,}<br>
        <b>Payment Status:</b> {self.school_data['payment_status']}<br>
        <b>Billing Address:</b> {self.school_data['billing_address']}<br>
        <b>GST Number:</b> {self.school_data['gst_number']}
        """
        
        contract_label = QLabel(contract_text)
        contract_label.setWordWrap(True)
        layout.addWidget(contract_label)
        
        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn)


class SchoolBusAssignmentTab(QWidget):
    """Tab for assigning buses to schools"""
    
    def __init__(self):
        super().__init__()
        self.current_school = None
        self.init_ui()
        
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)