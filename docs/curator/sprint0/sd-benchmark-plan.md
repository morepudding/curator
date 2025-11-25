# 🎨 Plan de Benchmarking Stable Diffusion - Sprint 0.2

**Date** : 24 novembre 2025  
**Objectif** : Sélectionner le meilleur modèle de génération d'images pour Medieval Dispatch

---

## 🎯 Critères d'Évaluation

### Performance Technique
- **VRAM requise** : Compatible GPU 8-16GB
- **Vitesse génération** : < 30s par image 1024x1024
- **Batch capability** : 5 images en < 5 minutes

### Qualité Visuelle
- **Style médiéval-fantastique** : Cohérence avec univers D&D
- **Cohérence inter-personnages** : Tous les héros du même univers
- **Variations émotionnelles** : Img2Img préserve identité
- **Détails** : Qualité suffisante pour portraits dialogue

---

## 📋 Modèles Candidats

### 1. Stable Diffusion 1.5
- **Base** : SD 1.5 (1024x1024)
- **LoRAs à tester** :
  - RPG v4 (fantasy characters)
  - Medieval Fantasy LoRA
  - Portrait Plus (détails visage)
- **Avantages** : Léger, rapide, stable
- **VRAM** : 6-8GB

### 2. SDXL (Stable Diffusion XL)
- **Base** : SDXL 1.0
- **Avantages** : Meilleure qualité, plus de détails
- **Inconvénients** : Plus lourd, plus lent
- **VRAM** : 10-16GB

### 3. DreamShaper
- **Base** : Checkpoint communautaire
- **Version** : DreamShaper 8
- **Avantages** : Style artistique cohérent
- **VRAM** : 8-10GB

### 4. RPG v4
- **Base** : Checkpoint spécialisé fantasy
- **Avantages** : Optimisé personnages D&D
- **VRAM** : 8-10GB

---

## 🧪 Batteries de Tests

### Test 1 : Styles Visuels Globaux

**Objectif** : Déterminer quel style artistique convient le mieux.

#### Test 1A : Style Cartoon
**Prompt** :
```
cartoon style medieval fantasy portrait, male human fighter, 
brown hair, blue eyes, leather armor, friendly expression,
vibrant colors, clean lines, stylized features
```

**Paramètres** :
- Steps: 30
- CFG Scale: 7
- Sampler: DPM++ 2M Karras
- Resolution: 1024x1024

#### Test 1B : Style Semi-Réaliste
**Prompt** :
```
semi-realistic medieval fantasy portrait, male human fighter,
brown hair, blue eyes, leather armor, friendly expression,
dramatic lighting, painterly style, detailed textures
```

#### Test 1C : Style Animé
**Prompt** :
```
anime style medieval fantasy portrait, male human fighter,
brown hair, blue eyes, leather armor, friendly expression,
soft colors, cel-shaded, manga aesthetic
```

#### Test 1D : Style Comics
**Prompt** :
```
comic book style medieval fantasy portrait, male human fighter,
brown hair, blue eyes, leather armor, friendly expression,
bold outlines, cell-shading, dynamic composition
```

**Critères validation** :
- [ ] Cohérence style avec univers médiéval-fantastique
- [ ] Qualité détails (visage, armure)
- [ ] Rendu professionnel
- [ ] Note style (0-10)

---

### Test 2 : Portrait de Base (Neutral)

**Objectif** : Générer portrait haute qualité d'un héros.

**Personnage Test** : Bjorn (Human Fighter)

**Prompt** :
```
[STYLE_CHOISI] medieval fantasy portrait, mature male human fighter,
rugged features, short brown hair, stern expression (neutral emotion),
leather armor with metal pauldrons, battle-worn, 
portrait composition, detailed face, high quality,
warm lighting, medieval background
```

**Negative Prompt** :
```
deformed, blurry, bad anatomy, disfigured, poorly drawn face,
mutation, extra limbs, ugly, poorly drawn hands, missing fingers,
low quality, watermark, signature
```

**Paramètres** :
- Seed: 123456 (fixe pour comparaisons)
- Steps: 40
- CFG Scale: 7.5
- Resolution: 1024x1024

**Critères validation** :
- [ ] Qualité globale (0-10)
- [ ] Détails visage (0-10)
- [ ] Cohérence avec description
- [ ] Temps génération (secondes)

---

### Test 3 : Variations Émotionnelles (Img2Img)

**Objectif** : Vérifier capacité à générer 5 émotions en préservant identité.

**Base** : Portrait neutral du Test 2

#### Test 3A : Happy
**Prompt** :
```
[Prompt Test 2 avec] happy smile, joyful expression, slight grin
```
- Denoising strength: 0.4
- Même seed

#### Test 3B : Sad
**Prompt** :
```
[Prompt Test 2 avec] sad expression, downcast eyes, melancholic
```

#### Test 3C : Angry
**Prompt** :
```
[Prompt Test 2 avec] angry scowl, furrowed brow, intense glare
```

#### Test 3D : Surprised
**Prompt** :
```
[Prompt Test 2 avec] surprised expression, wide eyes, raised eyebrows
```

**Critères validation** :
- [ ] Identité préservée (même personne ?)
- [ ] Émotion claire et lisible
- [ ] Qualité maintenue
- [ ] Temps génération batch (5 émotions)

---

### Test 4 : Cohérence Inter-Personnages

**Objectif** : Vérifier que 3 héros différents appartiennent au même univers.

**Personnages** :
1. **Bjorn** (Human Fighter) - Male, rugged, warrior
2. **Elira** (Elf Cleric) - Female, elegant, priest robes
3. **Durun** (Dwarf Blacksmith) - Male, stocky, craftsman

