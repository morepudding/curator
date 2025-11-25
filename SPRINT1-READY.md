# 🚀 Sprint 1 : Héros D&D 5e - PRÊT POUR GÉNÉRATION

**Date** : 24 novembre 2025  
**Statut** : ✅ Infrastructure complète - En attente génération curator

---

## ✅ Travaux Complétés (Dev)

### 1. Structure Base de Données

**Migration appliquée** : `add_dnd_character_structure` (24 nov 2025)

**Champs ajoutés à table `heroes`** :
```sql
-- Textes narratifs
voice       TEXT
secret      TEXT  
arc_day1    TEXT
arc_day2    TEXT
arc_day3    TEXT

-- Stats D&D 5e (6 stats principales)
dnd_strength     INTEGER
dnd_dexterity    INTEGER
dnd_constitution INTEGER
dnd_intelligence INTEGER
dnd_wisdom       INTEGER
dnd_charisma     INTEGER

-- Informations personnage D&D
level              INTEGER
race               TEXT
class              TEXT
background         TEXT
personality_traits TEXT[]  -- Array de traits
ideals             TEXT
bonds              TEXT
flaws              TEXT
```

**Nouvelle table `hero_image_variants`** :
```sql
CREATE TABLE hero_image_variants (
  id            TEXT PRIMARY KEY,
  hero_id       TEXT REFERENCES heroes(id),
  base_type     TEXT,        -- 'portrait' ou 'icon'
  resolution    TEXT,        -- 'high' (1024x1024) ou 'low' (256x256)
  emotion       TEXT,        -- 'neutral', 'happy', 'sad', 'angry', 'surprised'
  usage_context TEXT,        -- 'dialogue' ou 'map_icon'
  format        TEXT DEFAULT 'webp',
  url           TEXT,
  width         INTEGER,
  height        INTEGER,
  is_default    BOOLEAN DEFAULT false,
  created_at    TIMESTAMP DEFAULT now()
);
```

### 2. Prisma Schema

**Fichier** : `prisma/schema.prisma`  
**Statut** : ✅ Mis à jour avec tous les nouveaux champs  
**Client généré** : ✅ `npx prisma generate` exécuté avec succès (v5.22.0)

### 3. Documentation Curator

**Fichiers créés** :
- ✅ `docs/curator/workflow-dev-curator.md` - Workflow complet dev ↔ curator
- ✅ `docs/curator/specs/curator-spec-heroes-enrichment.md` - Spécification Sprint 1 complète
- ✅ `docs/curator/specs/README.md` - Index et tracking des specs

**Roadmap mise à jour** :
- ✅ `docs/roadmaps/roadmap-dev-curatorV2.md` - Intégration Supabase MCP

### 4. Contenu Existant en DB

5 héros avec IDs Supabase :

| ID | Slug | Name | Title | Statut Contenu |
|----|------|------|-------|----------------|
| `cfcb7953546ceb3c2cfc2b5a1` | `bjorn` | Bjorn | Bjorn le Vaillant | Placeholders génériques |
| `ce86dd7db8f82ccc9e28e0a1` | `owen` | Owen | Owen le Roublard | Placeholders génériques |
| `c6e8b8834b85c57c86c0e811` | `vi` | Vi | Vi la Sage | Placeholders génériques |
| `c1305ab705fd97dc84cb8f41` | `durun` | Durun | Durun le Robuste | Placeholders génériques |
| `c10dbcf79a1d6a1c95b36c81` | `elira` | Elira | Elira la Diplomate | Placeholders génériques |

---

## 📦 Livrables Attendus (Curator)

### Contenu par Héros (5 personnages)

**Personnage D&D 5e complet** :
- ✅ 6 stats D&D (STR, DEX, CON, INT, WIS, CHA) - Niveau 1
- ✅ Race D&D 5e (Human, Elf, Dwarf, etc.)
- ✅ Classe D&D 5e (Fighter, Rogue, Wizard, etc.)
- ✅ Background D&D 5e (Soldier, Criminal, etc.)
- ✅ Traits de personnalité (2-3 traits)
- ✅ Ideals, Bonds, Flaws

**Textes narratifs** :
- `description` : 150-250 mots (description physique)
- `lore` : 400-600 mots (backstory complète)
- `voice` : 50-100 mots (manière de parler)
- `secret` : 100-150 mots (secret personnel)
- `arc_day1` : 100-150 mots (arc narratif jour 1)
- `arc_day2` : 100-150 mots (arc narratif jour 2)
- `arc_day3` : 100-150 mots (arc narratif jour 3)

