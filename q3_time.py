from typing import List, Tuple
import os
from collections import defaultdict, Counter
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mention_counts = Counter()

    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            mentioned_users = tweet.get('mentionedUsers', [])
            if mentioned_users:
                for user in mentioned_users:
                    username = user.get('username')
                    if username:
                        mention_counts[username] += 1

    top_mentions = mention_counts.most_common(10)
    return top_mentions

if __name__ == "__main__":
    # Directorio del archivo JSON
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    
    # Ejecutar la función y mostrar el resultado
    result = q3_time(file_path)
    print(result)    