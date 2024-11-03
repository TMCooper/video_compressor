import os
import subprocess

class Cardinal():

    def compress_videos(folder_path):
        output_folder = folder_path
        # Crée le dossier de sortie s'il n'existe pas encore
        os.makedirs(output_folder, exist_ok=True)
        
        # Parcourt tous les fichiers dans le dossier
        for filename in os.listdir(folder_path):
            if filename.endswith(('.mp4', '.mkv', '.avi', '.mov', '.ts')):  # ajoute les extensions de ton choix
                input_path = os.path.join(folder_path, filename)
                output_path = os.path.join(output_folder, f"compressed_{filename}")
                
                # Obtient la taille d'origine du fichier
                original_size = os.path.getsize(input_path)
                
                # Définit le bitrate cible (environ 50 % de la taille initiale)
                target_bitrate = (original_size * 8 * 0.5) / (os.path.getsize(input_path) / 1000)  # en kbps
                
                # Utilise ffmpeg pour compresser la vidéo
                cmd = [
                    "ffmpeg", "-i", input_path,
                    "-b:v", f"{int(target_bitrate)}k",
                    "-b:a", "128k",  # bitrate audio standard, ajustable selon les besoins
                    output_path
                ]
                result = subprocess.run(cmd, check=True)
                
                # Si la compression est réussie, on supprime le fichier d'origine
                if result.returncode == 0:
                    os.remove(input_path)
                    print(f"Compression de {filename} terminée et fichier d'origine supprimé.")
                else:
                    print(f"Erreur lors de la compression de {filename}. Fichier d'origine conservé.")