**Images** (6 par héros = 30 total) :
- 5 portraits haute résolution (1024x1024, WebP, <500KB)
  - neutral.webp
  - happy.webp
  - sad.webp
  - angry.webp
  - surprised.webp
- 1 icône UI (256x256, WebP, <100KB)

### Format de Livraison

**1. Fichier JSON** : `curator-output-heroes-enrichment-2025-11-24.json`

Structure complète définie dans `curator-spec-heroes-enrichment.md` lignes 155-260.

**2. Assets organisés** : `assets/heroes/`

```
assets/
  heroes/
    bjorn/
      portraits/
        bjorn-portrait-high-neutral.webp
        bjorn-portrait-high-happy.webp
        bjorn-portrait-high-sad.webp
        bjorn-portrait-high-angry.webp
        bjorn-portrait-high-surprised.webp
      icons/
        bjorn-icon-low.webp
    owen/
      ... (même structure)
    vi/
      ... (même structure)
    durun/
      ... (même structure)
    elira/
      ... (même structure)
```

**3. Notes curator (optionnel)** : `curator-notes-heroes-enrichment.md`

---

## 🔧 Outils Disponibles pour Curator

### Accès Base de Données via Supabase MCP

**Project ID** : `hfusvyadhtmviezelabi` (medieval-dispatch-dev)

**Outils MCP disponibles** :
```typescript
// 1. Exécuter requêtes SQL
mcp_supabase_execute_sql({
  project_id: "hfusvyadhtmviezelabi",
  query: "SELECT * FROM heroes ORDER BY slug;"
})

// 2. Lister tables
mcp_supabase_list_tables({
  project_id: "hfusvyadhtmviezelabi",
  schemas: ["public"]
})

// 3. Générer types TypeScript (si besoin)
mcp_supabase_generate_typescript_types({
  project_id: "hfusvyadhtmviezelabi"
})
```

### Exemples Requêtes Utiles

**Lire un héro existant** :
```typescript
mcp_supabase_execute_sql({
  project_id: "hfusvyadhtmviezelabi",
  query: `
    SELECT id, slug, name, title, description, lore,
           strength, diplomacy, stealth, intelligence,
           dnd_strength, race, class
    FROM heroes 
    WHERE slug = 'bjorn';
  `
})
```

**Mettre à jour un héro** :
```typescript
mcp_supabase_execute_sql({
  project_id: "hfusvyadhtmviezelabi",
  query: `
    UPDATE heroes 
    SET 
      description = 'Nouvelle description...',
      lore = 'Nouvelle backstory...',
      voice = 'Voix grave et posée...',
      dnd_strength = 16,
      race = 'Human',
      class = 'Fighter',
      background = 'Soldier',
      personality_traits = ARRAY['Trait 1', 'Trait 2']
    WHERE slug = 'bjorn'
    RETURNING id, slug, name, race, class;
  `
})
```

**Insérer images** :
```typescript
mcp_supabase_execute_sql({
  project_id: "hfusvyadhtmviezelabi",
  query: `
    INSERT INTO hero_image_variants 
    (hero_id, base_type, resolution, emotion, usage_context, url, width, height, format, is_default)
    VALUES 
    ('cfcb7953546ceb3c2cfc2b5a1', 'portrait', 'high', 'neutral', 'dialogue', 
     'https://hfusvyadhtmviezelabi.supabase.co/storage/v1/object/public/hero-portraits/bjorn/portraits/bjorn-portrait-high-neutral.webp', 
     1024, 1024, 'webp', true)
    RETURNING id, hero_id, base_type, emotion;
  `
})
```

### IDs Héros Existants

| Slug | Hero ID | Nom |
|------|---------|-----|
| `bjorn` | `cfcb7953546ceb3c2cfc2b5a1` | Bjorn |
| `owen` | `ce86dd7db8f82ccc9e28e0a1` | Owen |
| `vi` | `c6e8b8834b85c57c86c0e811` | Vi |
| `durun` | `c1305ab705fd97dc84cb8f41` | Durun |
| `elira` | `c10dbcf79a1d6a1c95b36c81` | Elira |

### Upload Supabase Storage

**Bucket à créer** : `hero-portraits` (public)

