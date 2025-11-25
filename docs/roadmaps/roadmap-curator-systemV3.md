# 🗺️ Roadmap : Système Curator IA - Medieval Dispatch V3

**Date de création** : 24 novembre 2025  
**Objectif** : Construire l'application autonome "Curator" permettant de générer, affiner et valider le contenu narratif et visuel du jeu via IA avec un système multi-niveaux par type de contenu.

---

## 🎯 Vision Globale

Le **Curator** est une application standalone qui prend en charge **toute la création de contenu créatif** pour Medieval Dispatch. Il utilise un **système de curation multi-niveaux spécifique à chaque type de contenu** de la base de données.

### Philosophie : Curation Progressive par Type

Chaque élément de la DB (Héros, Missions, Dialogues, Bâtiments, Locations) passe par **3-4 niveaux de raffinement** :

- **Niveau 1** : Définition du style/ton global
- **Niveau 2** : Génération de variations majeures
- **Niveau 3** : Raffinement et variations mineures
- **Niveau 4** : Validation et export

---

## 📊 Tables de Base de Données Identifiées

D'après la structure Supabase actuelle :

| Table | Contenu à Générer | Champs Critiques |
|-------|-------------------|------------------|
| `heroes` | Personnages D&D complets | description, lore, voice, secret, arc_day1/2/3, race, class, background, personality_traits, ideals, bonds, flaws |
| `hero_image_variants` | Images portraits + icônes | base_type, resolution, emotion, url |
| `dialogues` + `dialogue_exchanges` | Conversations héros/joueur | speaker, text, emotion, order |
| `missions` | Quêtes narratives | title, description, success_text, failure_text |
| `buildings` | Bâtiments vivants | name, description, atmosphere, npc_name, npc_description, secret |
| `locations` | Lieux de la carte | name, description, image_url |
| `ambient_texts` | Textes d'ambiance | context, text, author |
| `hero_relationships` | Relations entre héros | type, description, strength |
| `mission_choices` | Choix narratifs | choice_text, consequence_text, flag_set |

---

## 📅 Sprint 0 : Recherche & Benchmarking (1-2 semaines)

**Objectif** : Valider les choix technologiques pour les modèles IA et définir l'architecture globale.

### 🧠 Sélection du Modèle de Langage (LLM)

#### Critères d'Évaluation
- **Performance locale** : GPU 8-16GB VRAM
- **Qualité narrative** : Textes longs cohérents (400-600 mots)
- **JSON structuré** : Respect schémas stricts
- **Vitesse** : < 30s par texte

#### Candidats à Tester
1. **OpenLLaMA** (3B, 7B, 13B)
   - Versions quantifiées (4-bit, 8-bit)
   - Prompt engineering pour stats D&D + narratif
2. **Mistral 7B** (alternative)
3. **Llama 2 7B/13B** (alternative)

#### Tests à Effectuer par Type de Contenu
- **Héros** : description (200 mots) + lore (500 mots) + voice (75 mots)
- **Dialogues** : 10 échanges cohérents avec émotions
- **Missions** : description + success/failure texts
- **Bâtiments** : atmosphere (150 mots) + NPC description
- **Relations** : génération dynamique selon personnalités

#### Livrable Sprint 0.1
- `model-selection-llm.md` avec benchmarks par type
- Choix modèle + configuration (température, top_p)
- Prompts "master" pour chaque table DB

---

### 🎨 Sélection du Modèle de Génération d'Images

#### Critères d'Évaluation
- **Style médiéval-fantastique** cohérent
- **Variations émotionnelles** : 5-8 émotions par personnage
- **Cohérence visuelle** : Même univers graphique
- **Vitesse** : < 30s par image
- **VRAM** : 8-16GB compatible

#### Candidats à Tester
1. **Stable Diffusion 1.5** + LoRAs (RPG, Fantasy)
2. **SDXL** (si VRAM suffisante)
3. **DreamShaper** (checkpoint communautaire)
4. **RPG v4** (checkpoint fantasy)

