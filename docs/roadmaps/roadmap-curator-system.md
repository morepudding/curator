# 🗺️ Roadmap : Développement du Système Curator IA

**Objectif** : Construire l'application autonome "Curator" permettant de générer, affiner et valider le contenu du jeu via IA, en séparant clairement la logique de génération (Backend Python) de l'interface de validation (Frontend Next.js).

---

## 📅 Sprint 1 : Architecture & Sélection des Modèles IA
**Focus** : Recherche, Benchmarking et Choix Technologiques pour le moteur de génération.

### 🧠 Sélection Modèle Langage (LLM)
- **Évaluation OpenLLaMA** : Comparatif des versions (3B, 7B, 13B) pour trouver le meilleur ratio qualité/vitesse en local.
- **Tests de Quantization** : Validation des modèles quantifiés (4-bit vs 8-bit) pour tourner sur du matériel standard.
- **Prompt Engineering** : Tests de capacité à générer du JSON structuré strict et du texte narratif créatif (Lore, Dialogues).
- **Choix Final** : Sélection du modèle définitif et configuration des hyperparamètres (température, top_p).

### 🎨 Sélection Modèle Image (Stable Diffusion)
- **Comparatif Modèles** : Tests entre SD 1.5, SDXL et modèles spécialisés (ex: RPG v4, DreamShaper) pour le style médiéval-fantastique.
- **Direction Artistique** : Définition des prompts "maîtres" pour garantir une cohérence visuelle entre les assets.
- **Optimisation** : Mesure des temps de génération et de l'usage VRAM pour le batch processing.
- **Choix Final** : Sélection du checkpoint principal et des LoRAs pour les variations d'émotions.

### 🏗️ Architecture Technique
- **Stack** : Validation de l'architecture hybride (Next.js Frontend + Python Backend).
- **Contrats d'Interface** : Définition des endpoints API pour la communication entre le front et le back.

---

## 📅 Sprint 2 : Backend Python & Moteurs de Génération
**Focus** : Création du "Cerveau" du système et des services API.

### 🐍 Service Backend Python
- **Environnement** : Setup de l'environnement Python isolé avec gestion des dépendances (Torch, Transformers, Diffusers).
- **API Server** : Création du serveur API (FastAPI ou Flask) pour exposer les fonctionnalités IA au frontend.
- **Gestion de File d'Attente** : Implémentation d'un système de queue pour gérer les générations longues sans bloquer l'interface.

### ⚙️ Moteurs d'Inférence
- **Service Texte** : Wrapper autour du LLM pour générer descriptions, dialogues et stats D&D à la demande.
- **Service Image** : Pipeline de génération d'images (Text-to-Image pour la base, Img-to-Img pour les variations).
- **Post-Processing** : Scripts automatiques de redimensionnement, conversion WebP et validation de poids des fichiers.

---

## 📅 Sprint 3 : Interface de Curation Multi-Niveaux (Next.js)
**Focus** : Création de l'interface utilisateur pour le workflow humain.

### 🖥️ Frontend Next.js 14
- **Setup Projet** : Initialisation Next.js avec App Router et librairie de composants UI.
- **Module d'Import** : Interface de drag-and-drop pour charger et parser les fichiers de spécification Markdown (`.md`).

### 🎚️ Interface de Curation (Workflow)
- **Niveau 1 (Configuration)** : Écran de paramétrage global (Style visuel, Ton narratif, Contraintes).
- **Niveau 2 (Génération)** : Dashboard de lancement des tâches et suivi de progression.
- **Niveau 3 (Enrichissement & Édition)** :
    - **Éditeur Narratif** : Interface pour relire et modifier les textes générés (Lore, Secrets).
    - **Sélecteur Visuel** : Galerie pour choisir les meilleures variations de portraits ou régénérer une image spécifique.
- **Niveau 4 (Validation)** : Vue synthétique de validation finale avant export.

---

## 📅 Sprint 4 : Intégration & Fonctionnalités Avancées
**Focus** : Pipeline complet, automatisation et connexion au jeu.

### 🔄 Pipeline de Données
- **Export JSON** : Générateur de fichier JSON final strictement conforme au schéma du jeu.
- **Organisation Assets** : Système de tri automatique des images générées dans l'arborescence du projet (`assets/heroes/...`).

### 🚀 Fonctionnalités Avancées
- **Mode Batch** : Capacité à traiter une liste complète de héros (ex: 5 à la fois) en arrière-plan.
- **Preview Temps Réel** : Composants UI simulant l'affichage dans le jeu (ex: fausse fenêtre de dialogue) pour valider le rendu.
- **Connecteur Supabase** : Intégration optionnelle pour pousser directement les résultats validés en base de données.

---

## 🎯 Livrable Final
Une application "Curator Studio" locale, permettant de transformer une simple spec technique en contenu de jeu riche, validé et formaté, prête à être utilisée par l'équipe de développement.
