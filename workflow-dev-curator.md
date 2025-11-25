# Workflow Développement ↔ Curator

**Date de création** : 24 novembre 2025  
**Dernière mise à jour** : 24 novembre 2025

---

## 🎯 Séparation des Responsabilités

### 👨‍💻 Équipe Développement
**Responsabilités UNIQUEMENT TECHNIQUES** :
- ✅ Créer les **mécaniques de jeu** (gameplay, systèmes, règles de calcul)
- ✅ Définir les **structures de données** (schéma Prisma, tables Supabase, champs requis)
- ✅ Créer les **entrées placeholder** vides ou avec valeurs minimales
- ✅ Développer les **API routes** et la **logique métier**
- ✅ Spécifier les **contraintes techniques** (formats, tailles, types de données)
- ✅ Intégrer le **contenu généré** dans le jeu
- ❌ **NE PAS** imposer de directives narratives, stylistiques ou créatives

### 🎨 Curator (Système IA)
**Responsabilités CRÉATIVES COMPLÈTES** :
- ✅ **LIBERTÉ TOTALE** sur les choix narratifs (personnalités, backstories, relations)
- ✅ **LIBERTÉ TOTALE** sur les choix visuels (apparences, styles, palettes)
- ✅ Créer des **personnages D&D complets** (race, classe, background, stats, traits)
- ✅ Générer tout le **contenu narratif** enrichi et cohérent
- ✅ Créer les **dialogues** avec voix uniques
- ✅ Générer les **images** multi-résolutions avec variations émotionnelles
- ✅ Assurer la **cohérence narrative globale** entre tous les éléments
- ✅ Prendre toutes les **décisions créatives** sans directives imposées

---

## 🔄 Processus de Collaboration

### Phase 1 : Développement crée les Structures

**Actions** :
1. **Définir la mécanique** (ex: nouveau type de héros, nouvelle mission)
2. **Créer/Modifier le schéma Prisma** avec tous les champs nécessaires
3. **Appliquer la migration Supabase**
4. **Insérer des entrées placeholder** :
   - IDs et relations fonctionnelles
   - Valeurs minimales pour que le jeu fonctionne
   - Champs texte = placeholders génériques
   - Champs image = références temporaires

**Livrable** : Document `.md` de spécification (SANS CODE) pour le Curator

### Phase 2 : Curator génère le Contenu

**Process de Curation Multi-Niveaux** :

Chaque type de contenu passe par plusieurs niveaux de raffinement progressif pour garantir la qualité finale.

#### 🎨 **Système de Curation pour Images**

**Niveau 1 : Définition du Style Global**
- Choix style visuel (animé/semi-réaliste/cartoon)
- Palette de couleurs
- Direction artistique générale

**Niveau 2 : Génération Portraits de Base**
- Portrait principal (haute résolution pour dialogues)
- Génération via Stable Diffusion avec prompts détaillés
- Validation cohérence avec style global

**Niveau 3 : Création des Variations**
- Icône (petite taille pour UI/maps)
- Variations émotionnelles (happy, sad, angry, surprised, neutral)
- Adaptation contexte (portrait_full, portrait_dialogue, icon)

**Niveau 4 : Post-Processing & Optimisation**
- Resize aux dimensions requises
- Optimisation poids (WebP)
- Validation qualité visuelle
- Export multi-résolutions

#### 📝 **Système de Curation pour Textes**

**Niveau 1 : Génération Contextuelle**
- Compréhension du contexte narratif global
- Génération descriptions/lore via OpenLLaMA
- Ton et style appropriés

**Niveau 2 : Enrichissement & Détails**
- Ajout de détails spécifiques
- Backstories cohérentes
- Relations entre personnages

**Niveau 3 : Cohérence Narrative**
- Vérification contradictions
- Harmonisation tonalité
- Validation arcs narratifs

**Niveau 4 : Finalisation & Polish**
- Correction grammaticale
- Ajustement longueurs
- Validation format JSON

#### 💬 **Système de Curation pour Dialogues**

**Niveau 1 : Structure Narrative**
- Définition objectif du dialogue
- Arc émotionnel
- Points clés à transmettre

**Niveau 2 : Rédaction des Échanges**
- Génération répliques hero/player
- Voix unique par personnage
- Émotions appropriées

**Niveau 3 : Dynamique & Rythme**
- Équilibre longueur répliques
- Alternance émotions
- Natural flow conversation

**Niveau 4 : Intégration Assets**
- Attribution portraits émotionnels
- Validation cohérence visuelle/textuelle
- Export format dialogue_exchanges

#### 🗺️ **Système de Curation pour Missions**

**Niveau 1 : Concept & Objectif**
- Définition mission (infiltration, combat, diplomatie)
- Stakes narratifs
- Récompenses cohérentes

