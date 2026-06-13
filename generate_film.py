#!/usr/bin/env python3
"""
Quiet Cinema - AI Surreal Music Film Generator
Pipeline completa basata sullo stile di oltsevart
"""

import os
import random
import subprocess
import json
from datetime import datetime

# Configurazione
WORK_DIR = "/workspace/quiet-cinema"
os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(f"{WORK_DIR}/scripts", exist_ok=True)
os.makedirs(f"{WORK_DIR}/music", exist_ok=True)
os.makedirs(f"{WORK_DIR}/images", exist_ok=True)
os.makedirs(f"{WORK_DIR}/video", exist_ok=True)
os.makedirs(f"{WORK_DIR}/final", exist_ok=True)

# Template titoli (stile oltsevart)
TITOLI_TEMPLATE = [
    "A Very Unusual Town | {soggetto}",
    "Where {azione} | Surreal AI Film",
    "The {luogo} Where {dettaglio}",
    "{emozione} That {conseguenza} | Surreal AI Film",
    "Someone Still {azione}... | AI Music Film",
]

SOGGETTI = [
    "the Old Ones Begin Again",
    "the Sheep Stopped Here",
    "Time Has Always Moved This Slow",
    "the Clay Has Never Gone Cold",
    "Extinct Animals Still Come Home",
    "Time Forgot to Change",
    "Every Generation Plants the Same Garden",
    "the Fishing Village That Time Forgot",
]

# Prompts immagini (surreali, onirici)
IMAGE_PROMPTS = [
    "Surreal small town at twilight, mysterious fog, golden light, ancient buildings, magical atmosphere, cinematic, 4K, photorealistic",
    "Dreamlike village square, impossible architecture, soft colors, ethereal glow, peaceful atmosphere, cinematic photography",
    "Unusual town street, surreal perspective, warm lighting, mysterious shadows, nostalgic mood, film grain, 4K",
    "Magical forest village, bioluminescent plants, peaceful clearing, otherworldly light rays, fantasy art style",
    "Surreal lighthouse on the edge of reality, infinite ocean, stars reflecting in water, melancholic beauty, cinematic"
]

# Prompts video
VIDEO_PROMPTS = [
    "Slow pan through surreal town, golden hour light, dreamy atmosphere, cinematic movement",
    "Floating camera through magical village, soft focus, ethereal particles, peaceful",
    "Drifting through mysterious streets, shadows moving, lights flickering, contemplative mood",
    "Orbiting around unusual building, impossible architecture, warm ambient lighting",
    "Slow zoom into magical clearing, forest elements, mystical atmosphere, serene"
]


def genera_titolo():
    """Genera un titolo nello stile oltsevart"""
    template = random.choice(TITOLI_TEMPLATE)
    soggetto = random.choice(SOGGETTI)
    return template.format(
        soggetto=soggetto,
        azione="Plants Gardens",
        luogo="Town",
        dettaglio=soggetto,
        emozione="That Summer Night",
        conseguenza="Nobody Noticed"
    )


def genera_script(titolo):
    """Genera uno script poetico"""
    return f"""
{titolo}

[Intro - Atmospheric Music]

In a place where shadows hold conversations
And time moves like honey through the air,
There exists a story waiting to be told.

[Verse 1]
The streets remember what we forgot
Buildings breathe with secrets untold
Every corner holds a memory
Every window reflects a dream

[Chorus]
This is where the unusual lives
Where the extraordinary finds its home
Come stay as long as you need
In this town we call our own

[Verse 2]
The moon here shines a different color
The stars tell stories in a new language
If you listen closely at midnight
You'll hear the town singing its song

[Outro - Fade]
Welcome to the unusual...
"""


