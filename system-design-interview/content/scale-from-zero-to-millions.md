# CHAPTER 1: SCALE FROM ZERO TO MILLIONS OF USERS

## Introduction
This chapter focuses on the foundations of high-scale architecture. One of the best ways of learning architecture patterns is to design a single server system and then gradually scale it up to support more load.

## Single Server Setup
The Single Server setup is simple - all components, line web servers, databases, caches, etc are running on a single machine. 
<table width="256px">
  <tr>
    <td><img src="../images/chapter1-single-server.png" /></td>
  </tr>
</table>
The flow is straightforward as well:
- User that using a browser or a smartphone, access the web server by using the domain name.
- The domain name is resolved in some a DNS server like [Route53](), [OpenDNS]()



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

