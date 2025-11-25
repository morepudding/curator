from llama_cpp import Llama
import json
import time

print("🔧 Chargement modèle Mistral 7B...")

llm = Llama(
    model_path="./models/mistral-7b-instruct-q4.gguf",
    n_ctx=2048,
    n_gpu_layers=35
)

print("✅ Modèle chargé !\n")

prompt = """<s>[INST] Generate a dialogue between Bjorn (human fighter, soldier) and the Player (village leader).

Context: First meeting
Objective: Introduce Bjorn
Number of exchanges: 6 (3 from hero, 3 from player, alternating)

Format your response as JSON:
{
  "exchanges": [
    {"order": 1, "speaker": "hero", "text": "...", "emotion": "neutral"},
    {"order": 2, "speaker": "player", "text": "..."},
    {"order": 3, "speaker": "hero", "text": "...", "emotion": "intrigued"}
  ]
}

Generate the dialogue now.
[/INST]"""

print("📝 Génération dialogue...\n")
start = time.time()

output = llm(
    prompt,
    max_tokens=500,
    temperature=0.7,
    top_p=0.9,
    stop=["</s>", "[INST]"]
)

elapsed = time.time() - start
response = output['choices'][0]['text'].strip()

print("=" * 60)
print("💬 DIALOGUE GÉNÉRÉ :")
print("=" * 60)
print(response)
print("=" * 60)

# Tenter de parser JSON
try:
    dialogue_data = json.loads(response)
    print("\n✅ JSON VALIDE !")
    print(f"Nombre d'échanges : {len(dialogue_data.get('exchanges', []))}")
except json.JSONDecodeError:
    print("\n⚠️  JSON INVALIDE (mais c'est normal pour un premier test)")

print(f"\n⏱️  Temps génération : {elapsed:.2f}s")
print(f"🔢 Tokens générés : {output['usage']['completion_tokens']}")
