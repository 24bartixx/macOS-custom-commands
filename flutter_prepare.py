import os

file_content = f"""
# Flutter flutetr_prepare Terminal command
flutter_prepare() {{
     dart fix --apply && \\
     dart format . && \\
    flutter analyze
}}
"""

shell_config_path = os.path.expanduser("~/.zshrc")

try:
     with open(shell_config_path, "a") as file:
        file.write(file_content)

     os.system("source ~/.zshrc")

     print(f"Success! You can now use flutter_prepare before git push of your Flutter project")

except Exception as e:
    print(f"An error occurred: {e}")