**Niveau 2 : Rédaction Descriptive**
- Description mission immersive
- Contexte géographique/temporel
- Personnalités impliquées (NPCs)

**Niveau 3 : Textes de Résolution**
- Success_text narratif et satisfaisant
- Failure_text avec conséquences
- Variations selon choix/héros

**Niveau 4 : Polish & Intégration**
- Harmonisation avec lore global
- Validation mécanique + narration
- Export JSON final

### Phase 3 : Intégration par le Dev

**Actions** :
1. **Valider le format** (JSON conforme aux specs)
2. **Vérifier les assets** (images présentes, formats corrects)
3. **Créer script d'import** (Prisma seed ou migration SQL)
4. **Exécuter l'import** dans Supabase
5. **Tester en jeu** (affichage correct, cohérence)
6. **Feedback au Curator** si ajustements nécessaires

---

## 🏗️ Architecture Technique du Curator

### Stack Technique

**Frontend** : Next.js 14 avec App Router
- Interface multi-niveaux de curation
- Prévisualisation en temps réel
- Édition manuelle si nécessaire
- Gestion de batch (plusieurs héros à la fois)

**Backend** : Services Python (Local)
- **OpenLLaMA** : Génération textes
- **Stable Diffusion** : Génération images
- API REST pour communication Next.js ↔ Python

**Stockage** :
- Base de données de travail (curation en cours)
- Export final en JSON + assets séparés
- Historique des versions générées

### Workflow Interface Curator

```
1. [Import Spec] → Upload spec .md du dev
   ↓
2. [Parsing] → Extraction placeholders à enrichir
   ↓
3. [Niveau 1] → Configuration globale (style, ton)
   ↓
4. [Niveau 2] → Génération contenu de base
   ↓
5. [Niveau 3] → Enrichissement & variations
   ↓
6. [Niveau 4] → Révision manuelle + validation
   ↓
7. [Export] → JSON + assets organisés
```

---

## 📊 Structure de Base de Données pour Accueillir le Contenu

### Schema Actuel vs Requis pour Multi-Résolutions Images

#### ❌ Limitation Actuelle (hero_images)
```prisma
model hero_images {
  id          String
  hero_id     String
  image_type  String  // Seulement 'portrait_full' actuellement
  url         String  // Une seule URL
  is_default  Boolean
}
```

#### ✅ Structure Améliorée Requise

**Nouvelle Table : `hero_image_variants`**
```prisma
model hero_image_variants {
  id            String   @id @default(cuid())
  hero_id       String
  base_type     String   // 'portrait', 'icon', 'illustration'
  resolution    String   // 'high' (1024x1024), 'medium' (512x512), 'low' (256x256)
  emotion       String?  // 'neutral', 'happy', 'sad', 'angry', 'surprised', null si non applicable
  usage_context String   // 'dialogue', 'map_icon', 'hero_select', 'village_placement'
  url           String   // URL Supabase Storage
  width         Int
  height        Int
  file_size     Int      // Bytes pour monitoring
  format        String   // 'webp', 'png'
  is_default    Boolean  @default(false) // Portrait neutre haute résolution
  created_at    DateTime @default(now())
  
  hero heroes @relation(fields: [hero_id], references: [id])
  
  @@unique([hero_id, base_type, resolution, emotion])
  @@index([hero_id, usage_context])
}
```

**Exemples d'entrées générées par le Curator** :
```json
[
  {
    "hero_id": "bjorn_id",
    "base_type": "portrait",
    "resolution": "high",
    "emotion": "neutral",
    "usage_context": "dialogue",
    "url": "supabase://hero-portraits/bjorn-portrait-high-neutral.webp",
    "width": 1024,
    "height": 1024,
    "is_default": true
  },
  {
    "hero_id": "bjorn_id",
    "base_type": "portrait",
    "resolution": "high",
    "emotion": "angry",
    "usage_context": "dialogue",
    "url": "supabase://hero-portraits/bjorn-portrait-high-angry.webp",
    "width": 1024,
    "height": 1024
  },
  {
    "hero_id": "bjorn_id",
    "base_type": "icon",
    "resolution": "low",
    "emotion": null,
    "usage_context": "map_icon",
    "url": "supabase://hero-icons/bjorn-icon-256.webp",
    "width": 256,
    "height": 256
  }
]
```

### Extension pour Personnages D&D Complets

