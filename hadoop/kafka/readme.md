
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
 

