---
title: "How to Write a Software Requirements Specification (SRS) Document in 5 Steps"
date: "2021-12-03"
categories:
  - "tech-knowledge"
tags:
  - "entrepreneurship"
  - "guide"
  - "software-development"
  - "tech-team"
  - "technology"
coverImage: "gabrielle-henderson-HJckKnwCXxQ-unsplash-scaled-1.jpg"
slug: how-to-write-an-srs-document
author: Claudio Teixeira
---

During my career, I’ve seen dozens of SRS documents for projects ranging in size using both agile and waterfall development methodologies

Some were better than others, but critically, I can now easily spot a good one, from one that will get ignored.

And if no one reads your SRS you will be left with problems like conflicts in features, unrelated data, team members not understanding whether or not the feature they’re building aligns with what the product team have asked for, the list goes on.

Throughout this article, I will delve into what it takes to create one that will serve as a singular source of truth for your development process. An SRS that everyone involved in the process can refer to drive engineering decisions and create preliminary development tickets for the dev planning stage. Thus increasing the chances of successfully executing the technical part of your product.

But first, I want to make a quick point on when you should (and should not) use one.

#### Contents

## Do You Really Need an SRS Document?

The short answer to this question is:

**Usually an early version of a startup product or MVP doesn’t consist of enough features to need an SRS Document**

Thanks to lean and agile methodologies, two kids with little or no experience can literally build an app in their dorm room.

This has caused a paradigm shift. Nowadays startup teams get in the trenches, get hands-on and tend to leave processes like SRS documentation behind.

