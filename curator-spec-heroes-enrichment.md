# Spécification Curator : Création de 5 Personnages D&D - Sprint 1

**Date** : 24 novembre 2025  
**Priorité** : 🔴 CRITIQUE  
**Quantité** : 5 personnages D&D complets (niveau 1)  
**Estimation** : 30 images + 5 personnages narratifs

---

## 🎯 Contexte de l'Univers (Info seulement)

**Setting** : Medieval Dispatch - Médiéval-fantastique standard D&D 5e
- Village de Phandallin entouré de dangers (forêts, grottes, ruines)
- Le joueur gère le village et envoie des aventuriers en mission
- Cycle de 3 jours de gameplay

**Liberté Créative du Curator** :
- ✅ **Tu décides TOUT** : races, classes, backgrounds, personnalités, apparences
- ✅ Crée des personnages D&D 5e authentiques et intéressants
- ✅ Assure la cohérence narrative entre eux (ils forment un groupe)
- ✅ Pas de contraintes sur le ton, style ou direction narrative
- ✅ Fais preuve de créativité et de diversité

---

## 📊 Placeholders Actuels en Base de Données

5 entrées existent avec IDs et slugs définis, mais contenu minimal :

| ID | Slug | Name | Title | Contenu Actuel |
|----|------|------|-------|----------------|
| `cfcb7953...` | `bjorn` | Bjorn | Bjorn le Vaillant | Placeholders génériques |
| `ce86dd7d...` | `owen` | Owen | Owen le Roublard | Placeholders génériques |
| `c6e8b883...` | `vi` | Vi | Vi la Sage | Placeholders génériques |
| `c1305ab7...` | `durun` | Durun | Durun le Robuste | Placeholders génériques |
| `c10dbcf7...` | `elira` | Elira | Elira la Diplomate | Placeholders génériques |

**Note** : Les noms et titres peuvent être modifiés si le Curator estime qu'ils ne correspondent pas aux personnages créés.

---

## ✍️ Contenu à Créer

### 📝 Pour Chaque Personnage : Structure D&D 5e Complète

#### **Stats D&D (6 stats principales)** - Méthode Point Buy ou Standard Array
- `dnd_strength` (Force) : 1-20
- `dnd_dexterity` (Dextérité) : 1-20
- `dnd_constitution` (Constitution) : 1-20
- `dnd_intelligence` (Intelligence) : 1-20  
- `dnd_wisdom` (Sagesse) : 1-20
- `dnd_charisma` (Charisme) : 1-20

**Note** : Personnages niveau 1, stats cohérentes avec la classe choisie.

#### **Informations D&D**
- `level` : 1 (tous niveau 1)
- `race` : Choix libre parmi races D&D 5e (Human, Elf, Dwarf, Halfling, Dragonborn, etc.)
- `class` : Choix libre parmi classes D&D 5e (Fighter, Rogue, Wizard, Cleric, Ranger, etc.)
- `background` : Choix libre parmi backgrounds D&D 5e (Soldier, Criminal, Scholar, Folk Hero, etc.)

#### **Traits de Personnalité D&D**
- `personality_traits` : Array de 2-3 traits distinctifs
- `ideals` : Ce qui motive fondamentalement le personnage
- `bonds` : Liens importants (personnes, lieux, organisations)
- `flaws` : Défauts significatifs

#### **Textes Narratifs**
- `description` (150-250 mots) : Description physique et première impression
- `lore` (400-600 mots) : Backstory complète cohérente avec le background D&D
- `voice` (50-100 mots) : Manière de parler, expressions
- `secret` (100-150 mots) : Secret personnel intrigant
- `arc_day1`, `arc_day2`, `arc_day3` (100-150 mots chacun) : Arcs narratifs sur 3 jours

### 🎨 Images à Générer

Pour chaque personnage : **6 images** (30 images total)

#### Portraits Haute Résolution (1024x1024)
- 5 variations émotionnelles : neutral, happy, sad, angry, surprised
- Style : **À la discrétion du Curator**
- Format : WebP optimisé, max 500KB

#### Icône UI (256x256)
- 1 icône neutre pour carte/interface
- Contraste élevé, lisible en petite taille
- Format : WebP optimisé, max 100KB

---

## 🔒 Contraintes Techniques (Structure DB)

## 🔒 Contraintes Techniques (Structure DB)

### Champs Base de Données

**Table `heroes`** - Champs à remplir :

