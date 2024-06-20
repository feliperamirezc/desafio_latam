from typing import List, Tuple
import os
import json
import emoji

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    from collections import Counter

    emoji_counts = Counter()
    
    # Leer el archivo línea por línea
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            content = tweet['content']
            emojis = [char for char in content if char in emoji.EMOJI_DATA]
            emoji_counts.update(emojis)
    
    # Obtener los top 10 emojis más usados
    top_emojis = emoji_counts.most_common(10)
    
    return top_emojis

if __name__ == "__main__":
    # Directorio del archivo JSON
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    
    # Ejecutar la función y mostrar el resultado
    result = q2_memory(file_path)
    print(result)    