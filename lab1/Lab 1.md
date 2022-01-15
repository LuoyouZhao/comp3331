### Lab 1

#### Luoyou Zhao z5225024

***

Exercise 1

1. www.koala.com.au has three different IP addresses, 104.18.61.21, 172.67.219.46, and 104.18.60.21. The website may want to balance the work of several servers by having different IP addresses.![截屏2020-06-09 下午2.56.34](/Users/zhaoluoyou/Desktop/截屏2020-06-09 下午2.56.34.png)

2. The name of IP address 127.0.0.1 is localhost. This is the IP address of this computer.

Exercise 2

www.unsw.edu.au](http://www.unsw.edu.au/), [www.mit.edu](http://www.mit.edu/), [www.intel.com.au](http://www.intel.com.au/), [www.tpg.com.au](http://www.tpg.com.au/), [www.amazon.com](http://www.amazon.com/), and [www.tsinghua.edu.cn](http://www.tsinghua.edu.cn/) is reachable. 

[www.kremlin.ru](http://www.kremlin.ru/) is not reachable by ping command but can be reached by Web browser. This could because of this russian website has some security measure to protect its website form ping command. 

[www.hola.hp](http://www.hola.hp/) and [www.getfittest.com.au](http://www.getfittest.com.au/) are not exist, so they cannot be reachable.

Exercise 3

1. The following picture shows there are 22 routers between my work station and [www.columbia.edu ](http://www.columbia.edu/). And the first 5 routes are part of UNSW network. Thr delay from route 7 to 8 nearly double, so  these two route  cross the Pacific Ocean.![截屏2020-06-09 下午3.53.01](/Users/zhaoluoyou/Desktop/截屏2020-06-09 下午3.53.01.png)

2. + UCLA![截屏2020-06-09 下午4.17.28](/Users/zhaoluoyou/Desktop/截屏2020-06-09 下午4.17.28.png)

   + u-Tokyo![截屏2020-06-09 下午4.25.47](/Users/zhaoluoyou/Library/Application Support/typora-user-images/截屏2020-06-09 下午4.25.47.png)

   + Lancaster![截屏2020-06-09 下午4.28.06](/Users/zhaoluoyou/Desktop/截屏2020-06-09 下午4.28.06.png)

     As the three pictures shows, the paths diverge from route 6, in route 7, these paths go to three different toutes. By Whois command, I find this route is an Asia Pacidic Network Information centre.![截屏2020-06-09 下午4.30.08](/Users/zhaoluoyou/Desktop/截屏2020-06-09 下午4.30.08.png)

     And there is no relation between the number of hops and the physical distance. 

     ***

     Distance between UNSW and Lancaster: 16,984 km 

     Routes Number: 23

     ***

     Distance between UNSW and UCLA:  12,051 km 

     Routes Number: 50+

     ***

3. + My IP address is 192.168.101.255,  www.lancaster.ac.uk IP address is 148.88.65.80. And I am using https://www.telstra.net/cgi-bin/trace to run trace route.
   + the reverse path go through different routers and different IP addresses as forward path. 

Exercise 4

1. Distance between UNSW and UQ : 921.3 km, the delay should be 3.07100 milliseconds

   Distance between UNSW and DLSU : 6,266 km, the delay should be 20.8866667 milliseconds

   Distance between UNSW and Berlin Institute of Technology : 16,095 km, the delay should be 53.65 milliseconds

   Clearly, the actual delay is far more than the thoretical delay. First, the distance above is distance as the crow flies, but the distance of cable should be larger. Second, light is reflexing in the cable, so the velocity of light in cable is slower than the therotical velocity.

2. As we can see, the delay to the destination is random. Because it could be affected by many factors such as network congestion, the size of packet, or the physical distance.

3. By using trace route command, I find the first 11 routes are still in Australia, and suddenly jump to a new IP address. By google this IP address, 104.20.229.42, I find it i belongs to CloudFlare Inc. in California, USA.![截屏2020-06-09 下午6.59.52](/Users/zhaoluoyou/Desktop/截屏2020-06-09 下午6.59.52.png)

4. The propagation delay has nothing to do with packet size. Queuing delay depends on network congestion instead of how big the file is. Processing and transmission delay are affected by packet size, and transmission delay is more efluenced than Processing delay.







