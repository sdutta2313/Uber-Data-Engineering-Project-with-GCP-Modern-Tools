from pandas import DataFrame
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data exporter
def export_data_to_big_query(data, **kwargs) → None:
"""
Template for exporting data to a BigQuery warehouse. 
Specify your configuration settings in 'io_config.yaml'
Docs: https://docs.mage.al/design/data-loading bigquery
"""

table_id = 'coral-circlet-401816.uber_data_engineering yt.fact_table'
config_path= path.join(get_repo_path(), 'io_config.yaml') 
config profile = 'default'
BigQuery.with config(ConfigFileLoader(config_path, config profile)).export(
    DataFrame(data['fact_table']), 
    table_id, if_exists='replace',
)