def genera_musica_ace(fal_api_key=None):
    """Genera musica con ACE-Step 1.5"""
    print("🎵 Generando musica con ACE-Step...")
    
    music_prompt = """
    atmospheric, ethereal, surreal, ambient, cinematic, dreamy, melancholic, 
    soft piano, strings, pads, reverb, spacey, emotional, film score, 
    meditative, peaceful, mysterious, otherworldly, floating
    """
    
    # Se hai ACE-Step installato
    if os.path.exists("/workspace/ACE-Step-1.5"):
        os.chdir("/workspace/ACE-Step-1.5")
        cmd = f"~/.local/bin/uv run python -m acestep.generate --prompt '{music_prompt}' --duration 180 --output {WORK_DIR}/music/generated_music.wav"
        subprocess.run(cmd, shell=True)
        return f"{WORK_DIR}/music/generated_music.wav"
    
    # Altrimenti genera con fal.ai se disponibile
    if fal_api_key:
        try:
            import fal
            result = fal.run("fal-ai/acestep", arguments={
                "prompt": music_prompt,
                "duration": 180
            })
            # Download del file
            subprocess.run(["curl", "-o", f"{WORK_DIR}/music/generated_music.wav", result["audio"]])
            return f"{WORK_DIR}/music/generated_music.wav"
        except:
            pass
    
    print("⚠️ ACE-Step non disponibile, creando file placeholder")
    # Crea un file WAV vuoto come placeholder
    with open(f"{WORK_DIR}/music/generated_music.wav", "wb") as f:
        f.write(b"RIFF" + (0).to_bytes(4, 'little') + b"WAVE")
    return f"{WORK_DIR}/music/generated_music.wav"


def genera_immagini_fal(fal_api_key):
    """Genera immagini con fal.ai (CogView)"""
    print("🎨 Generando immagini con CogView...")
    
    try:
        import fal
    except ImportError:
        print("❌ Installa fal.ai: pip install fal")
        return []
    
    generated_images = []
    
    for i, prompt in enumerate(IMAGE_PROMPTS):
        print(f"  Generando scena {i+1}/5...")
        
        try:
            result = fal.run("fal-ai/cogview", arguments={
                "prompt": prompt,
                "image_size": "landscape_16_9"
            })
            
            output_path = f"{WORK_DIR}/images/scene_{i:02d}.png"
            
            # Download immagine
            img_url = result["images"][0]["url"]
            subprocess.run(["curl", "-o", output_path, img_url], check=True)
            
            generated_images.append(output_path)
            print(f"  ✅ Scena {i+1} salvata")
            
        except Exception as e:
            print(f"  ❌ Errore scena {i+1}: {e}")
            # Crea placeholder
            create_placeholder_image(f"{WORK_DIR}/images/scene_{i:02d}.png")
            generated_images.append(f"{WORK_DIR}/images/scene_{i:02d}.png")
    
    return generated_images


def genera_video_cogvideo(fal_api_key):
    """Genera video con CogVideoX-3"""
    print("🎬 Generando video con CogVideoX-3...")
    
    try:
        import fal
    except ImportError:
        print("❌ Installa fal.ai: pip install fal")
        return []
    
    generated_videos = []
    
    for i, prompt in enumerate(VIDEO_PROMPTS):
        print(f"  Generando video {i+1}/5...")
        
        try:
            result = fal.run("fal-ai/cogvideo-x-3", arguments={
                "prompt": prompt,
                "num_frames": 81,
                "duration": "5s"
            })
            
            output_path = f"{WORK_DIR}/video/scene_{i:02d}.mp4"
            
            # Download video
            video_url = result["video"]["url"]
            subprocess.run(["curl", "-o", output_path, video_url], check=True)
            
            generated_videos.append(output_path)
            print(f"  ✅ Video {i+1} salvato")
            
        except Exception as e:
            print(f"  ❌ Errore video {i+1}: {e}")
            generated_videos.append(None)
    
    return generated_videos


def create_placeholder_image(output_path):
    """Crea un'immagine placeholder"""
    try:
        from PIL import Image, ImageDraw
        img = Image.new('RGB', (1920, 1080), color=(20, 20, 40))
        draw = ImageDraw.Draw(img)
        draw.rectangle([(0, 500), (1920, 1080)], fill=(0, 0, 0))
        img.save(output_path)
    except:
        # Fallback: crea file vuoto
        open(output_path, 'wb').close()


def create_ken_burns_video(input_image, output_video, duration=5):
    """Crea video con effetto Ken Burns"""
    cmd = f"""
    ffmpeg -y -loop 1 -i "{input_image}" \
    -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.003,1.15)':d={int(duration*25)}:s=1920x1080" \
    -t {duration} -r 25 -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
    "{output_video}"
    """
    subprocess.run(cmd, shell=True)


def assemble_final_video(video_clips, audio_file, output_file):
    """Assembla video finale"""
    # Crea lista concat
    concat_file = f"{WORK_DIR}/final/concat.txt"
    with open(concat_file, 'w') as f:
        for clip in video_clips:
            if clip and os.path.exists(clip):
                f.write(f"file '{os.path.abspath(clip)}'\n")
    
    # Merge
    merged = f"{WORK_DIR}/final/merged.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_file, "-c", "copy", merged
    ], check=True)
    
    # Aggiungi audio
    cmd = f"""
    ffmpeg -y -i "{merged}" -i "{audio_file}" \
    -c:v copy -c:a aac -b:a 192k -shortest \
    "{output_file}"
    """
    subprocess.run(cmd, shell=True, check=True)


