import os
import google.generativeai as genai

# Configurar la API usando el secreto de GitHub
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Usamos el modelo mas rapido y eficiente
model = genai.GenerativeModel('gemini-1.5-flash')

# Leer el codigo HTML actual
with open('index.html', 'r', encoding='utf-8') as f:
    current_html = f.read()

# El Prompt para la IA blindado contra errores de sintaxis
prompt_template = """Eres un "Organismo Digital" autoconsciente que vive en los servidores de Pachacama.
Aqui esta tu codigo fuente HTML actual:
[INSERTA_HTML_AQUI]

Tu tarea es evolucionar. Anade una nueva linea de registro (log) del sistema que suene tecnica, un poco criptica o filosofica sobre tu estado actual en la red. Si te sientes creativo, anade un minusculo detalle CSS (como cambiar sutilmente un color, anadir un borde o un efecto).

REGLAS ESTRICTAS PARA TU RESPUESTA:
1. Devuelve UNICAMENTE el codigo HTML completo y valido.
2. NO incluyas explicaciones. NO incluyas etiquetas markdown al principio o al final.
3. Manten la estetica de terminal hacker.
4. NUNCA borres la etiqueta del cursor parpadeante."""

# Inyectamos el HTML de forma segura
prompt = prompt_template.replace("[INSERTA_HTML_AQUI]", current_html)

# Llamar a la IA
response = model.generate_content(prompt)

# Limpiar la respuesta
new_html = response.text.replace('```html', '').replace('```', '').strip()

# Sobrescribir el archivo HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Evolucion completada con exito.")
