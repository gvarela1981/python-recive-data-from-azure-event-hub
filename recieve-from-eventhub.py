# pip install azure-eventhub
# https://learn.microsoft.com/en-us/pthon/api/overview/azure/eventhub-readme?view=azure-python

import logging
from azure.eventhub import EventHubConsumerClient

connection_str =  '' # pedir connection string 'Endpoint=sb://tenant.servicebus.windows.net/;SharedAccessKeyName=asa_gis_pbi;SharedAccessKey=LYgIg4vvG0pdP5Mf4+82nEXAoLAy0HaS......=;EntityPath=asa_gis_nuevo' 
consumer_group = 'pedir-cosumer-grooup' # pedir consumer group
eventhub_name = 'asa_gis_nuevo' # pedir event_hub_name
client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group, eventhub_name=eventhub_name)

logger = logging.getLogger("azure.eventhub")
logging.basicConfig(level=logging.INFO)

def on_event(partition_context, event):
    logger.info("Received event from partition {}".format(partition_context.partition_id))
    partition_context.update_checkpoint(event)

with client:
    client.receive(
        on_event=on_event,
        starting_position="-1",  # "-1" is from the beginning of the partition.
    )
    # receive events from specified partition:
    client.receive(on_event=on_event, partition_id='0')
    