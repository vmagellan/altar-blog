import csv
import os
import re
import pandas as pd

# Function to parse metadata and content from a markdown file
def parse_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regular expression to match metadata block
    metadata_match = re.search(r'---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    
    if metadata_match:
        metadata = metadata_match.group(1)
        body_content = metadata_match.group(2).strip()
        
        # Extract metadata into a dictionary
        metadata_dict = {}
        for line in metadata.splitlines():
            key_value = re.match(r'(\w+): (.*)', line)
            if key_value:
                key, value = key_value.groups()
                metadata_dict[key] = value.strip().replace('"', '')
        
        return metadata_dict, body_content
    else:
        return {}, content.strip()

# Load existing CSV metadata
csv_path = './posts_metadata.csv'
csv_data = pd.read_csv(csv_path)

# Directory containing markdown files (update the path to the root folder containing '2019', '2020', etc.)
root_directory = './posts/'

# Prepare list to collect parsed data
parsed_data = []

# Traverse the directory structure
for root, dirs, files in os.walk(root_directory):
    for filename in files:
        if filename.endswith(".md"):
            file_path = os.path.join(root, filename)
            metadata, content = parse_markdown_file(file_path)
            
            # Add 'content' as a new key in metadata
            metadata['content'] = content
            
            # Append parsed metadata and content to the list
            parsed_data.append(metadata)

# Convert parsed metadata and content to a DataFrame
parsed_df = pd.DataFrame(parsed_data)

# Merge with existing CSV metadata
merged_df = pd.merge(csv_data, parsed_df, on='title', how='outer')

# Output the merged data to a new CSV file
output_csv_path = './merged_blog_posts_metadata.csv'
merged_df.to_csv(output_csv_path, index=False)

print(f"Merged data has been saved to {output_csv_path}")