**Table `heroes` : Structure D&D 5e**
```prisma
model heroes {
  // Champs existants (id, slug, name, title, description, lore, voice, secret, arc_day1/2/3)
  
  // Stats D&D 5e (6 stats principales)
  dnd_strength      Int @default(10)  // 1-20
  dnd_dexterity     Int @default(10)  // 1-20
  dnd_constitution  Int @default(10)  // 1-20
  dnd_intelligence  Int @default(10)  // 1-20
  dnd_wisdom        Int @default(10)  // 1-20
  dnd_charisma      Int @default(10)  // 1-20
  
  // Informations D&D
  level       Int     @default(1)      // Niveau 1-20
  race        String?                  // Human, Elf, Dwarf, etc. (choix Curator)
  class       String?                  // Fighter, Rogue, Wizard, etc. (choix Curator)
  background  String?                  // Soldier, Criminal, etc. (choix Curator)
  
  // Traits de personnalité D&D
  personality_traits String[]          // Array de 2-3 traits
  ideals             String?           // Ce qui motive le personnage
  bonds              String?           // Liens et affiliations
  flaws              String?           // Défauts
}
```

**Note** : Les anciennes stats (strength, diplomacy, stealth, intelligence) sont conservées pour compatibilité et seront calculées/mappées depuis les stats D&D via l'API.

---

## 📋 Format des Documents de Spécification (Dev → Curator)

### Template Type

```markdown
# Spécification Curator : [Type de Contenu] - [Action]

**Date** : 2025-11-24
**Priorité** : Critique / Haute / Moyenne / Basse
**Quantité** : X héros / Y missions / Z dialogues

---

## 🎯 Contexte Narratif Global

[Description de l'univers, époque, enjeux, ton général]

---

## 📊 Contenu Actuel (Placeholders en DB)

### Table : [nom_table]
| ID | Champ 1 | Champ 2 | ... | Statut |
|----|---------|---------|-----|--------|
| xxx | placeholder | placeholder | ... | 🟡 À enrichir |

---

## ✍️ Contenu à Générer

### Contraintes Techniques UNIQUEMENT

**Textes** :
- Longueurs recommandées : descriptions (100-300 mots), lore (300-500 mots)
- Dialogues : 5-10 échanges (ajustable selon besoin narratif)
- Format : UTF-8, JSON-compatible
- **Le Curator décide** : ton, style, vocabulaire, personnalités

**Images** :
- Résolutions requises : 1024x1024 (dialogues), 256x256 (UI)
- Émotions à générer : neutral, happy, sad, angry, surprised (minimum)
- Format : WebP optimisé
- **Le Curator décide** : style visuel, palettes, apparences, détails

---

## 🔒 Contraintes Techniques

**Champs Base de Données** :
- [champ1] : VARCHAR(500) max
- [champ2] : TEXT illimité
- [champ3] : INTEGER entre 0-100

**Formats Fichiers** :
- Images : WebP optimisé
- Taille max : 500KB par image
- Nommage : `{slug}-{type}-{resolution}-{emotion}.webp`

**Relations** :
- Hero ID doit correspondre à table `heroes`
- Dialogues liés à `hero_id` existant

---

## 🧩 Cohérence Narrative Requise

**Éléments Existants à Respecter** :
- [Héros X] est un guerrier nordique
- [Lieu Y] est une forêt dangereuse
- Époque : Médiéval-fantastique

**Arcs Narratifs** :
- Jour 1 : Introduction des personnages
- Jour 2 : Développement conflits
- Jour 3 : Résolution / climax

---

## 📤 Format de Sortie Attendu

### Structure JSON
```json
{
  "content_type": "heroes",
  "generation_date": "2025-11-24",
  "curator_version": "1.0",
  "items": [
    {
      "id": "database_id_here",
      "slug": "hero-slug",
      "enriched_fields": {
        "description": "...",
        "lore": "...",
        "voice": "..."
      },
      "images": [
        {
          "base_type": "portrait",
          "resolution": "high",
          "emotion": "neutral",
          "filename": "bjorn-portrait-high-neutral.webp",
          "path": "assets/heroes/bjorn/portraits/"
        }
      ]
    }
  ]
}
```

### Organisation Assets
```
assets/
  heroes/
    bjorn/
      portraits/
        bjorn-portrait-high-neutral.webp
        bjorn-portrait-high-happy.webp
        bjorn-portrait-high-angry.webp
      icons/
        bjorn-icon-256.webp
  locations/
    foret/
      foret-main-1024.webp
      foret-thumbnail-512.webp
```

---

## ✅ Critères de Validation

- [ ] Tous les placeholders sont enrichis
- [ ] Longueurs de texte respectées
- [ ] Images dans formats/résolutions requis
- [ ] Cohérence narrative vérifiée
- [ ] JSON valide et conforme au schéma
- [ ] Assets organisés correctement
- [ ] Nomenclature respectée

```

---

## 📊 Suivi des Contenus

