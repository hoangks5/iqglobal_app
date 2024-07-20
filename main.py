from untitled import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt6.QtCore import QRect, QPropertyAnimation, QEasingCurve, QAbstractAnimation
from PyQt6.QtWidgets import QPushButton
import sys
from realtime_chart import RealTimeChart, WebSocketListener # Assuming you save the RealTimeChart class in a file named realtime_chart.py
import requests
import json
from utils import *
import time
import os
from datetime import datetime
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        # Instantiate RealTimeChart and add it to the chartContainer
        self.real_time_chart = RealTimeChart(parent=self.ui.widget)
        self.real_time_chart.setGeometry(self.ui.widget.rect())
        self.real_time_chart.show()
        # ẩn groupBox
        self.ui.groupBox.hide()
        self.ui.groupBox_2.hide()
        self.ui.label_3.raise_()
        self.last_signal = None
        self.session = None
        self.load_login()
        self.setFixedSize(self.size())
        
    def save_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        key = self.ui.lineEdit_3.text()
        with open('data/login.json', 'w') as f:
            json.dump({'username': username, 'password': password, 'key': key}, f)
    
    
    def load_login(self):
        try:
            with open('data/login.json', 'r') as f:
                data = json.load(f)
                self.ui.lineEdit.setText(data['username'])
                self.ui.lineEdit_2.setText(data['password'])
                self.ui.lineEdit_3.setText(data['key'])
        except:
            pass
    

    def login(self):
        self.save_login()
        self.session = requests.Session()
        url = "https://api.iqglobal.org/api/v1/web/auth/login"
        payload = json.dumps({
        "email": self.ui.lineEdit.text(),
        "username": self.ui.lineEdit.text(),
        "password": self.ui.lineEdit_2.text()
        })
        headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://app.iqglobal.org',
        'priority': 'u=1, i',
        'referer': 'https://app.iqglobal.org/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }
        self.session.headers.update(headers)
        response = self.session.post(url, headers=headers, data=payload)
        if response.json()['meta']['status'] == 200:
            # add cookie to session
            self.session.headers.update({'authorization': 'Bearer ' + response.json()['data']['accessToken']})
            self.load_info_account()
        else:
            QMessageBox.warning(self, 'Error', response.json()['meta']['externalMessage'])
            return
    
    def get_info_account(self):
        url = "https://api.iqglobal.org/api/v1/web/users/mine"
        response = self.session.get(url)
        if response.json()['meta']['status'] == 200:
            return response.json()
        else:
            return None
        
    def get_balance(self):
        url = "https://api.iqglobal.org/api/v1/web/users/mine"
        response = self.session.get(url)
        if response.json()['meta']['status'] == 200:
            self.ui.lineEdit_9.setText(str(response.json()['data']['balance']))
            return response.json()['data']['balance']
        else:
            return None
        
    def load_info_account(self):
        info = self.get_info_account()
        if info:
            QMessageBox.information(self, 'Success', 'Login success')
            self.ui.groupBox.show()
            self.ui.lineEdit_4.setText(info['data']['email'])
            #self.ui.lineEdit_5.setText(info['data']['name'])
            self.ui.lineEdit_8.setText(info['data']['shortId'])
            
            
            self.ui.lineEdit_9.setText(str(info['data']['balance']))
            #self.ui.lineEdit_6.setText(info['data']['tronWalletAddress'])
            #self.ui.lineEdit_7.setText(info['data']['bscWalletAddress'])
        else:
            QMessageBox.warning(self, 'Error', 'Username or password is invalid')
    
    def check_key(self):
        self.save_login()
        # kiểm tra xem đã login chưa bằng cách lấy thông tin account
        if self.ui.groupBox.isVisible() == False:
            QMessageBox.warning(self, 'Error', 'Bạn chưa đăng nhập')
            return
        key = self.ui.lineEdit_3.text()
        log = {
            "username": self.ui.lineEdit.text(),
            "password": self.ui.lineEdit_2.text(),
            "name_pc": os.getlogin(),
            "ip": requests.get('https://api64.ipify.org').text,
            "time": time.time()
        }
        status = call_check_key(key, log)
        if status['status'] == 'active':
            time_use = datetime.strptime(status['expired_time'], '%Y-%m-%d %H:%M:%S') - datetime.now()
            QMessageBox.information(self, 'Success', 'Thời gian sử dụng key còn lại: ' + str(time_use))
            self.ui.groupBox_2.show()
        if status['status'] == 'error':
            QMessageBox.warning(self, 'Error', status['message'])
            return
        
    def buy(self, tick):
        current_time = time.time()
        last_price = tick['price']
        self.ui.lineEdit_18.setText(str(last_price))

        if self.last_signal is None:
            self.ui.lineEdit_21.setText('Phiên giao dịch trước chưa kết thúc, đang chờ phiên giao dịch mới')
            return

        if self.last_signal == 'UP':
            if self.ui.checkBox.isChecked() == False:
                return
            self.ui.lineEdit_21.setText(f'Tín hiệu trước là UP, AI đang phân tích và dự đoán vào lệnh UP tiếp theo')
            time_remaining = 60 - (current_time - self.time_1)

            if time_remaining > 10:
                if last_price > self.open_price:
                    self.ui.lineEdit_21.setText(f'Giá hiện tại {last_price} đang tăng, còn {int(time_remaining)} giây để AI phân tích và dự đoán')
                    self.ui.lineEdit_19.setText('UP')
                    return
                else:
                    self.ui.lineEdit_21.setText(f'Giá hiện tại {last_price} đang giảm, AI đang phân tích và dự đoán đợi giá trị tăng')
                    self.ui.lineEdit_19.setText('DOWN')
                    return
            else:
                if last_price > self.open_price:
                    amount = self.ui.lineEdit_11.text()
                    signal = 'UP'
                    if self.id_session is None:
                        return
                    success, message = self.auto_buy(self.id_session, signal, amount)
                    if success:
                        self.ui.lineEdit_21.setText(f'Đã thực hiện lệnh mua UP thành công với giá {last_price}')
                        self.hold_signal = 'UP'
                        self.id_session = None
                        return
                    else:
                        self.ui.lineEdit_21.setText(f'Vào lệnh UP thất bại: {message}')
                        return
                else:
                    self.ui.lineEdit_21.setText(f'Không thực hiện lệnh vì giá hiện tại {last_price} đang giảm')
                    return

        else:  # self.last_signal == 'DOWN'
            if self.ui.checkBox_2.isChecked() == False:
                return
            self.ui.lineEdit_21.setText(f'Tín hiệu trước là DOWN, AI đang phân tích và dự đoán vào lệnh DOWN tiếp theo')
            time_remaining = 60 - (current_time - self.time_1)

            if time_remaining > 10:
                if last_price < self.open_price:
                    self.ui.lineEdit_21.setText(f'Giá hiện tại {last_price} đang giảm, còn {int(time_remaining)} giây để AI phân tích và dự đoán')
                    self.ui.lineEdit_19.setText('DOWN')
                    return
                else:
                    self.ui.lineEdit_21.setText(f'Giá hiện tại {last_price} đang tăng, AI đang phân tích và dự đoán đợi giá trị giảm')
                    self.ui.lineEdit_19.setText('UP')
                    return
            else:
                if last_price < self.open_price:
                    if self.id_session is None:
                        return
                    amount = self.ui.lineEdit_11.text()
                    signal = 'DOWN'
                    success, message = self.auto_buy(self.id_session, signal, amount)
                    if success:
                        self.ui.lineEdit_21.setText(f'Đã thực hiện lệnh mua DOWN thành công với giá {last_price}')
                        self.hold_signal = 'DOWN'
                        self.id_session = None
                        return
                    else:
                        self.ui.lineEdit_21.setText(f'Vào lệnh DOWN thất bại: {message}')
                        return
                else:
                    self.ui.lineEdit_21.setText(f'Không thực hiện lệnh vì giá hiện tại {last_price} đang tăng')
                    return


                
        
            
    def new_round(self, result):
        self.id_session = result['id']
        self.time_1 = time.time()
 
        balance = float(self.get_balance())
        stop_loss = self.ui.lineEdit_12.text()
        stop_win = self.ui.lineEdit_13.text()
        
        if stop_loss.isdigit():
            stop_loss = float(stop_loss)
            if balance < stop_loss:
                self.ui.lineEdit_21.setText('Số dư dưới mức stop loss, bot đã tắt')
                self.is_run_bot_1 = False
                self.web_socket_thread.stop()
                self.ui.pushButton_4.setText('Start Bot')
                self.ui.pushButton_4.setStyleSheet("font: 75 10pt \"Cascadia Mono\";\n"
"border-radius: 10px; \n"
"background-color: rgb(0, 255, 127);\n"
"color: rgb(255, 255, 255);")
                return
        if stop_win.isdigit():
            stop_win = float(stop_win)
            if balance > stop_win:
                self.ui.lineEdit_21.setText('Số dư vượt mức stop win, bot đã tắt')
                self.is_run_bot_1 = False
                self.web_socket_thread.stop()
                self.ui.pushButton_4.setText('Start Bot')
                self.ui.pushButton_4.setStyleSheet("font: 75 10pt \"Cascadia Mono\";\n"
"border-radius: 10px; \n"
"background-color: rgb(0, 255, 127);\n"
"color: rgb(255, 255, 255);")
                return
            
            
        
        
    def end_round(self, result):
        self.last_signal = result['positionWin']
        self.close_price = result['closePrice']
        self.open_price = self.close_price
        self.id_session_last = result['id']
        self.last_time_round = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        # load ui
        self.ui.lineEdit_17.setText(self.id_session_last)
        self.ui.lineEdit_20.setText(self.last_time_round)
        self.ui.lineEdit_15.setText(str(self.close_price))
        self.ui.lineEdit_16.setText(self.last_signal)
        
        # nơi kiểm tra lệnh hold_signal win hay lose
        try:
            if self.hold_signal == self.last_signal:
                # phát âm thanh win
                self.is_win = True
                self.hold_signal = None
            else:
                # phát âm thanh lose
                self.is_win = False
                self.hold_signal = None
        except:
            pass
        
        
    def start_bot(self):
        try:
            if self.is_run_bot_1 == True:
                self.is_run_bot_1 = False
                self.web_socket_thread.stop()
                self.ui.pushButton_4.setText('Start Bot')
                self.ui.pushButton_4.setStyleSheet("font: 75 10pt \"Cascadia Mono\";\n"
"border-radius: 10px; \n"
"background-color: rgb(0, 255, 127);\n"
"color: rgb(255, 255, 255);")
                QMessageBox.information(self, 'Success', 'Bot đã được tắt')
                return
        except Exception as e:
            pass
        
        if not self.ui.groupBox.isVisible():
            QMessageBox.warning(self, 'Error', 'Bạn chưa đăng nhập')
            return
        if self.ui.lineEdit_11.text().isnumeric() == False:
            QMessageBox.warning(self, 'Error', 'Số tiền phải là số')
            return
        if float(self.ui.lineEdit_11.text()) < 5:
            QMessageBox.warning(self, 'Error', 'Một lệnh tối thiểu là 5 USDT')
            return
        self.is_run_bot_1 = True
        # đổi màu nút thành màu đỏ và tên thành Stop
        self.ui.pushButton_4.setText('Stop Bot')
        self.ui.pushButton_4.setStyleSheet("font: 75 10pt \"Cascadia Mono\";\n"
"border-radius: 10px; \n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        # lấy thông tin session_id từ signal
        QMessageBox.information(self, 'Success', 'Bot đã được bật')
        self.web_socket_thread = WebSocketListener()
        self.web_socket_thread.end_round.connect(self.end_round)
        self.web_socket_thread.new_round.connect(self.new_round)
        self.web_socket_thread.new_tick.connect(self.buy)
        self.web_socket_thread.start()
        
        
    def auto_buy(self, id_session, signal, amount):
        url = f"https://api.iqglobal.org/api/v1/web/predicts/{id_session}"
        payload = json.dumps({
        "amount": amount,
        "position": signal
        })
        res = self.session.post(url, data=payload)
        if res.json()['meta']['status'] == 200:
            return True, res.json()['meta']['externalMessage']
        else:
            return False, res.json()['meta']['externalMessage']
        
   
        
    


            
    def connect_button(self):
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.check_key)
        self.ui.pushButton_4.clicked.connect(self.start_bot)
        self.ui.pushButton_5.clicked.connect(self.real_time_chart.turn_on_markes_bot_1)
        
        
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.connect_button()
    sys.exit(app.exec())