import sys
import re
from datetime import date, datetime

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QFormLayout, QMessageBox, QComboBox
)

from database import initialize_db, get_next_driver_id, insert_driver

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

        self.search_phone_input = QLineEdit()
        self.search_phone_input.setInputMask("0000000000")

        self.submit_btn = QPushButton("Save Driver")
        self.submit_btn.clicked.connect(self.save_driver)

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

        self.setLayout(layout)

    # DRIVER ID
    def load_driver_id(self):
        self.driver_id_input.setText(str(get_next_driver_id()))

    # VALIDATIONS
    def validate_name(self, name):
        if len(name) > 100:
            return False
        return bool(re.fullmatch(r"[A-Za-z ]+", name))

    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com$"
        return re.match(pattern, email)

    def validate_phone(self, phone):
        return re.match(r"^[6-9]\d{9}$", phone)

    def validate_and_calculate_age(self, dob_text):
        try:
            day, month, year = map(int, dob_text.split("-"))
            today = date.today()

            if year >= today.year:
                return False, "Year must be less than current year"

            if month < 1 or month > 12:
                return False, "Invalid month"

            if month in [4, 6, 9, 11]:
                max_days = 30
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                max_days = 31
            else:  # February
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    max_days = 29
                else:
                    max_days = 28

            if day < 1 or day > max_days:
                return False, "Invalid day for selected month"

            age = today.year - year - (
                (today.month, today.day) < (month, day)
            )

            if age < 18:
                return False, "Driver must be at least 18 years old"

            return True, age

        except ValueError:
            return False, "Invalid DOB format (DD-MM-YYYY)"

    # LIVE AGE
    def update_age(self):
        dob_text = self.dob_input.text()

        if len(dob_text) < 10:
            self.age_display.clear()
            return

        valid, result = self.validate_and_calculate_age(dob_text)
        if valid:
            self.age_display.setText(str(result))
        else:
            self.age_display.clear()

    # SAVE
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
            QMessageBox.warning(self, "Error", "Name must contain only letters and spaces (max 100 characters)")
            return

        valid, result = self.validate_and_calculate_age(dob_text)
        if not valid:
            QMessageBox.warning(self, "Error", result)
            return

        if gender == "Select":
            QMessageBox.warning(self, "Error", "Please select gender")
            return

        if not self.validate_phone(phone):
            QMessageBox.warning(self, "Error", "Phone must be 10 digits and start with 6–9")
            return

        if not self.validate_email(email):
            QMessageBox.warning(self, "Error", "Email must be valid and end with .com")
            return

        dob_db = datetime.strptime(dob_text, "%d-%m-%Y").strftime("%Y-%m-%d")

        success, error = insert_driver(
            name, dob_db, result, gender, phone, email
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

    # CLEAR
    def clear_form(self):
        self.name_input.clear()
        self.dob_input.clear()
        self.age_display.clear()
        self.gender_input.setCurrentIndex(0)
        self.phone_input.clear()
        self.email_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DriverForm()
    window.show()
    sys.exit(app.exec_())
