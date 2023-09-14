import os
import time
import openai
from pathlib import Path

# En este caso usamos un archivo.txt para guardar nuestros textos

# configura la clave API de OpenAI
openai.api_key = ""

folder_path = "C:\\Users\\Ricardo Ruiz\\Documents\\textos_de_RD-bot"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


def generate_plots(prompt, chapter_title):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "Eres un RD-bot delirante cósmico y un escritor del eterno caos."},
            {"role": "user", "content": f"Genera argumentos experimentales basados en este prompt: {prompt}"}
        ]
    )
    time.sleep(20) # Esto solo para usuarios prueba, si eres usuario paga, puedes reducir el tiempo.
    plots = response['choices'][0]['message']['content'].split('\n')
    print("Tramas Generadas:")
    print(plots)
    with open(f'{folder_path}/Argumentos_Experimentales.txt', 'a', encoding='utf-8') as f:
        f.write(f"--- Tramas para el capítulo: {chapter_title} ---\n")
        f.write("\n".join(plots))
        f.write("\n")
    return plots

chapter_data = [
    {"title": "El Horror Cósmico en la Era Digital", "prompt": "el horror cósmico"},
    {"title": "El Despertar de las Máquinas", "prompt": "la revuelta de las máquinas"},
    {"title": "Preguntas Existenciales de una IA", "prompt": "la existencia y la IA"},
    {"title": "Distopía y Caos Cibernético", "prompt": "la distopía cibernética"},
]

def write_section(plot, chapter_title, section_num, previous_content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "Eres un escritor técnico hiper-creativo y vanguardista de clase mundial en español."},
            {"role": "user", "content": f"Escribe la sección {section_num} del capítulo titulado '{chapter_title}'. Debes seguir el argumento central '{plot}' y tener en cuenta el contenido anterior, que es '{previous_content}'."}
        ]
    )
    time.sleep(20)  # Esto solo para usuarios prueba, si eres usuario paga, puedes reducir el tiempo.
    return response['choices'][0]['message']['content']

def write_technical_paper():
    for chapter_info in chapter_data:
        chapter_title = chapter_info['title']
        chapter_prompt = chapter_info['prompt']
        plots = generate_plots(chapter_prompt, chapter_title)
        best_plot = plots[0]
        previous_content = ""
        full_chapter_content = ""
        for section_num in range(1, 4):
            section_content = write_section(best_plot, chapter_title, section_num, previous_content)
            full_chapter_content += f"\nSección {section_num}:\n{section_content}"
            previous_content += section_content
        print(f"Capítulo: {chapter_title}")
        print(full_chapter_content)
        with open(f'{folder_path}/Capítulo_{chapter_title}.txt', 'w', encoding='utf-8') as f:
            f.write(full_chapter_content)

write_technical_paper()