| Type | Total | Placeholders | En Cours | Validés | Statut |
|------|-------|--------------|----------|---------|--------|
| Héros | 5 | 5 | 0 | 0 | 🔴 URGENT |
| Images Héros | 5 | 5 | 0 | 0 | 🔴 URGENT |
| Dialogues | 3 | 3 | 0 | 0 | 🟡 IMPORTANT |
| Missions | 15 | 15 | 0 | 0 | 🟡 IMPORTANT |
| Bâtiments | 5 | 5 | 0 | 0 | 🟢 MOYEN |
| Locations | 4 | 0 | 0 | 4 | ✅ COMPLET |

---

## 🚀 Roadmap Contenu

### Sprint 1 : Héros Enrichis (Priorité 1)
**Objectif** : Transformer 5 héros placeholder en personnages riches

**Dev** :
- [ ] Créer table `hero_image_variants`
- [ ] Migration Prisma/Supabase
- [ ] Créer `curator-spec-heroes-enrichment.md`
- [ ] Setup bucket Supabase Storage `hero-portraits`

**Curator** :
- [ ] Générer descriptions/lore pour Bjorn, Owen, Vi, Durun, Elira
- [ ] Créer 5 émotions × 5 héros = 25 portraits haute résolution
- [ ] Créer 5 icônes héros (256x256)
- [ ] Export JSON + assets organisés

**Intégration** :
- [ ] Import contenu dans Supabase
- [ ] Tester affichage en jeu
- [ ] Validation narrative

### Sprint 2 : Dialogues Complets (Priorité 2)
**Objectif** : 5 dialogues jour 1 complets et immersifs

**Dev** :
- [ ] Créer `curator-spec-dialogues-day1.md`
- [ ] Ajouter champs `emotional_arc`, `key_revelation` à table dialogues

**Curator** :
- [ ] Enrichir 3 dialogues existants (Bjorn, Owen, Vi)
- [ ] Créer 2 nouveaux dialogues (Durun, Elira)
- [ ] Attribution portraits émotionnels appropriés

### Sprint 3 : Missions Narratives (Priorité 3)
**Objectif** : 15 missions avec profondeur narrative

**Dev** :
- [ ] Créer `curator-spec-missions-enrichment.md`
- [ ] Ajouter champs narratifs à table missions

**Curator** :
- [ ] Enrichir 15 missions existantes
- [ ] Créer NPCs impliqués
- [ ] Rédiger textes de résolution immersifs

### Sprint 4 : Bâtiments Vivants (Priorité 4)
**Objectif** : Bâtiments avec NPCs et atmosphères

**Dev** :
- [ ] Créer `curator-spec-buildings-atmosphere.md`

**Curator** :
- [ ] Générer NPCs pour 5 bâtiments
- [ ] Créer descriptions atmosphériques
- [ ] Définir secrets/easter eggs

---

## 🔧 Scripts & Outils à Développer

### Côté Dev
```bash
# Générer spec depuis DB actuelle
npm run curator:generate-spec -- --type=heroes --output=docs/curator/specs/

# Valider JSON de sortie Curator
npm run curator:validate -- --file=curator-output-heroes.json --schema=schemas/heroes.json

# Importer contenu dans Supabase
npm run curator:import -- --file=curator-output-heroes.json --upload-assets

# Vérifier cohérence narrative globale
npm run curator:check-consistency -- --verbose
```

### Côté Curator
```bash
# Démarrer interface de curation
npm run curator:start

# Générer batch de contenu
python curator/generate.py --spec=heroes-enrichment.md --batch-size=5

# Preview contenu généré
python curator/preview.py --output=heroes-2025-11-24.json
```

---

## ⚠️ Points d'Attention

### Qualité du Contenu
- **Cohérence Narrative** : Tous les éléments doivent appartenir au même univers
- **Diversité** : Héros variés (genres, origines, personnalités, compétences)
- **Profondeur** : Éviter les stéréotypes, créer backstories riches

### Performance Technique
- **Taille Images** : Max 500KB par portrait (optimisation WebP)
- **Temps Génération** : < 5min par héros acceptable
- **Batch Processing** : Possibilité de générer 5 héros en parallèle

### Versioning & Rollback
- Garder historique des versions générées
- Possibilité de rollback si contenu non satisfaisant
- Changelog des modifications narratives

---

## 📚 Documentation Associée

- `docs/curator/curator-spec-heroes-enrichment.md` : Première spec à envoyer
- `docs/architecture/database.md` : Schéma DB complet
- `prisma/schema.prisma` : Source de vérité structures DB
- `docs/curator/examples/` : Exemples de sorties JSON

---

**Auteurs** : Équipe Medieval Dispatch  
**Prochaine révision** : Après Sprint 1 (enrichissement héros)