**Prompts** :
```
Bjorn: [STYLE] medieval fantasy portrait, male human fighter, 
       rugged features, brown hair, leather armor

Elira: [STYLE] medieval fantasy portrait, female elf cleric,
       elegant features, blonde hair, white priest robes

Durun: [STYLE] medieval fantasy portrait, male dwarf blacksmith,
       stocky build, red beard, leather apron
```

**Critères validation** :
- [ ] Style visuel cohérent entre 3 personnages
- [ ] Même univers artistique
- [ ] Mêmes conventions (lighting, rendering)
- [ ] Note cohérence (0-10)

---

### Test 5 : Icônes (Downscaling)

**Objectif** : Vérifier qualité après resize 1024x1024 → 256x256.

**Process** :
1. Prendre portrait neutral Test 2
2. Resize intelligent (Lanczos/Bicubic)
3. Conversion WebP qualité 85
4. Vérifier poids < 100KB

**Critères validation** :
- [ ] Lisibilité à 256x256
- [ ] Détails préservés
- [ ] Poids fichier < 100KB
- [ ] Qualité visuelle icône (0-10)

---

### Test 6 : Paysages (Locations)

**Objectif** : Tester génération illustrations locations.

#### Test 6A : Forêt Mystérieuse
**Prompt** :
```
[STYLE] mysterious medieval forest, ancient trees, misty atmosphere,
dappled sunlight, fantasy landscape, atmospheric, detailed foliage
```

#### Test 6B : Caverne Sombre
**Prompt** :
```
[STYLE] dark medieval cave entrance, rocky formations, ominous shadows,
torchlight glow, fantasy environment, atmospheric depth
```

**Critères validation** :
- [ ] Qualité paysage
- [ ] Atmosphère appropriée
- [ ] Cohérence style avec portraits
- [ ] Temps génération

---

### Test 7 : Intérieurs (Buildings)

**Objectif** : Tester génération illustrations bâtiments.

**Prompt Taverne** :
```
[STYLE] medieval tavern interior, wooden tables and chairs,
fireplace glow, ale barrels, warm atmosphere, cozy lighting,
fantasy interior, detailed environment
```

**Critères validation** :
- [ ] Qualité illustration
- [ ] Ambiance cohérente
- [ ] Détails architecture

---

### Test 8 : Batch Processing Performance

**Objectif** : Mesurer temps génération batch.

**Test** : Générer 1 héros complet (6 images)
- 1 portrait neutral 1024x1024
- 4 variations émotionnelles (Img2Img)
- 1 icône 256x256

**Critères** :
- [ ] Temps total batch < 5 minutes
- [ ] VRAM stable (pas de crash)
- [ ] Qualité maintenue sur toutes images

---

### Test 9 : Optimisation WebP

**Objectif** : Vérifier compression sans perte qualité.

**Process** :
1. Image PNG 1024x1024 (2-3 MB)
2. Conversion WebP qualité 85
3. Conversion WebP qualité 90
4. Comparaison visuelle

**Critères** :
- [ ] WebP Q85 : < 500KB
- [ ] WebP Q90 : < 700KB
- [ ] Différence qualité acceptable
- [ ] Note qualité compression (0-10)

---

### Test 10 : Seeds & Reproductibilité

**Objectif** : Vérifier reproductibilité génération.

**Test** :
1. Générer image avec seed fixe (123456)
2. Régénérer avec même seed + prompt
3. Comparer résultats

**Critères** :
- [ ] Images identiques (ou quasi)
- [ ] Reproductibilité fiable

---

## 📊 Grille de Notation

| Critère | Poids | Note (0-10) | Score |
|---------|-------|-------------|-------|
| **Qualité portraits** | 30% | | |
| **Cohérence visuelle globale** | 20% | | |
| **Variations émotionnelles** | 15% | | |
| **Vitesse génération** | 15% | | |
| **VRAM requise** | 10% | | |
| **Qualité paysages/intérieurs** | 10% | | |
| **TOTAL** | 100% | | **/100** |

---

## 📈 Tableau Comparatif (à remplir)

| Modèle | VRAM | Vitesse (1 image) | Qualité | Cohérence | Score Total |
|--------|------|------------------|---------|-----------|-------------|
| **SD 1.5 + RPG LoRA** | | | | | |
| **SD 1.5 + Medieval LoRA** | | | | | |
| **SDXL Base** | | | | | |
| **DreamShaper 8** | | | | | |
| **RPG v4** | | | | | |

---

## ✅ Décision Finale

**Checkpoint sélectionné** : [À remplir]

**LoRAs utilisés** : [À remplir]

**Configuration** :
- **Style recommandé** : [Cartoon / Semi-réaliste / Animé / Comics]
- **Steps** : [30-50]
- **CFG Scale** : [7-8]
- **Sampler** : [DPM++ 2M Karras / Euler a]
- **Denoising strength (Img2Img)** : [0.3-0.5]

**Prompts Master** :

### Portrait Hero (Neutral)
```
[À définir selon style choisi]
```

### Variations Émotionnelles (Img2Img)
```
Happy: [prompt additions]
Sad: [prompt additions]
Angry: [prompt additions]
Surprised: [prompt additions]
```

### Location Landscape
```
[À définir]
```

### Building Interior
```
[À définir]
```

**Justification** : [À remplir après benchmarks]

---

## 📝 Prochaines Étapes

1. Exécuter les 10 tests pour chaque checkpoint
2. Remplir grille de notation
3. Comparer résultats visuels côte à côte
4. Créer `model-selection-stable-diffusion.md` avec décision finale
5. Exporter prompts master optimisés
6. Créer galerie exemples visuels pour référence équipe