| Champ | Type | Contrainte | Description |
|-------|------|------------|-------------|
| `name` | TEXT | Requis | Nom du personnage (peut être modifié) |
| `title` | TEXT | Requis | Titre descriptif (peut être modifié) |
| `description` | TEXT | 150-250 mots | Description physique et impression |
| `lore` | TEXT | 400-600 mots | Backstory complète |
| `voice` | TEXT | 50-100 mots | Manière de parler |
| `secret` | TEXT | 100-150 mots | Secret personnel |
| `arc_day1` | TEXT | 100-150 mots | Arc narratif jour 1 |
| `arc_day2` | TEXT | 100-150 mots | Arc narratif jour 2 |
| `arc_day3` | TEXT | 100-150 mots | Arc narratif jour 3 |
| `dnd_strength` | INTEGER | 1-20 | Force D&D |
| `dnd_dexterity` | INTEGER | 1-20 | Dextérité D&D |
| `dnd_constitution` | INTEGER | 1-20 | Constitution D&D |
| `dnd_intelligence` | INTEGER | 1-20 | Intelligence D&D |
| `dnd_wisdom` | INTEGER | 1-20 | Sagesse D&D |
| `dnd_charisma` | INTEGER | 1-20 | Charisme D&D |
| `level` | INTEGER | 1 (fixe) | Niveau D&D |
| `race` | TEXT | Requis | Race D&D 5e |
| `class` | TEXT | Requis | Classe D&D 5e |
| `background` | TEXT | Requis | Background D&D 5e |
| `personality_traits` | TEXT[] | Array 2-3 éléments | Traits de personnalité |
| `ideals` | TEXT | Requis | Idéaux/motivations |
| `bonds` | TEXT | Requis | Liens importants |
| `flaws` | TEXT | Requis | Défauts |

**Table `hero_image_variants`** - Métadonnées images :

| Champ | Valeurs | Description |
|-------|---------|-------------|
| `base_type` | 'portrait' ou 'icon' | Type d'image |
| `resolution` | 'high' (1024x1024) ou 'low' (256x256) | Résolution |
| `emotion` | 'neutral', 'happy', 'sad', 'angry', 'surprised' | Émotion (null pour icon) |
| `usage_context` | 'dialogue' ou 'map_icon' | Contexte d'utilisation |
| `format` | 'webp' | Format fichier |
| `url` | TEXT | Chemin relatif assets |
| `width` | INTEGER | Largeur pixels |
| `height` | INTEGER | Hauteur pixels |

### Formats Fichiers

**Images** :
- Format : WebP (qualité 85)
- Portraits : 1024x1024, max 500KB
- Icônes : 256x256, max 100KB  
- Nomenclature : `{slug}-portrait-high-{emotion}.webp` ou `{slug}-icon-low.webp`

**Textes** :
- Encodage : UTF-8
- Échapper guillemets pour JSON : `"` → `\"`
- Pas de caractères spéciaux problématiques

---

## 📤 Format de Sortie (JSON)

### Structure JSON

```json
{
  "content_type": "heroes_enrichment",
  "generation_date": "2025-11-24",
  "curator_version": "1.0.0",
  "style_visual": "semi-realistic",
  "total_items": 5,
  "total_images": 30,
  "items": [
    {
      "id": "cfcb7953546ceb3c2cfc2b5a1",
      "slug": "bjorn",
      "enriched_fields": {
        "description": "Bjorn se tient devant vous, une présence imposante qui...",
        "lore": "Né dans les terres froides du nord, Bjorn a grandi dans...",
        "voice": "Bjorn parle d'une voix grave et mesurée. Ses mots sont rares...",
        "secret": "Peu le savent, mais Bjorn porte le poids d'une erreur...",
        "arc_day1": "Au premier jour, Bjorn observe le village avec...",
        "arc_day2": "Le deuxième jour révèle une facette plus vulnérable...",
        "arc_day3": "Au troisième jour, Bjorn doit faire face à..."
      },
      "images": [
        {
          "base_type": "portrait",
          "resolution": "high",
          "emotion": "neutral",
          "usage_context": "dialogue",
          "filename": "bjorn-portrait-high-neutral.webp",
          "path": "assets/heroes/bjorn/portraits/",
          "width": 1024,
          "height": 1024,
          "format": "webp",
          "is_default": true
        },
        {
          "base_type": "portrait",
          "resolution": "high",
          "emotion": "happy",
          "usage_context": "dialogue",
          "filename": "bjorn-portrait-high-happy.webp",
          "path": "assets/heroes/bjorn/portraits/",
          "width": 1024,
          "height": 1024,
          "format": "webp",
          "is_default": false
        },
        {
          "base_type": "portrait",
          "resolution": "high",
          "emotion": "sad",
          "usage_context": "dialogue",
          "filename": "bjorn-portrait-high-sad.webp",
          "path": "assets/heroes/bjorn/portraits/",
          "width": 1024,
          "height": 1024,
          "format": "webp",
          "is_default": false
        },
        {
          "base_type": "portrait",
          "resolution": "high",
          "emotion": "angry",
          "usage_context": "dialogue",
          "filename": "bjorn-portrait-high-angry.webp",
          "path": "assets/heroes/bjorn/portraits/",
          "width": 1024,
          "height": 1024,
          "format": "webp",
          "is_default": false
        },
        {
          "base_type": "portrait",
          "resolution": "high",
          "emotion": "surprised",
          "usage_context": "dialogue",
          "filename": "bjorn-portrait-high-surprised.webp",
          "path": "assets/heroes/bjorn/portraits/",
          "width": 1024,
          "height": 1024,
          "format": "webp",
          "is_default": false
        },
        {
          "base_type": "icon",
          "resolution": "low",
          "emotion": null,
          "usage_context": "map_icon",
          "filename": "bjorn-icon-low.webp",
          "path": "assets/heroes/bjorn/icons/",
          "width": 256,
          "height": 256,
          "format": "webp",
          "is_default": false
        }
      ]
    }
    // ... Répéter pour Owen, Vi, Durun, Elira
  ]
}
```

