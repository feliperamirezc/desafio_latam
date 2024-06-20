import os
import json
from typing import List, Tuple
from datetime import datetime, date
from collections import Counter, defaultdict

def q1_memory(file_path: str) -> List[Tuple[date, str]]:
    # definicion de variables
    date_counts = Counter()
    user_counts = defaultdict(Counter)

    # lectura de archivo linea por linea
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tweet_date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = tweet['user']['username']
            
            date_counts[tweet_date] += 1
            user_counts[tweet_date][user] += 1

    # top 10 de fechas con mas tweets
    top_dates = date_counts.most_common(10)

    # usuario con mas tweets en el top 10 de fechas
    result = [(top_date, user_counts[top_date].most_common(1)[0][0]) for top_date, _ in top_dates]

    return result

if __name__ == "__main__":
    # Directorio del archivo JSON
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    
    # Ejecutar la función y mostrar el resultado
    result = q1_memory(file_path)
    print(result)