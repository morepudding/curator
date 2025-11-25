# 🏗️ Architecture Système Curator - Sprint 0.3

**Date** : 24 novembre 2025  
**Objectif** : Définir l'architecture technique complète du système Curator

---

## 🎯 Vision Architecturale

Le Curator est une **application standalone fullstack** composée de :
- **Frontend Next.js** : Interface multi-niveaux de curation
- **Backend Python** : Services IA (LLM + Stable Diffusion)
- **Stockage Local** : SQLite pour état générations
- **Export** : JSON + Assets organisés pour Supabase

---

## 📊 Mapping Tables Supabase → Générateurs

### Tables et Contenus à Générer

| Table Supabase | Générateur Backend | Champs Générés | Endpoint API |
|----------------|-------------------|----------------|--------------|
| `heroes` | HeroGenerator | description, lore, voice, secret, arc_day1/2/3, race, class, background, personality_traits, ideals, bonds, flaws | POST /api/heroes/generate |
| `hero_image_variants` | HeroImageGenerator | url (portraits + icône) | POST /api/heroes/images/generate |
| `dialogues` + `dialogue_exchanges` | DialogueGenerator | exchanges (speaker, text, emotion) | POST /api/dialogues/generate |
| `missions` | MissionGenerator | description, success_text, failure_text | POST /api/missions/generate |
| `mission_choices` | MissionChoiceGenerator | choice_text, consequence_text, modifiers | POST /api/missions/choices/generate |
| `buildings` | BuildingGenerator | atmosphere, npc_name, npc_description, secret | POST /api/buildings/generate |
| `locations` | LocationGenerator | description, image_url | POST /api/locations/generate |
| `hero_relationships` | RelationshipGenerator | type, description, strength | POST /api/relationships/generate |
| `ambient_texts` | AmbientTextGenerator | text (contextuel) | POST /api/ambient/generate |

---

## 🔌 API Endpoints Détaillés

### 1. Heroes

#### POST /api/heroes/generate/text
**Body** :
```json
{
  "hero_id": "bjorn",
  "field": "lore",
  "context": {
    "race": "Human",
    "class": "Fighter",
    "background": "Soldier",
    "personality_traits": ["Disciplined", "Protective"]
  },
  "constraints": {
    "min_words": 400,
    "max_words": 600,
    "tone": "dramatic"
  }
}
```

**Response** :
```json
{
  "hero_id": "bjorn",
  "field": "lore",
  "text": "Né dans les terres froides du nord...",
  "word_count": 523,
  "validation": {
    "length_ok": true,
    "json_valid": true
  }
}
```

#### POST /api/heroes/generate/dnd-stats
**Body** :
```json
{
  "hero_id": "bjorn",
  "class": "Fighter",
  "method": "standard_array"
}
```

**Response** :
```json
{
  "hero_id": "bjorn",
  "dnd_strength": 16,
  "dnd_dexterity": 12,
  "dnd_constitution": 15,
  "dnd_intelligence": 10,
  "dnd_wisdom": 13,
  "dnd_charisma": 8,
  "race": "Human",
  "class": "Fighter",
  "background": "Soldier",
  "personality_traits": ["Disciplined", "Protective", "Direct"],
  "ideals": "La force doit servir à protéger les faibles",
  "bonds": "Je dois protéger mon village natal",
  "flaws": "Je fais confiance trop lentement"
}
```

#### POST /api/heroes/images/generate
**Body** :
```json
{
  "hero_id": "bjorn",
  "base_description": "male human fighter, rugged features, brown hair",
  "style": "semi-realistic",
  "emotions": ["neutral", "happy", "sad", "angry", "surprised"]
}
```

**Response** :
```json
{
  "hero_id": "bjorn",
  "job_id": "img_batch_abc123",
  "status": "queued",
  "images_to_generate": 6,
  "estimated_time": "4min"
}
```

#### GET /api/heroes/images/status/{job_id}
**Response** :
```json
{
  "job_id": "img_batch_abc123",
  "status": "completed",
  "progress": "6/6",
  "images": [
    {
      "emotion": "neutral",
      "url": "/temp/bjorn-neutral.webp",
      "width": 1024,
      "height": 1024,
      "file_size": 387000,
      "seed": 482756
    },
    {
      "emotion": "happy",
      "url": "/temp/bjorn-happy.webp",
      "width": 1024,
      "height": 1024,
      "file_size": 412000,
      "seed": 482756
    }
    // ... 4 autres
  ]
}
```

---

### 2. Dialogues

#### POST /api/dialogues/generate
**Body** :
```json
{
  "hero_id": "bjorn",
  "objective": "Présenter le héros au joueur",
  "emotional_arc": ["neutral", "intrigued", "confident"],
  "num_exchanges": 10,
  "key_points": ["backstory", "motivation"]
}
```