#### Tests à Effectuer par Type Visuel
- **Portraits héros** : 1 personnage en 5 émotions (neutral, happy, sad, angry, surprised)
- **Icônes héros** : Downscaling 1024x1024 → 256x256
- **Locations** : Paysages (forêt, caverne, ruines)
- **Bâtiments** : Illustrations intérieures (taverne, forge, temple)
- **Batch processing** : 5 héros × 6 images en < 30min

#### Livrable Sprint 0.2
- `model-selection-stable-diffusion.md` avec exemples
- Choix checkpoint + LoRAs + paramètres
- Prompts "master" par type visuel

---

### 🏗️ Architecture Technique du Système

#### Stack Validée

**Frontend** : Next.js 14 (App Router)
- Interface de curation multi-niveaux **par type de contenu**
- Preview temps réel selon type (dialogue, carte, portrait)
- Gestion états par table DB

**Backend** : Python (FastAPI)
- Service LLM (génération textes)
- Service Stable Diffusion (génération images)
- API REST exposée au frontend
- File d'attente pour jobs longs

**Stockage**
- SQLite locale : État générations en cours
- Export final : JSON + assets (prêt pour Supabase)
- Historique versions

#### Contrats d'Interface (API Endpoints)

```
POST /api/generate/hero/text
  Body: { hero_id, field: "lore", context, constraints }
  Response: { text, word_count, validation }

POST /api/generate/hero/image
  Body: { hero_id, emotion: "neutral", style_config }
  Response: { image_url, width, height }

POST /api/generate/dialogue
  Body: { hero_id, num_exchanges: 10, emotional_arc }
  Response: { exchanges: [{speaker, text, emotion}] }

POST /api/generate/mission
  Body: { mission_id, location_id, difficulty }
  Response: { description, success_text, failure_text }

POST /api/batch
  Body: { type: "heroes", ids: [...], operations: [...] }
  Response: { job_id, status }
```

#### Livrable Sprint 0.3
- `architecture-curator.md` détaillé
- Schéma communication Frontend ↔ Backend
- Définition endpoints complets
- Mapping tables DB → API

---

## 📅 Sprint 1 : Backend Python - Moteurs IA (2-3 semaines)

### 🐍 Setup Environnement Python

#### Actions
- Environnement isolé (`venv`)
- Dépendances : `torch`, `transformers`, `diffusers`, `fastapi`, `pillow`
- Configuration GPU (CUDA)
- Tests performance VRAM

#### Livrable Sprint 1.1
- Script `setup.py` installation auto
- `INSTALL.md` pour développeurs
- Tests charge GPU

---

### ⚙️ Service API Backend (FastAPI)

#### Fonctionnalités
- **Endpoints REST** par type de contenu
- **File d'attente** : Jobs longs sans blocage
- **Status monitoring** : Progression temps réel
- **Gestion erreurs** : Retry automatique

#### Structure
```
curator-backend/
  app/
    main.py
    services/
      llm_service.py
      sd_service.py
      queue_service.py
    generators/
      hero_generator.py
      dialogue_generator.py
      mission_generator.py
      building_generator.py
      location_generator.py
    models/
      schemas.py          # Pydantic models par table
    utils/
      prompt_builder.py
      postprocess.py
  requirements.txt
  .env
```

#### Livrable Sprint 1.2
- Serveur FastAPI fonctionnel (port 8000)
- Tests Postman pour chaque endpoint
- Documentation API (Swagger)

---

### 🧠 Service LLM - Générateurs par Type

#### Générateurs à Implémenter

##### 1. **Hero Generator** (table `heroes`)
**Prompts** :
- `generate_description` (150-250 mots)
- `generate_lore` (400-600 mots)
- `generate_voice` (50-100 mots)
- `generate_secret` (100-150 mots)
- `generate_arc_day` (100-150 mots) × 3
- `generate_dnd_stats` (race, class, background, traits, ideals, bonds, flaws)

