import time
import openai
import os

from openai import OpenAI
from openai._exceptions import RateLimitError  


#OpenAI API key:
api_key = "Ich-Bin-Ein-OpenAI-API-Key"
client = OpenAI(api_key=api_key)  


prompt = "schreibe mir eine Rede im Stil von Joachim Gauck."

# Anzahl an Generierten Texten:
num_generations = 100

# Output Ordner:
output_folder = "Ich-Bin-Ein-Dateipfad-Zu-Einem-Ordner"
os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

for i in range(1, num_generations + 1):
    retries = 3  # Max number of retries in case of rate limits
    wait_time = 2  # Initial wait time in seconds

    while retries > 0:
        try:
            # Generate response
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Use gpt-4o-mini
                messages=[{"role": "user", "content": prompt}]
            )
            text = response.choices[0].message.content  # Extract response text

            # Speichername:
            file_name = f"Gauck_KI4o_{i}.txt"
            file_path = os.path.join(output_folder, file_name)

          
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)

            print(f"Saved: {file_path}")

            # Wait to prevent rate limits
            time.sleep(wait_time)
            break  # Exit retry loop if successful

        except RateLimitError:
            print(f"Rate limit reached. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            wait_time *= 2  # Exponential backoff
            retries -= 1

print("All responses generated and saved successfully!")