**Response** :
```json
{
  "dialogue_id": "dialogue_bjorn_day1_temp",
  "exchanges": [
    {
      "order": 1,
      "speaker": "hero",
      "text": "Ainsi, vous êtes le nouveau maître de Phandallin...",
      "emotion": "neutral"
    },
    {
      "order": 2,
      "speaker": "player",
      "text": "C'est exact. On m'a parlé de vos exploits."
    }
    // ... 8 autres
  ],
  "word_count_total": 450,
  "validation": {
    "num_exchanges_ok": true,
    "emotional_arc_respected": true
  }
}
```

---

### 3. Missions

#### POST /api/missions/generate
**Body** :
```json
{
  "mission_type": "infiltration",
  "location_id": "cave_dark",
  "difficulty": 7,
  "stakes": "Récupérer un artefact volé",
  "required_stats": {
    "stealth": 12
  },
  "rewards": {
    "gold": 80,
    "reputation": 20
  }
}
```

**Response** :
```json
{
  "mission_id": "mission_temp_xyz",
  "title": "L'Artefact Volé",
  "description": "Des rumeurs circulent au village : la grotte sombre...",
  "success_text": "Vous avez réussi à infiltrer la grotte...",
  "failure_text": "L'alarme a été déclenchée...",
  "word_counts": {
    "description": 267,
    "success_text": 134,
    "failure_text": 128
  }
}
```

#### POST /api/missions/choices/generate
**Body** :
```json
{
  "mission_id": "mission_temp_xyz",
  "num_choices": 3,
  "context": "Après avoir récupéré l'artefact"
}
```

**Response** :
```json
{
  "mission_id": "mission_temp_xyz",
  "choices": [
    {
      "choice_order": 1,
      "choice_text": "Rendre l'artefact immédiatement au village",
      "consequence_text": "Les villageois vous acclament...",
      "gold_modifier": 0,
      "reputation_modifier": 30
    },
    {
      "choice_order": 2,
      "choice_text": "Étudier l'artefact avant de le rendre",
      "consequence_text": "Vous découvrez des runes anciennes...",
      "gold_modifier": 20,
      "reputation_modifier": 0,
      "flag_set": "artifact_studied"
    }
    // ... 1 autre
  ]
}
```

---

### 4. Buildings

#### POST /api/buildings/generate
**Body** :
```json
{
  "building_slug": "tavern",
  "building_name": "The Prancing Pony"
}
```

**Response** :
```json
{
  "building_id": "tavern",
  "atmosphere": "L'odeur de bière et de ragoût flotte dans l'air...",
  "npc_name": "Gundren Brassecuir",
  "npc_description": "Un tavernier jovial à la barbe rousse...",
  "secret": "Derrière le tonneau au fond se cache une trappe...",
  "word_counts": {
    "atmosphere": 178,
    "npc_description": 142,
    "secret": 87
  }
}
```

---

### 5. Locations

#### POST /api/locations/generate/text
**Body** :
```json
{
  "location_slug": "forest_mysterious",
  "location_name": "Forêt Mystérieuse",
  "tone": "mysterious"
}
```

**Response** :
```json
{
  "location_id": "forest_mysterious",
  "description": "La forêt s'étend à perte de vue...",
  "word_count": 274
}
```

#### POST /api/locations/generate/image
**Body** :
```json
{
  "location_id": "forest_mysterious",
  "style": "semi-realistic",
  "ambient": "day_sunny",
  "prompt_keywords": ["ancient trees", "misty", "dappled sunlight"]
}
```

**Response** :
```json
{
  "location_id": "forest_mysterious",
  "job_id": "loc_img_def456",
  "status": "processing",
  "estimated_time": "30s"
}
```

---

### 6. Batch Operations

#### POST /api/batch
**Body** :
```json
{
  "type": "heroes_complete",
  "hero_ids": ["bjorn", "owen", "vi", "durun", "elira"],
  "operations": ["texts", "dnd_stats", "images"],
  "style_config": {
    "visual_style": "semi-realistic",
    "narrative_tone": "dramatic"
  }
}
```

**Response** :
```json
{
  "batch_id": "batch_heroes_001",
  "status": "queued",
  "total_jobs": 15,
  "estimated_total_time": "25min",
  "breakdown": {
    "texts": "5 heroes × 7 fields = 35 texts (~10min)",
    "dnd_stats": "5 heroes (~1min)",
    "images": "5 heroes × 6 images = 30 images (~15min)"
  }
}
```

#### GET /api/batch/status/{batch_id}
**Response** :
```json
{
  "batch_id": "batch_heroes_001",
  "status": "processing",
  "progress": "12/15",
  "current_job": "Generating images for Owen (emotion: angry)",
  "elapsed_time": "14min",
  "estimated_remaining": "8min",
  "completed_jobs": [
    "bjorn_texts",
    "bjorn_dnd_stats",
    "bjorn_images",
    "owen_texts",
    "owen_dnd_stats"
  ]
}
```

