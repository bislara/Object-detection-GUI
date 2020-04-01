# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_ResoluteAI(object):
    def setupUi(self, ResoluteAI):
        ResoluteAI.setObjectName("ResoluteAI")
        ResoluteAI.resize(778, 504)
        self.centralwidget = QtWidgets.QWidget(ResoluteAI)
        # self.centralwidget2 = QtWidgets.QWidget(ResoluteAI)
        self.centralwidget.setObjectName("centralwidget")
        self.open_folder = QtWidgets.QPushButton(self.centralwidget)
        self.open_folder.setGeometry(QtCore.QRect(20, 40, 131, 31))
        self.open_folder.setObjectName("open_folder")
        self.prev_image = QtWidgets.QPushButton(self.centralwidget)
        self.prev_image.setGeometry(QtCore.QRect(20, 150, 131, 31))
        self.prev_image.setObjectName("prev_image")
        self.next_img = QtWidgets.QPushButton(self.centralwidget)
        self.next_img.setGeometry(QtCore.QRect(20, 250, 131, 31))
        self.next_img.setObjectName("next_img")
        self.save_anno = QtWidgets.QPushButton(self.centralwidget)
        self.save_anno.setGeometry(QtCore.QRect(20, 350, 131, 31))
        self.save_anno.setObjectName("save_anno")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 10, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 140, 121, 21))
        self.label_2.setObjectName("label_2")
        self.photo_img = QtWidgets.QLabel(self.centralwidget)
        self.photo_img.setGeometry(QtCore.QRect(160, 0, 471, 511))
        self.photo_img.setText("")
        self.photo_img.setPixmap(QtGui.QPixmap(""))
        self.photo_img.setScaledContents(True)
        self.photo_img.setObjectName("photo_img")

        self.frcnn_chk = QtWidgets.QRadioButton(self.centralwidget)
        self.frcnn_chk.setGeometry(QtCore.QRect(640, 40, 82, 17))
        self.frcnn_chk.setObjectName("frcnn_chk")
        self.mobilenet_chk = QtWidgets.QRadioButton(self.centralwidget)
        self.mobilenet_chk.setGeometry(QtCore.QRect(640, 70, 82, 17))
        self.mobilenet_chk.setObjectName("mobilenet_chk")
        self.ssd_chk = QtWidgets.QRadioButton(self.centralwidget)
        self.ssd_chk.setGeometry(QtCore.QRect(640, 100, 82, 17))
        self.ssd_chk.setObjectName("ssd_chk")

        self.Thres = QtWidgets.QSpinBox(self.centralwidget)
        self.Thres.setGeometry(QtCore.QRect(660, 170, 61, 21))
        self.Thres.setObjectName("Thres")
        self.Thres.valueChanged.connect(self.valuechange)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 210, 121, 16))
        self.label_3.setObjectName("label_3")

        self.person_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.person_chk.setGeometry(QtCore.QRect(640, 240, 82, 17))
        self.person_chk.setObjectName("person_chk")
        self.cat_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.cat_chk.setGeometry(QtCore.QRect(640, 270, 82, 17))
        self.cat_chk.setObjectName("cat_chk")
        self.dog_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.dog_chk.setGeometry(QtCore.QRect(640, 300, 82, 17))
        self.dog_chk.setObjectName("dog_chk")
        self.chair_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.chair_chk.setGeometry(QtCore.QRect(640, 330, 82, 17))
        self.chair_chk.setObjectName("chair_chk")
        self.bottle_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.bottle_chk.setGeometry(QtCore.QRect(640, 360, 82, 17))
        self.bottle_chk.setCheckable(True)
        self.bottle_chk.setChecked(False)
        self.bottle_chk.setObjectName("bottle_chk")
        self.detect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.detect_btn.setGeometry(QtCore.QRect(640, 400, 111, 31))
        self.detect_btn.setObjectName("detect_btn")
        ResoluteAI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ResoluteAI)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        ResoluteAI.setStatusBar(self.statusbar)

        self.retranslateUi(ResoluteAI)
        QtCore.QMetaObject.connectSlotsByName(ResoluteAI)

    def retranslateUi(self, ResoluteAI):
        _translate = QtCore.QCoreApplication.translate
        ResoluteAI.setWindowTitle(_translate("ResoluteAI", "MainWindow"))
        self.open_folder.setText(_translate("ResoluteAI", "Open Folder"))
        self.prev_image.setText(_translate("ResoluteAI", "Previous Image"))
        self.next_img.setText(_translate("ResoluteAI", "Next Image"))
        self.save_anno.setText(_translate("ResoluteAI", "Save Annotation"))
        self.label.setText(_translate("ResoluteAI", "Select Model"))
        self.label_2.setText(_translate("ResoluteAI", "Detection Threshold"))
        self.frcnn_chk.setText(_translate("ResoluteAI", "        FRCNN"))
        self.mobilenet_chk.setText(_translate("ResoluteAI", "     MobileNet"))
        self.ssd_chk.setText(_translate("ResoluteAI", "           SSD"))
        self.label_3.setText(_translate("ResoluteAI", "    Label Filter"))
        self.person_chk.setText(_translate("ResoluteAI", "      Person"))
        self.cat_chk.setText(_translate("ResoluteAI", "      Cat"))
        self.dog_chk.setText(_translate("ResoluteAI", "      Dog"))
        self.chair_chk.setText(_translate("ResoluteAI", "      Chair"))
        self.bottle_chk.setText(_translate("ResoluteAI", "      Bottle"))
        self.detect_btn.setText(_translate("ResoluteAI", "Detect"))


        self.open_folder.clicked.connect(self.pick_new)
        self.prev_image.clicked.connect(self.show_prev)
        self.next_img.clicked.connect(self.show_next)
        self.image_index=0

        self.detect_btn.clicked.connect(self.detect)

        self.params_dic = {}
        self.params_dic[1]=0   #person
        self.params_dic[17]=0  #cat
        self.params_dic[18]=0  #dog
        self.params_dic[44]=0  #bottle
        self.params_dic[62]=0  #chair
        

    def valuechange(self):
        self.thres_value = self.Thres.value()

    def detect(self):
        if self.person_chk.isChecked():
            self.params_dic[1]=1
        else:
            self.params_dic[1]=0

        if self.cat_chk.isChecked():
            self.params_dic[17]=1
        else:
            self.params_dic[17]=0
        
        if self.dog_chk.isChecked():
            self.params_dic[18]=1
        else:
            self.params_dic[18]=0

        if self.bottle_chk.isChecked():
            self.params_dic[44]=1
        else:
            self.params_dic[44]=0

        if self.chair_chk.isChecked():
            self.params_dic[62]=1
        else:
            self.params_dic[62]=0


        if self.frcnn_chk.isChecked():
            self.model_name = "faster_rcnn_inception_v2_coco_2018_01_28"
        elif self.ssd_chk.isChecked():
            self.model_name = "ssd_mobilenet_v1_coco_2018_01_28"
        elif self.mobilenet_chk.isChecked():
            self.model_name = "ssd_mobilenet_v1_ppn_shared_box_predictor_300x300_coco14_sync_2018_07_03"
        


    def show_prev(self):
        if self.image_index-1 < 0:
            print("Show valid image")
        else:
            self.image_index-=1
            print(self.file_name[self.image_index])
            self.photo_img.setPixmap(QtGui.QPixmap("images/"+str(self.file_name[self.image_index])))

    def show_next(self):
        if self.image_index >= len(self.file_name):
            print("Show valid image")
        else:
            print(self.file_name[self.image_index])
            self.photo_img.setPixmap(QtGui.QPixmap("images/"+str(self.file_name[self.image_index])))
            self.image_index+=1
            

    def pick_new(self):
        self.dialog = QtWidgets.QFileDialog()
        self.folder_path = self.dialog.getExistingDirectory(None, "Select Folder")
        print(self.folder_path)
        self.file_name = []
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                    self.file_name.append(file)

        print(self.file_name)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResoluteAI = QtWidgets.QMainWindow()
    ui = Ui_ResoluteAI()
    ui.setupUi(ResoluteAI)
    ResoluteAI.show()

    sys.exit(app.exec_())
