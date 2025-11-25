from llama_cpp import Llama
import time

print("🔧 Chargement modèle Mistral 7B...")

llm = Llama(
    model_path="./models/mistral-7b-instruct-q4.gguf",
    n_ctx=2048,
    n_gpu_layers=35
)

print("✅ Modèle chargé !\n")

prompt = """<s>[INST] You are a D&D 5e storyteller.

Generate a complete backstory for Bjorn, a human fighter with the Soldier background.

Requirements:
- Length: 400-500 words
- Include: childhood, pivotal event, motivation, current situation
- Personality: Disciplined, protective
- Tone: Dramatic, personal
- Make it emotionally engaging

[/INST]"""

print("📝 Génération lore (peut prendre 30-60s)...\n")
start = time.time()

output = llm(
    prompt,
    max_tokens=600,
    temperature=0.75,
    top_p=0.92,
    stop=["</s>", "[INST]"]
)

elapsed = time.time() - start
response = output['choices'][0]['text'].strip()

print("=" * 60)
print("📜 BACKSTORY BJORN :")
print("=" * 60)
print(response)
print("=" * 60)
print(f"\n⏱️  Temps génération : {elapsed:.2f}s")
print(f"📊 Nombre de mots : {len(response.split())}")
print(f"🔢 Tokens générés : {output['usage']['completion_tokens']}")
