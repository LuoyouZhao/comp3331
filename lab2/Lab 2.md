### Lab 2

#### Luoyou Zhao z5225024

***

##### Exercise 3

Q1

The status code is 200 and phrase is OK.

Q2

The last modified day is Tue, 23 Sep 2003 05:29:00 GMT. The response contains a DATA header.

Q3

Base on

> Connection : Keep-Alive

the connection established between the browser and the server is persistent.

Q4

The client sends 73 bytes of data.

Q5

> <html>\n
>
> Congratulations. You've downloaded the file lab2-1.html!\n
>
> <html>\n

##### Exercise 4

Q1

No

Q2

The last modified time is Tue, 23 Sep 2003 05:35:00 GMT.

Q3

The If-modified-Since is Tue, 23 Sep 2003 05:35:00 GMT and the If-None-Match is "1bfef-173-8f4ae900".

Q4

The status code is "304 Not Modified". The server didn't return the file. Because the brower was called that the server didn't modified the file since Tue, 23 Sep 2003 05:35:00 GMT, that means brower could use the cached file.

Q5

Etag is "1bfef-173-8f4ae900". Instead of sending the full file, web brower can use Etag to check if the content has been changed or not. 

This value haven't changed.