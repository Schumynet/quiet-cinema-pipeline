# 🎬 Quiet Cinema - AI Surreal Music Film Pipeline

Pipeline completa per generare **filmati AI surreali** nello stile di [oltsevart](https://youtube.com/@oltsevart)

## 📊 Analisi Competitor (oltsevart)

| Aspetto | Dettaglio |
|---------|-----------|
| **Tipo contenuto** | Surreal AI Music Films (4K) |
| **Formato** | Short film 2-5 minuti |
| **Stile** | Surreale, emozionale, onirico |
| **Musica** | AI-generated, evocativa, emotiva |
| **Titoli** | "A Very Unusual Town", "Where...", "The..." |
| **Visual** | Immagini/video AI cinematografici |

### Titoli Popolari (per ispirazione)
- "You Didn't Know It Was the Last Time..." (210K views)
- "If We Had Never Gone to War..." (8.9K views)
- "The Forest Village Where Time Has Always Moved This Slow" (14K views)

---

## 🚀 Pipeline Overview

```
1. Genera TITOLO/SCRIPT (ispirato al competitor)
     ↓
2. Genera MUSICA (ACE-Step 1.5 o HeartMuLa)
     ↓
3. Genera IMMAGINI (CogView/FLUX/fal.ai)
     ↓
4. Genera VIDEO CLIPS (CogVideoX o Ken Burns)
     ↓
5. Assembla con FFmpeg
     ↓
6. Aggiungi audio + export finale
     ↓
7. Crea Thumbnail
```

---

## 📁 Struttura File

```
quiet-cinema-pipeline/
├── Quiet_Cinema_Pipeline.ipynb  ← Notebook Jupyter per RunPod
├── generate_film.py             ← Script Python standalone
├── README.md                    ← Questa guida
└── requirements.txt             ← Dipendenze Python
```

---

## 🖥️ Setup su RunPod

### 1. Avvia il Pod
- Vai su https://www.runpod.io/console/pods
- Avvia **principal_turquoise_elk**

### 2. Apri Jupyter Lab
- Click su "Jupyter Lab" nella console del Pod
- Oppure usa il Web Terminal

### 3. Carica i file
```bash
# Clona il repository con i file
git clone https://github.com/Schumynet/quiet-cinema-pipeline.git
cd quiet-cinema-pipeline

# Oppure carica manualmente:
# - Quiet_Cinema_Pipeline.ipynb
# - generate_film.py
```

### 4. Installa dipendenze
```bash
pip install fal python-dotenv Pillow
```

---

## 🎮 Uso del Notebook

### Apri `Quiet_Cinema_Pipeline.ipynb` e esegui in ordine:

| Step | Titolo | Funzione |
|------|--------|----------|
| 1 | Setup & Installazioni | Verifica GPU, crea cartelle |
| 2 | Genera Script & Titoli | Crea titolo + script poetico |
| 3a | Installa ACE-Step | Setup generatore musica |
| 3b | Genera Musica | Crea traccia audio |
| 4a | Genera Immagini | Crea scene con CogView |
| 4b | Genera Video | Crea clip con CogVideoX |
| 5 | Assembla Video | Merge con FFmpeg |
| 6 | Aggiungi Audio | Combina video + musica |
| 7 | Merge Finale | Video finale con transizioni |
| 8 | Genera Thumbnail | Crea thumbnail YouTube |

---

## 🎵 Strumenti di Generazione

### Musica
| Strumento | Vantaggi | Link |
|-----------|----------|------|
| **ACE-Step 1.5** | Alta qualità, 50+ lingue | [GitHub](https://github.com/ACE-Step/ACE-Step-1.5) |
| **HeartMuLa 3B** | Open source, gratuito | [Colab](https://github.com/TeamAIQ/Colab-notebooks) |
| **Suno API** | Altissima qualità | Usa `$suno_api` dalle config |

### Immagini
| Strumento | Vantaggi | API |
|-----------|----------|-----|
| **CogView** | Alta qualità, veloce | `$fal_api` |
| **FLUX** | Realistico, dettagliato | `$fal_api` |
| **DALL-E** | OpenAI | `$openai_api` |

### Video
| Strumento | Vantaggi | API |
|-----------|----------|-----|
| **CogVideoX-3** | 5 secondi, alta qualità | `$fal_api` |
| **LTX-Video** | 10 secondi | Kaggle notebook |
| **Sora** | OpenAI (quando disponibile) | `$openai_api` |

---

## 📝 Template SEO per YouTube

### Titolo (stile oltsevart)
```
{soggetto} | {dettaglio_unico} | Surreal AI Film (4K)
```

### Descrizione
```
🎬 {titolo}

In a place where the unusual becomes ordinary...

━━━━━━━━━━━━━━━━━━━━━━━━
⏱️ TIMESTAMPS
00:00 - Introduction
00:30 - Scene 1
01:00 - Scene 2
...

━━━━━━━━━━━━━━━━━━━━━━━━
📚 LINKS
🎵 Music generated with ACE-Step 1.5
🎨 Images created with AI
...

━━━━━━━━━━━━━━━━━━━━━━━━
#Surreal #AIFilm #Dreamy #Cinematic #AIArt
```

### Tags
```
surreal, ai art, music film, dreamlike, cinematic, ai generated,
short film, atmospheric, mysterious, peaceful, otherworldly,
4k, film, art, fantasy, poetic
```

---

## 🔧 Configurazione API Keys

Il notebook usa le API keys dalla configurazione. Assicurati di avere:

```python
import os
os.environ["fal_api"] = "your-fal-api-key"
os.environ["openai_api"] = "your-openai-api-key"
# ecc.
```

Oppure crea un file `.env`:
```
FAL_API=your-key
OPENAI_API=your-key
```

---

## 🎨 Stile Visual (Consigli)

### Palette Colori
- **Primari**: Toni caldi (arancione, oro, ambra)
- **Secondari**: Blu notte, viola, verde smeraldo
- **Accenti**: Rosa pallido, bianco latte

### Elementi Ricorrenti
- Nebbia/s foschia
- Edifici antichi/impossibili
- Luce dorata del tramonto
- Strade vuote, paesaggi onirici
- Animali simbolici (pecore, uccelli)

### Movimento Camera
- Pan lenti e fluidi
- Dolly in avanti/indietro
- Orbite attorno a soggetti
- Zoom dolci (Ken Burns)

---

## 📊 Metriche Successo (riferimento oltsevart)

| Video | Views | Pattern |
|-------|-------|---------|
| Best performer | 210K | Emozionale, nostalgico |
| Media | 2-5K | Consistente |
| Worst | 500 | Pubblicato di recente |

---

## 🚨 Troubleshooting

### Pod non risponde
1. Verifica che il Pod sia attivo nella console RunPod
2. Riavvia il Pod se necessario
3. Controlla i logs per errori

### Out of Memory (OOM)
- Riduci il numero di immagini/video
- Usa immagini più piccole
- Chiudi altre applicazioni

### Generazione lenta
- Usa GPU T4 o superiore
- Batch processing quando possibile
- Salta step non necessari

---

## 📜 Licenza

MIT License - Libero uso commerciale per contenuti YouTube

---

## 🎬 Esempi Output

### Titolo Generato
```
A Very Unusual Town | Where Time Has Always Moved This Slow | Surreal AI Film (4K)
```

### Script Esempio
```
The streets remember what we forgot
Buildings breathe with secrets untold
Every corner holds a memory
Every window reflects a dream

This is where the unusual lives
Where the extraordinary finds its home
Come stay as long as you need
In this town we call our own
```

---

*Pipeline creata per Quiet Cinema*
*Basata sullo stile di oltsevart*
*2025*