##### 2. **Dialogue Generator** (tables `dialogues` + `dialogue_exchanges`)
**Prompts** :
- `generate_dialogue_structure` (objectif, arc émotionnel)
- `generate_exchanges` (10 répliques hero/player avec émotions)
- `assign_emotions` (neutral, happy, sad, angry, surprised)

##### 3. **Mission Generator** (table `missions`)
**Prompts** :
- `generate_mission_description` (200-300 mots)
- `generate_success_text` (100-150 mots)
- `generate_failure_text` (100-150 mots)
- `generate_mission_choices` (table `mission_choices`)

##### 4. **Building Generator** (table `buildings`)
**Prompts** :
- `generate_atmosphere` (150-200 mots)
- `generate_npc` (nom + description 100-150 mots)
- `generate_secret` (50-100 mots)

##### 5. **Location Generator** (table `locations`)
**Prompts** :
- `generate_description` (200-300 mots)

##### 6. **Relationship Generator** (table `hero_relationships`)
**Prompts** :
- `generate_relationship` (type + description selon héros impliqués)

##### 7. **Ambient Text Generator** (table `ambient_texts`)
**Prompts** :
- `generate_ambient` (texte court contextuel)

#### Livrable Sprint 1.3
- 7 générateurs opérationnels
- Tests unitaires par type
- `prompt-engineering.md` complet

---

### 🎨 Service Stable Diffusion - Générateurs Visuels

#### Générateurs à Implémenter

##### 1. **Hero Portrait Generator** (table `hero_image_variants`)
**Pipeline** :
- Génération base 1024x1024 (neutral)
- Img2Img pour 4 autres émotions (happy, sad, angry, surprised)
- Resize 256x256 pour icône
- Conversion WebP + compression

##### 2. **Location Illustration Generator** (table `locations`)
**Pipeline** :
- Génération paysage 1024x1024
- Variation jour/nuit (optionnel)
- WebP compression

##### 3. **Building Interior Generator** (table `buildings` - optionnel)
**Pipeline** :
- Illustration intérieure 1024x1024
- Style atmosphère selon type bâtiment

#### Livrable Sprint 1.4
- Service SD opérationnel
- Tests génération 1 héros (6 images)
- Temps génération < 5min/héros
- Tests locations (4 paysages)

---

### 🔧 Post-Processing & Optimisation

#### Fonctionnalités
- **Redimensionnement** : PIL pour resize
- **Conversion WebP** : Qualité 85
- **Validation** : Dimensions, poids, format
- **Organisation** : Tri automatique assets

#### Livrable Sprint 1.5
- Scripts post-processing auto
- Tests batch 30 images
- Comparaison PNG vs WebP

---

## 📅 Sprint 2 : Frontend Next.js - Système Multi-Niveaux (4-5 semaines)

**Objectif** : Créer l'interface avec workflow multi-niveaux **spécifique à chaque type de contenu** DB.

### 🖥️ Setup Projet Next.js

#### Structure
```
curator-frontend/
  app/
    page.tsx                      # Home (sélection type contenu)
    import/page.tsx               # Upload spec
    
    heroes/
      config/page.tsx             # Niveau 1 : Style global héros
      generate/page.tsx           # Niveau 2 : Variations majeures
      refine/[id]/page.tsx        # Niveau 3 : Raffinement
      validate/page.tsx           # Niveau 4 : Validation
    
    images/
      style/page.tsx              # Niveau 1 : Style graphique
      variations/page.tsx         # Niveau 2 : Variations générales
      emotions/page.tsx           # Niveau 3 : Variations légères
      validate/page.tsx           # Niveau 4 : Validation
    
    dialogues/
      structure/page.tsx          # Niveau 1 : Arcs narratifs
      exchanges/page.tsx          # Niveau 2 : Répliques
      emotions/page.tsx           # Niveau 3 : Attribution émotions
      validate/page.tsx           # Niveau 4 : Validation
    
    missions/
      concept/page.tsx            # Niveau 1 : Type mission
      narrative/page.tsx          # Niveau 2 : Descriptions
      outcomes/page.tsx           # Niveau 3 : Textes résolution
      validate/page.tsx           # Niveau 4 : Validation
    
    buildings/
      atmosphere/page.tsx         # Niveau 1 : Ambiance globale
      npcs/page.tsx               # Niveau 2 : Personnages
      secrets/page.tsx            # Niveau 3 : Easter eggs
      validate/page.tsx           # Niveau 4 : Validation
    
    locations/
      style/page.tsx              # Niveau 1 : Style visuel
      descriptions/page.tsx       # Niveau 2 : Textes
      images/page.tsx             # Niveau 3 : Illustrations
      validate/page.tsx           # Niveau 4 : Validation
    
    export/page.tsx               # Export final
    
  components/
    heroes/
      hero-text-editor.tsx
      hero-image-gallery.tsx
    dialogues/
      dialogue-editor.tsx
      emotion-selector.tsx
    missions/
      mission-editor.tsx
    common/
      progress-tracker.tsx
      preview-simulator.tsx
  
  lib/
    api-client.ts
    db-schemas.ts               # Types Supabase
```