---

## 🗄️ Schémas Pydantic (Backend)

### models/schemas.py

```python
from pydantic import BaseModel, Field
from typing import List, Optional

# Heroes
class HeroTextGenerateRequest(BaseModel):
    hero_id: str
    field: str  # "description", "lore", "voice", "secret", "arc_day1", etc.
    context: dict
    constraints: dict

class HeroTextGenerateResponse(BaseModel):
    hero_id: str
    field: str
    text: str
    word_count: int
    validation: dict

class HeroDnDStatsRequest(BaseModel):
    hero_id: str
    class_name: str
    method: str = "standard_array"

class HeroDnDStatsResponse(BaseModel):
    hero_id: str
    dnd_strength: int
    dnd_dexterity: int
    dnd_constitution: int
    dnd_intelligence: int
    dnd_wisdom: int
    dnd_charisma: int
    race: str
    class_name: str
    background: str
    personality_traits: List[str]
    ideals: str
    bonds: str
    flaws: str

class HeroImageGenerateRequest(BaseModel):
    hero_id: str
    base_description: str
    style: str
    emotions: List[str]

class HeroImageGenerateResponse(BaseModel):
    hero_id: str
    job_id: str
    status: str
    images_to_generate: int
    estimated_time: str

# Dialogues
class DialogueGenerateRequest(BaseModel):
    hero_id: str
    objective: str
    emotional_arc: List[str]
    num_exchanges: int
    key_points: List[str]

class DialogueExchange(BaseModel):
    order: int
    speaker: str
    text: str
    emotion: Optional[str] = None

class DialogueGenerateResponse(BaseModel):
    dialogue_id: str
    exchanges: List[DialogueExchange]
    word_count_total: int
    validation: dict

# Missions
class MissionGenerateRequest(BaseModel):
    mission_type: str
    location_id: str
    difficulty: int
    stakes: str
    required_stats: dict
    rewards: dict

class MissionGenerateResponse(BaseModel):
    mission_id: str
    title: str
    description: str
    success_text: str
    failure_text: str
    word_counts: dict

# Buildings
class BuildingGenerateRequest(BaseModel):
    building_slug: str
    building_name: str

class BuildingGenerateResponse(BaseModel):
    building_id: str
    atmosphere: str
    npc_name: str
    npc_description: str
    secret: str
    word_counts: dict

# Locations
class LocationTextGenerateRequest(BaseModel):
    location_slug: str
    location_name: str
    tone: str

class LocationTextGenerateResponse(BaseModel):
    location_id: str
    description: str
    word_count: int

class LocationImageGenerateRequest(BaseModel):
    location_id: str
    style: str
    ambient: str
    prompt_keywords: List[str]

# Batch
class BatchRequest(BaseModel):
    type: str
    hero_ids: Optional[List[str]] = None
    operations: List[str]
    style_config: dict

class BatchResponse(BaseModel):
    batch_id: str
    status: str
    total_jobs: int
    estimated_total_time: str
    breakdown: dict
```

---

## 📂 Structure Backend Python

```
curator-backend/
  app/
    main.py                      # FastAPI server entry point
    
    routers/
      heroes.py                  # Routes /api/heroes/*
      dialogues.py               # Routes /api/dialogues/*
      missions.py                # Routes /api/missions/*
      buildings.py               # Routes /api/buildings/*
      locations.py               # Routes /api/locations/*
      batch.py                   # Routes /api/batch/*
    
    services/
      llm_service.py             # Wrapper LLM (OpenLLaMA/Mistral)
      sd_service.py              # Wrapper Stable Diffusion
      queue_service.py           # Gestion file d'attente jobs
    
    generators/
      hero_generator.py          # Logique génération héros
      dialogue_generator.py      # Logique génération dialogues
      mission_generator.py       # Logique génération missions
      building_generator.py      # Logique génération bâtiments
      location_generator.py      # Logique génération locations
      relationship_generator.py  # Logique génération relations
      ambient_generator.py       # Logique génération ambient texts
    
    models/
      schemas.py                 # Pydantic schemas (requêtes/réponses)
      db_models.py               # SQLAlchemy models (SQLite local)
    
    utils/
      prompt_builder.py          # Construction prompts dynamiques
      postprocess.py             # Optimisation images (resize, WebP)
      validation.py              # Validation outputs (longueurs, JSON)
    
    config/
      settings.py                # Configuration (modèles, chemins, etc.)
    
    storage/
      temp/                      # Images temporaires avant export
      exports/                   # JSON + assets finaux
  
  requirements.txt
  .env
  README.md
```

