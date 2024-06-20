from typing import List, Tuple
import pandas as pd
import os
import emoji

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # leer el archivo json
    df = pd.read_json(file_path, lines=True)
    
    # funcion para extraer los emojis en una lista
    def extract_emojis(text):
        return [char for char in text if char in emoji.EMOJI_DATA]

    # añadir columna al df
    df['emojis'] = df['content'].apply(extract_emojis)
    
    # separar los n emojis de la lista en n registros
    df_emojis = df['emojis'].explode()

    # generar el top 10 de emojis
    top10_emojis = df_emojis.value_counts().nlargest(10)
    
    # convertir el top 10 de emojis en una lista
    emojis_top10_list = list(top10_emojis.items())
    
    return emojis_top10_list

if __name__ == "__main__":
    # Directorio del archivo JSON
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    
    # Ejecutar la función y mostrar el resultado
    result = q2_time(file_path)
    print(result)    