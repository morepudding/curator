# 🗺️ Roadmap : Système Curator IA - Medieval Dispatch

**Date de création** : 24 novembre 2025  
**Objectif** : Construire l'application autonome "Curator" permettant de générer, affiner et valider le contenu narratif et visuel du jeu via IA.

---

## 🎯 Vision Globale

Le **Curator** est une application standalone qui prend en charge **toute la création de contenu créatif** pour Medieval Dispatch. Il reçoit des spécifications techniques du développeur (fichiers `.md`) et génère du contenu narratif enrichi + assets visuels prêts à l'emploi.

### Philosophie : Séparation Dev ↔ Curator

- **Dev** = Infrastructure technique, mécaniques, structures DB
- **Curator** = Contenu narratif, personnages, dialogues, images
- **Interface** = Workflow multi-niveaux de curation (configuration → génération → édition → validation → export)

---

## 📅 Sprint 0 : Recherche & Benchmarking (1-2 semaines)

**Objectif** : Valider les choix technologiques pour les modèles IA et définir l'architecture globale.

### 🧠 Sélection du Modèle de Langage (LLM)

#### Critères d'Évaluation
- **Performance locale** : Capacité à tourner sur matériel standard (GPU 8-16GB VRAM)
- **Qualité narrative** : Génération cohérente de textes longs (400-600 mots)
- **JSON structuré** : Capacité à respecter des schémas stricts
- **Vitesse** : Temps de génération acceptable (< 30s par texte)

#### Candidats à Tester
1. **OpenLLaMA** (3B, 7B, 13B)
   - Tester versions quantifiées (4-bit, 8-bit)
   - Prompt engineering pour générer stats D&D + texte narratif
   - Validation génération JSON structuré
2. **Mistral 7B** (alternative)
3. **Llama 2 7B/13B** (alternative)

#### Tests à Effectuer
- **Prompt 1** : Générer description + lore d'un héros D&D (500 mots)
- **Prompt 2** : Créer dialogue entre héros et joueur (10 échanges)
- **Prompt 3** : Générer mission narrative avec success/failure texts
- **Validation** : Cohérence, créativité, respect consignes, format JSON

#### Livrable Sprint 0.1
- Document `model-selection-llm.md` avec benchmarks
- Choix final du modèle + configuration (température, top_p, max_tokens)
- Prompts "master" validés pour chaque type de contenu

---

### 🎨 Sélection du Modèle de Génération d'Images

#### Critères d'Évaluation
- **Style médiéval-fantastique** : Cohérence avec univers D&D
- **Cohérence visuelle** : Tous les héros appartiennent au même univers
- **Variations émotionnelles** : Capacité à générer 5 émotions d'un même personnage
- **Vitesse** : Temps de génération (< 30s par image)
- **VRAM** : Compatible GPU standard (8-16GB)

#### Candidats à Tester
1. **Stable Diffusion 1.5** + LoRAs spécialisés (RPG, Fantasy)
2. **SDXL** (si VRAM suffisante)
3. **DreamShaper** (checkpoint communautaire)
4. **RPG v4** (checkpoint fantasy)

#### Tests à Effectuer
- **Portrait Héros** : Générer 1 personnage en 5 émotions (neutral, happy, sad, angry, surprised)
- **Cohérence** : Générer 3 héros différents avec même style artistique
- **Icônes** : Tester downscaling 1024x1024 → 256x256 avec qualité préservée
- **Optimisation** : Tester WebP, mesure poids fichiers, batch processing

#### Livrable Sprint 0.2
- Document `model-selection-stable-diffusion.md` avec exemples visuels
- Choix final checkpoint + LoRAs + paramètres (steps, CFG scale, sampler)
- Prompts "master" pour portraits héros, icônes, illustrations locations

---

### 🏗️ Architecture Technique du Système

#### Stack Validée

**Frontend** : Next.js 14 (App Router)
- Interface de curation multi-niveaux
- Preview temps réel
- Gestion états (génération en cours, validé, édité)

**Backend** : Python (FastAPI)
- Service LLM (génération textes)
- Service Stable Diffusion (génération images)
- API REST exposée au frontend
- File d'attente pour jobs longs

