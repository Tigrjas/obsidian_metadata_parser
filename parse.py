import os, re

# Python script that removes words from keywords in YAML section and puts it into the genre section
# To use change the directory variable to your directory

directory = r"C:\Users\tigrjas\Desktop\testing\Anime"

def move_keywords_to_genre(content):
    # Define the regular expression patterns
    keywords_pattern = r'keywords:(.*?)---'
    genre_pattern = r'- genre::(.*?)$'
    keyword_pattern = r'\[\[(.*?)\]\]'

    # Find keywords section
    keywords_match = re.search(keywords_pattern, content, flags=re.DOTALL)
    if keywords_match:
        keywords_content = keywords_match.group(1).strip()
        # Find all keywords
        keywords = re.findall(keyword_pattern, keywords_content)
        if keywords:
            # Find the genre section under > [!Summary] Info
            genre_match = re.search(genre_pattern, content, flags=re.MULTILINE)
            if genre_match:
                # Extract existing genres
                existing_genres = genre_match.group(1).strip()
                # Append keywords to existing genres
                updated_genres = existing_genres + ", " + ", ".join(f"[[{keyword}]]" for keyword in keywords)
                # Replace genre section with updated genres
                content = re.sub(genre_pattern, f"- genre::{updated_genres}", content, flags=re.MULTILINE)

    return content

for root, dirs, files in os.walk(directory):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            modified_content = move_keywords_to_genre(content)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)

            

