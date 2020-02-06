# kafka_demo

This is a python project using kafka, on UBUNTU 19.10.

The project has 2 producers (A & B) and a consumer (C). Producer A generates an even number per second, Producer B generates an odd number per 2 seconds and Consumer C reads the data from Producers A & B.

**Kafka Installation :** See <https://kafka.apache.org/quickstart>

**Kafka requires Java :** ``` sudo apt install default-jre```

Run these following command in the kafka unzipped folder.
 
 **Start zookeeper :** ```bin/zookeeper-server-start.sh config/zookeeper.properties```
 
 **Start kafka server :** ```bin/kafka-server-start.sh config/server.properties```
 
 Download producerA.py, producerB.py, consumerC.py
 
 **Run Consumer C:** ```python3 consumerC.py```
 
 **Run Producer A :** ``` python3 producerA.py```
 
 **Run Producer B:** ```python3 producerB.py```
 
 To **delete the topic** after first run: ```bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic numtest1```
 
  *"numtest1" is topic name created in this project.*
  
  **Stop Kafka server :** ```sudo bin/kafka-server-stop.sh config/server.properties```
  
  **Stop zookeeper :** ```bin/zookeeper-server-stop.sh config/zookeeper.properties```
 
