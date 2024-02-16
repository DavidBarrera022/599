import yaml
import pandas as pd

from google.cloud import bigquery, storage
from app.net.bancodebogota.clLibFrameworkControl import ClLibFrameworkControl as Fc
from app.net.bancodebogota import parameters as p
fc = Fc()

def app_test(prueba):
    return prueba

def read_yaml_storage(blob_path: str) -> dict:
    """Read YAML file from GCS and returns a dictionary."""
    client = storage.Client()
    bucket_name, blob_name = blob_path.replace('gs://', '').split('/', 1)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    yaml_data = blob.download_as_text()
    query_params = yaml.safe_load(yaml_data)
    return query_params


def execute_sql_bigquery(consulta_sql, proyecto_id):
    """
    lectura tabla from BQ.
    Se hace laconsulta mediante un query y se almacena la data en un pd.DataFrame
    """
    try:
        client = bigquery.Client(project=proyecto_id)
        consulta = client.query(consulta_sql)
        # #resultados = consulta.result()
        return consulta
    except Exception as e:
        fc.append_df("ERROR", "Error al ejecutar la consulta en BigQuery:  " + str(e))
        print(f"Error al ejecutar la consulta en BigQuery: {str(e)}")
        fc.create_file_bucket(p.project_id)
        return None