**Stockage**
- Base de données locale (SQLite) : État des générations en cours
- Export final : JSON + assets organisés (prêts pour Supabase)
- Historique versions : Rollback possible

#### Contrats d'Interface (API Endpoints)

```
POST /api/generate/text
  Body: { type: "hero_lore", context: {...}, constraints: {...} }
  Response: { text: "...", word_count: 500 }

POST /api/generate/image
  Body: { type: "portrait", subject: "Bjorn", emotion: "neutral", style: {...} }
  Response: { image_url: "temp://...", width: 1024, height: 1024 }

POST /api/batch/heroes
  Body: { hero_ids: ["bjorn", "owen"], spec: {...} }
  Response: { job_id: "abc123", status: "queued" }

GET /api/batch/status/{job_id}
  Response: { status: "processing", progress: "3/10", eta: "5min" }
```

#### Livrable Sprint 0.3
- Document `architecture-curator.md` détaillé
- Schéma de communication Frontend ↔ Backend
- Définition endpoints API complets
- Choix base de données locale (SQLite vs PostgreSQL)

---

## 📅 Sprint 1 : Backend Python - Moteurs IA (2-3 semaines)

**Objectif** : Créer le "cerveau" du Curator avec les services de génération IA fonctionnels.

### 🐍 Setup Environnement Python

#### Actions
- Créer environnement Python isolé (`venv` ou `conda`)
- Installer dépendances : `torch`, `transformers`, `diffusers`, `fastapi`, `pillow`, etc.
- Configuration GPU (CUDA) et tests de performance
- Setup gestion mémoire (déchargement modèles après génération)

#### Livrable Sprint 1.1
- Script `setup.py` avec installation automatique
- Documentation `INSTALL.md` pour setup développeur
- Tests de charge GPU (mesure VRAM utilisée)

---

### ⚙️ Service API Backend (FastAPI)

#### Fonctionnalités
- **Endpoints REST** : Exposition services LLM et Stable Diffusion
- **File d'attente** : Gestion jobs longs sans bloquer interface
- **Status monitoring** : Progression temps réel des générations
- **Gestion erreurs** : Retry automatique si échec génération

#### Structure
```
curator-backend/
  app/
    main.py              # FastAPI server
    services/
      llm_service.py     # Wrapper LLM
      sd_service.py      # Wrapper Stable Diffusion
      queue_service.py   # Gestion file d'attente
    models/
      schemas.py         # Pydantic schemas (validation)
    utils/
      prompt_builder.py  # Construction prompts
      postprocess.py     # Optimisation images
  requirements.txt
  .env                   # Config modèles
```

#### Livrable Sprint 1.2
- Serveur FastAPI fonctionnel (port 8000)
- Tests Postman/curl pour chaque endpoint
- Documentation API (Swagger auto-généré)

---

### 🧠 Service LLM - Génération Textes

#### Fonctionnalités
- **Wrapper modèle** : Chargement OpenLLaMA + quantization
- **Prompt engineering** : Templates pour chaque type de contenu
- **Validation output** : Vérification longueur, format JSON
- **Gestion contexte** : Injection placeholders existants pour cohérence

#### Prompts à Implémenter
1. **Hero Description** (150-250 mots)
2. **Hero Lore** (400-600 mots)
3. **Hero Voice** (50-100 mots)
4. **Hero Secret** (100-150 mots)
5. **Hero Arc Day1/2/3** (100-150 mots chacun)
6. **Dialogue Exchange** (10 répliques hero/player)
7. **Mission Description** (200-300 mots)

#### Livrable Sprint 1.3
- Service LLM opérationnel
- Tests unitaires pour chaque type de prompt
- Exemples de sorties validées
- Document `prompt-engineering.md` avec tous les templates

---

### 🎨 Service Stable Diffusion - Génération Images

#### Fonctionnalités
- **Pipeline SD** : Chargement checkpoint + LoRAs
- **Batch generation** : 5 émotions d'un héros en une seule passe
- **Post-processing** : Resize, conversion WebP, optimisation poids
- **Seed management** : Garder seed pour régénérer variante

#### Pipeline de Génération
```
1. Prompt construction (sujet + style + émotion)
2. Génération image 1024x1024 (neutral)
3. Img2Img pour variations émotionnelles (même seed)
4. Resize 256x256 pour icône
5. Conversion WebP + compression
6. Validation poids (< 500KB portraits, < 100KB icônes)
```

