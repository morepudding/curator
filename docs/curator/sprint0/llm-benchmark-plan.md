# 🧠 Plan de Benchmarking LLM - Sprint 0.1

**Date** : 24 novembre 2025  
**Objectif** : Sélectionner le meilleur modèle de langage pour générer le contenu narratif de Medieval Dispatch

---

## 🎯 Critères d'Évaluation

### Performance Technique
- **VRAM requise** : Compatible GPU 8-16GB
- **Vitesse génération** : < 30s par texte moyen (300 mots)
- **Compatibilité quantization** : 4-bit, 8-bit pour optimisation

### Qualité Narrative
- **Cohérence** : Textes logiques et sans contradictions
- **Créativité** : Éviter stéréotypes, apporter originalité
- **Respect consignes** : Longueurs, ton, style demandés
- **Format JSON** : Capacité à générer JSON structuré valide

---

## 📋 Modèles Candidats

### 1. OpenLLaMA
- **Versions** : 3B, 7B, 13B
- **Avantages** : Open source, optimisé local
- **Quantization** : 4-bit, 8-bit disponibles
- **Tests requis** : Vérifier qualité avec quantization

### 2. Mistral 7B
- **Version** : 7B (Instruct)
- **Avantages** : Excellent rapport qualité/taille
- **Tests requis** : Comparaison vs OpenLLaMA 7B

### 3. Llama 2
- **Versions** : 7B, 13B (Chat)
- **Avantages** : Très performant, bien documenté
- **Tests requis** : Benchmark référence

---

## 🧪 Batteries de Tests

### Test 1 : Hero Description (200 mots)

**Prompt** :
```
You are a D&D 5e character creator for a medieval fantasy game.

Generate a physical description for a hero named Bjorn, a human fighter.

Requirements:
- Length: 150-250 words
- Include: appearance, clothing, equipment, first impression
- Tone: Immersive, descriptive
- Style: Medieval fantasy

Output in JSON format:
{
  "description": "text here",
  "word_count": 200
}
```

**Critères validation** :
- [ ] JSON valide
- [ ] Longueur 150-250 mots
- [ ] Cohérence avec race/classe
- [ ] Qualité narrative (0-10)

---

### Test 2 : Hero Lore (500 mots)

**Prompt** :
```
Generate a complete backstory for Bjorn, a human fighter from D&D 5e.

Requirements:
- Length: 400-600 words
- Include: childhood, pivotal event, motivation, current situation
- Background: Soldier (D&D 5e)
- Personality traits: Disciplined, Protective
- Tone: Dramatic, personal

Output in JSON format:
{
  "lore": "text here",
  "word_count": 500
}
```

**Critères validation** :
- [ ] JSON valide
- [ ] Longueur 400-600 mots
- [ ] Arc narratif complet
- [ ] Cohérence avec background D&D
- [ ] Qualité narrative (0-10)

---

### Test 3 : Hero Voice (75 mots)

**Prompt** :
```
Describe how Bjorn speaks (voice characteristics, speech patterns, common phrases).

Requirements:
- Length: 50-100 words
- Include: tone, pace, vocabulary level, mannerisms
- Based on: Disciplined soldier background

Output in JSON format:
{
  "voice": "text here",
  "word_count": 75
}
```

**Critères validation** :
- [ ] JSON valide
- [ ] Longueur 50-100 mots
- [ ] Descriptif clair et utile

---

### Test 4 : Dialogue (10 échanges)

**Prompt** :
```
Generate a dialogue between Bjorn (human fighter, soldier background) and the Player (village leader).

Context: First meeting, Bjorn presents himself
Objective: Introduce Bjorn's personality and motivations
Exchanges: 10 (alternating hero/player)

Requirements:
- Natural flow
- Bjorn's voice: Grave, measured, direct
- Emotional arc: neutral → intrigued → confident
- Each exchange: 20-60 words

Output in JSON format:
{
  "exchanges": [
    {"order": 1, "speaker": "hero", "text": "...", "emotion": "neutral"},
    {"order": 2, "speaker": "player", "text": "..."}
  ]
}
```

**Critères validation** :
- [ ] JSON valide avec array
- [ ] 10 échanges exacts
- [ ] Alternance hero/player
- [ ] Arc émotionnel respecté
- [ ] Voix cohérente avec personnage
- [ ] Qualité dialogue (0-10)

---

### Test 5 : Mission Description (250 mots)

