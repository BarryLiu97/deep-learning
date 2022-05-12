import sys

import matplotlib.pyplot as plt

sys.path.append("..")

import numpy as np
import torch
import cv2

from torch.autograd import Variable
from torchvision import transforms
from PIL import Image
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from MNIST.gui.main_ui import Ui_MainWindow
from model.mnist import Model

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('MNIST')

        self.center_win()
        self.slot_connection()

        self.mode = 'single_num'
        self.transform = transforms.Compose([
                        transforms.Resize((28, 28)),
                        transforms.ToTensor(),
                        ])
        self.num = ''

        check_point = '../checkpoint/param.pth'
        self.model = Model()
        self.model.load_state_dict(torch.load(check_point))
        print('Finish loading model parameters!')

        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        print(f'Using device {device}')
        self.model.to(device)

    def center_win(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def slot_connection(self):
        self._num_mode_btn.clicked.connect(self._toggle_num_mode)
        self._run_btn.clicked.connect(self._run_model)

    def _toggle_num_mode(self):
        if self._num_mode_btn.text() == 'Single number':
            self._num_mode_btn.setText('Serial numbers')
            self.mode = 'serial_num'
        else:
            self._num_mode_btn.setText('Single number')
            self.mode = 'single_num'

    def _run_model(self):
        input_data = self.get_pic()
        self._num_canvas.clear()
        self.model.eval()
        outputs = self.model(input_data)
        _, predicted = torch.max(outputs.data, dim=1)
        predict_num = str(predicted.cpu().numpy()[0])
        print(predict_num)
        if self.mode == 'single_num':
            self._num_le.setText(predict_num)
        else:
            self.num = self._num_le.text()
            self.num += predict_num
            self._num_le.setText(self.num)


    def get_pic(self):
        pic = self._num_canvas.pixmap().toImage()
        ptr = pic.constBits()
        ptr.setsize(pic.byteCount())
        pic_array = np.array(ptr).reshape(pic.height(), pic.width(), 4)  # 注意这地方通道数一定要填4，否则出错
        pic_array = cv2.cvtColor(pic_array, cv2.COLOR_BGR2RGB)
        PIL_image = Image.fromarray(pic_array)
        pic_array_trans = self.transform(PIL_image).unsqueeze(0)
        input_data = Variable(pic_array_trans, requires_grad=False)

        # pic_array = cv2.resize(pic_array, (28, 28))
        # pic_tensor = torch.from_numpy(pic_array).float().permute(2, 0, 1).unsqueeze(0)/255
        # input_data = Variable(pic_tensor, requires_grad=False)

        if torch.cuda.is_available():
            input_data = input_data.cuda()
        else:
            input_data = input_data.cpu()

        return input_data
