#!/usr/bin/python
from gi.repository import Gtk
class GEncrypt():
	def encrypt(self,str):
		self.list_string=list(str)
		self.return_string=''
		for i in range(0,len(self.list_string)):
			self.list_string[i]=chr(ord(self.list_string[i])+1)
			self.return_string=self.return_string+self.list_string[i]
		return self.return_string
	def write_file(self,data):
		filename=open('list.txt','a')
		filename.write(data)
	def __init__(self):
		self.gbuilder=Gtk.Builder()
		self.gbuilder.add_from_file('main_ui.ui')
		dic={'on_ButtonEncrypt_clicked':self.encrypt_data}
		self.gbuilder.connect_signals(dic)
		self.MainWindow=self.gbuilder.get_object('GEncrypt')
		self.MainWindow.show_all()
	def encrypt_data(self,widget):
		self.text_string=self.gbuilder.get_object('TextEntry')
		data=self.text_string.get_text()
		encoded=self.encrypt(data)
		self.write_file('\n'+encoded)
win=GEncrypt()
Gtk.main()
