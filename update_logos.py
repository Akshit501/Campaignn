import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the track content with images
new_track = """
          <!-- Track 1 -->
          <img src="assets/logos/accenture.svg" height="40" alt="Accenture" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/microsoft.svg" height="40" alt="Microsoft" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/google.svg" height="40" alt="Google" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/aws.svg" height="40" alt="AWS" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/ibm.svg" height="40" alt="IBM" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <div class="logo-text" style="font-family: Helvetica, sans-serif; letter-spacing: 2px; text-transform: uppercase;">Intel</div>
          <img src="assets/logos/meta.svg" height="40" alt="Meta" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/nvidia.svg" height="40" alt="NVIDIA" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <!-- Track 2 (Duplicate for infinite loop) -->
          <img src="assets/logos/accenture.svg" height="40" alt="Accenture" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/microsoft.svg" height="40" alt="Microsoft" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/google.svg" height="40" alt="Google" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/aws.svg" height="40" alt="AWS" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/ibm.svg" height="40" alt="IBM" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <div class="logo-text" style="font-family: Helvetica, sans-serif; letter-spacing: 2px; text-transform: uppercase;">Intel</div>
          <img src="assets/logos/meta.svg" height="40" alt="Meta" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
          <img src="assets/logos/nvidia.svg" height="40" alt="NVIDIA" style="filter: brightness(0); opacity: 0.8; max-width: 150px; object-fit: contain;">
"""

html = re.sub(r'<!-- Track 1 -->.*?<!-- Track 2 \(Duplicate for infinite loop\) -->.*?(?=</div>\s*</div>)', new_track, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
