
<h1> Kafka Architecture </h1>




The Kafka Components – Universal Modeling Language (UML)

Kafka’s main architectural components include
Producers, 
Topics,
Consumers, 
Consumer Groups, 
Clusters, 
Brokers, 
Partitions,
Replicas, 
Leaders, and 
Followers. 
This simplified UML diagram describes the ways these components relate to one another:

These are four main parts in a Kafka system:

Broker: Handles all requests from clients (produce, consume, and metadata) and keeps data replicated within the cluster. There can be one or more brokers in a cluster.
Zookeeper: Keeps the state of the cluster (brokers, topics, users).
Producer: Sends records to a broker.
Consumer: Consumes batches of records from the broker.


![](images/uml_diagram)




It’s important to note the relationships between broker, replica, and partition components that are highlighted, such as:

Kafka clusters can have one or more brokers.
Brokers can host multiple replicas.
Topics can have one or more partitions.
A broker can host zero or one replica per partition.
A partition has one leader replica and zero or more follower replicas.
Each replica for a partition needs to be on a separate broker.
Every partition replica needs to fit on a broker, and a partition can’t be divided over multiple brokers.
Every broker can have one or more leaders, covering different partitions and topics.

- Single Consumer can subscribe to multiple topics
- Single producer can send to multiple topics
- We can more consumers thatn the partitions and have some consumer lying idle , which can take over when an active
consumer dies or which can fill in when new partitions are added
- there are fewer consumers in a group that partitions, causing consumer A2 to be responsible for processing more messages than consumer A1:

"""
In understanding Kafka consumers from an architectural and resourcing standpoint, <h5> it’s critical to note that 
consumers and producers don’t run on Kafka brokers, but they do they require CPU and IO resources of their own. </h5>
This is advantageous in offering the flexibility to run consumers however, wherever, and in whatever quantity
is needed without concern for deployment to brokers or sharing their resources. However, a challenge 
remains in that the best method for deploying and resourcing consumers and producers must be
thoroughly thought out. An optimal strategy might be to enlist scalable and elastic
microservices for the task.  """
<h3> Consumers Rule! </h3>

A fundamental explanation of Kafka’s inner workings goes as follows: Every topic is associated with one
or more partitions, which are spread over one or more brokers. Every partition gets replicated to those 
one or more brokers depending on the replication factor that is set. The replication factor is then 
responsible for determining the reliability, while the number of partitions is responsible for the 
parallelism for consumers. A partition is associated with only a single consumer instance per consumer 
group. Since the total consumer instances per group is less than – or the same as – the number of 
partitions, adding support for extra consumer instances requires that more partitions be added as 
well, but ensures read scalability.

"" A partition is associated with only a single consumer instance per consumer group. ""


![](images_for_readme/one_partition_to_one_consumer_only.png)

![](images_for_readme/one_partition_to_one_consumer_only.png)


Normally, a partition can only support a single consumer in a group. This limit can be overcome, however, 
by manually connecting consumers to a specific partition in a topic, effectively overruling the dynamic 
protocol for those consumers. Such consumers should be in different groups. This has no effect on consumers 
that still connect dynamically:



<img src="images_for_readme/one_partition_to_one_consumer_only.png" width="300">

one_partition_to_one_consumer_only

https://github.com/doyager/play_around/blob/master/images_for_readme/one_partition_to_one_consumer_only.png


<h3>Manual Partition Assignment </h3>
  
In the previous examples, we subscribed to the topics we were interested in and let Kafka dynamically assign a fair 
share of the partitions for those topics based on the active consumers in the group. However, in some cases you may 
need finer control over the specific partitions that are assigned. For example:

If the process is maintaining some kind of local state associated with that partition (like a local on-disk key-value store), then it should only get records for the partition it is maintaining on disk.

If the process itself is highly available and will be restarted if it fails (perhaps using a cluster management framework 
like YARN, Mesos, or AWS facilities, or as part of a stream processing framework). In this case there is no need
for Kafka to detect the failure and reassign the partition since the consuming process will be restarted on another
machine.
To use this mode, instead of subscribing to the topic using subscribe, you just call assign(Collection) with 
the full list of partitions that you want to consume.


     String topic = "foo";
     TopicPartition partition0 = new TopicPartition(topic, 0);
     TopicPartition partition1 = new TopicPartition(topic, 1);
     consumer.assign(Arrays.asList(partition0, partition1));
     
     
 "More consumers than partitions"
 Another scenario is to have a more consumers in a group than partitions, with certain consumers remaining idle. 
 Kafka is able to failover to such idle consumers in cases where an active consumer dies, or 
 when a new partition is added:
 

<h3> Kafka Broker</h3>
A Kafka cluster consists of one or more servers (Kafka brokers) running Kafka. Producers are processes that push records into Kafka topics within the broker. A consumer pulls records off a Kafka topic.
Running a single Kafka broker is possible but it doesn’t give all the benefits that Kafka in a cluster can give, for example, data replication.
Kafka Broker
Management of the brokers in the cluster is performed by Zookeeper. There may be multiple Zookeepers in a cluster, in fact the recommendation is three to five, keeping an odd number so that there is always a majority and the number as low as possible to conserve overhead resources.


<h3> Consumers and consumer groups </h3>

Consumers can read messages starting from a specific offset and are allowed to read from any offset point they choose. This allows consumers to join the cluster at any point in time.

<h2>Low-level consumers</h2>

    There are two types of consumers in Kafka. First, the low-level consumer, where topics and partitions are specified as is the offset from which to read, either fixed position, at the beginning or at the end. This can, of course, be cumbersome to keep track of which offsets are consumed so the same records aren’t read more than once. So Kafka added another easier way of consuming with:

<h2>High-level consumer</h2>

      The high-level consumer (more known as consumer groups) consists of one or more consumers. Here a consumer group is created by adding the property “group.id” to a consumer. Giving the same group id to another consumer means it will join the same group.

      The broker will distribute according to which consumer should read from which partitions and it also keeps track of which offset the group is at for each partition. It tracks this by having all consumers committing which offset they have handled.

      Every time a consumer is added or removed from a group the consumption is rebalanced between the group. All consumers are stopped on every rebalance, so clients that time out or are restarted often will decrease the throughput. Make the consumers stateless since the consumer might get different partitions assigned on a rebalance.

      Consumers pull messages from topic partitions. Different consumers can be responsible for different partitions. Kafka can support a large number of consumers and retain large amounts of data with very little overhead. By using consumer groups, consumers can be parallelized so that multiple consumers can read from multiple partitions on a topic, allowing a very high message processing throughput. The number of partitions impacts the maximum parallelism of consumers as there cannot be more consumers than partitions.

<h3>Records are never pushed out to consumers, the consumer will ask for messages when the consumer is ready to handle the message.</h3>

The consumers will never overload themselves with lots of data or lose any data since all records are being queued up in Kafka. If the consumer is behind during message processing, it has the option to eventually catch up and get back to handle data in real-time.



<h2> Mirror Maker </h2>



<h4> Best Practices </h4>
It is a good idea to create any topics that are being mirrored on the destination cluster before starting Mirror Maker. 
Mirror Maker can create the topics automatically but they may not retain the exact same configuration as the originals.

If you are running multiple Mirror Maker instances, it is recommended that all instances share the same group-id in the consumer properties.