**Structure URLs** :
```
https://hfusvyadhtmviezelabi.supabase.co/storage/v1/object/public/hero-portraits/
  bjorn/
    portraits/
      bjorn-portrait-high-neutral.webp
      bjorn-portrait-high-happy.webp
      bjorn-portrait-high-sad.webp
      bjorn-portrait-high-angry.webp
      bjorn-portrait-high-surprised.webp
    icons/
      bjorn-icon-low.webp
  owen/
    ... (même structure)
  vi/
  durun/
  elira/
```

---

## 📋 Checklist Validation Pré-Génération

### Structure DB ✅
- [x] Table `heroes` contient champs D&D (vérifier via `list_tables`)
- [x] Table `hero_image_variants` existe
- [x] 5 héros existent avec IDs corrects
- [x] Prisma Client généré avec nouveaux types

### Documentation ✅
- [x] Spec complète `curator-spec-heroes-enrichment.md` (397 lignes)
- [x] Workflow `workflow-dev-curator.md` définit séparation dev/curator
- [x] Format JSON de sortie documenté avec exemple complet

### Outils ✅
- [x] Supabase MCP configuré (execute_sql, apply_migration, list_tables)
- [x] Connexion DB testée et fonctionnelle

---

## 🚀 Prochaines Étapes

### Pour le Curator (Sprint 1)

**Project ID Supabase** : `hfusvyadhtmviezelabi` (medieval-dispatch-dev)

#### Étape 1 : Préparation

1. **Lire la spec** : `docs/curator/specs/curator-spec-heroes-enrichment.md`
2. **Activer outils Supabase MCP** :
   ```typescript
   // Vérifier connexion
   mcp_supabase_execute_sql({
     project_id: "hfusvyadhtmviezelabi",
     query: "SELECT id, slug, name FROM heroes ORDER BY slug;"
   })
   ```

#### Étape 2 : Génération Contenu

3. **Générer contenu D&D** :
   - Créer 5 personnages D&D 5e niveau 1 cohérents
   - Stats appropriées à la classe (Point Buy ou Standard Array)
   - Races/classes/backgrounds variés et intéressants
4. **Écrire textes narratifs** : 7 champs × 5 héros = 35 textes (total ~12,000 mots)
5. **Générer images** : 30 images WebP (portraits + icônes)

#### Étape 3 : Upload Assets (Supabase Storage)

6. **Créer bucket Supabase Storage** :
   ```typescript
   // Via Supabase Dashboard ou API
   // Bucket name: hero-portraits
   // Public: true (pour affichage en jeu)
   // File size limit: 2MB
   ```

7. **Upload images vers Supabase Storage** :
   - Structure : `hero-portraits/bjorn/portraits/bjorn-portrait-high-neutral.webp`
   - Obtenir URLs publiques pour chaque image
   - Format URL : `https://[project].supabase.co/storage/v1/object/public/hero-portraits/bjorn/portraits/...`

#### Étape 4 : Import Direct en Base de Données (via MCP)

8. **UPDATE héros avec textes et stats D&D** :
   ```typescript
   // Pour chaque héro (exemple Bjorn)
   mcp_supabase_execute_sql({
     project_id: "hfusvyadhtmviezelabi",
     query: `
       UPDATE heroes 
       SET 
         description = 'Un guerrier nordique au regard acéré...',
         lore = 'Né dans les terres glacées du nord...',
         voice = 'Bjorn parle d''une voix grave et posée...',
         secret = 'Il cache une blessure ancienne...',
         arc_day1 = 'Au premier jour, Bjorn observe...',
         arc_day2 = 'Le deuxième jour révèle...',
         arc_day3 = 'Au troisième jour, Bjorn doit...',
         dnd_strength = 16,
         dnd_dexterity = 12,
         dnd_constitution = 15,
         dnd_intelligence = 10,
         dnd_wisdom = 13,
         dnd_charisma = 8,
         level = 1,
         race = 'Human',
         class = 'Fighter',
         background = 'Soldier',
         personality_traits = ARRAY['Discipliné', 'Protecteur', 'Direct'],
         ideals = 'La force doit servir à protéger les faibles',
         bonds = 'Je dois protéger mon village natal',
         flaws = 'Je fais confiance trop lentement'
       WHERE slug = 'bjorn';
     `
   })
   
   // Répéter pour owen, vi, durun, elira
   ```

