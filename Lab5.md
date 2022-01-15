### Lab 5

#### Luoyou Zhao z5225024

***

Excercise 1

Q1

The maximum size of the congestion window is 100. At that time, because of the network congestion, the packet loses. The algorithm set ssthresh to the half size of cwnd, then change condo to 1.

Q2

According to the graph, the average throughput is about 175 packets per second and each packet contains 480 Bytes of data.

> $175*480=84000$ Bytes/seconds

Q3

I find the maximum congestion window is about 50. The average throughput is close to 220 packet per second.

> $220*480=105600$ Bytes/seconds

It nearly use 85% capacity of the link which is 1Mbps.

Q4

When I set the window size to 100, the average throughput increase from 175 packets per second(in Q2) to nearly 200 packets per second in TCP Reno. However the average throughput doesn't change in which is windows size is 50 compare to what I set in Q3.



Excercise 2

Q1

In the end, yes. Becasue accoding to the graph, there doesn't exist any flow has the largest throughput for all time and all flow's throughput is changing at the same range.

Q2

When a new flow is created, the press-existing TCP flows' throughput decrease sharply until their throughput are nearly equal to each other. This is to ensure the flow fairness in TCP. 



Excercise 3

Q1

In the right, the red pipe is TCP. And in the left, the blue dots is UDP.

Q2

UDP's throughput is larger than TCP's. This is because TCP need to check if the packet is received after sending it. And TCP is more stable than UDP.

Q3

UDP is fast but unstable. TCP is slow but stable. If everyone use UDP instead of TCP, the network congestion will be a bery serious problem because of the sudden rise of the packets lost.