Even here at Altar, we’ve helped more than a few founders build products that have gone on to raise millions ([like this company for example](https://www.finextra.com/newsarticle/34583/swiss-regtech-apiax-secures-66-million-series-a)) without using an SRS document. We usually only use an SRS document on medium to large projects that consist of over 50 screens and more than two services, for example.

If you’re building a big product, keep reading and I’ll take you through everything you need to write your SRS.

If you’re building a standard MVP or the first iteration of your product, it may be enough to explain your product to your development team in terms of [product scope](https://altar.io/structured-process-develop-mvp/), epics or using a BPMN diagram if you have one or high fidelity prototypes.

![Claudio, CTO of Altar, Product and Software development company specialising in building MVPs, full custom software development projects & creating UX/UI that is both functional and beautiful](https://raw.githubusercontent.com/vmagellan/altar-blog/main/posts/images/cta-colors-claudio-happy.png)

##### Looking for Software Development Services?

Get straight to the point, jargon-free advice from a tech expert that has been building award-winning Startups for the past 10 years.

Let's Talk

## What Is a Software Requirements Specification (SRS) Document?

The software requirements specification (SRS) is a document providing a detailed overview of your software product, purpose, requirements and features.

A typical SRS document  includes:

- **The purpose of your product** – including its intended audience, intended use & product scope.
- **An overview of your product** – including your users’ needs and the assumptions and dependencies surrounding your product.
- **A Detailed rundown of your specific requirements** – including functional requirements, interface requirements, system features and non-functional requirements.

Now let’s go over how it can benefit you.

## Why Create an SRS Document?

An SRS acts as the blueprint for your project, that every team involved in the development process will follow.

It keeps everyone on the same page, from the development team, quality assurance team, operations, maintenance and product team.

The software requirements specification document can also help you make decisions about your product during its lifecycle – e.g. when to build a new feature, or sunset a feature that has become redundant - or your users simply ignore.

Importantly, however, when done correctly an SRS can and should reduce your development time and costs.

Not let’s look at how you can create a comprehensive SRS document.

## How to Write an SRS Document in 5 Steps

### 1\. Create an Outline

Like with drafting any kind of document, it’s critical you start with the structure, and an SRS is no different.

If you decide to create one for yourself here is a basic, lightweight, incomprehensive outline to give you an idea:

#### Software Requirements Specification (SRS) Document Outline

1.  Introduction 1.1 Purpose 1.2 Intended Audience 1.3 Intended Use 1.4 Scope 1.5 Definitions and Acronyms
2.  Overall Description 2.1 User Needs 2.2 Assumptions and Dependencies
3.  System Features and Requirements 3.1 Functional Requirements 3.2 External Interface Requirements 3.3 System Features 3.4 Nonfunctional Requirements

Once you’ve created a structure for your SRS it’s time to start fleshing it out. That all starts with the purpose.

### 2\. Start With a Purpose

In this section of your SRS document, outline the purpose of the product starting with:

#### Intended Audience/Use

Define which stakeholders will use the SRS and how they will use it. This will most likely include developers, quality assurance, product experts and project managers.

However, it may be relevant to share this document with stakeholders in other departments of such as marketing and sales.

#### Product Scope

Here is where you will describe your product from a business perspective. Include the benefits, objectives, and goals. This will help to align all departments on which direction your product is heading and why.

At Altar, our Product Team created their own process to do just that. Check out [this resource](https://altar.io/features-inside-mvp-3-steps-know-answer/) by our co-founder Daniel for more information. In it, he shares the exact process step by step.

#### Glossary of Terms

Here, define any terms relevant to your product. This will ensure that everyone is on the same page regardless of technical ability or department.

Also, include any references here (i.e. if you have to include any legal or best practice documents).

### 3\. Overview Your Product

In this section, describe the functionality of your product. Outline any informal requirements to give context going to the specific technical requirements explored in the next section.

In short, outline what you’re building, and who you’re building it for.

#### User Needs

It’s vital to outline your user needs (also known as user classes or user characteristics) within your overview.

List any primary or secondary users who will use the product on a regular basis and define their journey through the product.

This will again ensure the whole team is on the same page and focused on your end-user throughout the product development process.

#### Assumptions and Dependencies

This section of your SRS is used to outline any factors that may impede your ability to fulfil the needs of your project.

For example, are you making assumptions around your product that may be false? If they are proven false, what will the plan be to fix it?

Lastly, is your project dependent on any external factors? For example, an integration from a third-party SaaS may cause SLA issues, etc.

### 4\. Detail The System Requirements

Once you have an overview of your product in place, it’s time to become more granular. Keeping in mind your users’ needs it’s time to give a detailed overview of either the use cases of your product, as well as the non-functional requirements.

Let’s begin with a quick outline of use cases and non-functional requirements in an SRS document.

#### How to Write Use Cases in your SRS document

A use case describes how your user will interact with your product, in a simple story format. Creating a use case helps you put yourself in the shoes of the end-user.

To start, create a full list of your product’s end users. Then take those users one by one and:

- Break down their interactions into use cases (one case for one interaction)
- Describe the sequence of events for each case.
- Write a detailed description of what the user does, and how the system will respond

Repeat this process for every user until you’ve completed your list.

#### Non-functional Requirements

Your non-functional requirements are just as important as your functional ones. They include performance, safety, security & quality. Here's an example of how to write a non-functional requirement for a car’s LIDAR sensor:

**_The cars LIDAR sensors shall send data to the dashboard at the rate of 10Mbps up to (and including) 100Mbps._**

Once you have your use cases written and non-functional requirements listed, as well as provided any relevant supplemental information, you’re ready to take it to your stakeholders.

### 5\. Implement Your SRS Document

Once you’ve ensured all the teams are happy, and the document is signed, it’s time to implement it.

Make it accessible to the whole team, either printed or in a PDF on a shared drive. Or even on an MD file in platforms such as confluence, notion or monday.com.

This means presenting the document to all teams involved in your product development process, ticket management platform or code registry.

This is a vital step as if your SRS isn’t consumed regularly, its existence makes no sense.

## Wrapping Up

As I stated at the beginning of this article, in fast-paced startup environments where founders are pushed to move faster and faster, documentation like an SRS is often left behind - and if you have the right team around you, that’s not necessarily a bad thing.

That being said, should you need to create one, it’s important to make sure you follow the best practices listed above.

It will ensure that you create an SRS that clearly communicates the key requirements across all members of your team, reducing development time and costs. With the added benefit that it can help you make decisions about your product’s lifecycle further down the line.

If you have any more questions related to writing an SRS document, [reach out to me here](https://altar.io/start-a-project/) – I’d be happy to answer any questions you may have.

Thanks for reading.
