import os
import sys
from pathlib import Path

def create_directory(path):
    try:
        path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {path}")
    except Exception as e:
        print(f"Error creating directory {path}: {e}")

def write_file(path, content):
    if path.exists():
        response = input(f"File {path} already exists. Overwrite? (y/n): ").strip().lower()
        if response != 'y':
            print(f"Skipped writing to {path}")
            return
    try:
        with path.open('w', encoding='utf-8') as f:
            f.write(content)
        print(f"Written file: {path}")
    except Exception as e:
        print(f"Error writing file {path}: {e}")

def main():
    # Define project structure
    project_root = Path.cwd()

    directories = [
        project_root / "css",
        project_root / "js",
        project_root / "assets" / "images",
        project_root / "assets" / "videos",
        project_root / "assets" / "fonts",
        project_root / "plugins"
    ]

    for directory in directories:
        create_directory(directory)

    # Define file contents
    index_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI Presentation</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Reveal.js CSS -->
    <link rel="stylesheet" href="node_modules/reveal.js/dist/reveal.css">
    <link rel="stylesheet" href="node_modules/reveal.js/dist/theme/black.css" id="theme">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="css/custom.css">
</head>
<body>

    <div class="reveal">
        <div class="slides">
            <section>Slide 1: Introduction to AI</section>
            <section>Slide 2: Machine Learning</section>
            <!-- Add more slides as needed -->
        </div>
    </div>

    <!-- Reveal.js JS -->
    <script src="node_modules/reveal.js/dist/reveal.js"></script>

    <!-- Initialize Reveal.js -->
    <script>
        Reveal.initialize({
            hash: true,

            // Optional configurations
            transition: 'slide', // none/fade/slide/convex/concave/zoom
            // More options available at https://revealjs.com/config/
        });
    </script>

    <!-- Custom JS -->
    <script src="js/custom.js"></script>
</body>
</html>
"""

    custom_css_content = """/* custom.css */
body {
    font-family: 'Arial, sans-serif';
}

h2 {
    color: #2c3e50;
}
"""

    custom_js_content = """// custom.js
document.addEventListener('DOMContentLoaded', () => {
    console.log('AI Presentation Loaded');
});
"""

    readme_content = """# AI Presentation

This project is an HTML-based presentation on Artificial Intelligence using [Reveal.js](https://revealjs.com/).

## Project Structure

ai-presentation/ 
│ ├── index.html 
├── package.json 
├── README.md │ 
├── css/ │ 
├── custom.css 
│ ├── js/ │ 
├── custom.js 
│ ├── assets/ 
│ ├── images/ 
│ ├── videos/ 
│ └── fonts/ 
    └── plugins/ 
    └── [reveal.js plugins]

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) and npm installed.
- Reveal.js installed via npm:

    ```bash
    npm install reveal.js
    ```

### Running the Presentation

Use the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension in VSCode or any other static server to serve `index.html`.

## Customization

- **Adding Slides:** Edit `index.html` and add more `<section>` tags within the `.slides` container.
- **Custom Styles:** Modify `css/custom.css` to change the appearance.
- **Custom Scripts:** Add JavaScript functionality in `js/custom.js`.

## Deployment

Deploy your presentation using platforms like GitHub Pages, Netlify, or Vercel.

"""

    # Define file paths
    files = {
        project_root / "index.html": index_html_content,
        project_root / "css" / "custom.css": custom_css_content,
        project_root / "js" / "custom.js": custom_js_content,
        project_root / "README.md": readme_content
    }

    for file_path, content in files.items():
        write_file(file_path, content)

    print("\nProject setup complete! You can now open index.html with a live server to view your presentation.")

if __name__ == "__main__":
    main()