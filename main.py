from PySide6.QtWidgets import QApplication
import sys
from View import View
from Model import Model
from ViewModel import ViewModel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Model()
    viewModel = ViewModel(model)
    window = View(viewModel)
    window.show()
    sys.exit(app.exec())
