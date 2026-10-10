import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Match the entire section with id="media-coverage"
# We match from the <section to the closing </section>
pattern = r'(<!-- ==========================================================================\s*11 MEDIA COVERAGE\s*========================================================================== -->\s*)?<section id="media-coverage" class="section-pad">.*?</section>\s*'
html = re.sub(pattern, '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
