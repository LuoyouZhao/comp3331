### Lab 4

#### Luoyou Zhao z5225024

***

Excersice  1

Q1

The ip address of gaia.cs.umass.edu is 128.119.245.12. The port number is 80. The ip address of client is 192.168.1.102, and the port number is 1161

Q2

The sequence number is 232129013

Q3 and Q4

| Sequence  | sent time | received time | RTT      | ERTT     | Length |
| --------- | --------- | ------------- | -------- | -------- | ------ |
| 232129013 | 0.026477  | 0.053937      | 0.02746  | 0.02746  | 565    |
| 232129578 | 0.041737  | 0.077294      | 0.35557  | 0.028472 | 1460   |
| 232131038 | 0.054026  | 0.124085      | 0.070058 | 0.03367  | 1460   |
| 232132498 | 0.054690  | 0.169118      | 0.114427 | 0.043765 | 1460   |
| 232133958 | 0.077405  | 0.217299      | 0.13989  | 0.05578  | 1460   |
| 232135418 | 0.078157  | 0.267802      | 0.189645 | 0.072514 | 1460   |



Q5

The minimum amount of available buffer space is 5840. I don't fidn any sign of network congestion.

Q6

No, there aren't. Other wise it should have two segments have same sequence number.

Q7

Before segment 61, the receiver acknowledges each packet individually. However, after segment 61, for example in segment 61, the ACK=232169901 acknowledges two segment 232166981 and 232168441.

Q8

The mount of data is the ack of segment 202 minus the ack of segment4, which is $232293102-232129013=164089$ bytes.

And the time is $5.455830-0.026477=5.4294$ second.

So the throughput should be $164089/5.4294=30222.49235643$ Byte/sec.







Excersice  2

Q1

The sequence number is 2818463618.

Q2

The sequence number is 1247095790. ACK value is 2818463619. The value is added by one.

Q3

Sequence number is 2818463619, ACK is 1247095791. The segment doesn't contain any data.

Q4

The client and the server close simultaneous. Because they send FIN to each other in the same time.

Q5

The data sent is the sequence number of segment 308 minus the sequence number of segment 296 and minus 1.

$1247095831-1247095790-1=40$

The data is 40 Bytes.