#### Livrable Sprint 2.1
- Projet Next.js avec routing complet
- Navigation entre types de contenu
- Connexion API backend

---

### 🎨 Workflow Multi-Niveaux : IMAGES (hero_image_variants)

#### **Niveau 1 : Style Graphique Global**

**Objectif** : Définir la direction artistique de TOUTES les images du jeu.

**Interface** :
- Radio buttons : 
  - ⚫ **Cartoon** (stylisé, couleurs vives)
  - ⚫ **Semi-réaliste** (équilibre réalisme/artistique)
  - ⚫ **Animé** (style anime/manga)
  - ⚫ **Comics** (cell-shading, contours marqués)
- Preview exemples visuels par style
- Palette couleurs dominantes (chaud/froid/neutre)
- Slider intensité lumière/ombre

**Output Niveau 1** :
```json
{
  "visual_style": "semi-realistic",
  "color_palette": "warm",
  "lighting": "dramatic",
  "master_prompt_prefix": "semi-realistic medieval fantasy portrait, warm tones, dramatic lighting"
}
```

---

#### **Niveau 2 : Variations Générales (Morphologie & Apparence)**

**Objectif** : Générer différentes **versions majeures** d'un même personnage (visage, morphologie, âge).

**Interface** :
- Grille 3×3 affichant 9 variations du héros (même émotion : neutral)
- Variations automatiques :
  - Visage 1 : Angulaire, mâchoire carrée
  - Visage 2 : Rond, traits doux
  - Visage 3 : Allongé, traits fins
  - Morphologie : Musclé, svelte, corpulent
  - Âge : Jeune (20s), Mature (30s), Vétéran (40s+)
- Bouton "Générer plus de variations" (9 nouvelles)
- Sélection d'1 variante favorite → devient base pour Niveau 3

**Output Niveau 2** :
```json
{
  "selected_variant": "variation_3",
  "base_seed": 482756,
  "characteristics": {
    "face_shape": "angular",
    "build": "athletic",
    "age_range": "mature"
  }
}
```

---

#### **Niveau 3 : Variations Légères (Émotions)**

**Objectif** : Générer les **5-8 émotions** à partir de la variante sélectionnée (Niveau 2).

**Interface** :
- Affichage portrait de base (neutral) en grand
- Liste émotions à générer :
  - 😐 Neutral (déjà fait au Niveau 2)
  - 😊 Happy
  - 😢 Sad
  - 😠 Angry
  - 😲 Surprised
  - 😟 Worried (optionnel)
  - 😄 Excited (optionnel)
  - 🤔 Thoughtful (optionnel)
- Bouton "Générer toutes les émotions" (batch)
- Possibilité régénérer 1 émotion spécifique si insatisfaisante
- Preview hover pour comparer côte à côte

**Technique** :
- Utilise **Img2Img** avec même seed + prompt émotion
- Denoising strength : 0.3-0.5 (variations légères)

