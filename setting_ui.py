# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\teams_setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_all_team_basic_setting(object):
    def setupUi(self, all_team_basic_setting):
        all_team_basic_setting.setObjectName("all_team_basic_setting")
        all_team_basic_setting.resize(600, 500)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        all_team_basic_setting.setPalette(palette)
        self.confirm_button = PushButton(all_team_basic_setting)
        self.confirm_button.setGeometry(QtCore.QRect(230, 445, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        self.confirm_button.setFont(font)
        self.confirm_button.setObjectName("confirm_button")
        self.teams_basic_settings = QtWidgets.QWidget(all_team_basic_setting)
        self.teams_basic_settings.setGeometry(QtCore.QRect(30, 10, 541, 51))
        self.teams_basic_settings.setObjectName("teams_basic_settings")
        self.team_system = BodyLabel(self.teams_basic_settings)
        self.team_system.setGeometry(QtCore.QRect(10, 15, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        self.team_system.setFont(font)
        self.team_system.setObjectName("team_system")
        self.all_system = ComboBox(self.teams_basic_settings)
        self.all_system.setGeometry(QtCore.QRect(100, 10, 151, 32))
        self.all_system.setObjectName("all_system")
        self.all_teams = ComboBox(self.teams_basic_settings)
        self.all_teams.setGeometry(QtCore.QRect(380, 10, 151, 32))
        self.all_teams.setObjectName("all_teams")
        self.team_select = BodyLabel(self.teams_basic_settings)
        self.team_select.setGeometry(QtCore.QRect(290, 15, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        self.team_select.setFont(font)
        self.team_select.setObjectName("team_select")
        self.sinners_setting = QtWidgets.QWidget(all_team_basic_setting)
        self.sinners_setting.setGeometry(QtCore.QRect(30, 60, 541, 241))
        self.sinners_setting.setObjectName("sinners_setting")
        self.Gregor_order = LineEdit(self.sinners_setting)
        self.Gregor_order.setGeometry(QtCore.QRect(450, 190, 71, 33))
        self.Gregor_order.setAlignment(QtCore.Qt.AlignCenter)
        self.Gregor_order.setReadOnly(True)
        self.Gregor_order.setObjectName("Gregor_order")
        self.DonQuixote = CheckBox(self.sinners_setting)
        self.DonQuixote.setGeometry(QtCore.QRect(290, 50, 92, 22))
        self.DonQuixote.setObjectName("DonQuixote")
        self.HongLu = CheckBox(self.sinners_setting)
        self.HongLu.setGeometry(QtCore.QRect(150, 110, 92, 22))
        self.HongLu.setObjectName("HongLu")
        self.HongLu_order = LineEdit(self.sinners_setting)
        self.HongLu_order.setGeometry(QtCore.QRect(170, 130, 71, 33))
        self.HongLu_order.setAlignment(QtCore.Qt.AlignCenter)
        self.HongLu_order.setReadOnly(True)
        self.HongLu_order.setObjectName("HongLu_order")
        self.Meursault_order = LineEdit(self.sinners_setting)
        self.Meursault_order.setGeometry(QtCore.QRect(40, 130, 71, 33))
        self.Meursault_order.setAlignment(QtCore.Qt.AlignCenter)
        self.Meursault_order.setReadOnly(True)
        self.Meursault_order.setObjectName("Meursault_order")
        self.Ishmael_order = LineEdit(self.sinners_setting)
        self.Ishmael_order.setGeometry(QtCore.QRect(450, 130, 71, 33))
        self.Ishmael_order.setAlignment(QtCore.Qt.AlignCenter)
        self.Ishmael_order.setReadOnly(True)
        self.Ishmael_order.setObjectName("Ishmael_order")
        self.Rodion_order = LineEdit(self.sinners_setting)
        self.Rodion_order.setGeometry(QtCore.QRect(40, 190, 71, 33))
        self.Rodion_order.setAlignment(QtCore.Qt.AlignCenter)
        self.Rodion_order.setReadOnly(True)
        self.Rodion_order.setObjectName("Rodion_order")
        self.Outis = CheckBox(self.sinners_setting)
        self.Outis.setGeometry(QtCore.QRect(290, 170, 92, 22))
        self.Outis.setObjectName("Outis")
        self.Gregor = CheckBox(self.sinners_setting)
        self.Gregor.setGeometry(QtCore.QRect(430, 170, 92, 22))
        self.Gregor.setObjectName("Gregor")
        self.Faust = CheckBox(self.sinners_setting)
        self.Faust.setGeometry(QtCore.QRect(150, 50, 92, 22))
        self.Faust.setObjectName("Faust")
        self.Sinclair_order = LineEdit(self.sinners_setting)
        self.Sinclair_order.setGeometry(QtCore.QRect(170, 190, 71, 33))
        self.Sinclair_order.setAlignment(QtCore.Qt.AlignCenter)
        self.Sinclair_order.setReadOnly(True)
        self.Sinclair_order.setObjectName("Sinclair_order")
        self.Sinclair = CheckBox(self.sinners_setting)
        self.Sinclair.setGeometry(QtCore.QRect(150, 170, 92, 22))
        self.Sinclair.setObjectName("Sinclair")
        self.Outis_order = LineEdit(self.sinners_setting)
        self.Outis_order.setGeometry(QtCore.QRect(310, 190, 71, 33))
        self.Outis_order.setAlignment(QtCore.Qt.AlignCenter)
        self.Outis_order.setReadOnly(True)
        self.Outis_order.setObjectName("Outis_order")
        self.DonQuixote_order = LineEdit(self.sinners_setting)
        self.DonQuixote_order.setGeometry(QtCore.QRect(310, 70, 71, 33))
        self.DonQuixote_order.setAlignment(QtCore.Qt.AlignCenter)
        self.DonQuixote_order.setReadOnly(True)
        self.DonQuixote_order.setObjectName("DonQuixote_order")
        self.Ryoshu_order = LineEdit(self.sinners_setting)
        self.Ryoshu_order.setGeometry(QtCore.QRect(450, 70, 71, 33))
        self.Ryoshu_order.setAlignment(QtCore.Qt.AlignCenter)
        self.Ryoshu_order.setReadOnly(True)
        self.Ryoshu_order.setObjectName("Ryoshu_order")
        self.Ishmael = CheckBox(self.sinners_setting)
        self.Ishmael.setGeometry(QtCore.QRect(430, 110, 92, 22))
        self.Ishmael.setObjectName("Ishmael")
        self.Heathcliff = CheckBox(self.sinners_setting)
        self.Heathcliff.setGeometry(QtCore.QRect(290, 110, 101, 22))
        self.Heathcliff.setObjectName("Heathcliff")
        self.Heathcliff_order = LineEdit(self.sinners_setting)
        self.Heathcliff_order.setGeometry(QtCore.QRect(310, 130, 71, 33))
        self.Heathcliff_order.setAlignment(QtCore.Qt.AlignCenter)
        self.Heathcliff_order.setReadOnly(True)
        self.Heathcliff_order.setObjectName("Heathcliff_order")
        self.team_selection = BodyLabel(self.sinners_setting)
        self.team_selection.setGeometry(QtCore.QRect(10, 15, 81, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        self.team_selection.setFont(font)
        self.team_selection.setObjectName("team_selection")
        self.Ryoshu = CheckBox(self.sinners_setting)
        self.Ryoshu.setGeometry(QtCore.QRect(430, 50, 92, 22))
        self.Ryoshu.setObjectName("Ryoshu")
        self.Rodion = CheckBox(self.sinners_setting)
        self.Rodion.setGeometry(QtCore.QRect(20, 170, 92, 22))
        self.Rodion.setObjectName("Rodion")
        self.Meursault = CheckBox(self.sinners_setting)
        self.Meursault.setGeometry(QtCore.QRect(20, 110, 92, 22))
        self.Meursault.setObjectName("Meursault")
        self.Faust_order = LineEdit(self.sinners_setting)
        self.Faust_order.setGeometry(QtCore.QRect(170, 70, 71, 33))
        self.Faust_order.setAlignment(QtCore.Qt.AlignCenter)
        self.Faust_order.setReadOnly(True)
        self.Faust_order.setObjectName("Faust_order")
        self.YiSang = CheckBox(self.sinners_setting)
        self.YiSang.setGeometry(QtCore.QRect(20, 50, 92, 22))
        self.YiSang.setObjectName("YiSang")
        self.YiSang_order = LineEdit(self.sinners_setting)
        self.YiSang_order.setGeometry(QtCore.QRect(30, 70, 71, 33))
        self.YiSang_order.setAlignment(QtCore.Qt.AlignCenter)
        self.YiSang_order.setReadOnly(True)
        self.YiSang_order.setObjectName("YiSang_order")
        self.shop_setting = QtWidgets.QWidget(all_team_basic_setting)
        self.shop_setting.setGeometry(QtCore.QRect(30, 300, 541, 131))
        self.shop_setting.setObjectName("shop_setting")
        self.poise = CheckBox(self.shop_setting)
        self.poise.setGeometry(QtCore.QRect(460, 50, 92, 22))
        self.poise.setObjectName("poise")
        self.sell_gift_select = BodyLabel(self.shop_setting)
        self.sell_gift_select.setGeometry(QtCore.QRect(10, 15, 81, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        self.sell_gift_select.setFont(font)
        self.sell_gift_select.setObjectName("sell_gift_select")
        self.sinking = CheckBox(self.shop_setting)
        self.sinking.setGeometry(QtCore.QRect(20, 90, 92, 22))
        self.sinking.setObjectName("sinking")
        self.bleed = CheckBox(self.shop_setting)
        self.bleed.setGeometry(QtCore.QRect(130, 50, 92, 22))
        self.bleed.setObjectName("bleed")
        self.burn = CheckBox(self.shop_setting)
        self.burn.setGeometry(QtCore.QRect(20, 50, 92, 22))
        self.burn.setObjectName("burn")
        self.blunt = CheckBox(self.shop_setting)
        self.blunt.setGeometry(QtCore.QRect(460, 90, 92, 22))
        self.blunt.setObjectName("blunt")
        self.repture = CheckBox(self.shop_setting)
        self.repture.setGeometry(QtCore.QRect(350, 50, 92, 22))
        self.repture.setObjectName("repture")
        self.charge = CheckBox(self.shop_setting)
        self.charge.setGeometry(QtCore.QRect(130, 90, 92, 22))
        self.charge.setObjectName("charge")
        self.slash = CheckBox(self.shop_setting)
        self.slash.setGeometry(QtCore.QRect(240, 90, 92, 22))
        self.slash.setObjectName("slash")
        self.tremor = CheckBox(self.shop_setting)
        self.tremor.setGeometry(QtCore.QRect(240, 50, 92, 22))
        self.tremor.setObjectName("tremor")
        self.clash = CheckBox(self.shop_setting)
        self.clash.setGeometry(QtCore.QRect(350, 90, 92, 22))
        self.clash.setObjectName("clash")
        self.line1 = QtWidgets.QFrame(all_team_basic_setting)
        self.line1.setGeometry(QtCore.QRect(30, 50, 541, 20))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line1.setLineWidth(1)
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QFrame(all_team_basic_setting)
        self.line2.setGeometry(QtCore.QRect(30, 290, 541, 20))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line2.setLineWidth(1)
        self.line2.setObjectName("line2")
        self.line2_2 = QtWidgets.QFrame(all_team_basic_setting)
        self.line2_2.setGeometry(QtCore.QRect(30, 420, 541, 20))
        self.line2_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line2_2.setLineWidth(1)
        self.line2_2.setObjectName("line2_2")
        self.background = QtWidgets.QWidget(all_team_basic_setting)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.background.setPalette(palette)
        self.background.setStyleSheet("QWidget { border: 1px solid gray; border-radius: 15px; }")
        self.background.setObjectName("background")
        self.background.raise_()
        self.shop_setting.raise_()
        self.sinners_setting.raise_()
        self.teams_basic_settings.raise_()
        self.confirm_button.raise_()
        self.line1.raise_()
        self.line2.raise_()
        self.line2_2.raise_()

        self.retranslateUi(all_team_basic_setting)
        QtCore.QMetaObject.connectSlotsByName(all_team_basic_setting)

    def retranslateUi(self, all_team_basic_setting):
        _translate = QtCore.QCoreApplication.translate
        all_team_basic_setting.setWindowTitle(_translate("all_team_basic_setting", "Dialog"))
        self.confirm_button.setText(_translate("all_team_basic_setting", "完 成"))
        self.team_system.setText(_translate("all_team_basic_setting", "队伍体系"))
        self.all_system.setText(_translate("all_team_basic_setting", "烧伤（burn）"))
        self.all_teams.setText(_translate("all_team_basic_setting", "TEAM 1"))
        self.team_select.setText(_translate("all_team_basic_setting", "选择配队"))
        self.DonQuixote.setText(_translate("all_team_basic_setting", "堂吉诃德"))
        self.HongLu.setText(_translate("all_team_basic_setting", "鸿璐"))
        self.Outis.setText(_translate("all_team_basic_setting", "奥提斯"))
        self.Gregor.setText(_translate("all_team_basic_setting", "格里高尔"))
        self.Faust.setText(_translate("all_team_basic_setting", "浮士德"))
        self.Sinclair.setText(_translate("all_team_basic_setting", "辛克莱"))
        self.Ishmael.setText(_translate("all_team_basic_setting", "以实玛利"))
        self.Heathcliff.setText(_translate("all_team_basic_setting", "希斯克利夫"))
        self.team_selection.setText(_translate("all_team_basic_setting", "配队选择"))
        self.Ryoshu.setText(_translate("all_team_basic_setting", "良秀"))
        self.Rodion.setText(_translate("all_team_basic_setting", "罗佳"))
        self.Meursault.setText(_translate("all_team_basic_setting", "默尔索"))
        self.YiSang.setText(_translate("all_team_basic_setting", "李箱"))
        self.poise.setText(_translate("all_team_basic_setting", "呼吸"))
        self.sell_gift_select.setText(_translate("all_team_basic_setting", "出售饰品"))
        self.sinking.setText(_translate("all_team_basic_setting", "沉沦"))
        self.bleed.setText(_translate("all_team_basic_setting", "流血"))
        self.burn.setText(_translate("all_team_basic_setting", "烧伤"))
        self.blunt.setText(_translate("all_team_basic_setting", "打击"))
        self.repture.setText(_translate("all_team_basic_setting", "破裂"))
        self.charge.setText(_translate("all_team_basic_setting", "充能"))
        self.slash.setText(_translate("all_team_basic_setting", "斩击"))
        self.tremor.setText(_translate("all_team_basic_setting", "震颤"))
        self.clash.setText(_translate("all_team_basic_setting", "突刺"))
from qfluentwidgets import BodyLabel, CheckBox, ComboBox, LineEdit, PushButton