### Organisation Assets

```
assets/
  heroes/
    bjorn/
      portraits/
        bjorn-portrait-high-neutral.webp (500KB max)
        bjorn-portrait-high-happy.webp
        bjorn-portrait-high-sad.webp
        bjorn-portrait-high-angry.webp
        bjorn-portrait-high-surprised.webp
      icons/
        bjorn-icon-low.webp (100KB max)
    owen/
      portraits/
        owen-portrait-high-neutral.webp
        owen-portrait-high-happy.webp
        owen-portrait-high-sad.webp
        owen-portrait-high-angry.webp
        owen-portrait-high-surprised.webp
      icons/
        owen-icon-low.webp
    vi/
      portraits/
        vi-portrait-high-neutral.webp
        vi-portrait-high-happy.webp
        vi-portrait-high-sad.webp
        vi-portrait-high-angry.webp
        vi-portrait-high-surprised.webp
      icons/
        vi-icon-low.webp
    durun/
      portraits/
        durun-portrait-high-neutral.webp
        durun-portrait-high-happy.webp
        durun-portrait-high-sad.webp
        durun-portrait-high-angry.webp
        durun-portrait-high-surprised.webp
      icons/
        durun-icon-low.webp
    elira/
      portraits/
        elira-portrait-high-neutral.webp
        elira-portrait-high-happy.webp
        elira-portrait-high-sad.webp
        elira-portrait-high-angry.webp
        elira-portrait-high-surprised.webp
      icons/
        elira-icon-low.webp
```

**Total fichiers** : 30 images (5 héros × 6 images)

---

## ✅ Critères de Validation

### Textes
- [ ] Tous les champs enrichis (description, lore, voice, secret, arc_day1/2/3) sont remplis
- [ ] Longueurs respectent les contraintes techniques (150-600 mots selon champ)
- [ ] Encodage UTF-8 valide, guillemets échappés pour JSON

### Images
- [ ] 30 images générées (5 héros × 6 variations)
- [ ] Portraits haute résolution : 1024x1024, < 500KB, WebP
- [ ] Icônes basse résolution : 256x256, < 100KB, WebP
- [ ] Format WebP qualité 85

### JSON
- [ ] JSON valide (pas d'erreurs de syntaxe)
- [ ] Tous les IDs correspondent aux IDs Supabase existants
- [ ] Structure conforme au template fourni
- [ ] Chemins de fichiers corrects et cohérents
- [ ] Métadonnées complètes (width, height, format, etc.)

### Organisation
- [ ] Assets organisés par héros puis par type (portraits/, icons/)
- [ ] Nomenclature des fichiers respectée (`{slug}-portrait-high-{emotion}.webp`)
- [ ] Pas de fichiers manquants
- [ ] Pas de doublons

---

## 🚀 Livrables Attendus

1. **Fichier JSON** : `curator-output-heroes-enrichment-2025-11-24.json`
2. **Dossier Assets** : `assets/heroes/` avec structure complète
3. **Document Récapitulatif** : `curator-notes-heroes-enrichment.md` (OPTIONNEL)

---

## 📅 Timeline Suggérée

**Estimation totale** : 4-6 heures (selon processus)

1. **Génération Textes** : 2-3h
2. **Génération Images** : 2-3h  
3. **Export et Validation** : 30min

---

**Document créé par** : Équipe Dev Medieval Dispatch  
**Pour** : Système Curator IA
