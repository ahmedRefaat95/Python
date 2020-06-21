# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DIO_config_tool.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sys

#creating a dictionary initialized with default pin values
data_dict={'mode': "INPUT" , 'config' : "HIGH_IMPEDANCE"}

#creating lists to save the config of each port and each pin
portList =[]
pinlist = []

#creating two global variables to save the indices of the selected Ports
oldPortIndex =0
NewPortIndex =0

#creating two global variables to save the indices of the selected pins
oldPinIndex=0
NewPinIndex=0

#initializing the pins with their default values
for i in range (0,8):
  data_dict['pin'] = i
  pinlist.append(data_dict.copy())

#saving the pin values to each port 
#so that the 4 ports have the default values
for i in range (0,4):
  portList.append(pinlist.copy())


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(544, 479)
        font = QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.Pin_groupBox = QGroupBox(Form)
        self.Pin_groupBox.setObjectName(u"Pin_groupBox")
        self.Pin_groupBox.setGeometry(QRect(10, 20, 521, 311))
        self.Pin_groupBox.setFont(font)
        self.Mode_groupBox = QGroupBox(self.Pin_groupBox)
        self.Mode_groupBox.setObjectName(u"Mode_groupBox")
        self.Mode_groupBox.setGeometry(QRect(20, 100, 101, 131))
        self.Output_radioButton = QRadioButton(self.Mode_groupBox)
        self.Output_radioButton.setObjectName(u"Output_radioButton")
        self.Output_radioButton.setGeometry(QRect(20, 40, 83, 18))
        self.Input_radioButton = QRadioButton(self.Mode_groupBox)
        self.Input_radioButton.setObjectName(u"Input_radioButton")
        self.Input_radioButton.setGeometry(QRect(20, 80, 83, 18))
        self.Input_radioButton.setChecked(True)
        self.OutputConfig_groupBox = QGroupBox(self.Pin_groupBox)
        self.OutputConfig_groupBox.setObjectName(u"OutputConfig_groupBox")
        self.OutputConfig_groupBox.setEnabled(False)
        self.OutputConfig_groupBox.setGeometry(QRect(170, 100, 301, 51))
        self.High_radioButton = QRadioButton(self.OutputConfig_groupBox)
        self.High_radioButton.setObjectName(u"High_radioButton")
        self.High_radioButton.setGeometry(QRect(20, 20, 83, 18))
        self.Low_radioButton = QRadioButton(self.OutputConfig_groupBox)
        self.Low_radioButton.setObjectName(u"Low_radioButton")
        self.Low_radioButton.setGeometry(QRect(160, 20, 83, 18))
        self.Low_radioButton.setChecked(True)
        self.InputConfig_groupBox = QGroupBox(self.Pin_groupBox)
        self.InputConfig_groupBox.setObjectName(u"InputConfig_groupBox")
        self.InputConfig_groupBox.setGeometry(QRect(170, 180, 311, 51))
        self.PullUp_radioButton = QRadioButton(self.InputConfig_groupBox)
        self.PullUp_radioButton.setObjectName(u"PullUp_radioButton")
        self.PullUp_radioButton.setGeometry(QRect(20, 20, 83, 18))
        self.HightImp_radioButton = QRadioButton(self.InputConfig_groupBox)
        self.HightImp_radioButton.setObjectName(u"HightImp_radioButton")
        self.HightImp_radioButton.setGeometry(QRect(160, 20, 121, 21))
        self.HightImp_radioButton.setChecked(True)
        self.PinName_lineEdit = QLineEdit(self.Pin_groupBox)
        self.PinName_lineEdit.setObjectName(u"PinName_lineEdit")
        self.PinName_lineEdit.setEnabled(False)
        self.PinName_lineEdit.setGeometry(QRect(20, 260, 161, 31))
        self.DefaultName_checkBox = QCheckBox(self.Pin_groupBox)
        self.DefaultName_checkBox.setObjectName(u"DefaultName_checkBox")
        self.DefaultName_checkBox.setGeometry(QRect(220, 260, 131, 31))
        self.DefaultName_checkBox.setChecked(True)
                
        
        self.SelectPin_combobox = QComboBox(self.Pin_groupBox)
        self.SelectPin_combobox.addItems(['Pin 0','Pin 1','Pin 2','Pin 3','Pin 4','Pin 5','Pin 6','Pin 7'])
        self.SelectPin_combobox.setObjectName(u"SelectPin_combobox")
        self.SelectPin_combobox.setGeometry(QRect(330, 40, 101, 31))
        self.SelectPin_combobox.setLayoutDirection(Qt.LeftToRight)
        
                
        self.label = QLabel(self.Pin_groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 71, 31))
        self.label_2 = QLabel(self.Pin_groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 40, 61, 31))
        
        self.SelectPort_combobox = QComboBox(self.Pin_groupBox)
        self.SelectPort_combobox.setObjectName(u"SelectPort_combobox")
        self.SelectPort_combobox.setGeometry(QRect(100, 40, 81, 31))
        self.SelectPort_combobox.addItems(['Port A','Port B','Port C','Port D'])
        
        self.OutputPath_lineEdit = QLineEdit(Form)
        self.OutputPath_lineEdit.setObjectName(u"OutputPath_lineEdit")
        self.OutputPath_lineEdit.setGeometry(QRect(30, 350, 291, 31))
        
        self.Generate_pushButton = QPushButton(Form)
        self.Generate_pushButton.setObjectName(u"Generate_pushButton")
        self.Generate_pushButton.setGeometry(QRect(340, 350, 101, 31))
        
        
        self.New_pushButton = QPushButton(Form)
        self.New_pushButton.setObjectName(u"New_pushButton")
        self.New_pushButton.setGeometry(QRect(60, 420, 91, 31))
        self.Save_pushButton = QPushButton(Form)
        self.Save_pushButton.setObjectName(u"Save_pushButton")
        self.Save_pushButton.setGeometry(QRect(170, 420, 91, 31))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 420, 91, 31))

        self.retranslateUi(Form)
        
        QObject.connect(self.Output_radioButton,SIGNAL("clicked(bool)"),self.InputConfig_groupBox.setDisabled)
        QObject.connect(self.Output_radioButton,SIGNAL("clicked(bool)"),self.OutputConfig_groupBox.setEnabled)
        QObject.connect(self.Input_radioButton,SIGNAL("clicked(bool)"),self.OutputConfig_groupBox.setDisabled)
        QObject.connect(self.Input_radioButton,SIGNAL("clicked(bool)"),self.InputConfig_groupBox.setEnabled)
        QObject.connect(self.DefaultName_checkBox,SIGNAL("clicked(bool)"),self.PinName_lineEdit.setDisabled)


        self.Output_radioButton.clicked.connect(self.outPut_pin)
        self.Input_radioButton.clicked.connect(self.inPut_pin)
        
        self.High_radioButton.clicked.connect(self.output_high)
        self.Low_radioButton.clicked.connect(self.output_low)
        
        self.HightImp_radioButton.clicked.connect(self.inPut_highImp)
        self.PullUp_radioButton.clicked.connect(self.inPut_pullUp)

        self.SelectPort_combobox.currentTextChanged.connect(self.SelectPortFunction)
        self.SelectPin_combobox.currentTextChanged.connect(self.SelectPinFunction)
        
        self.Generate_pushButton.clicked.connect(self.GenerateFunction)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
    
    #creating a function for each radio button to save
    #the status of the current selection to the dictionary
    def outPut_pin(self):
        if self.Output_radioButton.isChecked():
          data_dict ['mode'] = "OUTPUT"
          
        if self.High_radioButton.isChecked():
          data_dict ['config'] = "HIGH"
          
        if self.Low_radioButton.isChecked():
          data_dict ['config'] = "LOW"

    def inPut_pin(self):
        if self.Input_radioButton.isChecked():
          data_dict ['mode'] = "INPUT"
          
        if self.HightImp_radioButton.isChecked():
          data_dict ['config'] = "HIGH_IMPEDANCE"
          
        if self.PullUp_radioButton.isChecked():
          data_dict ['config'] = "PULLUP"
        
    def output_high(self):
        if self.High_radioButton.isChecked():
          data_dict ['config'] = "HIGH"
    
    def output_low(self):
        if self.Low_radioButton.isChecked():
          data_dict ['config'] = "LOW"
          
    def inPut_highImp(self):
        if self.HightImp_radioButton.isChecked():
          data_dict ['config'] = "HIGH_IMPEDANCE"
          
    def inPut_pullUp(self):
        if self.PullUp_radioButton.isChecked():
          data_dict ['config'] = "PULLUP"
    
    #function which gets called when a different port is chosen
    def SelectPortFunction(self):
      global oldPinIndex
      global NewPinIndex
      
      global oldPortIndex
      global NewPortIndex
      
      #saving the values of chosen indices before the new port is chosen
      oldPinIndex = NewPinIndex
      oldPortIndex = NewPortIndex
      
      #updating the indices with the current chosen value
      NewPinIndex = self.SelectPin_combobox.currentIndex()
      NewPortIndex = self.SelectPort_combobox.currentIndex()
      
      #updating the current title with the chosen port and pin
      PortText = self.SelectPort_combobox.currentText()
      PinText = self.SelectPin_combobox.currentText()
      self.Pin_groupBox.setTitle(PortText+": "+PinText+" configuration ")
      
      #saving the current pin config before a different port is chosen
      portList[oldPortIndex][oldPinIndex] = data_dict.copy()
      self.getPinConfig()
      
    #function which gets called when a different pin is chosen
    def SelectPinFunction(self):
        global oldPinIndex
        global NewPinIndex

        global NewPortIndex
        
        #saving the values of chosen pin index before a different pin is chosen
        oldPinIndex = NewPinIndex
        
        #saving the old pin index in a dictionary key
        data_dict ['pin'] = oldPinIndex
        
        #updating the pin index with the current chosen value
        NewPinIndex = self.SelectPin_combobox.currentIndex()
        #saving the status of the pin config before a different pin is chosen 
        portList[NewPortIndex][oldPinIndex] = data_dict.copy()
          
        self.getPinConfig()
        
        #updating the current title with the chosen port and pin
        PortText = self.SelectPort_combobox.currentText()
        PinText = self.SelectPin_combobox.currentText()
        self.Pin_groupBox.setTitle(PortText+": "+PinText+" configuration ")
        
    
    #function which retrieves the configuration of the chosen pin
    def getPinConfig(self):
    
        NewPinIndex = self.SelectPin_combobox.currentIndex()
        
        if portList[NewPortIndex][NewPinIndex]['mode'] == "OUTPUT":
          data_dict ['mode'] = "OUTPUT"
          self.Output_radioButton.setChecked(1)
          self.Output_radioButton.click()
          self.Input_radioButton.setChecked(0)
          
          if portList[NewPortIndex][NewPinIndex]['config'] == "HIGH":
            data_dict ['config'] == "HIGH"
            self.High_radioButton.setChecked(1)
            self.High_radioButton.click()
            self.Low_radioButton.setChecked(0)
            
          else:
            data_dict ['config'] == "LOW"
            self.Low_radioButton.setChecked(1)
            self.Low_radioButton.click()
            self.High_radioButton.setChecked(0)
          
        else:
          data_dict ['mode'] = "INPUT"
          self.Input_radioButton.setChecked(1)
          self.Input_radioButton.click()
          self.Output_radioButton.setChecked(0)
          
          if portList[NewPortIndex][NewPinIndex]['config'] == "HIGH_IMPEDANCE":
            data_dict ['config'] == "HIGH_IMPEDANCE"
            self.HightImp_radioButton.setChecked(1)
            self.HightImp_radioButton.click()
            self.PullUp_radioButton.setChecked(0)
          
          else:
            data_dict ['config'] == "PULLUP"
            self.PullUp_radioButton.setChecked(1)
            self.PullUp_radioButton.click()
            self.HightImp_radioButton.setChecked(0)
    
    #function which generates the output configuration files
    def GenerateFunction(self):
        
        portNames= ['PORTA','PORTB','PORTC','PORTD']
        j=0;
        
        if self.OutputPath_lineEdit.text() != 'Enter Output Path':
          
          self.SelectPinFunction()
          MFIC_Handler = open(self.OutputPath_lineEdit.text() + r'\MFIC.h' ,'w')
          DIO_Handler = open(self.OutputPath_lineEdit.text() + r'\DIO_config.h' ,'w')
          
          for port in portList:
            DIO_Handler.write("/*--------"+portNames[j]+" pins configuration--------*/\n")
            for pin in port:
              DIO_Handler.write('#define  DIO_u8'+portNames[j]+'_PIN'+str(pin['pin'])+'_MODE   DIO_u8'+pin['mode']+'_'+pin['config']+'\n')
            j+=1
            DIO_Handler.write("\n")
          
          j=0
          if self.DefaultName_checkBox.isChecked():
            for port in portList:
              MFIC_Handler.write("/*-----------"+portNames[j]+" MFIC pins-----------*/\n")
              for pin in port:
                MFIC_Handler.write('#define  DIO_u8'+portNames[j]+'_PIN'+str(pin['pin'])+'   '+str(pin['pin'])+'\n')
              j+=1
              MFIC_Handler.write("\n")
            
          else:
            for port in portList:
              MFIC_Handler.write("/*--------"+portNames[j]+" MFIC pins--------*/\n")
              for pin in port:
                MFIC_Handler.write('#define  '+self.PinName_lineEdit.text()+'_PIN'+str(pin['pin'])+'   '+str(pin['pin'])+'\n')
              j+=1
              MFIC_Handler.write("\n")
            
            
          MFIC_Handler.close()
          DIO_Handler.close()
        else:
          pass
    

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"DIO config tool", None))
        self.Pin_groupBox.setTitle(QCoreApplication.translate("Form", u"Pin 0 Configuration", None))
        self.Mode_groupBox.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.Output_radioButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_radioButton.setText(QCoreApplication.translate("Form", u"Input", None))
        self.OutputConfig_groupBox.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.High_radioButton.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_radioButton.setText(QCoreApplication.translate("Form", u"Low", None))
        self.InputConfig_groupBox.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PullUp_radioButton.setText(QCoreApplication.translate("Form", u"Pull Up", None))
        self.HightImp_radioButton.setText(QCoreApplication.translate("Form", u"High Impedance", None))
        self.PinName_lineEdit.setText(QCoreApplication.translate("Form", u"Enter Pin Name", None))
        self.DefaultName_checkBox.setText(QCoreApplication.translate("Form", u"Use Default Name", None))
        self.SelectPin_combobox.setItemText(0, QCoreApplication.translate("Form", u"Pin 0", None))
        self.SelectPin_combobox.setItemText(1, QCoreApplication.translate("Form", u"Pin 1", None))

        self.label.setText(QCoreApplication.translate("Form", u"DIO Port :", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"DIO Pin :", None))
        self.OutputPath_lineEdit.setText(QCoreApplication.translate("Form", u"Enter Output Path", None))
        self.Generate_pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.New_pushButton.setText(QCoreApplication.translate("Form", u"New", None))
        self.Save_pushButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Load", None))
    # retranslateUi


app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
app.exec_()