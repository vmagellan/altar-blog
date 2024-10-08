---
title: "Angulartics2 – A Powerful Analytics tool for Angular Applications"
date: "2019-03-21"
categories:
  - "tech-knowledge"
coverImage: "Angulartics-2-first-image.png"
slug: powerful-analytics-tool-for-angular-applications-angulartics2
author: Joao Ribeiro
---

We’ve created the open-source library [Angulartics2](https://github.com/angulartics/angulartics2) to plug into your Angular single-page app (SPA) for analytics integration. It allows you to do event tracking and it is ready to integrate with Google Analytics, Google Tag Manager, Kissmetrics, Mixpanel, Piwik, Segment, Baidu Analytics and Facebook Pixel.

![Angulartics 2 first image](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/Angulartics-2-first-image.png)

## Problem

Most analytics providers do not automatically track the browser’s navigation history, making it difficult to track single-page applications (SPAs) like Angular applications.

## Simple Solution

To tackle this problem we developed a simple open-source library called [Angulartics2](https://github.com/angulartics/angulartics2). By plugging [Angulartics2](https://github.com/angulartics/angulartics2) in your Angular apps it will automatically track navigation events and send them to your plugged-in Provider, such as [Google Analytics](https://www.google.com/analytics/analytics/#?modal_active=none).

[Angulartics2](https://github.com/angulartics/angulartics2) also comes with easy ways to send custom events to your providers enabling you to easily send any kind of event such as when your users buy an article or download a file. This is mostly useful for tracking conversion within your apps.

## Diving into some simple code snippets

Plugging [Angulartics2](https://github.com/angulartics/angulartics2) into your Angular app is simple and similar to any other module

You have to import Angulartics2Module.forRoot() into your main module and pass an array with the providers you are using.

Then, in you main component you need to pass each provider to the component constructor function. And that’s it, you now have automatic page tracking.

Make sure you also import the RouterModule into your main module. [Angulartics2](https://github.com/angulartics/angulartics2) uses Router to track your app’s current state.

![Claudio, CTO of Altar, Product and Software development company specialising in building MVPs, full custom software development projects & creating UX/UI that is both functional and beautiful](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/cta-colors-claudio-happy.png)

## Tracking custom events

After setting up [Angulartics2](https://github.com/angulartics/angulartics2) you can then easily trigger custom events:

You just need to import **Angulartics2Module.forChild()** in your modules and use **angulartics2On** directive in your templates.

You can also trigger custom events programmatically, by injecting **Angulartics2** service in your components.

[**Angulartics2**](https://github.com/angulartics/angulartics2) is under active development and maintenance and we will be adding new providers based on community’s requests.

We currently support providers for: – [Google Analytics](https://www.google.com/analytics/analytics/#?modal_active=none) – [Google Tag Manager](https://www.google.com/analytics/tag-manager/) – [Kissmetrics](https://www.kissmetrics.com/) – [Mixpanel](https://mixpanel.com/) – [Piwik](https://piwik.org/) – [Segment](https://segment.com/) – [Baidu Analytics](http://tongji.baidu.com/) – [Facebook Pixel](https://www.facebook.com/business/a/facebook-pixel)

As with most good work, this could not be done without the help of great contributors. Many thanks for all the help to [Nathan Walker](https://github.com/NathanWalker), [Jonathan Reyes](https://github.com/jylinman), [Niels Kristian](https://github.com/skovmand), [Roland Oldengarm](https://github.com/rolandoldengarm), [kris](https://github.com/kwv), [Tim Elfelt](https://github.com/timelf123), [Matthew Daniels](https://github.com/MatthewDaniels), [Adam S. Kirschner](https://github.com/hikirsch), [Hongbo Miao](https://github.com/Hongbo-Miao), [Smithi](https://github.com/smith64fx) and [Júlio César](https://github.com/JulioC).
