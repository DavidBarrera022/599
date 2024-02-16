# PARAMETERS

# Especifica el ID del proyecto y el nombre del conjunto de datos y la tabla en BigQuery
project_id = 'bdb-gcp-qa-cds-idt'
dataset_id = 'ba_public'
table_id = 'MASTER_TABLE_599'

# Lee diccionario xls del storage
bucket_name = 'bdb-gcp-qa-cds-idt-mlops'
blob_name = 'gs://bdb-gcp-qa-cds-idt-mlops/model/propensity-model-599/input/feature-store-dictionaries/tag_dict.xlsx'


# Ruta al archivo YAML
blob_path = "gs://bdb-gcp-qa-cds-idt-mlops/model/propensity-model-599/input/feature-store-dictionaries/catalog.yml"

# Ruta al archivo YAML
blob_path2 = "gs://bdb-gcp-qa-cds-idt-mlops/model/churn-model-639/input/feature-store-dictionaries/primary.yml"


# bucket y directorio
bucket_name2 = 'bdb-gcp-qa-cds-idt-mlops'
bucket_dir = 'propensity-model-599/output/primary-process/'