**Output Niveau 3** :
```json
{
  "hero_id": "bjorn",
  "base_variant_seed": 482756,
  "emotions_generated": [
    { "emotion": "neutral", "url": "...", "seed": 482756 },
    { "emotion": "happy", "url": "...", "seed": 482756 },
    { "emotion": "sad", "url": "...", "seed": 482756 },
    { "emotion": "angry", "url": "...", "seed": 482756 },
    { "emotion": "surprised", "url": "...", "seed": 482756 }
  ]
}
```

---

#### **Niveau 4 : Validation & Génération Icônes**

**Objectif** : Valider toutes les émotions + générer icône 256×256.

**Interface** :
- Tableau récapitulatif :
  | Émotion | Preview | Poids | Actions |
  |---------|---------|-------|---------|
  | Neutral | 🖼️ | 385 KB | ✅ Valide |
  | Happy | 🖼️ | 412 KB | ⚠️ Re-générer |
- Génération automatique icône (resize + crop intelligent)
- Validation poids (< 500KB portraits, < 100KB icône)
- Bouton "Exporter vers Supabase"

**Output Niveau 4** :
- 6 images insérées dans table `hero_image_variants`
- URLs Supabase Storage publiques

---

### 💬 Workflow Multi-Niveaux : DIALOGUES

#### **Niveau 1 : Structure Narrative**

**Objectif** : Définir l'arc narratif du dialogue.

**Interface** :
- Sélection héros (dropdown)
- Objectif dialogue (textarea) : "Présenter le héros au joueur"
- Arc émotionnel (sliders) :
  - Début : Neutre/Méfiant/Joyeux
  - Milieu : Intrigué/Préoccupé/Enthousiaste
  - Fin : Confiant/Inquiet/Déterminé
- Nombre échanges (slider 5-15)
- Points clés à transmettre (liste tags) : "backstory", "motivation", "secret_hint"

**Output Niveau 1** :
```json
{
  "hero_id": "bjorn",
  "objective": "Présenter le héros",
  "emotional_arc": ["neutral", "intrigued", "confident"],
  "num_exchanges": 10,
  "key_points": ["backstory", "motivation"]
}
```

---

#### **Niveau 2 : Génération Répliques**

**Objectif** : Créer les échanges hero/player avec voix unique.

**Interface** :
- Bouton "Générer dialogue complet"
- Affichage temps réel des répliques générées
- Liste échanges :
  ```
  [1] HERO (neutral): "Ainsi, vous êtes le nouveau maître de Phandallin..."
  [2] PLAYER: "C'est exact. On m'a parlé de vos exploits."
  [3] HERO (intrigued): "Des exploits ? *rire amer* J'ai surtout..."
  ```
- Bouton "Re-générer réplique X" si insatisfaisante
- Compteur mots par réplique (éviter trop long/court)

**Output Niveau 2** :
```json
{
  "dialogue_id": "dialogue_bjorn_day1",
  "exchanges": [
    { "order": 1, "speaker": "hero", "text": "...", "emotion": "neutral" },
    { "order": 2, "speaker": "player", "text": "..." },
    { "order": 3, "speaker": "hero", "text": "...", "emotion": "intrigued" }
  ]
}
```

---

#### **Niveau 3 : Attribution Émotions & Ajustements**

**Objectif** : Affiner les émotions et peaufiner textes.

**Interface** :
- Vue échange par échange
- Dropdown émotion pour chaque réplique hero :
  - neutral, happy, sad, angry, surprised, worried, excited, thoughtful
- Éditeur texte pour modifications manuelles
- Preview portrait émotionnel à côté de chaque réplique
- Validation cohérence émotionnelle (arc respecté ?)

**Output Niveau 3** :
```json
{
  "dialogue_id": "dialogue_bjorn_day1",
  "exchanges_refined": [
    { "order": 1, "speaker": "hero", "text": "...", "emotion": "neutral", "image_type": "portrait_high" },
    { "order": 2, "speaker": "player", "text": "..." },
    { "order": 3, "speaker": "hero", "text": "...", "emotion": "thoughtful", "image_type": "portrait_high" }
  ]
}
```

---

#### **Niveau 4 : Validation Dialogue Complet**