9. **INSERT images dans hero_image_variants** :
   ```typescript
   // Pour chaque image (exemple portraits Bjorn)
   mcp_supabase_execute_sql({
     project_id: "hfusvyadhtmviezelabi",
     query: `
       INSERT INTO hero_image_variants 
       (hero_id, base_type, resolution, emotion, usage_context, url, width, height, format, is_default)
       VALUES 
       ('cfcb7953546ceb3c2cfc2b5a1', 'portrait', 'high', 'neutral', 'dialogue', 
        'https://hfusvyadhtmviezelabi.supabase.co/storage/v1/object/public/hero-portraits/bjorn/portraits/bjorn-portrait-high-neutral.webp', 
        1024, 1024, 'webp', true),
       ('cfcb7953546ceb3c2cfc2b5a1', 'portrait', 'high', 'happy', 'dialogue', 
        'https://hfusvyadhtmviezelabi.supabase.co/storage/v1/object/public/hero-portraits/bjorn/portraits/bjorn-portrait-high-happy.webp', 
        1024, 1024, 'webp', false),
       ('cfcb7953546ceb3c2cfc2b5a1', 'portrait', 'high', 'sad', 'dialogue', 
        'https://hfusvyadhtmviezelabi.supabase.co/storage/v1/object/public/hero-portraits/bjorn/portraits/bjorn-portrait-high-sad.webp', 
        1024, 1024, 'webp', false),
       ('cfcb7953546ceb3c2cfc2b5a1', 'portrait', 'high', 'angry', 'dialogue', 
        'https://hfusvyadhtmviezelabi.supabase.co/storage/v1/object/public/hero-portraits/bjorn/portraits/bjorn-portrait-high-angry.webp', 
        1024, 1024, 'webp', false),
       ('cfcb7953546ceb3c2cfc2b5a1', 'portrait', 'high', 'surprised', 'dialogue', 
        'https://hfusvyadhtmviezelabi.supabase.co/storage/v1/object/public/hero-portraits/bjorn/portraits/bjorn-portrait-high-surprised.webp', 
        1024, 1024, 'webp', false),
       ('cfcb7953546ceb3c2cfc2b5a1', 'icon', 'low', NULL, 'map_icon', 
        'https://hfusvyadhtmviezelabi.supabase.co/storage/v1/object/public/hero-portraits/bjorn/icons/bjorn-icon-low.webp', 
        256, 256, 'webp', false);
     `
   })
   
   // Répéter pour les 4 autres héros (30 images total)
   ```

#### Étape 5 : Validation et Livraison

10. **Vérifier import complet** :
    ```typescript
    // Vérifier textes enrichis
    mcp_supabase_execute_sql({
      project_id: "hfusvyadhtmviezelabi",
      query: `
        SELECT slug, name, race, class, 
               LENGTH(description) as desc_length,
               LENGTH(lore) as lore_length,
               dnd_strength, dnd_dexterity
        FROM heroes 
        WHERE slug IN ('bjorn', 'owen', 'vi', 'durun', 'elira')
        ORDER BY slug;
      `
    })
    
    // Vérifier images importées
    mcp_supabase_execute_sql({
      project_id: "hfusvyadhtmviezelabi",
      query: `
        SELECT h.slug, h.name, 
               COUNT(hiv.id) as image_count,
               COUNT(CASE WHEN hiv.base_type = 'portrait' THEN 1 END) as portraits,
               COUNT(CASE WHEN hiv.base_type = 'icon' THEN 1 END) as icons
        FROM heroes h
        LEFT JOIN hero_image_variants hiv ON h.id = hiv.hero_id
        GROUP BY h.slug, h.name
        ORDER BY h.slug;
      `
    })
    ```

11. **Livrer notes (optionnel)** : 
    - Document `curator-notes-heroes-enrichment.md` avec :
      - Décisions créatives prises (races/classes choisies)
      - Difficultés rencontrées
      - Suggestions pour futurs sprints

**Résumé Livraison** :
- ✅ 5 héros enrichis directement en DB Supabase
- ✅ 30 images uploadées dans Supabase Storage
- ✅ 30 entrées `hero_image_variants` insérées
- ✅ Pas de JSON intermédiaire ni fichiers locaux à transférer

### Pour Dev (Après livraison curator)

**Note** : Le curator livre **directement en DB** via Supabase MCP - pas de JSON/assets locaux à importer.

#### ✅ Phase 1 : Validation Import Curator

1. **Vérifier héros enrichis** :
   ```typescript
   mcp_supabase_execute_sql({
     project_id: "hfusvyadhtmviezelabi",
     query: `
       SELECT slug, name, race, class, background,
              dnd_strength, dnd_dexterity, dnd_constitution,
              LENGTH(description) as desc_len,
              LENGTH(lore) as lore_len,
              LENGTH(voice) as voice_len
       FROM heroes 
       WHERE slug IN ('bjorn', 'owen', 'vi', 'durun', 'elira')
       ORDER BY slug;
     `
   })
   ```

