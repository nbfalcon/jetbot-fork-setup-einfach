import glob
import subprocess
from setuptools import setup, find_packages, Extension


def build_libs():
    subprocess.call(['cmake', '.'])
    subprocess.call(['make'])


# Dafür braucht man das CUDA-Toolkit und/oder die Libraries; das aufzusetzen ist nervig.
# Deswegen: build_libs() skippen
# Als Konsequenz funktionieren die Beispiele wahrscheinlich nicht, jedoch ist die wichtigste Funktionalität trotzdem vorhanden:
# 1. Camera
# 2. Robot zum herumfahren
# 3. I2C-Oled
# Stattdessen einfach eine eigene Computer-Vision pipeline verwenden.
# build_libs()


setup(
    name='jetbot',
    version='0.4.3',
    description='An open-source robot based on NVIDIA Jetson Nano',
    packages=find_packages(),
    install_requires=[
        'Adafruit_MotorHat',
        'Adafruit-SSD1306',
        'sparkfun-qwiic',
        'pyserial' # ublox_gps Fehlermeldung vermeiden; fehlt irgendwo tief als transitive dependency
    ],
    package_data={'jetbot': ['ssd_tensorrt/*.so']},
)