**Objectif** : Simuler dialogue en jeu et valider.

**Interface** :
- **Simulateur DialogueModal** : Preview exacte du rendu en jeu
- Navigation flèches pour parcourir échanges
- Portraits émotionnels affichés dynamiquement
- Checklist :
  - [ ] Arc émotionnel cohérent
  - [ ] Voix du héros respectée
  - [ ] Longueurs répliques OK
  - [ ] Émotions correspondent aux portraits
- Bouton "Exporter vers Supabase"

**Output Niveau 4** :
- Insertion dans tables `dialogues` + `dialogue_exchanges`

---

### 🗺️ Workflow Multi-Niveaux : MISSIONS

#### **Niveau 1 : Concept & Type Mission**

**Objectif** : Définir le type et les enjeux.

**Interface** :
- Sélection type mission :
  - ⚔️ Combat (required_strength élevé)
  - 🎭 Diplomatie (required_diplomacy élevé)
  - 🕵️ Infiltration (required_stealth élevé)
  - 🧠 Enquête (required_intelligence élevé)
  - 🎲 Mixte
- Sélection location (dropdown : Forest, Cave, Ruins, Village)
- Difficulté (slider 1-10)
- Stakes narratifs (textarea) : "Sauver un villageois kidnappé"
- Récompenses (gold, reputation)

**Output Niveau 1** :
```json
{
  "mission_type": "infiltration",
  "location_id": "cave_dark",
  "difficulty": 7,
  "stakes": "Récupérer un artefact volé",
  "required_stealth": 12,
  "reward_gold": 80,
  "reward_reputation": 20
}
```

---

#### **Niveau 2 : Rédaction Description**

**Objectif** : Générer description immersive mission.

**Interface** :
- Bouton "Générer description"
- Textarea éditable (200-300 mots)
- Contraintes :
  - Mentionner location
  - Expliquer objectif
  - Créer urgence/tension
- Preview carte avec emplacement mission

**Output Niveau 2** :
```json
{
  "description": "Des rumeurs circulent au village : la grotte sombre au nord abriterait des bandits..."
}
```

---

#### **Niveau 3 : Textes de Résolution (Success/Failure)**

**Objectif** : Rédiger textes après mission.

**Interface** :
- **Success Text** :
  - Bouton "Générer texte succès"
  - Textarea (100-150 mots)
  - Ton : Victorieux, satisfaisant
- **Failure Text** :
  - Bouton "Générer texte échec"
  - Textarea (100-150 mots)
  - Ton : Conséquences, regrets
- Preview rewards (affichage +gold +reputation)

**Output Niveau 3** :
```json
{
  "success_text": "Vous avez réussi à infiltrer la grotte sans vous faire repérer...",
  "failure_text": "L'alarme a été déclenchée. Les bandits se sont enfuis avec l'artefact..."
}
```

---

#### **Niveau 4 : Validation & Choix Narratifs (Optionnel)**

**Objectif** : Ajouter choix narratifs (table `mission_choices`).

**Interface** :
- Checkbox "Ajouter choix narratifs"
- Si activé :
  - Génération 2-3 choix après mission
  - Chaque choix : texte + conséquence + modifiers (gold, reputation, flag)
- Simulateur résolution mission
- Validation complète

**Output Niveau 4** :
- Insertion dans tables `missions` + `mission_choices`

---

### 🏛️ Workflow Multi-Niveaux : BUILDINGS

#### **Niveau 1 : Ambiance Globale**

**Objectif** : Définir l'atmosphère du bâtiment.

**Interface** :
- Sélection bâtiment (Tavern, Blacksmith, Temple, Market, Barracks)
- Génération automatique `atmosphere` (150-200 mots)
  - Sons (crépitement feu, enclume, prières)
  - Odeurs (bière, métal chaud, encens)
  - Lumière (tamisée, forge éclatante, bougies)
- Textarea éditable

**Output Niveau 1** :
```json
{
  "building_id": "tavern",
  "atmosphere": "L'odeur de bière et de ragoût flotte dans l'air. Le crépitement du feu..."
}
```