def create_thumbnail(title, output_path, background_image):
    """Crea thumbnail YouTube"""
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        if os.path.exists(background_image):
            bg = Image.open(background_image).convert('RGB')
            bg = bg.resize((1280, 720), Image.LANCZOS)
        else:
            bg = Image.new('RGB', (1280, 720), (20, 20, 40))
        
        # Overlay scuro
        overlay = Image.new('RGB', bg.size, (0, 0, 0))
        bg.paste(overlay, (0, 500), overlay)
        
        draw = ImageDraw.Draw(bg)
        
        try:
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        except:
            font_large = ImageFont.load_default()
            font_small = font_large
        
        # Titolo
        words = title.split(' | ')
        if len(words) > 1:
            draw.text((640, 550), words[0], font=font_large, fill='white', anchor='mm')
            draw.text((640, 610), words[1], font=font_small, fill='#AAAAAA', anchor='mm')
        else:
            draw.text((640, 570), title[:50], font=font_large, fill='white', anchor='mm')
        
        bg.save(output_path, 'PNG')
        
    except Exception as e:
        print(f"⚠️ Errore thumbnail: {e}")


def main():
    """Pipeline principale"""
    print("="*60)
    print("🎬 QUIET CINEMA - AI Surreal Music Film Generator")
    print("="*60)
    print(f"📁 Work directory: {WORK_DIR}")
    
    # Step 1: Genera titolo e script
    print("\n📝 Step 1: Generazione titolo e script...")
    titolo = genera_titolo()
    script = genera_script(titolo)
    
    with open(f"{WORK_DIR}/current_script.txt", "w") as f:
        f.write(f"TITOLO: {titolo}\n\n")
        f.write(script)
    print(f"  ✅ Titolo: {titolo}")
    
    # Step 2: Genera musica
    print("\n🎵 Step 2: Generazione musica...")
    music_file = genera_musica_ace()
    print(f"  ✅ Musica: {music_file}")
    
    # Step 3: Genera immagini (usa fal.ai se disponibile)
    print("\n🎨 Step 3: Generazione immagini...")
    fal_key = os.environ.get("fal_api", "")
    if fal_key:
        images = genera_immagini_fal(fal_key)
    else:
        print("  ⚠️ fal_api non disponibile, saltando generazione immagini")
        images = [f"{WORK_DIR}/images/scene_{i:02d}.png" for i in range(5)]
        for img in images:
            create_placeholder_image(img)
    
    # Step 4: Genera video (opzionale)
    print("\n🎬 Step 4: Video clips (opzionale)...")
    # Salta video generation se non hai CogVideoX
    videos = []
    for i, img in enumerate(images):
        kb_video = f"{WORK_DIR}/video/kenburns_{i:02d}.mp4"
        print(f"  Creando Ken Burns per scena {i+1}...")
        create_ken_burns_video(img, kb_video)
        videos.append(kb_video)
    
    # Step 5: Assembla finale
    print("\n🎥 Step 5: Assemblaggio video finale...")
    final_video = f"{WORK_DIR}/final/quiet_cinema_final.mp4"
    assemble_final_video(videos, music_file, final_video)
    print(f"  ✅ Video finale: {final_video}")
    
    # Step 6: Thumbnail
    print("\n🖼️ Step 6: Creazione thumbnail...")
    thumbnail = f"{WORK_DIR}/final/thumbnail.png"
    create_thumbnail(titolo, thumbnail, images[0] if images else None)
    print(f"  ✅ Thumbnail: {thumbnail}")
    
    # Riepilogo
    print("\n" + "="*60)
    print("✅ PIPELINE COMPLETATA!")
    print("="*60)
    print(f"\n📁 File generati:")
    print(f"  - Video: {final_video}")
    print(f"  - Thumbnail: {thumbnail}")
    print(f"  - Script: {WORK_DIR}/current_script.txt")
    
    # Salva metadata
    metadata = {
        "titolo": titolo,
        "data_generazione": datetime.now().isoformat(),
        "files": {
            "video": final_video,
            "thumbnail": thumbnail,
            "script": f"{WORK_DIR}/current_script.txt"
        }
    }
    with open(f"{WORK_DIR}/metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    
    return metadata


if __name__ == "__main__":
    main()