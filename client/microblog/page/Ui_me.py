# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-07
# Version: v0.2

'''
个人信息页面
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import imgs_me_rc

class Ui_me(object):

    def __init__(self, client):
        self.client = client

    # 页面样式
    def setupUi(self, me):
        self.Me = me
        me.setObjectName("me")
        me.setEnabled(True)
        me.resize(400, 600)
        me.setMinimumSize(QtCore.QSize(400, 600))
        me.setMaximumSize(QtCore.QSize(400, 600))
        me.setMouseTracking(False)
        me.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        
        self.centralWidget = QtWidgets.QWidget(me)
        self.centralWidget.setObjectName("centralWidget")
        self.userinfo = QtWidgets.QGroupBox(self.centralWidget)
        self.userinfo.setGeometry(QtCore.QRect(10, 20, 381, 341))
        self.userinfo.setTitle("")
        self.userinfo.setObjectName("userinfo")
        self.nickname = QtWidgets.QLabel(self.userinfo)
        self.nickname.setGeometry(QtCore.QRect(40, 18, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nickname.setFont(font)
        self.nickname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nickname.setObjectName("nickname")
        self.introduction = QtWidgets.QLabel(self.userinfo)
        self.introduction.setGeometry(QtCore.QRect(33, 200, 325, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.introduction.setFont(font)
        self.introduction.setWordWrap(True)
        self.introduction.setIndent(0)
        self.introduction.setObjectName("introduction")
        self.change_info = QtWidgets.QCommandLinkButton(self.userinfo)
        self.change_info.setGeometry(QtCore.QRect(30, 290, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.change_info.setFont(font)
        self.change_info.setObjectName("change_info")
        self.change_info.setStyleSheet("color: rgb(70, 70, 70); font-weight:normal;vertical-align:middle;")
        self.gender = QtWidgets.QLabel(self.userinfo)
        self.gender.setGeometry(QtCore.QRect(33, 65, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.birthday = QtWidgets.QLabel(self.userinfo)
        self.birthday.setGeometry(QtCore.QRect(33, 115, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.birthday.setFont(font)
        self.birthday.setObjectName("birthday")
        self.gender_t = QtWidgets.QLabel(self.userinfo)
        self.gender_t.setGeometry(QtCore.QRect(130, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gender_t.setFont(font)
        self.gender_t.setObjectName("gender_t")
        self.birthday_t = QtWidgets.QLabel(self.userinfo)
        self.birthday_t.setGeometry(QtCore.QRect(130, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.birthday_t.setFont(font)
        self.birthday_t.setObjectName("birthday_t")
        self.change_pwd = QtWidgets.QCommandLinkButton(self.userinfo)
        self.change_pwd.setGeometry(QtCore.QRect(220, 290, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.change_pwd.setFont(font)
        self.change_pwd.setObjectName("change_pwd")
        self.change_pwd.setStyleSheet("color: rgb(70, 70, 70); font-weight:normal;vertical-align:middle;")
        self.stime_t = QtWidgets.QLabel(self.userinfo)
        self.stime_t.setGeometry(QtCore.QRect(130, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stime_t.setFont(font)
        self.stime_t.setObjectName("stime_t")
        self.siguptime = QtWidgets.QLabel(self.userinfo)
        self.siguptime.setGeometry(QtCore.QRect(33, 165, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.siguptime.setFont(font)
        self.siguptime.setObjectName("siguptime")
        self.history = QtWidgets.QGroupBox(self.centralWidget)
        self.history.setGeometry(QtCore.QRect(10, 370, 381, 161))
        self.history.setTitle("")
        self.history.setObjectName("history")
        self.blog = QtWidgets.QCommandLinkButton(self.history)
        self.blog.setGeometry(QtCore.QRect(30, 29, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.blog.setFont(font)
        self.blog.setAutoDefault(False)
        self.blog.setDefault(False)
        self.blog.setObjectName("blog")
        self.blog.setStyleSheet("color: rgb(70, 70, 70); font-weight:normal;border-radius:5px;vertical-align:middle;")
        self.good = QtWidgets.QCommandLinkButton(self.history)
        self.good.setGeometry(QtCore.QRect(30, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.good.setFont(font)
        self.good.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.good.setAutoDefault(False)
        self.good.setDefault(False)
        self.good.setObjectName("good")
        self.good.setStyleSheet("color: rgb(70, 70, 70); font-weight:normal;border-radius:5px;vertical-align:middle;")
        self.blog_count = QtWidgets.QLabel(self.history)
        self.blog_count.setGeometry(QtCore.QRect(170, 42, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.blog_count.setFont(font)
        self.blog_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.blog_count.setObjectName("blog_count")
        self.good_count = QtWidgets.QLabel(self.history)
        self.good_count.setGeometry(QtCore.QRect(170, 113, 61, 21))
        self.tip = QtWidgets.QLabel(me)
        self.tip.setGeometry(QtCore.QRect(30, 6, 301, 31))
        self.tip.setText("")
        self.tip.setObjectName("tip")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.good_count.setFont(font)
        self.good_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.good_count.setObjectName("good_count")
        self.aboutme = QtWidgets.QLabel(self.centralWidget)
        self.aboutme.setGeometry(QtCore.QRect(330, 575, 41, 20))
        self.aboutme.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutme.setObjectName("aboutme")
        self.search_ = QtWidgets.QLabel(self.centralWidget)
        self.search_.setGeometry(QtCore.QRect(260, 575, 41, 20))
        self.search_.setObjectName("search_")
        self.home = QtWidgets.QLabel(self.centralWidget)
        self.home.setGeometry(QtCore.QRect(30, 575, 41, 20))
        self.home.setObjectName("home")
        self.message = QtWidgets.QPushButton(self.centralWidget)
        self.message.setGeometry(QtCore.QRect(88, 535, 75, 41))
        self.message.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/me/imgs/white_information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.message.setIcon(icon)
        self.message.setIconSize(QtCore.QSize(30, 30))
        self.message.setFlat(True)
        self.message.setObjectName("message")
        self.me_ = QtWidgets.QPushButton(self.centralWidget)
        self.me_.setGeometry(QtCore.QRect(320, 540, 61, 31))
        self.me_.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/me/imgs/black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.me_.setIcon(icon1)
        self.me_.setIconSize(QtCore.QSize(30, 30))
        self.me_.setFlat(True)
        self.me_.setObjectName("me_")
        self.search = QtWidgets.QPushButton(self.centralWidget)
        self.search.setGeometry(QtCore.QRect(240, 540, 61, 31))
        self.search.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/me/imgs/white_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon2)
        self.search.setIconSize(QtCore.QSize(30, 30))
        self.search.setFlat(True)
        self.search.setObjectName("search")
        self.home_page = QtWidgets.QPushButton(self.centralWidget)
        self.home_page.setGeometry(QtCore.QRect(10, 530, 71, 51))
        self.home_page.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/me/imgs/white_house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_page.setIcon(icon3)
        self.home_page.setIconSize(QtCore.QSize(30, 30))
        self.home_page.setFlat(True)
        self.home_page.setObjectName("home_page")
        self.msg = QtWidgets.QLabel(self.centralWidget)
        self.msg.setGeometry(QtCore.QRect(110, 575, 41, 20))
        self.msg.setObjectName("msg")
        self.new_blog = QtWidgets.QPushButton(self.centralWidget)
        self.new_blog.setGeometry(QtCore.QRect(144, 540, 111, 51))
        self.new_blog.setAutoFillBackground(False)
        self.new_blog.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/me/imgs/plus_sign.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_blog.setIcon(icon4)
        self.new_blog.setIconSize(QtCore.QSize(50, 50))
        self.new_blog.setFlat(True)
        self.new_blog.setObjectName("new_blog")

        self.retranslateUi(me)


    def retranslateUi(self, me):
        _translate = QtCore.QCoreApplication.translate
        me.setWindowTitle(_translate("me", "个人信息"))
        self.nickname.setText(_translate("me", "昵称"))
        self.introduction.setText(_translate("me", ""))
        self.change_info.setText(_translate("me", "个人信息修改"))
        self.gender.setText(_translate("me", "性    别:"))
        self.birthday.setText(_translate("me", "生    日"))
        self.gender_t.setText(_translate("me", "女"))
        self.birthday_t.setText(_translate("me", "2018-06-01"))
        self.change_pwd.setText(_translate("me", "密码修改"))
        self.stime_t.setText(_translate("me", "2018-06-01"))
        self.siguptime.setText(_translate("me", "注册时间:"))
        self.blog.setText(_translate("me", "微博"))
        self.good.setText(_translate("me", "点赞"))
        self.blog_count.setText(_translate("me", "0"))
        self.good_count.setText(_translate("me", "0"))
        self.aboutme.setText(_translate("me", "我"))
        self.search_.setText(_translate("me", "发 现"))
        self.home.setText(_translate("me", "微 博"))
        self.msg.setText(_translate("me", "消 息"))

    # 从主函数获取到用户信息, 并添加到页面中展示
    def get_info(self,username,introduction,gender,brithday,stime,blog,good):
        self.nickname.setText(username)
        self.birthday_t.setText(brithday)
        self.gender_t.setText(gender)
        self.stime_t.setText(stime)
        self.introduction.setText(introduction)
        if (not blog) or (not good):
            self.blog_count.setText("0")
            self.good_count.setText("0")
        else:
            self.blog_count.setText(blog)
            self.good_count.setText(good)


if __name__ == "__main__":
    import sys
    client = ClientMsgDeal()
    app = QtWidgets.QApplication(sys.argv)
    me = QtWidgets.QMainWindow()
    ui = Ui_me(client)
    ui.setupUi(me)
    me.show()
    sys.exit(app.exec_())