#### Livrable Sprint 1.4
- Service SD opérationnel
- Tests génération 1 héros complet (6 images)
- Validation qualité visuelle + poids fichiers
- Temps génération mesuré (objectif < 5min pour 1 héros)

---

### 🔧 Post-Processing & Optimisation

#### Fonctionnalités
- **Redimensionnement** : PIL/Pillow pour resize propre
- **Conversion WebP** : Compression avec qualité 85
- **Validation** : Vérification dimensions, poids, format
- **Organisation** : Tri automatique dans arborescence assets

#### Livrable Sprint 1.5
- Scripts de post-processing automatique
- Tests sur batch de 30 images (5 héros × 6 variations)
- Mesure qualité compression (comparaison PNG vs WebP)

---

## 📅 Sprint 2 : Frontend Next.js - Interface de Curation (3-4 semaines)

**Objectif** : Créer l'interface utilisateur permettant de piloter le workflow multi-niveaux de curation.

### 🖥️ Setup Projet Next.js

#### Actions
- Initialiser projet Next.js 14 (App Router)
- Installer librairies UI : Shadcn/ui, Radix UI, Tailwind CSS
- Setup communication API backend (Axios/Fetch)
- Configuration routing (pages pour chaque niveau)

#### Structure
```
curator-frontend/
  app/
    page.tsx                    # Home (sélection projet)
    import/
      page.tsx                  # Upload spec .md
    config/
      page.tsx                  # Niveau 1 : Configuration globale
    generate/
      page.tsx                  # Niveau 2 : Lancement générations
    edit/
      [heroId]/page.tsx         # Niveau 3 : Édition textes
      [heroId]/images/page.tsx  # Niveau 3 : Sélection images
    validate/
      page.tsx                  # Niveau 4 : Validation finale
    export/
      page.tsx                  # Export JSON + assets
  components/
    spec-parser.tsx
    hero-editor.tsx
    image-gallery.tsx
    progress-tracker.tsx
  lib/
    api-client.ts
```

#### Livrable Sprint 2.1
- Projet Next.js fonctionnel
- Navigation entre niveaux opérationnelle
- Connexion API backend testée

---

### 📄 Module d'Import & Parsing (Niveau 0)

#### Fonctionnalités
- **Drag & drop** : Upload fichier `.md` (spec du dev)
- **Parser Markdown** : Extraction placeholders, contraintes, IDs
- **Validation** : Vérification format spec conforme
- **Preview** : Affichage résumé (5 héros à enrichir, 35 textes, 30 images)

#### Livrable Sprint 2.2
- Interface upload fichier
- Parser Markdown fonctionnel
- Tests avec `curator-spec-heroes-enrichment.md`

---

### 🎚️ Configuration Globale (Niveau 1)

#### Fonctionnalités
- **Style visuel** : Choix direction artistique (semi-realistic, cartoon, anime)
- **Ton narratif** : Sérieux, humoristique, épique, sombre
- **Contraintes** : Min/max longueurs textes, émotions à générer
- **Batch settings** : Nombre de héros en parallèle

#### Interface
- Radio buttons pour choix style/ton
- Sliders pour contraintes longueur
- Preview exemples visuels selon style choisi

#### Livrable Sprint 2.3
- Page configuration complète
- Sauvegarde settings en state global (Context API ou Zustand)

---

### 🚀 Lancement Générations (Niveau 2)

#### Fonctionnalités
- **Dashboard** : Vue d'ensemble des 5 héros
- **Lancement batch** : Bouton "Générer tout" ou sélection manuelle
- **Suivi progression** : Barre de progression temps réel (WebSocket ou polling)
- **Preview génération** : Affichage textes/images au fur et à mesure

#### Interface
- Cards pour chaque héros (status : pending, generating, done)
- Logs génération en temps réel
- Estimation temps restant

#### Livrable Sprint 2.4
- Dashboard génération fonctionnel
- Appels API batch backend
- Polling status toutes les 2 secondes

---

### ✍️ Édition & Enrichissement (Niveau 3)

#### Sous-module : Éditeur de Textes

