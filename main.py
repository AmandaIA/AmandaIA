import openai
import os
import sys
import json

# Configuração da API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Função para executar a ação
def execute_action(prompt):
    response = openai.Completion.create(
        model="gpt-4-turbo",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
    )
    return response.choices[0].text

# Recebendo a entrada do webhook
if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    prompt_text = data.get("prompt")
    print(execute_action(prompt_text))
