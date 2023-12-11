from PyQt6 import QtWidgets
import sys
SEP = 40

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('投資計算機')
        self.resize(800, 600)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.move(50,50)                       # 移動到 (50, 50) 的位置
        self.label_1.setText('請輸入初始金額')
        self.label_1.setStyleSheet('font-size:30px')
        self.input_1 = QtWidgets.QLineEdit(self)   # 建立單行輸入框
        self.input_1.setGeometry(50,50+SEP,200,30)     # 設定位置和尺寸
        self.input_1.setText("10000")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.move(50,50+SEP*2)
        self.label_2.setText('請輸入每年投入金額')
        self.label_2.setStyleSheet('font-size:30px')
        self.input_2 = QtWidgets.QLineEdit(self)   # 建立單行輸入框
        self.input_2.setGeometry(50,50+SEP*3,200,30)
        self.input_2.setText("10000")
        

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.move(50,50+SEP*4)
        self.label_3.setText('請選擇每年投資利率(單位：%)')
        self.label_3.setStyleSheet('font-size:30px')
        self.box = QtWidgets.QComboBox(self)   # 加入下拉選單
        self.box.addItems(['3','4','5','6','7'])   # 加入選項
        self.box.setGeometry(50,50+SEP*5,200,30)
        self.box.setCurrentText('3')
        
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.move(50,50+SEP*6)
        self.label_4.setText('請輸入投資年期(單位：年)')
        self.label_4.setStyleSheet('font-size:30px')
        self.input_3 = QtWidgets.QLineEdit(self)   # 建立單行輸入框
        self.input_3.setGeometry(50,50+SEP*7,200,30)
        self.input_3.setText("10")
        

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('開始計算')
        self.btn.setStyleSheet('font-size:30px')
        self.btn.setGeometry(50,50+SEP*8,150,50)
        self.btn.clicked.connect(lambda: self.count()) 

        
    
    def count(self):
        self.money = int(self.input_1.text())
        self.save = int(self.input_2.text())
        self.rate = int(self.box.currentText())
        self.years = int(self.input_3.text())

        self.futureValue = str(self.money*(1+self.rate/100)**self.years + self.save*((self.rate/100+1)**self.years-1)/self.rate*100)
        
        self.mbox = QtWidgets.QMessageBox(self)
        self.mbox.information(self, "計算結果", self.futureValue)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())