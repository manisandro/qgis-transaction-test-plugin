# -*- coding: utf-8 -*-
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    copyright            : (C) 2015 by Sandro Mani / Sourcepole AG
#    email                : smani@sourcepole.ch

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os

from ui_dialog import Ui_Dialog
import resources


class TransactionTestPlugin(QObject):
    def __init__(self, iface):
        QObject.__init__(self)

        self.iface = iface
        self.transaction = None

    def initGui(self):
        self.dialog = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)

        self.pluginAction = QAction(QIcon(":/plugins/transactiontest/icon.png"), "Transaction test", self.iface.mainWindow())
        self.pluginAction.triggered.connect(self.dialog.show)
        self.iface.addPluginToMenu("Transaction test", self.pluginAction)

        QgsMapLayerRegistry.instance().layersAdded.connect(self.updateLayers)
        QgsMapLayerRegistry.instance().layersRemoved.connect(self.updateLayers)
        self.ui.pushButton_create.clicked.connect(self.createTransaction)
        self.ui.pushButton_sql.clicked.connect(self.transactionSql)
        self.ui.pushButton_commit.clicked.connect(lambda: self.endTransaction(True))
        self.ui.pushButton_rollback.clicked.connect(lambda: self.endTransaction(False))

        self.updateLayers()

    def updateLayers(self):
        self.ui.listWidget_layers.clear()
        layers = QgsMapLayerRegistry.instance().mapLayers().iteritems()
        for (id, layer) in layers:
            if layer.type() == QgsMapLayer.VectorLayer:
                item = QListWidgetItem(layer.name())
                item.setData(Qt.UserRole, id)
                self.ui.listWidget_layers.addItem(item)
        self.ui.pushButton_create.setEnabled(self.ui.listWidget_layers.count() > 0)

    def createTransaction(self):
        items = self.ui.listWidget_layers.selectedItems()
        if not items:
            return
        layerIds = [str(item.data(Qt.UserRole)) for item in items]
        self.transaction = QgsTransaction.create(layerIds)
        errmsg = str()
        if not self.transaction:
            QMessageBox.critical(self.dialog, "Error", "Failed to create transaction, likely incompatible layers, or data provider does not support transactions.")
        elif not self.transaction.begin(errmsg):
            QMessageBox.critical(self.dialog, "Error", "Failed to start transaction: %s." % errmsg)
            self.transaction = None
        else:
            self.ui.pushButton_create.setEnabled(False)
            self.ui.pushButton_sql.setEnabled(True)
            self.ui.pushButton_commit.setEnabled(True)
            self.ui.lineEdit_sql.setEnabled(True)
            self.ui.pushButton_rollback.setEnabled(True)


    def transactionSql(self):
        error = str()
        if not self.transaction.executeSql(self.ui.lineEdit_sql.text(), error):
            QMessageBox.critical(self.dialog, "SQL Failure", "SQL failed: %s." % error)
        else:
            QMessageBox.information(self.dialog, "SQL Success", "SQL succeeded.")

    def endTransaction(self, commit):
        if not self.transaction:
            return

        errmsg = str()
        if commit:
            if not self.transaction.commit(errmsg):
                QMessageBox.critical(self.dialog, "Error", "Failed to commit transaction: %s." % errmsg)
        else:
            if not self.transaction.rollback(errmsg):
                QMessageBox.critical(self.dialog, "Error", "Failed to rollback transaction: %s." % errmsg)

        self.ui.pushButton_create.setEnabled(True)
        self.ui.pushButton_sql.setEnabled(False)
        self.ui.pushButton_commit.setEnabled(False)
        self.ui.lineEdit_sql.setEnabled(False)
        self.ui.pushButton_rollback.setEnabled(False)
        self.transaction = None

    def unload(self):
        if self.transaction:
            self.endTransaction(False)
        self.dialog = None
        self.iface.removePluginMenu("Transaction test", self.pluginAction)
        QgsMapLayerRegistry.instance().layersAdded.disconnect(self.updateLayers)
        QgsMapLayerRegistry.instance().layersRemoved.disconnect(self.updateLayers)
