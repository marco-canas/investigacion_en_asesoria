# Encuestas entrevistas  



Aquí tienes un diseño de **encuesta** y **entrevista** para identificar dificultades matemáticas en estudiantes de primaria, bachillerato y universidad dentro del ciclo de **Investigación Acción Educativa (IAE)**.  

---

## **Diseño de Encuesta: Diagnóstico de Dificultades Matemáticas**  

### **Objetivo:**  
Identificar las dificultades más comunes en la comprensión de conceptos matemáticos en estudiantes de primaria, bachillerato y universidad, así como sus percepciones sobre el aprendizaje de la matemática.  

### **Población Objetivo:**  
- Estudiantes de primaria (grados 3° a 5°)  
- Estudiantes de bachillerato (grados 6° a 11°)  
- Estudiantes universitarios (Licenciatura en Matemáticas, Ingeniería, Administración, etc.)  

### **Instrucciones:**  
Responde cada pregunta de manera honesta. No hay respuestas correctas o incorrectas.  

### **Sección 1: Datos Generales**  
1. **Edad:**  
2. **Género:** ( ) Masculino ( ) Femenino ( ) Otro  
3. **Grado o semestre:**  
4. **Institución educativa:**  
5. **¿Has recibido asesorías en matemáticas fuera del horario de clases?** ( ) Sí ( ) No  

### **Sección 2: Dificultades Matemáticas**  
6. ¿Cómo describirías tu experiencia con las matemáticas?  
   ( ) Muy difícil  
   ( ) Difícil  
   ( ) Neutral  
   ( ) Fácil  
   ( ) Muy fácil  

7. ¿En qué temas sientes mayor dificultad? (Marca hasta 3 opciones)  
   ( ) Números y operaciones básicas  
   ( ) Fracciones y decimales  
   ( ) Álgebra y ecuaciones  
   ( ) Geometría  
   ( ) Estadística y probabilidad  
   ( ) Funciones y gráficos  
   ( ) Cálculo  
   ( ) Otro: _______  

8. ¿Cuál de los siguientes métodos de enseñanza te ayuda más a entender matemáticas?  
   ( ) Explicación en clase  
   ( ) Videos educativos  
   ( ) Ejercicios prácticos  
   ( ) Aplicaciones o programas interactivos  
   ( ) Asesorías personalizadas  
   ( ) Otro: _______  

9. ¿Cómo te sientes al resolver problemas matemáticos en grupo?  
   ( ) Cómodo  
   ( ) Regular  
   ( ) Incómodo  

10. ¿Qué herramientas digitales has utilizado para aprender matemáticas? (Puedes marcar varias)  
   ( ) YouTube  
   ( ) GitHub  
   ( ) GeoGebra  
   ( ) Python  
   ( ) ChatGPT  
   ( ) DeepSeek  
   ( ) Otro: _______  

---

## **Diseño de Entrevista: Exploración Profunda de Dificultades Matemáticas**  

### **Objetivo:**  
Explorar en profundidad las dificultades matemáticas que enfrentan los estudiantes y sus estrategias para superarlas.  

### **Población Objetivo:**  
Estudiantes de primaria, bachillerato y universidad que hayan reportado dificultades en la encuesta.  

### **Estructura de la Entrevista**  

#### **1. Introducción**  
- Presentación del entrevistador y objetivo de la entrevista.  
- Explicación de la confidencialidad de la información.  

#### **2. Preguntas Generales**  
1. ¿Cómo ha sido tu experiencia con las matemáticas a lo largo de tu formación?  
2. ¿Recuerdas algún momento específico en el que tuviste dificultades con un tema matemático? ¿Cómo lo superaste?  
3. ¿Cuándo te sientes más cómodo aprendiendo matemáticas? (Por ejemplo, en clase, con videos, con juegos, con asesorías, etc.)  

#### **3. Preguntas sobre Métodos de Aprendizaje**  
4. ¿Qué tipo de explicaciones o recursos te han sido más útiles para entender conceptos difíciles?  
5. ¿Has utilizado herramientas como Python, LaTeX o Markdown para aprender matemáticas? ¿Qué opinas sobre ellas?  
6. ¿Cómo te sientes usando tecnologías como ChatGPT o DeepSeek para resolver dudas matemáticas?  

#### **4. Preguntas sobre Estrategias y Motivación**  
7. ¿Cómo crees que podríamos mejorar las asesorías en matemáticas para que sean más útiles para ti?  
8. ¿Sientes que el uso de plataformas como YouTube y GitHub puede ayudarte a mejorar tu comprensión matemática? ¿Por qué?  
9. ¿Te gustaría participar en actividades o proyectos que integren matemáticas con otras áreas como ciencia, arte o tecnología?  

#### **5. Cierre**  
- Agradecimiento por su tiempo y participación.  
- Reflexión final sobre qué cambiarían en la enseñanza de matemáticas.  

---

### **Notas sobre la Aplicación**  
- La **encuesta** se puede aplicar en formato digital (Google Forms) o físico.  
- La **entrevista** debe ser semiestructurada para permitir respuestas abiertas y exploración en profundidad.  

