import sys
from PyQt5.QtWidgets import QWidget, QComboBox, QApplication


class ComboxDemo(QWidget):
    def __init__(self):
        super().__init__()
        # 设置标题
        self.setWindowTitle('ComBox例子')
        # 设置初始界面大小
        self.resize(300, 200)

        # 实例化QComBox对象
        self.cb = QComboBox(self)
        self.cb.move(100, 20)

        # 单个添加条目
        self.cb.addItem('C')
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        # 多个添加条目
        self.cb.addItems(['Java', 'C#', 'PHP'])

        # 信号
        self.cb.currentIndexChanged[str].connect(self.print_value) # 条目发生改变，发射信号，传递条目内容
        self.cb.currentIndexChanged[int].connect(self.print_value)  # 条目发生改变，发射信号，传递条目索引
        self.cb.highlighted[str].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目内容
        self.cb.highlighted[int].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目索引

    def print_value(self, i):
        print(i)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec_())