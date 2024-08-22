Task1: 
Here, there are 2 publisher nodes and 2 subscriber nodes.
The pub1 node publishes to topic t1 and sub1 node is subscribed to t1.
Similiar is the working of pub2 and sub2, infact they are just copies of pub1 and sub1 respectively with changes in topic name.

Task2: 
Here, we take the node name as input during startup. All the different nodes publish data to topic "channel", while also being subscribed to the topic "channel", so data sent by any node to "channel" is printed to all the other nodes. Incase, a node with the same name is already running the older one is shutdown and the newer one continues to run. 

Bonus Task:
(still on it...)
