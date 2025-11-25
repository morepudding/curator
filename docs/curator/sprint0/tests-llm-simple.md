# 🧪 Tests Simples LLM - Mistral 7B Instruct

**Date** : 24 novembre 2025  
**Modèle** : Mistral 7B Instruct (4-bit GPTQ)  
**GPU** : GTX 1660 Super (6GB)

---

## 📝 Test 1 : Hero Description (Simple)

**Objectif** : Tester génération description physique héros

### Script Python : `test_llm_hero_description.py`

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import time

print("🔧 Chargement modèle...")
model_path = "./models/mistral-7b-instruct-gptq"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True
)

print(f"✅ Modèle chargé sur {model.device}")

# Prompt
prompt = """<s>[INST] You are a D&D 5e character creator.

Generate a physical description for a hero named Bjorn, a human fighter.

Requirements:
- Length: 150-200 words
- Include: appearance, clothing, equipment
- Tone: Descriptive, immersive
- Style: Medieval fantasy

[/INST]"""

print("\n📝 Génération en cours...\n")
start = time.time()

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=300,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

result = tokenizer.decode(outputs[0], skip_special_tokens=True)
elapsed = time.time() - start

# Extraire seulement la réponse (après [/INST])
response = result.split("[/INST]")[-1].strip()

print("=" * 60)
print("📜 RÉSULTAT :")
print("=" * 60)
print(response)
print("=" * 60)
print(f"\n⏱️  Temps génération : {elapsed:.2f}s")
print(f"📊 Nombre de mots : {len(response.split())}")
print(f"💾 VRAM utilisée : {torch.cuda.max_memory_allocated() / 1024**3:.2f} GB")
```

### Commandes

```powershell
# Activer environnement
cd c:\Users\BOTTEROOOW\dispatchgenerator\curator-backend
.\venv\Scripts\Activate.ps1

# Créer le fichier
# [Copier le script ci-dessus dans test_llm_hero_description.py]

# Exécuter
python test_llm_hero_description.py
```

### ✅ Critères Validation

- [ ] Génération réussie (pas d'erreur)
- [ ] Temps < 30s
- [ ] Texte cohérent (150-200 mots)
- [ ] Qualité narrative (1-5) : ___
- [ ] VRAM < 5GB

---

## 📝 Test 2 : Hero Lore (Moyen)

**Objectif** : Tester génération backstory longue

### Script Python : `test_llm_hero_lore.py`

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import time

print("🔧 Chargement modèle...")
model_path = "./models/mistral-7b-instruct-gptq"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True
)

prompt = """<s>[INST] You are a D&D 5e storyteller.

Generate a complete backstory for Bjorn, a human fighter with the Soldier background.

Requirements:
- Length: 400-500 words
- Include: childhood, pivotal event, motivation, current situation
- Personality: Disciplined, protective
- Tone: Dramatic, personal
- Make it emotionally engaging

[/INST]"""

print("\n📝 Génération lore (peut prendre 30-60s)...\n")
start = time.time()

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=600,
    temperature=0.75,
    top_p=0.92,
    do_sample=True
)

result = tokenizer.decode(outputs[0], skip_special_tokens=True)
elapsed = time.time() - start
response = result.split("[/INST]")[-1].strip()

print("=" * 60)
print("📜 BACKSTORY BJORN :")
print("=" * 60)
print(response)
print("=" * 60)
print(f"\n⏱️  Temps génération : {elapsed:.2f}s")
print(f"📊 Nombre de mots : {len(response.split())}")
print(f"💾 VRAM utilisée : {torch.cuda.max_memory_allocated() / 1024**3:.2f} GB")
```

### ✅ Critères Validation

- [ ] Génération réussie
- [ ] Temps < 60s
- [ ] Texte cohérent (400-500 mots)
- [ ] Arc narratif complet (enfance → événement → motivation)
- [ ] Qualité narrative (1-5) : ___

---

## 📝 Test 3 : Dialogue (Avancé)

**Objectif** : Tester génération dialogue structuré

### Script Python : `test_llm_dialogue.py`

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import json
import time

print("🔧 Chargement modèle...")
model_path = "./models/mistral-7b-instruct-gptq"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True
)

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

print("\n📝 Génération dialogue...\n")
start = time.time()

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=500,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

result = tokenizer.decode(outputs[0], skip_special_tokens=True)
elapsed = time.time() - start
response = result.split("[/INST]")[-1].strip()

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
print(f"💾 VRAM utilisée : {torch.cuda.max_memory_allocated() / 1024**3:.2f} GB")
```

### ✅ Critères Validation

- [ ] Génération réussie
- [ ] JSON valide (ou proche)
- [ ] 6 échanges alternés
- [ ] Dialogue naturel
- [ ] Qualité (1-5) : ___

---

## 📝 Test 4 : Mission Description

**Objectif** : Tester génération contenu mission

### Script Python : `test_llm_mission.py`

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import time

print("🔧 Chargement modèle...")
model_path = "./models/mistral-7b-instruct-gptq"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True
)

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

print("\n📝 Génération mission...\n")
start = time.time()

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=600,
    temperature=0.75,
    top_p=0.9,
    do_sample=True
)

result = tokenizer.decode(outputs[0], skip_special_tokens=True)
elapsed = time.time() - start
response = result.split("[/INST]")[-1].strip()

print("=" * 60)
print("🗺️  MISSION GÉNÉRÉE :")
print("=" * 60)
print(response)
print("=" * 60)
print(f"\n⏱️  Temps génération : {elapsed:.2f}s")
print(f"📊 Nombre de mots : {len(response.split())}")
print(f"💾 VRAM utilisée : {torch.cuda.max_memory_allocated() / 1024**3:.2f} GB")
```

### ✅ Critères Validation

- [ ] Génération réussie
- [ ] Description + success + failure présents
- [ ] Longueurs appropriées
- [ ] Tons distincts (urgence → victoire → échec)
- [ ] Qualité (1-5) : ___

---

## 📊 Fiche Résultats Tests

| Test | Temps | VRAM | Qualité (1-5) | Notes |
|------|-------|------|---------------|-------|
| Test 1 (Description) | ___s | ___GB | ___ | |
| Test 2 (Lore) | ___s | ___GB | ___ | |
| Test 3 (Dialogue) | ___s | ___GB | ___ | |
| Test 4 (Mission) | ___s | ___GB | ___ | |

---

## 🎯 Prochaines Étapes

Après avoir exécuté ces 4 tests, on pourra :
1. Ajuster paramètres (temperature, top_p) si besoin
2. Créer prompts optimisés pour chaque type
3. Passer aux tests Stable Diffusion
