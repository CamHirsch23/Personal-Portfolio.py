import os
import subprocess

# Define the structure of the portfolio
portfolio_structure = {
    'index.html': 'Hi My Name is Cameron James Hirschboeck Thank you, Cameron UN',
    'about.html': 'Hi I am currently employed as a Material Handler at Fedex. I am currently Enrolled at Coding Temple and National University. I am going into technology because the employment rate high. I like to walk. Thank you, Cameron',
    'projects.html': 'Hi This is my example of Web Fundamentals You are tasked with creating a Python application that interfaces with a public API, fetches data, and processes it. Thank you, Cameron',
    'skills.html': 'Hi I have taken computer courses in the past and I think with help I can be a better coder Thank you, Cameron',
    'contact.html': 'Hi My Contact Number is 414-469-9038 and My git hub is https://github.com/CamHirsch23 Thank you, Cameron',
}

# Function to create HTML files with basic structure
def create_html_file(filename, title):
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <!-- Content goes here -->
</body>
</html>
"""
    with open(filename, 'w') as file:
        file.write(content)

# Create the portfolio directory if it doesn't exist
if not os.path.exists('portfolio'):
    os.makedirs('portfolio')

# Change the current working directory to 'portfolio'
os.chdir('portfolio')

# Create each HTML file based on the structure
for filename, title in portfolio_structure.items():
    create_html_file(filename, title)

# Initialize a new git repository
subprocess.run(['git', 'init'])

# Create a README.md file
with open('README.md', 'w') as readme:
    readme_content = """# Personal Portfolio Project

This repository contains the code for my personal portfolio website.

## How to Run

Open the `index.html` file in a web browser to view the portfolio.

## Project Structure

- `index.html`: Home Page/Section
- `about.html`: About Me Page/Section
- `projects.html`: Projects Page/Section
- `skills.html`: Skills Page/Section
- `contact.html`: Contact Page/Section

## Contributions

Contributions are welcome! Please fork the repository and open a pull request with your changes.

## License

This project is licensed under the MIT License.
"""
    readme.write(readme_content)

# Add all files to the git repository
subprocess.run(['git', 'add', '.'])

# Commit the changes
subprocess.run(['git', 'commit', '-m', 'Initial commit of portfolio structure'])

print("Portfolio structure created and initial commit made in git repository.")
