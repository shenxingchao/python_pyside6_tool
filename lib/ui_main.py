# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPHEupv.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_top_layout = QHBoxLayout()
        self.main_top_layout.setSpacing(20)
        self.main_top_layout.setObjectName(u"main_top_layout")
        self.main_top_layout.setContentsMargins(20, 20, 20, 20)
        self.start_auto_scroll_btn = QPushButton(self.centralwidget)
        self.start_auto_scroll_btn.setObjectName(u"start_auto_scroll_btn")
        self.start_auto_scroll_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_auto_scroll_btn.setCheckable(True)

        self.main_top_layout.addWidget(self.start_auto_scroll_btn)

        self.auto_send_btn = QPushButton(self.centralwidget)
        self.auto_send_btn.setObjectName(u"auto_send_btn")
        self.auto_send_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.auto_send_btn.setCheckable(True)

        self.main_top_layout.addWidget(self.auto_send_btn)

        self.record_btn = QPushButton(self.centralwidget)
        self.record_btn.setObjectName(u"record_btn")
        self.record_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.record_btn.setCheckable(True)

        self.main_top_layout.addWidget(self.record_btn)


        self.main_layout.addLayout(self.main_top_layout)

        self.main_container_layout = QHBoxLayout()
        self.main_container_layout.setSpacing(6)
        self.main_container_layout.setObjectName(u"main_container_layout")
        self.main_container_layout.setContentsMargins(20, 20, 20, 20)
        self.main_container_widget = QStackedWidget(self.centralwidget)
        self.main_container_widget.setObjectName(u"main_container_widget")
        self.default_page = QWidget()
        self.default_page.setObjectName(u"default_page")
        self.verticalLayout = QVBoxLayout(self.default_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.default_page)
        self.widget.setObjectName(u"widget")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 140, 55, 16))

        self.verticalLayout.addWidget(self.widget)

        self.main_container_widget.addWidget(self.default_page)
        self.auto_send_form_widget = QWidget()
        self.auto_send_form_widget.setObjectName(u"auto_send_form_widget")
        self.verticalLayout_3 = QVBoxLayout(self.auto_send_form_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.auto_send_form_layout = QFormLayout()
        self.auto_send_form_layout.setObjectName(u"auto_send_form_layout")
        self.auto_send_form_layout.setHorizontalSpacing(20)
        self.auto_send_form_layout.setVerticalSpacing(20)
        self.auto_send_pos_label = QLabel(self.auto_send_form_widget)
        self.auto_send_pos_label.setObjectName(u"auto_send_pos_label")

        self.auto_send_form_layout.setWidget(0, QFormLayout.LabelRole, self.auto_send_pos_label)

        self.auto_send_pos_input = QLineEdit(self.auto_send_form_widget)
        self.auto_send_pos_input.setObjectName(u"auto_send_pos_input")

        self.auto_send_form_layout.setWidget(0, QFormLayout.FieldRole, self.auto_send_pos_input)

        self.auto_send_time_label = QLabel(self.auto_send_form_widget)
        self.auto_send_time_label.setObjectName(u"auto_send_time_label")

        self.auto_send_form_layout.setWidget(1, QFormLayout.LabelRole, self.auto_send_time_label)

        self.auto_send_time_input = QLineEdit(self.auto_send_form_widget)
        self.auto_send_time_input.setObjectName(u"auto_send_time_input")

        self.auto_send_form_layout.setWidget(1, QFormLayout.FieldRole, self.auto_send_time_input)

        self.auto_send_content_label = QLabel(self.auto_send_form_widget)
        self.auto_send_content_label.setObjectName(u"auto_send_content_label")

        self.auto_send_form_layout.setWidget(2, QFormLayout.LabelRole, self.auto_send_content_label)

        self.auto_send_content_input = QLineEdit(self.auto_send_form_widget)
        self.auto_send_content_input.setObjectName(u"auto_send_content_input")

        self.auto_send_form_layout.setWidget(2, QFormLayout.FieldRole, self.auto_send_content_input)

        self.auto_send_count_label = QLabel(self.auto_send_form_widget)
        self.auto_send_count_label.setObjectName(u"auto_send_count_label")

        self.auto_send_form_layout.setWidget(3, QFormLayout.LabelRole, self.auto_send_count_label)

        self.auto_send_count_input = QLineEdit(self.auto_send_form_widget)
        self.auto_send_count_input.setObjectName(u"auto_send_count_input")

        self.auto_send_form_layout.setWidget(3, QFormLayout.FieldRole, self.auto_send_count_input)

        self.auto_send_get_post_btn = QPushButton(self.auto_send_form_widget)
        self.auto_send_get_post_btn.setObjectName(u"auto_send_get_post_btn")
        self.auto_send_get_post_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.auto_send_form_layout.setWidget(4, QFormLayout.LabelRole, self.auto_send_get_post_btn)

        self.auto_send_submit_btn = QPushButton(self.auto_send_form_widget)
        self.auto_send_submit_btn.setObjectName(u"auto_send_submit_btn")
        self.auto_send_submit_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.auto_send_submit_btn.setCheckable(True)

        self.auto_send_form_layout.setWidget(4, QFormLayout.FieldRole, self.auto_send_submit_btn)


        self.verticalLayout_3.addLayout(self.auto_send_form_layout)

        self.main_container_widget.addWidget(self.auto_send_form_widget)
        self.record_form_widget = QWidget()
        self.record_form_widget.setObjectName(u"record_form_widget")
        self.verticalLayout_4 = QVBoxLayout(self.record_form_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.record_form_layout = QFormLayout()
        self.record_form_layout.setObjectName(u"record_form_layout")
        self.record_form_layout.setHorizontalSpacing(20)
        self.record_form_layout.setVerticalSpacing(20)
        self.record_type_label = QLabel(self.record_form_widget)
        self.record_type_label.setObjectName(u"record_type_label")

        self.record_form_layout.setWidget(0, QFormLayout.LabelRole, self.record_type_label)

        self.record_type_layout = QHBoxLayout()
        self.record_type_layout.setSpacing(20)
        self.record_type_layout.setObjectName(u"record_type_layout")
        self.record_type_checkbox_1 = QCheckBox(self.record_form_widget)
        self.record_type_checkbox_group = QButtonGroup(MainWindow)
        self.record_type_checkbox_group.setObjectName(u"record_type_checkbox_group")
        self.record_type_checkbox_group.setExclusive(False)
        self.record_type_checkbox_group.addButton(self.record_type_checkbox_1)
        self.record_type_checkbox_1.setObjectName(u"record_type_checkbox_1")

        self.record_type_layout.addWidget(self.record_type_checkbox_1)

        self.record_type_checkbox_2 = QCheckBox(self.record_form_widget)
        self.record_type_checkbox_group.addButton(self.record_type_checkbox_2)
        self.record_type_checkbox_2.setObjectName(u"record_type_checkbox_2")

        self.record_type_layout.addWidget(self.record_type_checkbox_2)

        self.record_type_layout.setStretch(1, 1)

        self.record_form_layout.setLayout(0, QFormLayout.FieldRole, self.record_type_layout)

        self.record_play_rate_label = QLabel(self.record_form_widget)
        self.record_play_rate_label.setObjectName(u"record_play_rate_label")

        self.record_form_layout.setWidget(1, QFormLayout.LabelRole, self.record_play_rate_label)

        self.record_play_rate_input = QLineEdit(self.record_form_widget)
        self.record_play_rate_input.setObjectName(u"record_play_rate_input")

        self.record_form_layout.setWidget(1, QFormLayout.FieldRole, self.record_play_rate_input)

        self.record_submit_btn = QPushButton(self.record_form_widget)
        self.record_submit_btn.setObjectName(u"record_submit_btn")
        self.record_submit_btn.setEnabled(True)
        self.record_submit_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.record_submit_btn.setCheckable(True)

        self.record_form_layout.setWidget(2, QFormLayout.LabelRole, self.record_submit_btn)

        self.record_play_btn = QPushButton(self.record_form_widget)
        self.record_play_btn.setObjectName(u"record_play_btn")
        self.record_play_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.record_play_btn.setCheckable(True)

        self.record_form_layout.setWidget(2, QFormLayout.FieldRole, self.record_play_btn)


        self.verticalLayout_4.addLayout(self.record_form_layout)

        self.main_container_widget.addWidget(self.record_form_widget)

        self.main_container_layout.addWidget(self.main_container_widget)


        self.main_layout.addLayout(self.main_container_layout)

        self.main_layout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.main_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.start_auto_scroll_btn.clicked.connect(MainWindow.handleClickStartAutoScrollBtn)
        self.auto_send_btn.clicked.connect(MainWindow.handleClickAutoSendBtn)
        self.auto_send_get_post_btn.clicked.connect(MainWindow.handleClickAutoSendGetPosBtn)
        self.auto_send_submit_btn.clicked.connect(MainWindow.handleClickAutoSendSubmitBtn)
        self.record_btn.clicked.connect(MainWindow.handleClickRecordBtn)
        self.record_submit_btn.clicked.connect(MainWindow.handleClickChangeRecord)
        self.record_play_btn.clicked.connect(MainWindow.handleClickPlayRecord)

        self.main_container_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_auto_scroll_btn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u81ea\u52a8\u6eda\u8f6e", None))
        self.auto_send_btn.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u53d1\u9001", None))
        self.record_btn.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5236\u811a\u672c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\uff01", None))
        self.auto_send_pos_label.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807\uff08x,y\uff09", None))
        self.auto_send_pos_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165x,y\u5750\u6807 \u6216 ctrl+G\u83b7\u53d6\u5750\u6807", None))
        self.auto_send_time_label.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u95f4\u9694\uff08ms\uff09", None))
        self.auto_send_time_input.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.auto_send_time_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u53d1\u9001\u95f4\u9694", None))
        self.auto_send_content_label.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5185\u5bb9", None))
        self.auto_send_content_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u53d1\u9001\u5185\u5bb9", None))
        self.auto_send_count_label.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6b21\u6570", None))
        self.auto_send_count_input.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.auto_send_count_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u53d1\u9001\u6b21\u6570", None))
        self.auto_send_get_post_btn.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u5750\u6807\uff08Ctrl+G\uff09", None))
#if QT_CONFIG(shortcut)
        self.auto_send_get_post_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.auto_send_submit_btn.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\uff08Ctrl+S\uff09", None))
#if QT_CONFIG(shortcut)
        self.auto_send_submit_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.record_type_label.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5236\u7c7b\u578b", None))
        self.record_type_checkbox_1.setText(QCoreApplication.translate("MainWindow", u"\u9f20\u6807", None))
        self.record_type_checkbox_2.setText(QCoreApplication.translate("MainWindow", u"\u952e\u76d8", None))
        self.record_play_rate_label.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u500d\u7387", None))
        self.record_play_rate_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.record_submit_btn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5f55\u5236(CTRL+S)", None))
#if QT_CONFIG(shortcut)
        self.record_submit_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.record_play_btn.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
    # retranslateUi

