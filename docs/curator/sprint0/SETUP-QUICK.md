# 🚀 Setup Rapide Curator - GTX 1660 Super

**GPU** : NVIDIA GeForce GTX 1660 Super (6GB VRAM)  
**Date** : 24 novembre 2025

---

## 📦 Installation

### 1. Créer environnement Python

```powershell
# Créer dossier projet
cd c:\Users\BOTTEROOOW\dispatchgenerator
mkdir curator-backend
cd curator-backend

# Créer environnement virtuel
python -m venv venv

# Activer
.\venv\Scripts\Activate.ps1

# Installer dépendances de base
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate bitsandbytes
pip install diffusers pillow safetensors
```

---

## 🧠 Télécharger Mistral 7B Instruct (4-bit)

```powershell
# Installer huggingface-cli
pip install huggingface-hub

# Se connecter (optionnel, mais recommandé)
huggingface-cli login

# Télécharger modèle quantifié 4-bit
huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GPTQ --local-dir ./models/mistral-7b-instruct-gptq
```

**Alternative si GPTQ pose problème** :
```powershell
# Télécharger version GGUF (plus simple)
huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF --local-dir ./models/mistral-7b-instruct-gguf --include "*Q4_K_M.gguf"
```

---

## 🎨 Télécharger Stable Diffusion 1.5 + RPG v4

```powershell
# SD 1.5 base (sera téléchargé automatiquement par diffusers)
# Pas besoin de téléchargement manuel

# LoRA RPG v4
huggingface-cli download Anashel/rpg-v4 --local-dir ./models/loras/rpg-v4
```

---

## ✅ Vérifier Installation GPU

```powershell
python -c "import torch; print(f'CUDA disponible: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"None\"}')"
```

**Résultat attendu** :
```
CUDA disponible: True
GPU: NVIDIA GeForce GTX 1660 SUPER
```

---

## 📝 Prochaine étape

Une fois l'installation terminée, on créera les scripts de test simples pour valider les modèles.
