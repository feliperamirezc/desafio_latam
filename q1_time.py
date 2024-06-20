from typing import List, Tuple
from datetime import datetime,date
import pandas as pd
import os

#variable con el archivo
file_path = '/Users/feliperamirez/Desktop/desafio latam/challenge_DE/src/farmers-protest-tweets-2021-2-4.json'

def q1_time(file_path: str) -> List[Tuple[date, str]]:
    # Leer el archivo JSON
    df = pd.read_json(file_path, lines=True)

    # Convertir la columna de fechas a formato datetime
    df['date'] = pd.to_datetime(df['date']).dt.date

    # ranking  top 10 de fechas con mas tweets
    top_date_q1 = df['date'].value_counts().nlargest(10)

    # usuarios con mas tweets por fecha y append a lista
    top_users_list = []
    for i in top_date_q1.index:
        top_user = df[df['date'] == i]['user'].apply(lambda x: x['username']).value_counts().idxmax()
        top_users_list.append((i, top_user))        

    return top_users_list

if __name__ == "__main__":
    # Directorio del archivo JSON
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    
    # Ejecutar la función y mostrar el resultado
    result = q1_time(file_path)
    print(result)    