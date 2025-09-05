from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
import sys

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout(window)

text = """
<ul style="margin:0; padding-left:15px;">
  <li>This is a very long bullet point that will wrap correctly when it reaches the edge of the widget.</li>
  <li>Another long bullet point with proper indentation and word wrapping in PyQt.</li>
</ul>
"""

label = QLabel(text)
label.setWordWrap(True)
label.setTextFormat(Qt.TextFormat.RichText)
label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

layout.addWidget(label)
window.setLayout(layout)
window.show()

sys.exit(app.exec())