**Fonctionnalités** :
- **Éditeur riche** : Textarea avec compteur mots, formatage Markdown
- **Navigation** : Onglets pour chaque champ (Description, Lore, Voice, Secret, Arc Day1/2/3)
- **Régénération** : Bouton "Re-générer" si texte insatisfaisant
- **Sauvegarde auto** : Enregistrement toutes les 30 secondes

**Interface** :
- Layout 2 colonnes : Texte à gauche, Preview à droite
- Validation temps réel (longueur min/max)

#### Sous-module : Galerie d'Images

**Fonctionnalités** :
- **Galerie** : Affichage 6 images du héros (5 portraits + 1 icône)
- **Sélection** : Marquer image favorite (is_default)
- **Régénération** : Re-générer 1 émotion spécifique si insatisfaisante
- **Upload manuel** : Possibilité d'uploader image custom

**Interface** :
- Grille 3×2 avec preview hover
- Boutons "Régénérer" par image
- Indicateur poids fichier

#### Livrable Sprint 2.5
- Éditeur textes fonctionnel pour 1 héros
- Galerie images avec sélection
- Tests édition + sauvegarde

---

### ✅ Validation Finale (Niveau 4)

#### Fonctionnalités
- **Vue synthétique** : Tableau récapitulatif des 5 héros
- **Validation checklist** : Tous textes remplis, 30 images générées, JSON valide
- **Preview jeu** : Composant simulant affichage dialogue en jeu
- **Correction rapide** : Liens directs vers pages édition si erreur détectée

#### Interface
- Tableau avec colonnes : Héros | Textes | Images | Statut
- Checkboxes validation (auto-coché si OK)
- Bouton "Valider et exporter" (disabled si erreurs)

#### Livrable Sprint 2.6
- Page validation complète
- Tests validation automatique
- Preview dialogue fonctionnelle

---

### 📤 Export & Livraison (Niveau 5)

#### Fonctionnalités
- **Génération JSON** : Structure conforme à spec dev
- **Organisation assets** : Tri images dans arborescence correcte
- **Compression finale** : Archive `.zip` avec JSON + assets
- **Notes curator** : Génération automatique `curator-notes.md`

#### Format de Sortie
```
export-2025-11-24/
  curator-output-heroes-enrichment-2025-11-24.json
  assets/
    heroes/
      bjorn/
        portraits/
          bjorn-portrait-high-neutral.webp
          bjorn-portrait-high-happy.webp
          ...
        icons/
          bjorn-icon-low.webp
      owen/
      vi/
      durun/
      elira/
  curator-notes-heroes-enrichment.md
```

#### Livrable Sprint 2.7
- Export JSON fonctionnel
- Organisation assets automatique
- Tests import dans jeu (via dev)

---

## 📅 Sprint 3 : Intégration & Fonctionnalités Avancées (2 semaines)

**Objectif** : Pipeline complet end-to-end + features avancées pour productivité.

### 🔄 Pipeline Complet End-to-End

#### Actions
- **Tests intégration** : Workflow complet (import spec → export JSON)
- **Tests batch** : Génération 5 héros en parallèle
- **Mesure performance** : Temps total génération, goulots d'étranglement
- **Optimisation** : Cache résultats, parallélisation jobs

#### Livrable Sprint 3.1
- Pipeline testé avec `curator-spec-heroes-enrichment.md`
- 5 héros complets générés en < 30 minutes
- Document `performance-benchmarks.md`

---

### 🚀 Mode Batch Avancé

#### Fonctionnalités
- **Génération nuit** : Lancer batch lourd et laisser tourner
- **Priorités** : Générer d'abord textes, puis images (si VRAM limitée)
- **Parallélisation** : 2-3 héros en simultané (si GPU le permet)
- **Reprise crash** : Reprendre là où ça s'est arrêté

#### Livrable Sprint 3.2
- Mode batch avec file d'attente persistante
- Tests génération 10 héros (2 batchs)

---

### 🎭 Preview Temps Réel (Composants Simulateurs)

#### Fonctionnalités
- **Faux DialogueModal** : Simule affichage dialogue en jeu
- **Faux HeroCard** : Simule carte héros dans sélection
- **Toggle émotions** : Changer émotion portrait en live
- **Export preview** : Captures d'écran des previews pour validation dev

