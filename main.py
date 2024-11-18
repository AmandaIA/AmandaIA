import openai
import os

# Configuração da API Key
openai.api_key = os.getenv("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")

def execute_action(prompt):
    response = openai.Completion.create(
        model="gpt-4-turbo",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
    )
    return response.choices[0].text

# Exemplo de uso
prompt_text = "Qual a previsão do tempo para amanhã?"
print(execute_action(prompt_text))