---

#### **Niveau 2 : NPCs (Personnages)**

**Objectif** : Créer les NPCs présents.

**Interface** :
- Génération NPC automatique :
  - `npc_name` : Nom généré
  - `npc_description` : Apparence + personnalité (100-150 mots)
- Bouton "Générer NPC alternatif" si insatisfaisant
- Preview NPC dans contexte bâtiment

**Output Niveau 2** :
```json
{
  "npc_name": "Gundren Brassecuir",
  "npc_description": "Un tavernier jovial à la barbe rousse..."
}
```

---

#### **Niveau 3 : Secrets & Easter Eggs**

**Objectif** : Ajouter profondeur narrative.

**Interface** :
- Génération `secret` (50-100 mots)
  - Secret du lieu (passage caché, trésor, histoire sombre)
- Textarea éditable
- Preview intégration en jeu (unlock condition, dialogue révélation)

**Output Niveau 3** :
```json
{
  "secret": "Derrière le tonneau au fond de la taverne se cache une trappe..."
}
```

---

#### **Niveau 4 : Validation Bâtiment Complet**

**Objectif** : Vérifier cohérence.

**Interface** :
- Preview ambiance + NPC + secret
- Checklist :
  - [ ] Atmosphere immersive
  - [ ] NPC cohérent avec bâtiment
  - [ ] Secret intéressant
- Bouton "Exporter vers Supabase"

**Output Niveau 4** :
- UPDATE table `buildings` avec champs enrichis

---

### 🗺️ Workflow Multi-Niveaux : LOCATIONS

#### **Niveau 1 : Style Visuel Paysage**

**Objectif** : Définir style illustrations locations.

**Interface** :
- Même choix que images héros (cartoon, semi-realistic, animé, comics)
- Variations ambiance :
  - ☀️ Jour ensoleillé
  - 🌙 Nuit étoilée
  - ⛈️ Orageux
  - 🌫️ Brumeux
- Slider détails (minimaliste vs ultra-détaillé)

**Output Niveau 1** :
```json
{
  "location_style": "semi-realistic",
  "ambient": "day_sunny",
  "detail_level": 8
}
```

---

#### **Niveau 2 : Descriptions Narratives**

**Objectif** : Générer textes descriptions.

**Interface** :
- Sélection location (Forest, Cave, Ruins, Village)
- Génération description (200-300 mots)
- Textarea éditable

**Output Niveau 2** :
```json
{
  "location_id": "forest_mysterious",
  "description": "La forêt s'étend à perte de vue, ses arbres centenaires..."
}
```

---

#### **Niveau 3 : Illustrations Paysages**

**Objectif** : Générer images 1024x1024.

**Interface** :
- Bouton "Générer illustration"
- Preview image générée
- Bouton "Re-générer" si insatisfaisant
- Validation poids (< 500KB)

**Output Niveau 3** :
```json
{
  "image_url": "https://...supabase.co/.../forest-mysterious.webp"
}
```

---

#### **Niveau 4 : Validation Location**

**Objectif** : Preview sur carte + validation.

**Interface** :
- Simulateur carte avec location placée
- Preview hover affiche image + description
- Validation complète

**Output Niveau 4** :
- UPDATE table `locations` avec description + image_url

---

## 📅 Sprint 3 : Intégration & Features Avancées (2 semaines)

### 🔄 Pipeline Complet End-to-End

#### Tests à Effectuer
- **Héros complet** : Workflow 4 niveaux images + textes
- **Dialogue complet** : 10 échanges avec émotions
- **Mission complète** : Description + success/failure
- **Bâtiment complet** : Atmosphere + NPC + secret
- **Location complète** : Description + illustration

#### Livrable Sprint 3.1
- Pipeline testé pour chaque type
- Batch 5 héros en < 30 minutes
- `performance-benchmarks.md`

---

### 🚀 Mode Batch Avancé