2. **Vérifier images Supabase Storage** :
   - Ouvrir Supabase Dashboard → Storage → `hero-portraits`
   - Vérifier 30 images présentes avec structure correcte
   - Tester URLs publiques dans navigateur

3. **Vérifier hero_image_variants** :
   ```typescript
   mcp_supabase_execute_sql({
     project_id: "hfusvyadhtmviezelabi",
     query: `
       SELECT h.slug, COUNT(*) as image_count
       FROM hero_image_variants hiv
       JOIN heroes h ON h.id = hiv.hero_id
       GROUP BY h.slug
       ORDER BY h.slug;
     `
   })
   // Attendu : 6 images par héro (5 portraits + 1 icône)
   ```

#### 🔧 Phase 2 : Adaptations Code Jeu

**Project ID Supabase** : `hfusvyadhtmviezelabi` (medieval-dispatch-dev)

##### 1. **API `/api/heroes/route.ts` - Support images variants**

**Problème actuel** :
```typescript
// Ligne 16-20
include: {
  images: {
    where: { is_default: true }  // Ancien système hero_images
  }
}

// Ligne 32
src: hero.images[0]?.url || '/portraits/default.png',
```

**Adaptation requise** :
```typescript
include: {
  image_variants: {
    where: {
      base_type: 'portrait',
      resolution: 'high',
      emotion: 'neutral',
      is_default: true
    }
  }
}

// Mapper
src: hero.image_variants[0]?.url || '/portraits/default.png',
```

##### 2. **`DialogueModal.tsx` - Portraits émotionnels dynamiques**

**Problème actuel** :
```typescript
// Ligne 12-18 : Mapping statique
const HERO_PORTRAITS: { [key: string]: string } = {
  'bjorn': '/portraits/bjorn.png',
  'owen': '/portraits/owen.png',
  // ...
}
```

**Adaptation requise** :
- Supprimer mapping statique
- Récupérer `hero.image_variants` depuis GameContext
- Fonction helper pour sélectionner portrait selon `exchange.emotion`
```typescript
const getHeroPortrait = (heroSlug: string, emotion?: string) => {
  const hero = gameState.heroes.find(h => h.id === heroSlug)
  const variant = hero?.image_variants?.find(v => 
    v.base_type === 'portrait' && 
    v.resolution === 'high' && 
    v.emotion === (emotion || 'neutral')
  )
  return variant?.url || '/portraits/default.png'
}
```

##### 3. **`HeroStatsModal.tsx` - Stats depuis DB**

**Problème actuel** :
```typescript
// Ligne 11-16 : Stats hardcodées
const HERO_STATS: Record<string, { force: number, ... }> = {
  'Bjorn': { force: 18, dexterite: 12, ... },
  // ...
}
```

**Adaptation requise** :
- Supprimer constante `HERO_STATS`
- Lire `hero.stats` depuis props (via GameContext)
- Ajouter affichage stats D&D 5e :
```typescript
// Afficher stats mécaniques jeu
<div>Force: {hero.stats.force}</div>

// NOUVEAU : Afficher stats D&D
<div style={{ marginTop: '20px', borderTop: '1px solid #444', paddingTop: '15px' }}>
  <h4>⚔️ Statistiques D&D 5e</h4>
  <div>STR: {hero.dnd_strength}</div>
  <div>DEX: {hero.dnd_dexterity}</div>
  <div>CON: {hero.dnd_constitution}</div>
  <div>INT: {hero.dnd_intelligence}</div>
  <div>WIS: {hero.dnd_wisdom}</div>
  <div>CHA: {hero.dnd_charisma}</div>
</div>
```

##### 4. **Nouveaux Composants à Créer**

###### `HeroLoreModal.tsx` (NOUVEAU)
- Afficher `description`, `lore`, `voice`, `secret`
- Afficher `race`, `class`, `background`
- Afficher `personality_traits[]`, `ideals`, `bonds`, `flaws`
- Portrait neutre haute résolution
- Bouton pour ouvrir depuis Village/Hero Select

###### `HeroArcDisplay.tsx` (NOUVEAU)  
- Afficher `arc_day1`, `arc_day2`, `arc_day3` selon jour actuel
- Texte narratif contextualisé
- Intégration dans VillageModal ou dialogue d'introduction jour

##### 5. **Types TypeScript - Étendre interfaces**

