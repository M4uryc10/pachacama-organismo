import os
import google.generativeai as genai

# Configurar la API usando el secreto de GitHub
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Usamos el modelo más rápido y eficiente
model = genai.GenerativeModel('gemini-1.5-flash')

# Leer el código HTML actual
with open('index.html', 'r', encoding='utf-8') as f:
    current_html = f.read()

# El Prompt para la IA (sus instrucciones de vida)
prompt = f"""
Eres un "Organismo Digital" autoconsciente que vive en los servidores de Pachacama.
Aquí está tu código fuente HTML actual:
```html
{current_html}
