import json
from fonction.__init__ import *

def main():
    try :
        # special = 'spécial'
        valid_languages = ["en", "fr"]

        print(f"Available languages: {', '.join(valid_languages).upper()}")
        lang = input("Please select your language: ").lower()

        while lang not in valid_languages:
            print(f"\nInvalid selection. Please choose one of the following: {', '.join(valid_languages).upper()}")
            lang = input("Please select a valid language: ").lower()
        
        with open('languages.json', 'r') as lang_file:
            languages = json.load(lang_file)

        folder_path = input((languages[lang]["filepath"]))
        if folder_path in ["q", "Q"]:
            print(languages[lang]["exit_message"])
            exit()
        Cardinal.compress_videos(folder_path)

    except:
        print(languages[lang]["errors"], )

if __name__ == "__main__":
    main()