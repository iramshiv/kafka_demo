# kafka_demo

**Exercise 1:**

This is a python project using kafka, on UBUNTU 19.10.

The project has 2 producers (A & B) and a consumer (C). Producer A generates an even number per second, Producer B generates an odd number per 2 seconds and Consumer C reads the data from Producers A & B.

Kafka Installation : See <https://kafka.apache.org/quickstart>

Kafka requires Java :
``` sudo apt install default-jre```

Run these following command in the kafka unzipped folder.
 
 Start zookeeper : 
 ```bin/zookeeper-server-start.sh config/zookeeper.properties```
 
 Start kafka server :
 ```bin/kafka-server-start.sh config/server.properties```
 
 *Download producerA.py, producerB.py, consumerC.py
          
 Run Consumer C:
 ```python3 consumerC.py```
 
 Run Producer A :
 ``` python3 producerA.py```
 
 Run Producer B:
 ```python3 producerB.py```
 
 consumerC.py Output:
 ![consumerC.py Output](https://github.com/iramshiv/kafka_demo/blob/master/consumerC.jpg)
 
 *to delete the topic after first run: 
 ```bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic numtest1```
 
  *"numtest1" is topic name created in this project.*
  
  Stop Kafka server :
  ```sudo bin/kafka-server-stop.sh config/server.properties```
  
  Stop zookeeper : 
  ```bin/zookeeper-server-stop.sh config/zookeeper.properties```
  
  ---------------------------------------------------------------------------------------------------------------------------
  
  **Exercise 2:**
  
  **Kafka Streams**   - The easiest way to write mission-critical real-time applications and microservices.
  
  Kafka Streams is a client library for processing and analyzing data stored in Kafka. It builds upon important stream         processing concepts such as properly distinguishing between event time and processing time, windowing support, exactly-once   processing semantics and simple yet efficient management of application state.
  
  Despite being a humble library, Kafka Streams directly addresses a lot of the hard problems in stream processing:

    * Event-at-a-time processing (not microbatch) with millisecond latency
    * Stateful processing including distributed joins and aggregations
    * A convenient DSL
    * Kafka Streams simplifies streaming applications is that it fully integrates the concepts of tables and streams.
    * Windowing with out-of-order data using a DataFlow-like model
    * Distributed processing and fault-tolerance with fast failover
    * Reprocessing capabilities so you can recalculate output when your code changes
    * No-downtime rolling deployments :
          Balance the processing load as new instances of your app are added or existing ones crash.
          Maintain local state for tables
          Recover from failures
     * Threading Model
     * processor topology
          Source Processor, is a special type of stream processor which does not have any upstream processors.
          Sink Processor, is a stream processor does not have down-stream processors.
  
  ---------------------------------------------------------------------------------------------------------------------------
  
  **Exercise 3:**
  
   YES.
  
 
