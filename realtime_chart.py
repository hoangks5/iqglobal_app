import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtCore import QThread, pyqtSignal
from lightweight_charts.widgets import QtChart
from websockets.sync.client import connect
from datetime import datetime
from utils import *

class WebSocketListenerChart(QThread):
    new_tick = pyqtSignal(pd.Series)
    new_bar = pyqtSignal(pd.Series)

    def __init__(self):
        super().__init__()
    def run(self):
        self.main()

    def write_data(self, open_price, high_price, low_price, close_price):
        with open('ohlc.csv', 'a') as f:
            date_tick = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            f.write(f'add,{date_tick},{open_price},{high_price},{low_price},{close_price}\n')
    
    def main(self):
        with connect("wss://api.iqglobal.org/socket.io/?EIO=4&transport=websocket") as websocket:
            websocket.send('40/users,')
            websocket.send('40/users,{"sid":"D916RbgrMhHafsICBLyX"}')
            message = websocket.recv()
            websocket.send('42/users,["users/JOIN",{"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2NjQ5YTU0MWJjYjc2ODk4MDJmN2NjZiIsImVtYWlsIjoiaG9hbmduZC51dGVAZ21haWwuY29tIiwiaWF0IjoxNzE4MDQxOTQzLCJleHAiOjE3MTg2NDY3NDN9.mYac1x8ZSbP5xX0scgMEJb7GQnxM5XF5VhqJLJunTrc"}]')
            data_session = []
            while True:
                try:
                    message = websocket.recv(timeout=10)
                except:
                    return self.main()
                if '40/users,{"sid' in message:
                    continue
                elif message == '2':
                    websocket.send('3')
                    message = websocket.recv()
        
        
                rs = get_data_last_price(message)
                if rs:
                    data_session.append(rs['lastPrice'])
                    date_tick = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                    data_update = [date_tick, rs['lastPrice']]
                    tick = pd.Series(data_update, index=['time', 'price'])
                    self.new_tick.emit(tick)
                    
                rs = get_data_last_round(message)
                if rs:
                    if len(data_session) == 0:
                        return self.main()
                    open_price = rs['lockPrice']
                    close_price = rs['closePrice']
                    high_price = max(data_session)
                    low_price = min(data_session)
                    bar = pd.Series([datetime.now().strftime('%Y-%m-%dT%H:%M:%S'), open_price, high_price, low_price, close_price], index=['date', 'open', 'high', 'low', 'close'])
                    self.new_bar.emit(bar)
                    self.write_data(open_price, high_price, low_price, close_price)
                    data_session = [ close_price ]


class RealTimeChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_markes_bot_1 = False
        
        self.layout = QVBoxLayout(self)
        self.chart = QtChart(self)
        self.layout.addWidget(self.chart.get_webview())
        
        self.chart.legend(True)
        self.chart.topbar.textbox('symbol', 'BTC/USDT')

        get_histories_1min()
        self.df = pd.read_csv('ohlc.csv')
        self.chart.set(self.df)

        self.web_socket_thread = WebSocketListenerChart()
        self.web_socket_thread.new_tick.connect(self.update_from_tick)
        self.web_socket_thread.new_bar.connect(self.update_chart)
        self.web_socket_thread.start()

    def turn_on_markes_bot_1(self):
        if self.is_markes_bot_1 == False:
            self.is_markes_bot_1 = True
            self.update_markes_bot_1()
        else:
            self.is_markes_bot_1 = False
            self.clear_chart()
        
    def update_markes_bot_1(self):
        self.df = pd.read_csv('ohlc.csv')
        win = 0
        lose = 0
        for i in range(len(self.df)):
            # kiểm tra nếu 2 cột trước liên tiếp đều là UP thì thêm marker cho cột sau là 'Nên vào UP'
            if i > 1 and self.df.loc[i-2, 'close'] - self.df.loc[i-2, 'open'] > 0 and self.df.loc[i-1, 'close'] - self.df.loc[i-1, 'open'] > 0:
                self.chart.marker(text='', color='green', position='above', shape='arrow_up', time=self.df.loc[i, 'date'])
                # kiểm tra cột i là up hay down
                if self.df.loc[i, 'close'] - self.df.loc[i, 'open'] > 0:
                    self.chart.marker(text='', color='green', position='below', shape='circle', time=self.df.loc[i, 'date'])
                    win += 1
                else:
                    self.chart.marker(text='', color='red', position='below', shape='circle', time=self.df.loc[i, 'date'])
                    lose += 1
            # kiểm tra nếu 2 cột trước liên tiếp đều là DOWN thì thêm marker cho cột sau là 'Nên vào DOWN'
            if i > 1 and self.df.loc[i-2, 'close'] - self.df.loc[i-2, 'open'] < 0 and self.df.loc[i-1, 'close'] - self.df.loc[i-1, 'open'] < 0:
                self.chart.marker(text='', color='red', position='above', shape='arrow_down', time=self.df.loc[i, 'date'])
                # kiểm tra cột i là up hay down
                if self.df.loc[i, 'close'] - self.df.loc[i, 'open'] > 0:
                    self.chart.marker(text='', color='red', position='below', shape='circle', time=self.df.loc[i, 'date'])
                    lose += 1
                else:
                    self.chart.marker(text='', color='green', position='below', shape='circle', time=self.df.loc[i, 'date'])
                    win += 1
        ti_le = round(win/(win+lose)*100 + win/(win+lose)*10, 0)
        self.chart.watermark(f'Win rate: {ti_le}%', color='green', font_size=25)

    def clear_chart(self):
        self.chart.clear_markers()
        self.chart.watermark('')

    def update_from_tick(self, tick):
        try:
            pass
            #self.chart.update_from_tick(tick)
        except:
            pass
        
    def update_chart(self, bar):
        self.chart.update(bar)
        
        """ if bar['open'] == bar['close']:
            self.chart.marker(text='Cancel', color='gray', position='below')
        if bar['open'] < bar['close']:
            up = (bar['close'] - bar['open'])
            up = round(up, 2)
            self.chart.marker(text=f'+ {up}', color='green', position='above', shape='arrow_up')
        if bar['open'] > bar['close']:
            down = (bar['open'] - bar['close'])
            down = round(down, 2)
            self.chart.marker(text=f'- {down}', color='red', position='below', shape='arrow_down') """
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            


class WebSocketListener(QThread):
    new_tick = pyqtSignal(pd.Series)
    
    new_round = pyqtSignal(dict)
    end_round = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self):
        self.main()

    def main(self):
        with connect("wss://api.iqglobal.org/socket.io/?EIO=4&transport=websocket") as websocket:
            websocket.send('40/users,')
            websocket.send('40/users,{"sid":"D916RbgrMhHafsICBLyX"}')
            message = websocket.recv()
            websocket.send('42/users,["users/JOIN",{"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2NjQ5YTU0MWJjYjc2ODk4MDJmN2NjZiIsImVtYWlsIjoiaG9hbmduZC51dGVAZ21haWwuY29tIiwiaWF0IjoxNzE4MDQxOTQzLCJleHAiOjE3MTg2NDY3NDN9.mYac1x8ZSbP5xX0scgMEJb7GQnxM5XF5VhqJLJunTrc"}]')
            data_session = []

            while True:
                try:
                    message = websocket.recv(timeout=10)
                except:
                    return self.main()
                if '40/users,{"sid' in message:
                    continue
                elif message == '2':
                    websocket.send('3')
                    message = websocket.recv()
                    
            
                rs = get_data_new_round_1(message)
                if rs:
                    self.new_round.emit(rs)
                    
                rs = get_data_last_price(message)
                if rs:
                    data_session.append(rs['lastPrice'])
                    date_tick = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                    data_update = [date_tick, rs['lastPrice']]
                    tick = pd.Series(data_update, index=['time', 'price'])
                    self.new_tick.emit(tick)
                    
                rs = get_data_last_round(message)
                if rs:
                    self.end_round.emit(rs)
                    
    def stop(self):
        self.terminate()
        self.wait()


            
            