---

## 📂 Structure Frontend Next.js

```
curator-frontend/
  app/
    page.tsx                              # Home (sélection type contenu)
    layout.tsx
    
    import/
      page.tsx                            # Upload spec .md
    
    heroes/
      config/page.tsx                     # Niveau 1 : Config héros
      generate/page.tsx                   # Niveau 2 : Génération
      refine/[id]/page.tsx                # Niveau 3 : Raffinement
      validate/page.tsx                   # Niveau 4 : Validation
    
    images/
      style/page.tsx                      # Niveau 1 : Style graphique
      variations/page.tsx                 # Niveau 2 : Variations générales
      emotions/page.tsx                   # Niveau 3 : Émotions
      validate/page.tsx                   # Niveau 4 : Validation
    
    dialogues/
      structure/page.tsx                  # Niveau 1 : Structure narrative
      exchanges/page.tsx                  # Niveau 2 : Répliques
      emotions/page.tsx                   # Niveau 3 : Attribution émotions
      validate/page.tsx                   # Niveau 4 : Validation
    
    missions/
      concept/page.tsx                    # Niveau 1 : Concept mission
      narrative/page.tsx                  # Niveau 2 : Descriptions
      outcomes/page.tsx                   # Niveau 3 : Résolutions
      validate/page.tsx                   # Niveau 4 : Validation
    
    buildings/
      atmosphere/page.tsx                 # Niveau 1 : Ambiance
      npcs/page.tsx                       # Niveau 2 : NPCs
      secrets/page.tsx                    # Niveau 3 : Secrets
      validate/page.tsx                   # Niveau 4 : Validation
    
    locations/
      style/page.tsx                      # Niveau 1 : Style visuel
      descriptions/page.tsx               # Niveau 2 : Textes
      images/page.tsx                     # Niveau 3 : Illustrations
      validate/page.tsx                   # Niveau 4 : Validation
    
    export/
      page.tsx                            # Export JSON + assets
    
  components/
    heroes/
      hero-text-editor.tsx
      hero-image-gallery.tsx
      hero-stats-form.tsx
    dialogues/
      dialogue-editor.tsx
      emotion-selector.tsx
      preview-simulator.tsx
    missions/
      mission-editor.tsx
      choice-editor.tsx
    buildings/
      building-editor.tsx
    locations/
      location-editor.tsx
    common/
      progress-tracker.tsx
      loading-spinner.tsx
      validation-checklist.tsx
  
  lib/
    api-client.ts                         # Axios wrapper pour Backend
    db-schemas.ts                         # Types Supabase (sync)
    state-manager.ts                      # Zustand store global
  
  public/
    temp-previews/                        # Previews images temporaires
  
  package.json
  next.config.js
```

---

## 🔄 Flux de Communication

### Exemple : Génération 1 Héros Complet

```
1. [Frontend] User clique "Générer Bjorn" (config: semi-realistic, dramatic)
   ↓
2. [Frontend] POST /api/batch
   Body: { type: "heroes_complete", hero_ids: ["bjorn"], operations: ["texts", "dnd_stats", "images"] }
   ↓
3. [Backend] Queue service crée jobs:
   - Job 1: Generate texts (7 champs)
   - Job 2: Generate DnD stats
   - Job 3: Generate images (6 images)
   ↓
4. [Backend] Job 1 démarre → LLM service génère 7 textes → Sauvegarde SQLite
   ↓
5. [Backend] Job 2 démarre → LLM service génère stats D&D → Sauvegarde SQLite
   ↓
6. [Backend] Job 3 démarre → SD service génère 6 images → Sauvegarde /temp/
   ↓
7. [Frontend] Polling GET /api/batch/status/{batch_id} toutes les 2s
   Response: { status: "processing", progress: "2/3", current_job: "Generating images..." }
   ↓
8. [Backend] Tous jobs complétés → Status = "completed"
   ↓
9. [Frontend] Affiche résultats (textes + images) dans interface Niveau 3 (Raffinement)
   ↓
10. [User] Valide ou édite manuellement
    ↓
11. [Frontend] User clique "Valider et Exporter"
    ↓
12. [Backend] Génère JSON final + organise assets dans /exports/
    ↓
13. [Frontend] Télécharge export ou push direct Supabase
```

---

## 📝 Prochaines Étapes Sprint 0.3

1. Créer document `architecture-curator.md` avec tous les détails ci-dessus
2. Définir schémas Pydantic complets dans `models/schemas.py`
3. Créer diagrammes :
   - Architecture globale (Frontend ↔ Backend)
   - Flux de données (Request → Response)
   - Structure fichiers (arborescence complète)
4. Valider endpoints API avec équipe
5. Préparer Sprint 1 (implémentation Backend)
