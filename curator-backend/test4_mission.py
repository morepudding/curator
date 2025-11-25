from llama_cpp import Llama
import time

print("🔧 Chargement modèle Mistral 7B...")

llm = Llama(
    model_path="./models/mistral-7b-instruct-q4.gguf",
    n_ctx=2048,
    n_gpu_layers=35
)

print("✅ Modèle chargé !\n")

prompt = """<s>[INST] Generate a D&D mission description.

Type: Infiltration
Location: Dark Cave (north of village)
Objective: Retrieve stolen artifact
Difficulty: Medium (7/10)

Generate:
1. Mission description (200-250 words) - urgent, tense tone
2. Success text (100 words) - victorious tone
3. Failure text (100 words) - consequences tone

Format clearly with headers.
[/INST]"""

print("📝 Génération mission...\n")
start = time.time()

output = llm(
    prompt,
    max_tokens=600,
    temperature=0.75,
    top_p=0.9,
    stop=["</s>", "[INST]"]
)

elapsed = time.time() - start
response = output['choices'][0]['text'].strip()

print("=" * 60)
print("🗺️  MISSION GÉNÉRÉE :")
print("=" * 60)
print(response)
print("=" * 60)
print(f"\n⏱️  Temps génération : {elapsed:.2f}s")
print(f"📊 Nombre de mots : {len(response.split())}")
print(f"🔢 Tokens générés : {output['usage']['completion_tokens']}")