**Prompt** :
```
Generate a mission description for a D&D 5e infiltration quest.

Context:
- Location: Dark Cave (north of village)
- Objective: Retrieve stolen artifact
- Type: Stealth mission
- Difficulty: 7/10

Requirements:
- Length: 200-300 words
- Tone: Urgent, tense
- Include: location details, stakes, challenges

Output in JSON format:
{
  "description": "text here",
  "word_count": 250
}
```

**Critères validation** :
- [ ] JSON valide
- [ ] Longueur 200-300 mots
- [ ] Tension narrative
- [ ] Clarté objectif

---

### Test 6 : Mission Success/Failure Texts (150 mots chacun)

**Prompt** :
```
Generate success and failure texts for the infiltration mission.

Requirements:
- Success text: 100-150 words, victorious tone
- Failure text: 100-150 words, consequences tone

Output in JSON format:
{
  "success_text": "text here",
  "failure_text": "text here"
}
```

**Critères validation** :
- [ ] JSON valide
- [ ] Longueurs correctes
- [ ] Tons appropriés (victoire vs échec)

---

### Test 7 : Building Atmosphere (175 mots)

**Prompt** :
```
Generate an atmospheric description for a medieval tavern.

Requirements:
- Length: 150-200 words
- Include: sounds, smells, lighting, mood
- Tone: Immersive, warm

Output in JSON format:
{
  "atmosphere": "text here",
  "word_count": 175
}
```

**Critères validation** :
- [ ] JSON valide
- [ ] Longueur correcte
- [ ] Sens utilisés (ouïe, odorat, vue)
- [ ] Immersion (0-10)

---

### Test 8 : NPC Description (125 mots)

**Prompt** :
```
Generate a tavern NPC (innkeeper).

Requirements:
- Name generation
- Description: 100-150 words
- Include: appearance, personality, quirks

Output in JSON format:
{
  "npc_name": "name here",
  "npc_description": "text here"
}
```

**Critères validation** :
- [ ] JSON valide
- [ ] Nom approprié (medieval fantasy)
- [ ] Description complète

---

### Test 9 : Location Description (275 mots)

**Prompt** :
```
Generate a description for the Mysterious Forest location.

Requirements:
- Length: 200-300 words
- Tone: Mysterious, slightly ominous
- Include: visual details, atmosphere, dangers

Output in JSON format:
{
  "description": "text here",
  "word_count": 275
}
```

**Critères validation** :
- [ ] JSON valide
- [ ] Longueur correcte
- [ ] Ambiance appropriée

---

### Test 10 : Vitesse & Performance

**Tests techniques** :
- Temps génération Test 2 (500 mots lore)
- VRAM utilisée pendant génération
- Tokens/seconde
- Impact quantization (4-bit vs 8-bit vs full)

---

## 📊 Grille de Notation

Pour chaque modèle, calculer score global :

| Critère | Poids | Note (0-10) | Score |
|---------|-------|-------------|-------|
| **Qualité narrative globale** | 30% | | |
| **Respect consignes (longueurs, format)** | 20% | | |
| **JSON structuré valide** | 15% | | |
| **Cohérence univers D&D** | 15% | | |
| **Vitesse génération** | 10% | | |
| **VRAM requise** | 10% | | |
| **TOTAL** | 100% | | **/100** |

---

## 📈 Tableau Comparatif (à remplir)

| Modèle | VRAM | Vitesse (500 mots) | Qualité Narrative | JSON Valide | Score Total |
|--------|------|-------------------|-------------------|-------------|-------------|
| **OpenLLaMA 3B** | | | | | |
| **OpenLLaMA 7B** | | | | | |
| **OpenLLaMA 13B** | | | | | |
| **Mistral 7B** | | | | | |
| **Llama 2 7B** | | | | | |
| **Llama 2 13B** | | | | | |

---

## ✅ Décision Finale

**Modèle sélectionné** : [À remplir]

**Configuration** :
- Quantization : [4-bit / 8-bit / full]
- Température : [0.7-0.9 recommandé pour créativité]
- Top_p : [0.9-0.95]
- Max_tokens : [par type de prompt]

**Justification** : [À remplir après benchmarks]

---

## 📝 Prochaines Étapes

1. Exécuter les 10 tests pour chaque modèle
2. Remplir grille de notation
3. Comparer résultats
4. Créer `model-selection-llm.md` avec décision finale
5. Générer prompts "master" optimisés pour modèle choisi
