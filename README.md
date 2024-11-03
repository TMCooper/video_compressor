#### install Chocolatey 

- execute powershell in administrator
- copy and pasth this line on your powershell : `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
- after the download finish
- tap on the same powershell (or you can reopen an new but in administrator too) `choco install ffmpeg` and if the program asks you for a yes or an a then type one or the other (the result is the same)
- then you can re execute the compresseur.py