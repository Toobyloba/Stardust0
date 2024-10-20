import os
import re

def find_and_replace_javadoc(directory, s1, s2):
    # Traverse all subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("TestSet.java"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Find the first Javadoc comment
                javadoc_match = re.search(r'/\*\*(.*?)\*/', content, re.DOTALL)
                if javadoc_match:
                    javadoc_content = javadoc_match.group(1)
                    # Replace s1 with s2 in the Javadoc content
                    new_javadoc_content = javadoc_content.replace(s1, s2)
                    # Replace the old Javadoc content with the new one in the file content
                    new_content = content.replace(javadoc_content, new_javadoc_content)
                    
                    # Write the new content back to the file
                    with open(file_path, 'w') as f:
                        f.write(new_content)
                    print(f"Updated {file_path}")
                else:
                    print(f"No Javadoc found in {file_path}")

# Example usage
directory = '/path/to/your/directory'
s1 = 'old_text'
s2 = 'new_text'
find_and_replace_javadoc(directory, s1, s2)
