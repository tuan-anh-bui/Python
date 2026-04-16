import sys
import sqlite3
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import QDate

class HRManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(HRManager, self).__init__()
        # Load file UI từ Qt Designer
        uic.loadUi('main.ui', self)

        # Kết nối cơ sở dữ liệu
        self.init_db()

        # Thiết lập các sự kiện nút bấm
        self.btn_add.clicked.connect(self.add_hr)
        self.btn_update.clicked.connect(self.update_hr)
        self.btn_delete.clicked.connect(self.delete_hr)
        self.btn_clear.clicked.connect(self.clear_form)
        self.btn_search.clicked.connect(self.search_hr)
        self.btn_show_all.clicked.connect(self.load_data)
        
        # Sự kiện click vào dòng trong bảng
        self.table_hr.itemClicked.connect(self.fill_form_from_table)
        
        # Tự động căn chỉnh các cột của bảng
        self.table_hr.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Hiển thị dữ liệu ban đầu
        self.load_data()

    def init_db(self):
        """Khởi tạo cơ sở dữ liệu SQLite"""
        self.conn = sqlite3.connect('nhan_su.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS nhan_su (
                cccd TEXT PRIMARY KEY,
                name TEXT,
                dob TEXT,
                gender TEXT,
                address TEXT
            )
        ''')
        self.conn.commit()

    def load_data(self, query="SELECT * FROM nhan_su"):
        """Tải dữ liệu từ database lên bảng"""
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        
        self.table_hr.setRowCount(0)
        for row_index, row_data in enumerate(rows):
            self.table_hr.insertRow(row_index)
            for col_index, data in enumerate(row_data):
                self.table_hr.setItem(row_index, col_index, QTableWidgetItem(str(data)))

    def add_hr(self):
        """Thêm mới nhân sự"""
        cccd = self.edit_cccd.text().strip()
        name = self.edit_name.text().strip()
        dob = self.edit_dob.date().toString("dd/MM/yyyy")
        gender = self.combo_gender.currentText()
        address = self.edit_address.text().strip()

        if not cccd or not name:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập Số CCCD và Họ tên!")
            return

        try:
            self.cursor.execute("INSERT INTO nhan_su VALUES (?, ?, ?, ?, ?)", 
                                (cccd, name, dob, gender, address))
            self.conn.commit()
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Thành công", "Đã thêm nhân sự mới!")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Lỗi", "Số CCCD này đã tồn tại trong hệ thống!")

    def update_hr(self):
        """Cập nhật thông tin nhân sự"""
        cccd = self.edit_cccd.text().strip()
        name = self.edit_name.text().strip()
        dob = self.edit_dob.date().toString("dd/MM/yyyy")
        gender = self.combo_gender.currentText()
        address = self.edit_address.text().strip()

        if not cccd:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn nhân sự cần sửa (Số CCCD)!")
            return

        self.cursor.execute("UPDATE nhan_su SET name=?, dob=?, gender=?, address=? WHERE cccd=?", 
                            (name, dob, gender, address, cccd))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            self.load_data()
            QMessageBox.information(self, "Thành công", "Đã cập nhật thông tin!")
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy nhân sự có số CCCD này để cập nhật!")

    def delete_hr(self):
        """Xóa nhân sự"""
        cccd = self.edit_cccd.text().strip()
        if not cccd:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn nhân sự cần xóa (Số CCCD)!")
            return

        confirm = QMessageBox.question(self, "Xác nhận", f"Bạn có chắc chắn muốn xóa nhân sự có CCCD: {cccd}?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.cursor.execute("DELETE FROM nhan_su WHERE cccd=?", (cccd,))
            self.conn.commit()
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Thành công", "Đã xóa nhân sự!")

    def search_hr(self):
        """Tìm kiếm nhân sự theo CCCD, Tên hoặc Địa chỉ"""
        search_text = self.edit_search.text().strip()
        if not search_text:
            self.load_data()
            return

        query = f"SELECT * FROM nhan_su WHERE cccd LIKE '%{search_text}%' OR name LIKE '%{search_text}%' OR address LIKE '%{search_text}%'"
        self.load_data(query)

    def fill_form_from_table(self, item):
        """Điền thông tin từ dòng được chọn vào các ô nhập liệu"""
        row = item.row()
        self.edit_cccd.setText(self.table_hr.item(row, 0).text())
        self.edit_name.setText(self.table_hr.item(row, 1).text())
        
        # Chuyển đổi ngày sinh ngược lại để set vào QDateEdit
        date_str = self.table_hr.item(row, 2).text()
        self.edit_dob.setDate(QDate.fromString(date_str, "dd/MM/yyyy"))
        
        self.combo_gender.setCurrentText(self.table_hr.item(row, 3).text())
        self.edit_address.setText(self.table_hr.item(row, 4).text())

    def clear_form(self):
        """Làm sạch các ô nhập liệu"""
        self.edit_cccd.clear()
        self.edit_name.clear()
        self.edit_dob.setDate(QDate.currentDate())
        self.combo_gender.setCurrentIndex(0)
        self.edit_address.clear()
        self.edit_search.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = HRManager()
    window.show()
    sys.exit(app.exec())
