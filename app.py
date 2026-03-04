import webview
import sys
import os

# Get the correct path whether running as .py or compiled .exe
if getattr(sys, '_MEIPASS', None):
    base = sys._MEIPASS
else:
    base = os.path.dirname(os.path.abspath(__file__))

html_path = os.path.join(base, 'KrownVault.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

webview.create_window(
    'KrownVault',
    html=html,
    width=540,
    height=920,
    resizable=True,
    min_size=(400, 600)
)

webview.start()