**Fichier** : `app/types/game.ts`

```typescript
// Ajouter à Hero interface
export interface Hero {
  id: string
  name: string
  src: string
  alt: string
  color: string
  stats: HeroStats
  isAvailable: boolean
  currentMissionId?: string
  
  // NOUVEAUX champs D&D
  dnd_strength?: number
  dnd_dexterity?: number
  dnd_constitution?: number
  dnd_intelligence?: number
  dnd_wisdom?: number
  dnd_charisma?: number
  level?: number
  race?: string
  class?: string
  background?: string
  personality_traits?: string[]
  ideals?: string
  bonds?: string
  flaws?: string
  
  // NOUVEAUX champs narratifs
  voice?: string
  secret?: string
  arc_day1?: string
  arc_day2?: string
  arc_day3?: string
  
  // NOUVEAUX champs images
  image_variants?: HeroImageVariant[]
}

// NOUVELLE interface
export interface HeroImageVariant {
  id: string
  hero_id: string
  base_type: 'portrait' | 'icon'
  resolution: 'high' | 'low'
  emotion?: 'neutral' | 'happy' | 'sad' | 'angry' | 'surprised'
  usage_context: string
  url: string
  width: number
  height: number
  format: string
  is_default: boolean
}
```

##### 6. **GameContext - Chargement complet héros**

**Fichier** : `app/contexts/GameContext.tsx`

Adapter ligne ~588 pour inclure tous les nouveaux champs lors du chargement sauvegarde :
```typescript
heroes: save.player_heroes.map((ph: any) => ({
  id: ph.hero.slug,
  name: ph.hero.name,
  src: ph.hero.image_variants?.find((v: any) => 
    v.base_type === 'portrait' && v.emotion === 'neutral'
  )?.url || '/portraits/default.png',
  alt: ph.hero.name,
  color: '#ff4444',
  stats: { /* stats mécaniques */ },
  isAvailable: !ph.is_on_mission,
  
  // NOUVEAUX champs
  dnd_strength: ph.hero.dnd_strength,
  dnd_dexterity: ph.hero.dnd_dexterity,
  dnd_constitution: ph.hero.dnd_constitution,
  dnd_intelligence: ph.hero.dnd_intelligence,
  dnd_wisdom: ph.hero.dnd_wisdom,
  dnd_charisma: ph.hero.dnd_charisma,
  level: ph.hero.level,
  race: ph.hero.race,
  class: ph.hero.class,
  background: ph.hero.background,
  personality_traits: ph.hero.personality_traits,
  ideals: ph.hero.ideals,
  bonds: ph.hero.bonds,
  flaws: ph.hero.flaws,
  voice: ph.hero.voice,
  secret: ph.hero.secret,
  arc_day1: ph.hero.arc_day1,
  arc_day2: ph.hero.arc_day2,
  arc_day3: ph.hero.arc_day3,
  image_variants: ph.hero.image_variants
}))
```

#### 🧪 Phase 3 : Tests & Validation

1. **Affichage portraits** : Dialogues avec émotions correctes
2. **Stats D&D** : Visibles dans HeroStatsModal
3. **Lore/Voice/Secret** : Accessibles via nouveau modal
4. **Arcs narratifs** : Affichage selon jour actuel
5. **Images variants** : 30 images chargées, URLs valides
6. **Cohérence narrative** : Textes enrichis cohérents avec gameplay

#### 🐛 Feedback

Si problèmes **techniques uniquement** (JSON invalide, images manquantes, champs DB incorrects)

---

## 📊 Métriques Sprint 1

| Métrique | Quantité |
|----------|----------|
| Personnages D&D complets | 5 |
| Champs DB par héro | 21 (7 textes + 14 D&D) |
| Mots textuels (estimation) | ~12,000 |
| Images générées | 30 (25 portraits + 5 icônes) |
| Taille assets totale (estimation) | ~10-12 MB |
| Entrées DB hero_image_variants | 30 |

---

## 📞 Contact & Support

**Questions techniques DB** : Consulter utilisez mcp supabase
**Questions workflow** : Consulter `docs/curator/workflow-dev-curator.md`  
**Questions format** : Consulter `curator-spec-heroes-enrichment.md` sections 📤 et ✅

---

**Statut final** : ✅ PRÊT - Infrastructure complète, documentation exhaustive, outils configurés. Le curator peut démarrer la génération dès maintenant.

**Date limite suggérée Sprint 1** : 1er décembre 2025 (1 semaine)
