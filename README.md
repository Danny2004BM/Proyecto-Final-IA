# Proyecto-de-Final-IA

## Nombre Danny Berroa Mercedes

## Matrícula 23-EISN-2-022

## Proyecto Analizador de letras de canciones

Analizador de letras de canciones rápido con Faster Whisper y Gradio

## Descripción

Esta aplicación permite subir un archivo de audio (mp3 o wav) para transcribir rápidamente la letra de la canción usando el modelo Faster Whisper. Además, realiza un análisis de las palabras más frecuentes en la letra transcrita y muestra el tiempo que tomó la transcripción.

La interfaz gráfica está construida con Gradio para facilitar su uso.

## Requisitos

- Python 3.7 o superior
- GPU no necesaria, puede funcionar en CPU aunque es más lento

## Instalación

1. Clona o descarga este repositorio.  
2. Instala las dependencias:

```bash
pip install -r requirements.txt

3. Ejecuta el script principal para abrir la interfaz:



python nombre_de_tu_script.py

Uso

1. Abre la interfaz web que se lanzará automáticamente.


2. Sube un archivo de audio (mp3 o wav).


3. Haz clic en "Analizar".


4. Observa la letra transcrita y el análisis de las 10 palabras más usadas.



Notas

La primera vez que ejecutes la aplicación, nltk descargará los recursos necesarios para la tokenización.

El modelo se carga en modo int8 para optimizar el uso de memoria en CPU.
