# 📘 RAG Penal Español

Este proyecto implementa un sistema de **Retrieval-Augmented Generation (RAG)** utilizando el **Código Penal Español** como corpus base. El objetivo es responder preguntas del usuario únicamente con información contenida en dicho corpus, sin alucinaciones o invenciones.

## 🚀 Tecnologías usadas

- [`sentence-transformers`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) para generar embeddings semánticos.
- [`PyMuPDF`](https://pymupdf.readthedocs.io/) (`fitz`) para leer el PDF del Código Penal.
- [`Ollama`](https://ollama.com) como backend LLM (probado con `llama3.2`).
- Python 3.9+

## 📂 Estructura del proyecto

```
├── RAG.py             # Clase para dividir el corpus y recuperar chunks relevantes
├── Ollama.py          # Clase HTTP para interactuar con Ollama
├── iaiao.ipynb        # Notebook de preguntas/respuestas
├── docs/
│   └── codigo_penal.pdf  # Corpus base (Código Penal Español)
```

## ⚙️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/rag-penal-espanol.git
cd rag-penal-espanol
```

2. Instala las dependencias:
```bash
pip install sentence-transformers pymupdf requests numpy
```

3. Asegúrate de tener [Ollama](https://ollama.com) corriendo localmente y tener el modelo descargado:
```bash
ollama run llama3.2:3b
```

4. Coloca `codigo_penal.pdf` dentro de la carpeta `./docs/`

## 🧠 ¿Cómo funciona?

1. El corpus se divide en chunks solapados.
2. Se generan embeddings con `all-MiniLM-L6-v2`.
3. El usuario hace una pregunta → se genera un embedding de la misma.
4. Se seleccionan los 3 chunks más similares al embedding de la pregunta.
5. Estos chunks se usan como contexto para generar una respuesta precisa con el modelo LLM.


## 🛑 Limitaciones

- Solo responde con base en el texto proporcionado.
- Si la información no está en el corpus, el modelo indica que no puede responder.

## 📄 Licencia

MIT License