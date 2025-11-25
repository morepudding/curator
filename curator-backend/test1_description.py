from llama_cpp import Llama
import time

print("🔧 Chargement modèle Mistral 7B...")
print("(Cela peut prendre 30 secondes)")

llm = Llama(
    model_path="./models/mistral-7b-instruct-q4.gguf",
    n_ctx=2048,
    n_gpu_layers=35  # Décharger sur GPU si disponible
)

print("✅ Modèle chargé !\n")

# Prompt
prompt = """<s>[INST] You are a D&D 5e character creator.

Generate a physical description for a hero named Bjorn, a human fighter.

Requirements:
- Length: 150-200 words
- Include: appearance, clothing, equipment
- Tone: Descriptive, immersive
- Style: Medieval fantasy

[/INST]"""

print("📝 Génération en cours...\n")
start = time.time()

output = llm(
    prompt,
    max_tokens=300,
    temperature=0.7,
    top_p=0.9,
    stop=["</s>", "[INST]"]
)

elapsed = time.time() - start
response = output['choices'][0]['text'].strip()

print("=" * 60)
print("📜 RÉSULTAT :")
print("=" * 60)
print(response)
print("=" * 60)
print(f"\n⏱️  Temps génération : {elapsed:.2f}s")
print(f"📊 Nombre de mots : {len(response.split())}")
print(f"🔢 Tokens générés : {output['usage']['completion_tokens']}")
