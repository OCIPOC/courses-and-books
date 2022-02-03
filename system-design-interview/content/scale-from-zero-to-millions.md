# CHAPTER 1: SCALE FROM ZERO TO MILLIONS OF USERS

## Introduction
This chapter focuses on the foundations of high-scale architecture. One of the best ways of learning architecture patterns is to design a single server system and then gradually scale it up to support more load.

## Single Server Setup
The Single Server setup is simple - all components, like web servers, databases, caches, etc are running on a single machine. 
<table width="256px">
  <tr>
    <td><img src="../images/chapter1-single-server.png" /></td>
  </tr>
</table>
  
The flow is straightforward as well:
- User accesses the web server by using the domain name from a browser or a smartphone 
- The domain name is resolved in some a DNS server like [Route53](https://en.wikipedia.org/wiki/Amazon_Route_53) or [OpenDNS](https://en.wikipedia.org/wiki/OpenDNS).
- Once the IP is obtained, an HTTP request is sent to the Web Server
- Web Server responses by sending HTML or JSON 


## Database

## Which databases to use?

## Vertical scaling vs horizontal scaling

## Load balancer

## Database replication

## Cache
- Cache Tier
- Consideration for using Cache

## Content delivery network (CDN)

## Stateful Architecture

## Stateless Architecture

## Message queue

## Logging, metrics, automation

## Database scaling
- Vertical
- Horizontal