#### Livrable Sprint 3.3
- Composants preview fonctionnels
- Intégration dans page validation

---

### 🔗 Connecteur Supabase (Optionnel - Avancé)

#### Fonctionnalités
- **Push direct DB** : Au lieu d'exporter JSON, insérer directement en Supabase
- **Upload Storage** : Uploader images dans bucket `hero-portraits`
- **Validation DB** : Vérifier insertion réussie (requêtes SQL)

**Note** : Alternative à export JSON, pour workflows plus avancés.

#### Livrable Sprint 3.4 (Optionnel)
- Module connexion Supabase
- Tests insertion 1 héro complet
- Documentation intégration

---

## 📅 Sprint 4 : Polish, Documentation & Formation (1 semaine)

**Objectif** : Finaliser l'application, documenter et former l'équipe.

### 📚 Documentation Complète

#### Documents à Créer
1. **User Guide** : `curator-user-guide.md`
   - Installation (dev + prod)
   - Workflow complet illustré (screenshots)
   - Troubleshooting courants
2. **Technical Guide** : `curator-technical-guide.md`
   - Architecture détaillée
   - API documentation complète
   - Prompts engineering expliqués
3. **Model Configuration** : `model-config.md`
   - Settings LLM (température, top_p, etc.)
   - Settings SD (steps, CFG scale, etc.)
   - Guide fine-tuning si nécessaire

#### Livrable Sprint 4.1
- Documentation exhaustive (3 guides)
- README.md racine avec quick start

---

### 🎓 Formation & Handover

#### Actions
- Session formation équipe (2h) : Demo workflow complet
- Génération 1er batch "production" supervisée
- Feedback utilisateurs et ajustements UX
- Création vidéos tutoriels (si budget)

#### Livrable Sprint 4.2
- 1 batch production généré avec succès
- Feedback intégré dans backlog v2

---

### 🐛 Tests & Qualité

#### Actions
- **Tests unitaires** : Backend (services LLM/SD)
- **Tests intégration** : Frontend ↔ Backend
- **Tests end-to-end** : Workflow complet automatisé (Playwright)
- **Gestion erreurs** : Tous les edge cases couverts

#### Livrable Sprint 4.3
- Coverage tests > 70%
- CI/CD pipeline (GitHub Actions)

---

## 📊 Métriques de Succès

| Métrique | Objectif |
|----------|----------|
| **Temps génération 1 héros complet** | < 5 minutes |
| **Temps génération batch 5 héros** | < 30 minutes |
| **Qualité narrative** | Validation manuelle 80% des textes sans édition |
| **Qualité visuelle** | 90% des images satisfaisantes sans régénération |
| **Poids moyen portrait** | < 400KB (objectif 500KB max) |
| **Cohérence visuelle** | Tous héros reconnaissables même univers |
| **Uptime API Backend** | 99% (gestion erreurs robuste) |
| **Satisfaction utilisateur** | 4/5 après formation |

---

## 🔮 Roadmap Contenu (Post-Système)

Une fois le **système Curator opérationnel**, sprints dédiés à la génération de contenu :

### Sprint Contenu 1 : Héros D&D (Priorité 1)
- 5 héros complets (textes + 30 images)
- Import dans jeu + tests

### Sprint Contenu 2 : Dialogues Jour 1 (Priorité 2)
- 5 dialogues enrichis (10 échanges chacun)
- Intégration portraits émotionnels

### Sprint Contenu 3 : Missions Narratives (Priorité 3)
- 15 missions avec textes immersifs
- NPCs + success/failure texts

### Sprint Contenu 4 : Bâtiments Vivants (Priorité 4)
- 5 bâtiments avec NPCs et descriptions
- Secrets et easter eggs

---

## 📞 Support & Maintenance

**Post-livraison** :
- Maintenance modèles (mise à jour checkpoints SD)
- Amélioration prompts selon feedback
- Ajout nouveaux types de contenu (locations, items, etc.)
- Fine-tuning LLM sur style Medieval Dispatch (si corpus suffisant)

---

**Document créé par** : Équipe Dev Medieval Dispatch  
**Version** : 2.0  
**Prochaine révision** : Après Sprint 0 (validation modèles)
