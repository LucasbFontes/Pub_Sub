# Context
This project was made during a workshop provided by [The Plumbers](https://theplumbers.com.br/). The goal here is to use Google PubSub as a messaging service to send data to different locations within GCP: GCS and Bigquery. I used MongoDB as a source for the data and data pipeline is partitioned as follows:

 * MongoDB: Source containing the JSON files;
 * PubSub: Messaging Service; 
 * GCS: Google datalake used as a landingzone;
 * Dataflow: Streaming service;
 * Bigquery: Highly Scalable and Serverless DataWarehouse;

# Technologies

## MongoDB

MongoDB is a noSQL databased document oriented which means that it stores data in the semi-structured or unstructured way, instead of table as a "traditional" database. By doing so, it gain:

 * Schema Flexibility: Meaning that it hasn't a fixed schema and each document have it own structured even within a collection. In other words, a document can have one specific field and the others don't.
 * Horizontal scalability: This type of databased is designed to scale horizontally, meaning that it can be distributed along differents nodes, gaining fault tolerance and high performance. A perfect match for a Big Data environment!

## Google PubSub

Pubsub is a scalable messaging service that uses services to produce and consume messages, it has the capability of communicate asynchronously with 100 milliseconds of latency. Most used in streaming analytics and integration pipelines. 

With Pub/Sub is possible to create systems using producers and consumers, in this case called publishers and subscribers. These tools can work decoupled which means that it's possible to send an event with the published but not to consume right away
(in this particular case one needs to pay attention to the time that the message stays in the system before being automatically deleted). 

Pub/Sub works in a very similar way as Apache Kafka, given that also has a topic in which the subscription must connect in order to receive the data from the publisher. The difference is that 
## GCS

## Bigquery

# The Project
