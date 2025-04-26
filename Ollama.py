import requests

class OllamaClient:
    def __init__(self, model: str, base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url.rstrip("/")

    def generate(self, prompt: str, stream: bool = False):
        """
        Envía una solicitud de generación a Ollama.

        :param prompt: El texto de entrada para el modelo.
        :param stream: Si se desea respuesta por streaming (por ahora no implementado).
        :return: Respuesta del modelo.
        """
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()

        if stream:
            for line in response.iter_lines():
                if line:
                    print(line.decode("utf-8"))
        else:
            return response.json()["response"]

    def list_models(self):
        """Lista los modelos disponibles en Ollama."""
        url = f"{self.base_url}/api/tags"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["models"]