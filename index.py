"""
引用自定义的标题栏 copy内的就是窗口拖动和缩放的代码 ps:全屏状态下 边界拖动问题 没解决 影响不大
打包后，需要把qss和images文件夹拖到应用根目录 
其他问题 设置了centralwidget 背景色导致按钮背景色不见的问题，需要把centralwidget的背景色也放到qss里面去，反正全部写在css里面读取就可以了
"""
from re import T
from time import sleep
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import QRect, QSize, Qt, QTimer
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QPushButton
from lib.ui_main import Ui_MainWindow
import sys

# 鼠标键盘自动化操作基于窗口
import pyautogui

# 复制粘贴
import pyperclip

# 全局键盘监听
import keyboard

# 鼠标监听
import mouse

# 导入多线程
from threading import Thread

# 迭代工具
import itertools as it

""" copy start """
# 默认标题栏高度 必须设
DEFAULT_TITILE_BAR_HEIGHT = 40
# 鼠标缩放窗口最小宽度，必须设
MIN_WINDOW_WIDTH = 500
MIN_WINDOW_HEIGHT = 500


class QCustomTitleBar:
    def __init__(self, window: QtWidgets):
        self.window = window
        # 1.设置无边框 和 透明背景
        self.window.setWindowFlags(Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)
        # 2.添加自定义的标题栏到最顶部
        self.title = QLabel("Python+Pyside6+小工具", self.window)
        # 3.设置标题栏样式
        self.setStyle()
        # 4.添加按钮
        # 添加关闭按钮
        self.close_btn = QPushButton("", self.window)
        self.close_btn.setGeometry(self.window.width() - 33, 10, 20, 20)
        # 添加最大化按钮
        self.max_btn = QPushButton("", self.window)
        self.max_btn.setGeometry(self.window.width() - 66, 10, 20, 20)
        # 添加最小化按钮
        self.min_btn = QPushButton("", self.window)
        self.min_btn.setGeometry(self.window.width() - 99, 10, 20, 20)
        # 设置三个按钮的鼠标样式
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.max_btn.setCursor(Qt.PointingHandCursor)
        self.min_btn.setCursor(Qt.PointingHandCursor)
        # 设置三个按钮的样式
        self.close_btn.setStyleSheet(
            "QPushButton{border-image:url('./images/close.png');background:#ff625f;border-radius:10px;}"
            "QPushButton:hover{background:#eb4845;}"
        )
        self.max_btn.setStyleSheet(
            "QPushButton{border-image:url('./images/max.png');background:#ffbe2f;border-radius:10px;}"
            "QPushButton:hover{background:#ecae27;}"
        )
        self.min_btn.setStyleSheet(
            "QPushButton{border-image:url('./images/min.png');background:#29c941;border-radius:10px;}"
            "QPushButton:hover{background:#1ac033;}"
        )

        # 5.添加工具栏按钮事件
        # 关闭按钮点击绑定窗口关闭事件
        self.close_btn.pressed.connect(self.window.close)
        # 最大化按钮绑定窗口最大化事件
        self.max_btn.pressed.connect(self.setMaxEvent)
        # 最小化按钮绑定窗口最小化事件
        self.min_btn.pressed.connect(self.window.showMinimized)
        # 6.记录恢复前的大小-ps非常有用
        self.restore_window_size = None
        # 7.设置标题栏鼠标跟踪 鼠标移入触发，不设置，移入标题栏不触发
        self.title.setMouseTracking(True)

    def setMaxEvent(self, flag=False):
        """
        @description  最大化按钮绑定窗口最大化事件和事件 拿出来是因为拖动标题栏时需要恢复界面大小
        @param flag 是否是拖动标题栏 bool
        @return
        """
        if flag:
            if self.window.isMaximized():
                self.window.showNormal()
                self.max_btn.setStyleSheet(
                    "QPushButton{border-image:url('./images/max.png');background:#ffbe2f;border-radius:10px;}"
                    "QPushButton:hover{background:#ecae27;}"
                )
                return self.restore_window_size
            return None
        else:
            if self.window.isMaximized():
                self.window.showNormal()
                self.max_btn.setStyleSheet(
                    "QPushButton{border-image:url('./images/max.png');background:#ffbe2f;border-radius:10px;}"
                    "QPushButton:hover{background:#ecae27;}"
                )
            else:
                self.window.showMaximized()
                self.max_btn.setStyleSheet(
                    "QPushButton{border-image:url('./images/restore.png');background:#ffbe2f;border-radius:10px;}"
                    "QPushButton:hover{background:#ecae27;}"
                )
                # 最大化的时候记录最大化前窗口大小 用于返回最大化时拖动窗口恢复后的大小，不然恢复的时候窗口大小是最大化的，这个程序循环帧会取不到恢复后的宽度
                self.restore_window_size = QSize(self.window.width(), self.window.height())

    def setStyle(self, style: str = ""):
        """
        @description 设置自定义标题栏样式
        @param
        @return
        """
        # 想要边框 加上border:1px solid #cccccc;
        DEFAULT_STYLE = """
                            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #fafafa,stop:1 #d1d1d1);
                            color:#333333;padding:10px;border:1px solid #c6c6c6;
                            border-top-left-radius:4px;
                            border-top-right-radius:4px;
                        """
        self.title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # 设置样式
        self.title.setStyleSheet(DEFAULT_STYLE if not style else DEFAULT_STYLE + style)
        # 设置大小
        self.title.setGeometry(0, 0, self.window.width(), DEFAULT_TITILE_BAR_HEIGHT)


