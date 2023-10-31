# diagram.py
from diagrams import Diagram,Cluster,Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.analytics import Superset
from diagrams.custom import Custom

with Diagram("Vehicle Telemetry Stream", show=False):
    elm327=Custom("ELM327","./diagrams/my_resources/elm327bluetooth.jpg")
    androbd=Custom("AndrOBD","./diagrams/my_resources/androbd.png")

    with Cluster("Stream Process Cluster"):
        hivemqtt=Custom("HiveMQTT","./diagrams/my_resources/hivemq.png")
        k_broker=Kafka("Kafka Broker")
        ksqldb=Kafka("ksqlDB")
        superset=Superset("Superset")
        postgres=PostgreSQL("Warehouse")

    elm327 >> androbd >> hivemqtt >> k_broker >> ksqldb
    ksqldb >> Edge(label="enrich") >> k_broker
    k_broker >> postgres >> superset