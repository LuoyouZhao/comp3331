### Lab 3

#### Luoyou Zhao z5225024

***

Exercise 3

Q1)

The ip address is 23.185.0.1. Type A



Q2)

The canonical name is fe1.edge.pantheon.io.



Q3)

 The machine can use DNS name servers that shown in the authority section  to find out the ip address of the website. The addition section contains the IP address of these name servers.



Q4)

The ip address of my local name server is 129.94.242.2



Q5)

The name servers and the are corresponding ip addresses are:

| name server           | ip address      |
| --------------------- | --------------- |
| adns1.berkeley.edu    | 128.32.136.3    |
| adns2.berkeley.edu    | 128.32.136.14   |
| adns3.berkeley.edu    | 192.107.102.142 |
| ns.eecs.berkeley.edu. | 169.229.60.153  |
| ns.CS.berkeley.edu    | 169.229.60.61   |

 Type A.



Q6)

The name is a.root-servers.net. nstld.verisign-grs.com. Type A



Q7) 

I think I get the authoritative answers both by querying to 192.94.242.2 and 192.94.242.33.

| name server   | ip address    |
| ------------- | ------------- |
| ns1.yahoo.com | 68.180.131.16 |
| ns2.yahoo.com | 68.142.255.16 |
| ns3.yahoo.com | 27.123.42.42  |
| ns4.yahoo.com | 98.138.11.157 |
| ns5.yahoo.com | 202.165.97.53 |

Q8)

The result does not contain either answer section nor authority section. It means the Berkeley's name servers doesn't associate with yahoo.com.



Q9)

Type A.



Q10)

1. By querying to my name server(192.94.242.2), get 

   name server f.root-servers.net(192.5.5.241).

2.  By querying to f.root-servers.net(192.5.5.241), get name server t.au(65.22.199.1)

3. By querying to t.au(65.22.199.1), get name server ns2.unsw.edu.au(129.94.0.193)

4. By querying tons2.unsw.edu.au(129.94.0.193), get ip addresses.

During this process, the mechine queries to four DNS servers.