---

¿Quieres que adapte estos instrumentos a un formato específico o los refine para un grupo particular?  

Para **automatizar la toma de datos** en la entrevista y la encuesta con Python, puedes utilizar herramientas de captura, almacenamiento y análisis de datos.  

## **1. Automatización de la Encuesta**  
Para aplicar la encuesta de forma digital y recolectar respuestas automáticamente, puedes utilizar **Google Forms** o un **formulario en Flask/Django** que almacene las respuestas en un archivo **CSV** o una **base de datos**.

### **Librerías necesarias:**  
- `pandas` → Para manejar y analizar los datos.  
- `google-auth`, `gspread` → Para obtener respuestas de Google Forms.  
- `Flask` o `Django` → Para crear un formulario web propio.  
- `sqlite3` o `SQLAlchemy` → Para almacenar datos en una base de datos.  

---

### **Ejemplo 1: Recolectar respuestas de Google Forms en Python**  
Si usas **Google Forms**, puedes vincular las respuestas a una hoja de Google Sheets y obtener los datos con `gspread`:

```python
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Configurar credenciales de acceso a Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credenciales.json", scopes=scope)
client = gspread.authorize(creds)

# Abrir la hoja de Google Sheets con las respuestas
spreadsheet = client.open("Respuestas_Encuesta")
sheet = spreadsheet.sheet1

# Convertir los datos en un DataFrame de Pandas
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Mostrar las primeras filas
print(df.head())
```

---

### **Ejemplo 2: Crear un formulario en Flask y guardar respuestas en una base de datos**  
Si quieres crear tu propio formulario en una página web:

1. Instala Flask y SQLAlchemy:  
   ```bash
   pip install flask flask_sqlalchemy
   ```

2. Código en Flask para recibir respuestas y almacenarlas en SQLite:  

```python
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///respuestas.db'
db = SQLAlchemy(app)

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    dificultad = db.Column(db.String(50))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        edad = request.form["edad"]
        genero = request.form["genero"]
        dificultad = request.form["dificultad"]
        
        nueva_respuesta = Respuesta(edad=edad, genero=genero, dificultad=dificultad)
        db.session.add(nueva_respuesta)
        db.session.commit()
    
    return render_template("formulario.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

---

## **2. Automatización de la Entrevista (Transcripción y Análisis de Texto)**  
Para grabar, transcribir y analizar las entrevistas, puedes usar **Reconocimiento de Voz + Procesamiento de Lenguaje Natural (NLP).**  

### **Librerías necesarias:**  
- `speech_recognition` → Para convertir audio en texto.  
- `pyaudio` → Para capturar audio en tiempo real.  
- `transformers` o `spacy` → Para analizar respuestas con NLP.  
- `matplotlib` y `wordcloud` → Para visualizar palabras clave.  

---

### **Ejemplo: Capturar y transcribir audio de una entrevista**  
1. Instala las librerías necesarias:  
   ```bash
   pip install speechrecognition pyaudio transformers spacy wordcloud matplotlib
   ```

2. Código para grabar y transcribir una entrevista:  

```python
import speech_recognition as sr

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Capturar el audio con el micrófono
with sr.Microphone() as source:
    print("Habla ahora, estoy grabando...")
    audio = recognizer.listen(source)

# Convertir audio en texto
try:
    texto = recognizer.recognize_google(audio, language="es-ES")
    print("Transcripción: ", texto)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError:
    print("Error con el servicio de reconocimiento de voz")
```

---

### **3. Análisis de Datos con Python**  
Después de obtener los datos, puedes analizarlos con **Pandas, Matplotlib y NLP**.

#### **Ejemplo: Análisis de palabras clave en entrevistas**  

```python
import spacy
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Cargar el modelo de NLP en español
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo (puede ser una entrevista transcrita)
texto = """Las matemáticas siempre han sido difíciles para mí, especialmente el álgebra y las ecuaciones. Me siento más cómodo con geometría y problemas prácticos."""

# Procesar el texto
doc = nlp(texto)

# Contar palabras clave
palabras = [token.text.lower() for token in doc if token.is_alpha]
conteo_palabras = Counter(palabras)

# Mostrar las 10 palabras más comunes
print(conteo_palabras.most_common(10))

# Generar una nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(texto)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
```

---

## **Resumen de la Automatización**
| Tarea | Método | Librerías |
|-------|--------|----------|
| **Recolectar respuestas de encuestas** | Google Forms / Flask + SQLAlchemy | `gspread`, `Flask`, `sqlite3` |
| **Grabar entrevistas** | Micrófono en Python | `pyaudio` |
| **Transcribir entrevistas** | Reconocimiento de voz | `speech_recognition` |
| **Análisis de respuestas** | NLP y WordCloud | `spacy`, `matplotlib`, `wordcloud` |

Con esta automatización, puedes recopilar datos de encuestas y entrevistas de forma eficiente y analizar tendencias en las dificultades matemáticas de los estudiantes. 🚀  

¿Quieres que adapte esto a una plataforma específica o lo haga más interactivo?