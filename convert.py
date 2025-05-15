# This file will take a markdown file as an argument and convert it to html. 

import markdown
import sys
import os
import re

start = '''
<!doctype html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>DeltaKat</title>

  <meta name="author" content="Kat">
  <meta name="keywords" content="Python, AI, options, Delta">
  <meta name="robots" content="index, follow">

  <meta name="description" content="Where Python meets profit (or not): coding, AI, options and flying by Delta.">
  <link rel="icon" href="./cat-solid.svg" type="image/x-icon">
  <link rel="apple-touch-icon" href="./cat-solid.svg">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap"
    rel="stylesheet">

  <link rel="stylesheet" href="style.css">
</head>

<body>
  <main style="display:flex; align-items: center; flex-direction: column;">
   <section style="display: flex; flex-direction: column; gap: 1rem;">
'''

end = '''
    </section>
    </main>
    <footer style="height: 1.5rem; display: flex; justify-content: center; margin-top: 1.5rem;">
      <a href="https://www.linkedin.com/in/katrina-medvedeva-7a849012/" target="_blank"><img src="LI-In-Bug.png"
          alt="Katrina's Linkedin Profile" style="height: 100%"></a>
      <a href="https://github.com/med4kat" target="_blank"><img src="GitHub-Mark-120px-plus.png"
          alt="Katrina's GitHub Profile" style="height: 100%"></a>
    </footer>

</body>

</html>

'''

def convert_markdown_to_html(input_file, output_file):
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    
    # Convert markdown to HTML
    converted = markdown.markdown(text)
    html = start + converted + end


    # Write the HTML to a file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)


convert_markdown_to_html('Bigrams.md', 'Bigrams.html')