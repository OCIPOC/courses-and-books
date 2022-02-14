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
When the traffic increases, one server is not enough. It makes sense to separate the Web Tier and the Database Tier. Such a separation will allow to scale out each tier independently. 
<table width="256px">
  <tr>
    <td><img src="../images/ch1-server-db.png" /></td>
  </tr>
</table>


## Which databases to use?
There are two types of databases: [Relational](https://en.wikipedia.org/wiki/Relational_database) (SQL) and [NoSQL](https://en.wikipedia.org/wiki/NoSQL) databases. Relational databases organize the data in tables with relations. For example, think about an online e-commerce system. We can organize the data in Customers and Orders tables, where for each customer, there are multiple entries in the Orders Table (aka one-to-many relation). An [SQL language](https://www.w3schools.com/sql/sql_intro.asp) is used to query the data in Relational Databases. The most popular Relation Databases are MySQL, Oracle, PostgreSQL.
NoSQL databases are comparably new and used when dealing with unstructured data, huge volumes of data, or when a low-latency data access is required. There are four families of NoSQL databases
- Key-Value databases
- Document databases 
- Graph Databases
- Column Databases  

Some popular NoSQL databases are CouchDB, DynamoDB, Cassandra. Neo4j, Redis, etc.

## Vertical scaling vs horizontal scaling
We can increase the power of the software component by scaling it [up](https://en.wikipedia.org/wiki/Scalability) (Vertical) or [out](https://en.wikipedia.org/wiki/Scalability) (Horizontal). Scaling up is just adding additional hardware. For example, we scale up a MySQL database by increasing the number of CPU cores of the underlying server. On the other hand, we can scale out software components by increasing the number of underlying servers. For example, we scale out MongoDB by increasing the number of underlying machines. 
Each of the methods has its limitation. We cannot scale up [infinitely](). There are certain hard limits for the number of CPU cores, RAM, and network bandwidth on each server. Another point is that the Vertical scaling doesn't have failover or redundancy. The Horizontal Scaling doesn't work in some cases too. Some software components (example: Relational Databases) cannot scale out. 


## Load balancer
A load balancer evenly distributes incoming traffic among web servers defined in a load-balanced set.
<table width="256px">
  <tr>
    <td><img src="../images/ch1-load-balancer.png" /></td>
  </tr>
</table>

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

