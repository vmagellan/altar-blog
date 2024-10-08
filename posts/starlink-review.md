---
title: "Hands-On Starlink Review: Does it Live Up to the Hype?"
date: "2022-07-27"
categories:
  - "tech-knowledge"
coverImage: "Starlink-Unbox-over-shoulder.png"
slug: starlink-review
author: Claudio Teixeira
---

Recently, SpaceX launched Starlink in Portugal. So, naturally, I got one for Altar as soon as the pre-orders opened.

A couple of weeks ago, the sleek satellite dish finally arrived. In no time at all, a couple of devs from my team and I had unboxed it and set it up in the garden outside our offices.

https://altar.io/wp-content/uploads/2021/10/altarXstarlink.mp4

Fast forward to today, and I’ve had the opportunity to use Starlink, as well as run some tests.

I’ll go through those later in the article, but first I want to talk about my initial impressions.

## Starlink Unboxing & First Impressions

Inside the large grey Starlink packaging, you’ll find:

- The Starlink, motorised, satellite dish– connected to a 30-meter (100 foot) Power-over-Ethernet (PoE) cable
- A metal tripod stand
- A power adaptor
- A small metal Wi-Fi Router with its own PoE cable.

![Starlink box contents](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/Starlink-unbox-1-1024x573.png)

The initial set-up was incredibly simple:

Click the dish into the tripod mount, plug the PoE cables from both the router and the dish into the power adaptor, plug it into the wall socket, download the app and you’re ready to go.

The hardware is well designed, especially the metal Wi-Fi router, which looks like it’s been freshly carved out of a Cybertruck.

The dish itself is plastic mounted on a metal pole. The PoE cable is permanently attached to the dish. I feel this last part is worth noting – without a way to easily detach the PoE cable from the dish, you could face having to replace the whole dish if the cable gets damaged.

To run it out of your house you’re looking at either drilling a hole in the wall or permanently leaving a window open as the cable is quite thick (7mm) and includes an even thicker ferrite bead (19mm).

The app is also well designed, with the consistent UX you would expect from a company like SpaceX. The seamless setup continues here with no login requirements – keeping the experience truly “plug and play”.

![Starlink App Key Screens](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/Starlink-App-Collage-1024x471.png)

This brings me to the crux of this article, the internet tests.

## Starlink Setup & Internet Tests

To cut a long story short, Starlink offers a moderately fast, if somewhat inconsistent, broadband connection – **under the right circumstances**.

I initially set up Starlink in the garden outside our offices. Despite the fact there were no obstructions directly above the dish, the garden is located in the centre of the building, and is surrounded on all sides.

This was enough of an obstruction to mean that I wasn’t able to connect to the internet using Starlink (after 30 minutes of adjusting the dish positioning).

It’s worth noting here, however, that Starlink’s value proposition is not for inner-city use. Rather, its goal is to bring high-speed internet to rural areas.

So, I packed Starlink back up, popped it in the back of my car and headed home to run some further tests.

I set Starlink up in my garden initially, 5 meters away from the house. Despite it being much more of an open space vs. the office, the height of my house (~7 meters) still obstructed the satellite dishes view.

So, once I had run all the intended tests, I moved Starlink to an open field with no obstructions and repeated my tests.

Aside from the placement of the dish (garden/obstructed & field/unobstructed) I kept all other aspects of the testing parameters the same.

Here are the results:

### Testing Information

**ISP:** SpaceX Services, Inc.

**External IP address:** 217.65.138.\*\*\*.

Access to 1700 Starlink satellites orbiting at 550km of altitude, operating downlinks between 10.7Ghz and 29.1GHz.

**Distance between Device (Android 11 Smartphone) and Access Point WiFi:** 2m

**RSSI:** -62dBm  (Good)

**Noise:** -80dBm (Good)

