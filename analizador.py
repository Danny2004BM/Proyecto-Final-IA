# Autor: Danny Berroa Mercedes
# Matrícula: 23-EISN-2-022
# Descripción: Analizador de letras de canciones rápido con análisis de palabras usando Faster Whisper y Gradio

from faster_whisper import WhisperModel
import gradio as gr
import time
import nltk
from collections import Counter

# Descargar recursos para tokenización de nltk (solo la primera vez)
nltk.download('punkt')