#### Fonctionnalités
- **Batch Heroes** : Générer 5 héros (textes + images) en parallèle
- **Batch Dialogues** : 5 dialogues jour 1
- **Batch Missions** : 10-15 missions
- **Priorités** : Textes d'abord, puis images (si VRAM limitée)

#### Livrable Sprint 3.2
- Mode batch avec file d'attente
- Tests génération 10 héros

---

### 🎭 Preview Temps Réel par Type

#### Composants Simulateurs
- **DialogueModal Simulator** : Preview dialogue avec portraits
- **MissionCard Simulator** : Card mission sur carte
- **VillageBuilding Simulator** : Hover bâtiment avec NPC
- **HeroCard Simulator** : Card sélection héros

#### Livrable Sprint 3.3
- 4 simulateurs fonctionnels
- Intégration dans pages validation

---

### 🔗 Connecteur Supabase (Direct Push)

#### Fonctionnalités
- **Push heroes** : INSERT textes + stats D&D
- **Push hero_image_variants** : INSERT 6 images par héros
- **Push dialogues + exchanges** : INSERT structure complète
- **Push missions** : INSERT avec success/failure texts
- **Upload Storage** : Images dans buckets (`hero-portraits`, `locations`)

#### Livrable Sprint 3.4
- Module connexion Supabase
- Tests insertion 1 de chaque type
- Documentation intégration

---

## 📅 Sprint 4 : Polish & Documentation (1 semaine)

### 📚 Documentation Complète

#### Documents à Créer
1. **User Guide** : `curator-user-guide.md`
   - Workflow par type de contenu (screenshots)
   - Explication système multi-niveaux
2. **Technical Guide** : `curator-technical-guide.md`
   - Architecture par générateur
   - Prompts par table DB
3. **Model Configuration** : `model-config.md`
   - Settings LLM/SD par type

#### Livrable Sprint 4.1
- Documentation exhaustive (3 guides)
- README avec quick start

---

### 🎓 Formation & Tests

#### Actions
- Session formation 3h (demo tous workflows)
- Génération 1er batch production :
  - 5 héros complets
  - 5 dialogues
  - 10 missions
  - 5 bâtiments
  - 4 locations
- Feedback utilisateurs

#### Livrable Sprint 4.2
- Batch production généré
- Feedback intégré backlog v2

---

## 📊 Métriques de Succès

| Métrique | Objectif |
|----------|----------|
| **Temps génération 1 héros complet (textes + 6 images)** | < 5 minutes |
| **Temps génération batch 5 héros** | < 30 minutes |
| **Temps génération 1 dialogue (10 échanges)** | < 2 minutes |
| **Temps génération 1 mission complète** | < 1 minute |
| **Qualité narrative** | 80% textes sans édition manuelle |
| **Qualité visuelle** | 90% images sans régénération |
| **Cohérence visuelle globale** | Style unifié reconnaissable |
| **Poids moyen portrait** | < 400KB (max 500KB) |
| **Uptime API Backend** | 99% |

---

## 🔮 Roadmap Contenu (Post-Système)

### Sprint Contenu 1 : Héros D&D (5 héros × 4 niveaux)
- Niveau 1-4 Images : Style + variations + émotions + validation
- Génération textes (description, lore, voice, secret, arcs)
- Import Supabase

### Sprint Contenu 2 : Dialogues Jour 1 (5 dialogues × 4 niveaux)
- Structure narrative + répliques + émotions + validation
- Intégration portraits émotionnels

### Sprint Contenu 3 : Missions (15 missions × 4 niveaux)
- Concepts + descriptions + résolutions + validation
- Génération choix narratifs

### Sprint Contenu 4 : Bâtiments (5 bâtiments × 4 niveaux)
- Atmosphères + NPCs + secrets + validation

### Sprint Contenu 5 : Locations (4 locations × 4 niveaux)
- Style + descriptions + illustrations + validation

---

**Document créé par** : Équipe Dev Medieval Dispatch  
**Version** : 3.0  
**Basé sur** : Structure DB Supabase `hfusvyadhtmviezelabi`  
**Prochaine révision** : Après Sprint 0 (validation modèles)
