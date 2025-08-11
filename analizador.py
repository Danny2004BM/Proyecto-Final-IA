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

# Cargar modelo rápido y eficiente
modelo = WhisperModel("small", device="cpu", compute_type="int8")

# Función para transcribir y analizar texto
def transcribir_y_analizar(ruta_audio):
    if ruta_audio is None:
        return "Por favor, sube un archivo de audio.", ""

    inicio = time.time()

    # Transcripción por segmentos
    segmentos, _ = modelo.transcribe(ruta_audio, beam_size=5)
    letra = "\n".join([segmento.text.strip() for segmento in segmentos])

    fin = time.time()
    tiempo = fin - inicio

    # Análisis de palabras
    palabras = nltk.word_tokenize(letra.lower())
    palabras_filtradas = [p for p in palabras if p.isalpha()]
    conteo = Counter(palabras_filtradas)
    top10 = conteo.most_common(10)
    resumen = "\n".join([f"{palabra}: {frecuencia}" for palabra, frecuencia in top10])

    # Añadir tiempo al texto transcrito
    letra_con_tiempo = f"{letra}\n\n---\nTiempo de análisis: {tiempo:.2f} segundos"

    return letra_con_tiempo, resumen

# Interfaz gráfica con Gradio
with gr.Blocks() as demo:
    gr.Markdown("#  Analizador de letras de canciones (versión mejorada)")
    gr.Markdown("Sube un archivo mp3 o wav y obtén la letra con análisis de palabras y tiempo de transcripción.")

    entrada_audio = gr.Audio(type="filepath", label="Subir canción (mp3 o wav)")
    salida_letra = gr.Textbox(label="Letra transcrita", lines=20)
    salida_analisis = gr.Textbox(label="Top 10 palabras más usadas", lines=10)
    boton = gr.Button("Analizar")

    boton.click(transcribir_y_analizar, inputs=entrada_audio, outputs=[salida_letra, salida_analisis])
