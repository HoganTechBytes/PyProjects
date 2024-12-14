import tkinter as tk
from tkinter import filedialog
import pygame
import wave
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import threading

# tkinter window
window = tk.Tk()
window.title("HTB Media Player")

# pygame mixer
pygame.mixer.init()
