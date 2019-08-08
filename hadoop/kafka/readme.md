


Consumers Rule!

A fundamental explanation of Kafka’s inner workings goes as follows: Every topic is associated with one
or more partitions, which are spread over one or more brokers. Every partition gets replicated to those 
one or more brokers depending on the replication factor that is set. The replication factor is then 
responsible for determining the reliability, while the number of partitions is responsible for the 
parallelism for consumers. A partition is associated with only a single consumer instance per consumer 
group. Since the total consumer instances per group is less than – or the same as – the number of 
partitions, adding support for extra consumer instances requires that more partitions be added as 
well, but ensures read scalability.

"" A partition is associated with only a single consumer instance per consumer group. ""