""" copy end"""


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 调用父类的方法
        super(MainWindow, self).__init__()
        # 初始化界面
        self.setupUi(self)
        """ copy start"""
        # 初始化标题栏
        self.titleBar = QCustomTitleBar(self)
        # 设置ui文件里main_layout上边距，以免遮挡标题栏
        self.main_layout.setContentsMargins(0, DEFAULT_TITILE_BAR_HEIGHT, 0, 0)
        # 初始化鼠标拖动标题栏标志
        self.drag_flag = False
        # 记录按下时窗口坐标， 这个用于窗口移动
        self.win_x = 0
        self.win_y = 0
        # 记录按下时鼠标坐标，这个用于计算鼠标移动的距离
        self.mouse_x = 0
        self.mouse_y = 0
        # 记录鼠标移入的拖动区域，共8种区域 左上 左 左下 上 下 右上 右 右下
        self.left_up = None
        self.left = None
        self.left_down = None
        self.up = None
        self.down = None
        self.right_up = None
        self.right = None
        self.right_down = None
        # 设置为True则mouseMoveEvent事件不需要按下也能触发,不然要按着鼠标左键或右键才能触发
        self.setMouseTracking(True)
        # 设置子类的mousetrack
        self.centralwidget.setMouseTracking(True)
        # 记录按下时窗口的大小，用于计算鼠标相对于窗口移动的距离，用于缩放
        self.win_w = 0
        self.win_h = 0
        # 初始化鼠标缩放标志
        self.move_left_up_flag = False
        self.move_left_flag = False
        self.move_left_down_flag = False
        self.move_up_flag = False
        self.move_down_flag = False
        self.move_right_up_flag = False
        self.move_right_flag = False
        self.move_right_down_flag = False
        """ copy end"""
        # 初始化表单隐藏
        # 隐藏自动发送表单
        self.auto_send_form_widget.setVisible(False)

    """ copy start"""

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        """
        @description  窗口缩放事件
        @param
        @return
        """
        # 最大化最小化的时候，需要去改变按钮组位置
        self.titleBar.close_btn.move(self.width() - 33, 10)
        self.titleBar.max_btn.move(self.width() - 66, 10)
        self.titleBar.min_btn.move(self.width() - 99, 10)
        self.titleBar.title.resize(self.width(), DEFAULT_TITILE_BAR_HEIGHT)

        # 记录鼠标移入的拖动区域，共8种区域
        self.left_up = QRect(0, 0, 10, 10)
        self.left = QRect(0, 10, 10, self.height() - 20)
        self.left_down = QRect(0, self.height() - 10, 10, 10)
        self.up = QRect(10, 0, self.width() - 20, 10)
        self.down = QRect(10, self.height() - 10, self.width() - 20, 10)
        self.right_up = QRect(self.width() - 10, 0, 10, 10)
        self.right = QRect(self.width() - 10, 10, 10, self.height() - 20)
        self.right_down = QRect(self.width() - 10, self.height() - 10, 10, 10)

        return super().resizeEvent(a0)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        @description 鼠标按下事件
        @param
        @return
        """
        # 记录按下时窗口坐标， 这个用于窗口移动
        self.win_x = self.x()
        self.win_y = self.y()
        # 记录按下时鼠标坐标，这个用于计算鼠标移动的距离
        self.mouse_x = a0.globalPosition().x()
        self.mouse_y = a0.globalPosition().y()
        # 记录按下时窗口的大小，用于计算鼠标相对于窗口移动的距离，用于缩放
        self.win_w = self.width()
        self.win_h = self.height()

        # 如果按下的是鼠标左键
        if a0.button() == Qt.MouseButton.LeftButton and self.left_up.contains(a0.position().x(), a0.position().y()):
            self.move_left_up_flag = True
        if a0.button() == Qt.MouseButton.LeftButton and self.left.contains(a0.position().x(), a0.position().y()):
            self.move_left_flag = True
        if a0.button() == Qt.MouseButton.LeftButton and self.left_down.contains(a0.position().x(), a0.position().y()):
            self.move_left_down_flag = True
        if a0.button() == Qt.MouseButton.LeftButton and self.up.contains(a0.position().x(), a0.position().y()):
            self.move_up_flag = True
        if a0.button() == Qt.MouseButton.LeftButton and self.down.contains(a0.position().x(), a0.position().y()):
            self.move_down_flag = True
        if a0.button() == Qt.MouseButton.LeftButton and self.right_up.contains(a0.position().x(), a0.position().y()):
            self.move_right_up_flag = True
        if a0.button() == Qt.MouseButton.LeftButton and self.right.contains(a0.position().x(), a0.position().y()):
            self.move_right_flag = True
        if a0.button() == Qt.MouseButton.LeftButton and self.right_down.contains(a0.position().x(), a0.position().y()):
            self.move_right_down_flag = True
        # 如果按下的是鼠标左键 且在标题栏范围内
        elif a0.button() == Qt.MouseButton.LeftButton and a0.position().y() < self.titleBar.title.height():
            # 设置为按下
            self.drag_flag = True
        return super().mousePressEvent(a0)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        @description 鼠标按下移动事件
        @param
        @return
        """
        # 获取移动后鼠标的位置
        mouse_move_x = a0.globalPosition().x()
        mouse_move_y = a0.globalPosition().y()
        # 计算移动的距离
        offset_x = mouse_move_x - self.mouse_x
        offset_y = mouse_move_y - self.mouse_y
        # 左上
        if self.left_up.contains(a0.position().x(), a0.position().y()):
            self.setCursor(Qt.SizeFDiagCursor)
        # 左
        elif self.left.contains(a0.position().x(), a0.position().y()):
            self.setCursor(Qt.SizeHorCursor)
        # 左下
        elif self.left_down.contains(a0.position().x(), a0.position().y()):
            self.setCursor(Qt.SizeBDiagCursor)
        # 上
        elif self.up.contains(a0.position().x(), a0.position().y()):
            self.setCursor(Qt.SizeVerCursor)
        # 下
        elif self.down.contains(a0.position().x(), a0.position().y()):
            self.setCursor(Qt.SizeVerCursor)
        # 右上
        elif self.right_up.contains(a0.position().x(), a0.position().y()):
            self.setCursor(Qt.SizeBDiagCursor)
        # 右
        elif self.right.contains(a0.position().x(), a0.position().y()):
            self.setCursor(Qt.SizeHorCursor)
        # 右下
        elif self.right_down.contains(a0.position().x(), a0.position().y()):
            self.setCursor(Qt.SizeFDiagCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        # 如果按下且在左上角范围内则缩放（其他代码参考左上）
        if self.move_left_up_flag:
            # 拖动的时候也要设置一下形状
            self.setCursor(Qt.SizeFDiagCursor)
            resize_w = self.win_w - offset_x
            resize_h = self.win_h - offset_y
            # 如果缩放后的尺寸小于最小尺寸则窗口不能缩放了
            resize_w = MIN_WINDOW_WIDTH if resize_w < MIN_WINDOW_WIDTH else resize_w
            resize_h = MIN_WINDOW_HEIGHT if resize_h < MIN_WINDOW_HEIGHT else resize_h
            # 设置窗口缩放尺寸
            self.resize(resize_w, resize_h)
            # 设置窗口移动,需要鼠标跟随
            # x y 都要鼠标跟随
            if resize_w != MIN_WINDOW_WIDTH and resize_h != MIN_WINDOW_HEIGHT:
                self.move(self.win_x + offset_x, self.win_y + offset_y)
            # 缩放宽度等于最小宽度，高度鼠标跟随
            if resize_w == MIN_WINDOW_WIDTH and resize_h != MIN_WINDOW_HEIGHT:
                self.move(self.x(), self.win_y + offset_y)
            # 缩放高度等于最小高度，宽度鼠标跟随
            if resize_w != MIN_WINDOW_WIDTH and resize_h == MIN_WINDOW_HEIGHT:
                self.move(self.win_x + offset_x, self.y())
        # 如果按下且在左边范围内则缩放
        elif self.move_left_flag:
            # 拖动的时候也要设置一下形状
            self.setCursor(Qt.SizeHorCursor)
            resize_w = self.win_w - offset_x
            resize_h = self.win_h
            # 如果缩放后的尺寸小于最小尺寸则窗口不能缩放了
            resize_w = MIN_WINDOW_WIDTH if resize_w < MIN_WINDOW_WIDTH else resize_w
            # 设置窗口缩放尺寸
            self.resize(resize_w, resize_h)
            # 设置窗口移动,需要鼠标跟随
            # 只要宽度鼠标跟随
            if resize_w != MIN_WINDOW_WIDTH:
                self.move(self.win_x + offset_x, self.win_y)
        # 如果按下且在左下角范围内则缩放
        elif self.move_left_down_flag:
            # 拖动的时候也要设置一下形状
            self.setCursor(Qt.SizeBDiagCursor)
            resize_w = self.win_w - offset_x
            resize_h = self.win_h + offset_y
            # 如果缩放后的尺寸小于最小尺寸则窗口不能缩放了
            resize_w = MIN_WINDOW_WIDTH if resize_w < MIN_WINDOW_WIDTH else resize_w
            resize_h = MIN_WINDOW_HEIGHT if resize_h < MIN_WINDOW_HEIGHT else resize_h
            # 设置窗口缩放尺寸
            self.resize(resize_w, resize_h)
            # 设置窗口移动,需要鼠标跟随
            # x y 都要鼠标跟随
            if resize_w != MIN_WINDOW_WIDTH and resize_h != MIN_WINDOW_HEIGHT:
                self.move(self.win_x + offset_x, self.y())
            # 缩放高度等于最小高度，宽度鼠标跟随
            if resize_w != MIN_WINDOW_WIDTH and resize_h == MIN_WINDOW_HEIGHT:
                self.move(self.win_x + offset_x, self.y())
        # 如果按下且在上边范围内则缩放
        elif self.move_up_flag:
            # 拖动的时候也要设置一下形状
            self.setCursor(Qt.SizeVerCursor)
            resize_w = self.win_w
            resize_h = self.win_h - offset_y
            # 如果缩放后的尺寸小于最小尺寸则窗口不能缩放了
            resize_h = MIN_WINDOW_HEIGHT if resize_h < MIN_WINDOW_HEIGHT else resize_h
            # 设置窗口缩放尺寸
            self.resize(resize_w, resize_h)
            # 设置窗口移动,需要鼠标跟随
            # 只要高度鼠标跟随
            if resize_h != MIN_WINDOW_HEIGHT:
                self.move(self.win_x, self.win_y + offset_y)
        # 如果按下且在下边范围内则缩放
        elif self.move_down_flag:
            # 拖动的时候也要设置一下形状
            self.setCursor(Qt.SizeVerCursor)
            resize_w = self.win_w
            resize_h = self.win_h + offset_y
            # 如果缩放后的尺寸小于最小尺寸则窗口不能缩放了
            resize_h = MIN_WINDOW_HEIGHT if resize_h < MIN_WINDOW_HEIGHT else resize_h
            # 设置窗口缩放尺寸
            self.resize(resize_w, resize_h)
        # 如果按下且在右上角范围内则缩放
        elif self.move_right_up_flag:
            # 拖动的时候也要设置一下形状
            self.setCursor(Qt.SizeBDiagCursor)
            resize_w = self.win_w + offset_x
            resize_h = self.win_h - offset_y
            # 如果缩放后的尺寸小于最小尺寸则窗口不能缩放了
            resize_w = MIN_WINDOW_WIDTH if resize_w < MIN_WINDOW_WIDTH else resize_w
            resize_h = MIN_WINDOW_HEIGHT if resize_h < MIN_WINDOW_HEIGHT else resize_h
            # 设置窗口缩放尺寸
            self.resize(resize_w, resize_h)
            # 设置窗口移动,需要鼠标跟随
            # x y 都要鼠标跟随
            if resize_w != MIN_WINDOW_WIDTH and resize_h != MIN_WINDOW_HEIGHT:
                self.move(self.win_x, self.win_y + offset_y)
            # 缩放宽度等于最小宽度，高度鼠标跟随
            if resize_w == MIN_WINDOW_WIDTH and resize_h != MIN_WINDOW_HEIGHT:
                self.move(self.x(), self.win_y + offset_y)
        # 如果按下且在右边范围内则缩放
        elif self.move_right_flag:
            # 拖动的时候也要设置一下形状
            self.setCursor(Qt.SizeHorCursor)
            resize_w = self.win_w + offset_x
            resize_h = self.win_h
            # 如果缩放后的尺寸小于最小尺寸则窗口不能缩放了
            resize_w = MIN_WINDOW_WIDTH if resize_w < MIN_WINDOW_WIDTH else resize_w
            # 设置窗口缩放尺寸
            self.resize(resize_w, resize_h)
        # 如果按下且在右下角范围内则缩放
        elif self.move_right_down_flag:
            # 拖动的时候也要设置一下形状
            self.setCursor(Qt.SizeFDiagCursor)
            resize_w = self.win_w + offset_x
            resize_h = self.win_h + offset_y
            # 如果缩放后的尺寸小于最小尺寸则窗口不能缩放了
            resize_w = MIN_WINDOW_WIDTH if resize_w < MIN_WINDOW_WIDTH else resize_w
            resize_h = MIN_WINDOW_HEIGHT if resize_h < MIN_WINDOW_HEIGHT else resize_h
            # 设置窗口缩放尺寸
            self.resize(resize_w, resize_h)
        # 如果按下才能移动
        elif self.drag_flag:
            # 窗口恢复
            restore_window_size = self.titleBar.setMaxEvent(True)
            # 如果有恢复窗口，则返回恢复时窗口坐标
            if restore_window_size:
                # 这里没有解决双屏BUG
                # 移动到鼠标正确的比例位置 按下时的位置减去(比例 * 恢复前的宽度)
                self.win_x = self.mouse_x - (self.mouse_x / self.width()) * restore_window_size.width()
            # 设置窗口移动的距离
            self.move(self.win_x + offset_x, self.win_y + offset_y)
        return super().mouseMoveEvent(a0)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        @description 鼠标按下松开事件
        @param
        @return
        """
        self.drag_flag = False
        self.move_left_up_flag = False
        self.move_left_flag = False
        self.move_left_down_flag = False
        self.move_up_flag = False
        self.move_down_flag = False
        self.move_right_up_flag = False
        self.move_right_flag = False
        self.move_right_down_flag = False
        return super().mouseReleaseEvent(a0)

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        @description 鼠标双击事件
        @param
        @return
        """
        # 如果双击的是鼠标左键 且在标题栏范围内 则放大缩小窗口
        if a0.button() == Qt.MouseButton.LeftButton and a0.position().y() < self.titleBar.title.height():
            self.titleBar.setMaxEvent()
        return super().mouseDoubleClickEvent(a0)

    """ copy end"""

    def handleClickStartAutoScrollBtn(self, bool):
        """
        @description 点击自动滚轮按钮 在 button 的属性里面选择 checkable
        @param
        @return
        """
        # 开启
        if bool:
            self.start_auto_scroll_btn.setText("关闭自动滚轮")
        # 关闭
        else:
            self.start_auto_scroll_btn.setText("开启自动滚轮")
        self.changeAutoScroll(bool)

    def changeAutoScroll(self, bool):
        """
        @description 改变自动滚轮状态
        @param  bool True 开启 False关闭 这个状态也能从self.start_auto_scroll_btn.isChecked()获得
        @return
        """

        def autoScroll():
            pyautogui.scroll(100)
            pyautogui.scroll(-100)

        if bool:
            # 创建定时器对象
            self.auto_scroll_timer = QTimer(self)
            # 时间定时信号
            self.auto_scroll_timer.timeout.connect(autoScroll)
            # 设置定时时间20ms
            self.auto_scroll_timer.start(20)
        else:
            # 停止定时器
            self.auto_scroll_timer.stop()

    def handleClickAutoSendBtn(self):
        """
        @description 点击自动发送
        @param
        @return
        """
        self.main_container_widget.setCurrentIndex(1)

    def handleClickAutoSendGetPosBtn(self):
        """
        @description 点击自动发送表单获取坐标按钮获取当前鼠标坐标位置
        @param
        @return
        """
        x, y = pyautogui.position()
        self.auto_send_pos_input.setText(str(x) + "," + str(y))

    def handleClickAutoSendSubmitBtn(self, bool):
        """
        @description 点击自动发送内容
        @param
        @return
        """
        # 开启
        if bool:
            self.auto_send_submit_btn.setText("停止发送（ESC）")
        # 关闭
        else:
            self.auto_send_submit_btn.setText("发送（Ctrl+S）")
            # 注意这里 取消选中checked后 快捷键会失效 需要重新设置
            self.auto_send_submit_btn.setShortcut("Ctrl+S")
        self.changeAutoSend(bool)

    def changeAutoSend(self, bool):
        """
        @description 改变自动发送状态
        @param  bool True 开启 False关闭
        @return
        """

        def autoSend():
            # 判断是否读取坐标
            # 判断时间
            # 判断内容
            pos = self.auto_send_pos_input.text()
            time = self.auto_send_time_input.text()
            content = self.auto_send_content_input.text()

            if pos == "" or time == "" or content == "":
                QMessageBox(QMessageBox.Warning, "提示", "参数未填写，请检查", QMessageBox.Ok, self).show()
                # 停止定时器
                self.auto_send_timer.stop()
            else:
                # 等于设定次数  停止计时器
                if self.auto_send_timer_count == int(self.auto_send_count_input.text()):
                    # 主动点击停止按钮
                    self.auto_send_submit_btn.click()
                    return
                # 模拟点击
                pyautogui.click(x=int(pos.split(",")[0]), y=pos.split(",")[1])
                # 复制文字
                pyperclip.copy(content)
                # 模拟组合热键
                pyautogui.hotkey("ctrl", "v")
                # 发送
                pyautogui.press("enter")
                # 次数+1
                self.auto_send_timer_count = self.auto_send_timer_count + 1

        if bool:
            # 创建定时器对象
            self.auto_send_timer = QTimer(self)
            # 时间定时信号
            self.auto_send_timer.timeout.connect(autoSend)
            # 设置定时时间
            self.auto_send_timer.start(int(self.auto_send_time_input.text()))
            # 设置次数
            self.auto_send_timer_count = 0

            def stop():
                # 删除监听
                keyboard.remove_hotkey("esc")
                if self.auto_send_submit_btn.isChecked():
                    self.auto_send_submit_btn.click()

            # 开启全局键盘监听
            keyboard.add_hotkey("esc", stop)
            # 阻塞进程，任意键终止后继续运行
            # keyboard.wait(stop)
        else:
            # 停止定时器
            self.auto_send_timer.stop()

    def handleClickRecordBtn(self):
        """
        @description 点击录制脚本
        @param
        @return
        """
        self.main_container_widget.setCurrentIndex(2)

    def handleClickChangeRecord(self, bool):
        """
        @description 点击开始录制按钮
        @param
        @return
        """

        def stop():
            if self.record_submit_btn.isChecked():
                self.record_submit_btn.click()

        # 开启
        if bool:
            self.record_submit_btn.setText("停止（ESC）")
            # 定义2个录制类型的选中全局变量 和 录制脚本对象变量
            self.mouse_checked = False
            self.keyboard_checked = False
            self.mouse_record = []
            self.keyboard_record = []
            # 推导式语法 获取选中的checkbox
            checkboxs = [checkbox for checkbox in self.record_type_checkbox_group.buttons() if checkbox.isChecked()]
            # 选中鼠标录制
            if self.record_type_checkbox_1 in checkboxs:
                # 设为选中
                self.mouse_checked = True
                self.mouse_record = []
                # 开启鼠标录制
                mouse.hook(self.mouse_record.append)
            # 选中键盘录制
            if self.record_type_checkbox_2 in checkboxs:
                # 设为选中
                self.keyboard_checked = True
                self.keyboard_record = []
                # 开启键盘录制
                keyboard.hook(self.keyboard_record.append)
            # 开启全局键盘监听
            keyboard.add_hotkey("esc", stop)
        # 关闭
        else:
            self.record_submit_btn.setText("开始录制(CTRL+S)")
            # 注意这里 取消选中checked后 快捷键会失效 需要重新设置
            self.record_submit_btn.setShortcut("Ctrl+S")
            if self.mouse_checked:
                # 停止鼠标录制
                mouse.unhook(self.mouse_record.append)
            if self.keyboard_checked:
                # 停止键盘录制
                keyboard.unhook(self.keyboard_record.append)

    def handleClickPlayRecord(self, bool):
        """
        @description 点击播放按钮 同时播放代码来自 https://github.com/boppreh/mouse/issues/5
        @param
        @return
        """

        def stop():
            if self.record_play_btn.isChecked():
                self.record_play_btn.click()

        if bool:
            speed_factor = int(self.record_play_rate_input.text())
            self.record_play_btn.setText("停止(ESC)")
            # 立即刷新界面
            QApplication.processEvents()

            def fn():
                # 播放录制脚本
                k = sorted(self.mouse_record + self.keyboard_record, key=lambda i: i.time)
                for c, m in it.groupby(k, key=lambda i: isinstance(i, keyboard.KeyboardEvent)):
                    # 如果没有选中
                    if not self.record_play_btn.isChecked():
                        break
                    # 如果是键盘
                    if c:
                        if self.keyboard_record:
                            keyboard.play(m, speed_factor=speed_factor)
                    # 否则是鼠标
                    else:
                        if self.mouse_record:
                            mouse.play(m, speed_factor=speed_factor)
                stop()

            t = Thread(target=fn)
            # 开启全局键盘监听
            keyboard.add_hotkey("esc", stop)
            t.start()
            t.join()

        else:
            self.record_play_btn.setText("播放")


def main():
    # 创建应用程序对象  argv是命令行输入参数列表
    app = QApplication(sys.argv)
    # 创建窗口对象
    window = MainWindow()
    # 设置全局css样式
    with open("./qss/index.qss", "r", encoding="UTF-8") as f:
        app.setStyleSheet(f.read())
    # 显示窗口
    window.show()
    # app.exec()程序一直循环运行直到主窗口被关闭终止进程  sys.exit返回退出时的状态码
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