**Method used:** [Ookla SpeedTest](https://www.speedtest.net/) using the Native Android Application.

A Speed Test estimates the available capacity of the network between the client and the server.

The throughput of the tests depends on the distance between the 2 endpoints (Round Trip Time), meaning the closest server will give the most accurate results. The Ookla app automatically chose my server.

Per the Association for Computing Machinery (ACM) Recommendation, I executed the tests at randomly selected times throughout the day (including peak and off peak time).

![Claudio, CTO of Altar, Product and Software development company specialising in building MVPs, full custom software development projects & creating UX/UI that is both functional and beautiful](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/cta-colors-claudio-happy.png)

##### Looking for Software Development Services?

Get straight to the point, jargon-free advice from a tech expert that has been building award-winning Startups for the past 10 years.

Let's Talk

Test #1: Throughput (Downstream, Upstream)

Using the Native Ookla Application, I took 31 measurements at random intervals over two days against the fastest nearby server (automatically selected by the Ookla app).

![Ookla Speedtest results using starlink at random intervals](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/Starlink-Ookla-Final-509x1024.jpeg)

Here are the throughput results for both the obstructed and unobstructed conditions:

![Average, Median, Maximum & Minimum throuput results](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/Starlink-Throughput-Graph.png)

Once I had completed the throughput tests, I moved on to test Latency & Timeouts

### Test #2: Latency & Timeouts

For this test, I carried out a continuous measurement over 260 mins. The goal here was to measure the number of timeouts that occur under both the obstructed and unobstructed scenarios.

In the obstructed scenario (in my garden, 5 meters from my ~7 meters tall house) I observed 576 timeouts over the 260-minute test.

Meaning, there was the chance of an outage every minute:

![Starlink Ping Timeouts under obstructed conditions](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/Ping-Timeouts-Obstructed.png)

In contrast, in the unobstructed scenario (open field) I observed 47 timeouts over the 260-minute test.

Now, the chance of an outage had reduced to once every ~5 minutes:

![Starlink Ping Timeouts under unobstructed conditions](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/Ping-Timeouts-Unobstructed.png)

## Key Takeaways

There are no two ways about it, for optimal connection, where you position the dish is paramount.

In an unobstructed scenario, I had no problem working using Starlink. I was able to keep a database connection most of the time, whilst streaming Spotify, downloading files and browsing the internet.

In an obstructed scenario, however, it was almost unusable for work. There were simply too many outages. My connection was interrupted too often, my database connection was unstable and I often had to refresh web pages and wait before they would work.

That being said, for normal smartphone usage, there were no noticeable differences between the obstructed and unobstructed scenarios. By “normal smartphone usage” I mean music/[video streaming](https://www.movavi.com/support/how-to/how-to-capture-streaming-video.html) and using social media/chat apps).

In terms of power consumption, Starlink runs at about 100W – although this can vary if the dishes motors are active.

I haven’t observed any overheating or thermal issues with any of the kit parts and the dish seems to sit at a comfortable 23ºC - 25ºC when in use.

![Starlink Thermal Tests](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/Starlink-Thermals-Collage-1024x435.png)

## Is Starlink a True Competitor to Rural Cable Broadband?

In rural areas with a good internet infrastructure (basic fibre optic for example), Starlink can’t compete at this time.

In areas where minimum cable broadband connections are unstable, however, is where Starlink starts to compete.

The other bonus of Starlink is the fact it doesn’t come with a contract. Therefore, if you’re heading to a rural area temporarily (where a 24-month contract wouldn’t be worth it)  then it may be work installing a Starlink kit.

After all, once you’ve bought the kit it’s yours, and although you can’t resell it, if you don’t end up using it, it could make a nice (if very expensive) coffee table.

## Wrapping Up

Starlink is a remarkable feat of engineering and SpaceX’s ability to turn it into a consumer product is impressive.

That being said, traditional cable companies won't be overthrown by Starlink any time soon.

Firstly, it carries a hefty price tag. The equipment costs €500 plus an added monthly service fee of €99 here in Portugal.

It’s a lot to pay for, in the best-case scenario, the reasonable broadband speeds with inconsistent connectivity and large swings in latency that Starlink offers.

Perhaps this will change as SpaceX launches more satellites. We may well see it work better when surrounded by tall trees or buildings, but that remains to be seen.

However, I do believe that the traditional telecom companies should take note of Starlink. The execution of the product and the hype and excitement of a democratised internet connection should serve as a warning.

A warning that people don’t want to be tied down to a 24-month contract just to get a decent internet connection – and that disruption is coming.
