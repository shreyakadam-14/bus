import sys
import re
from datetime import date, datetime

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QFormLayout, QMessageBox, QComboBox,
    QTableWidget, QTableWidgetItem
)

from database import (
    initialize_db, get_next_driver_id,
    insert_driver, fetch_all_drivers
)


class DriverForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Driver Details Form")
        self.setGeometry(100, 100, 450, 520)

        initialize_db()
        self.init_ui()
        self.load_driver_id()

    # UI
    def init_ui(self):
        form_layout = QFormLayout()

        self.driver_id_input = QLineEdit()
        self.driver_id_input.setReadOnly(True)

        self.name_input = QLineEdit()
        self.name_input.setMaxLength(100)

        self.dob_input = QLineEdit()
        self.dob_input.setPlaceholderText("DD-MM-YYYY")
        self.dob_input.setInputMask("00-00-0000")
        self.dob_input.textChanged.connect(self.update_age)

        self.age_display = QLineEdit()
        self.age_display.setReadOnly(True)

        self.gender_input = QComboBox()
        self.gender_input.addItems(["Select", "Male", "Female", "Other"])

        self.phone_input = QLineEdit()
        self.phone_input.setInputMask("0000000000")

        self.email_input = QLineEdit()

        self.submit_btn = QPushButton("Save Driver")
        self.submit_btn.clicked.connect(self.save_driver)

        self.view_btn = QPushButton("View Drivers")
        self.view_btn.clicked.connect(self.open_driver_list)

        form_layout.addRow("Driver ID:", self.driver_id_input)
        form_layout.addRow("Full Name:", self.name_input)
        form_layout.addRow("Date of Birth:", self.dob_input)
        form_layout.addRow("Age (Auto):", self.age_display)
        form_layout.addRow("Gender:", self.gender_input)
        form_layout.addRow("Phone:", self.phone_input)
        form_layout.addRow("Email ID:", self.email_input)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.submit_btn)
        layout.addWidget(self.view_btn)

        self.setLayout(layout)

    # DRIVER ID
    def load_driver_id(self):
        self.driver_id_input.setText(str(get_next_driver_id()))

    # VALIDATIONS
    def validate_name(self, name):
        return bool(re.fullmatch(r"[A-Za-z ]{1,100}", name))

    def validate_email(self, email):
        # ONLY gmail.com allowed
        pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
        return re.fullmatch(pattern, email)

    def validate_phone(self, phone):
        return re.fullmatch(r"[6-9]\d{9}", phone)

    def validate_and_calculate_age(self, dob_text):
        try:
            day, month, year = map(int, dob_text.split("-"))
            today = date.today()

            if year < 1960 or year > today.year:
                return False, f"Year must be between 1950 and {today.year}"

            if month < 1 or month > 12:
                return False, "Invalid month"

            if month in [4, 6, 9, 11]:
                max_days = 30
            elif month == 2:
                max_days = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
            else:
                max_days = 31

            if day < 1 or day > max_days:
                return False, "Invalid day"

            age = today.year - year - (
                (today.month, today.day) < (month, day)
            )

            if age < 18:
                return False, "Driver must be at least 18 years old"

            return True, age

        except:
            return False, "Invalid DOB format (DD-MM-YYYY)"

    # LIVE AGE UPDATE
    def update_age(self):
        dob_text = self.dob_input.text()
        if len(dob_text) < 10:
            self.age_display.clear()
            return

        valid, result = self.validate_and_calculate_age(dob_text)
        self.age_display.setText(str(result)) if valid else self.age_display.clear()

    # SAVE DRIVER
    def save_driver(self):
        name = self.name_input.text().strip()
        dob_text = self.dob_input.text().strip()
        gender = self.gender_input.currentText()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()

        if not all([name, dob_text, phone, email]):
            QMessageBox.warning(self, "Error", "All fields are required")
            return

        if not self.validate_name(name):
            QMessageBox.warning(self, "Error", "Invalid name")
            return

        valid, age = self.validate_and_calculate_age(dob_text)
        if not valid:
            QMessageBox.warning(self, "Error", age)
            return

        if gender == "Select":
            QMessageBox.warning(self, "Error", "Select gender")
            return

        if not self.validate_phone(phone):
            QMessageBox.warning(self, "Error", "Invalid phone number")
            return

        if not self.validate_email(email):
            QMessageBox.warning(self, "Error", "Only @gmail.com emails allowed")
            return

        dob_db = datetime.strptime(dob_text, "%d-%m-%Y").strftime("%Y-%m-%d")

        success, error = insert_driver(
            name, dob_db, age, gender, phone, email
        )

        if not success:
            if "phone" in error:
                QMessageBox.warning(self, "Error", "Phone already exists")
            elif "email" in error:
                QMessageBox.warning(self, "Error", "Email already exists")
            else:
                QMessageBox.warning(self, "Error", "Database error")
            return

        QMessageBox.information(self, "Success", "Driver saved successfully")
        self.clear_form()
        self.load_driver_id()

    # CLEAR FORM
    def clear_form(self):
        self.name_input.clear()
        self.dob_input.clear()
        self.age_display.clear()
        self.gender_input.setCurrentIndex(0)
        self.phone_input.clear()
        self.email_input.clear()

    # OPEN RETRIEVAL WINDOW
    def open_driver_list(self):
        self.driver_window = DriverListWindow()
        self.driver_window.show()


class DriverListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Saved Drivers")
        self.setGeometry(200, 200, 850, 400)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.load_data()

    def load_data(self):
        drivers = fetch_all_drivers()

        self.table.setRowCount(len(drivers))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Name", "DOB", "Age", "Gender", "Phone", "Email"]
        )

        for r, row in enumerate(drivers):
            for c, value in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(value)))

        self.table.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DriverForm()
    window.show()
    sys.exit(app.exec_())
