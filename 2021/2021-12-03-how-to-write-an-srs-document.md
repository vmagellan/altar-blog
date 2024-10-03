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
---

During my career, I’ve seen dozens of SRS documents for projects ranging in size using both agile and waterfall development methodologies

Some were better than others, but critically, I can now easily spot a good one, from one that will get ignored.

And if no one reads your SRS you will be left with problems like conflicts in features, unrelated data, team members not understanding whether or not the feature they’re building aligns with what the product team have asked for, the list goes on.

Throughout this article, I will delve into what it takes to create one that will serve as a singular source of truth for your development process. An SRS that everyone involved in the process can refer to drive engineering decisions and create preliminary development tickets for the dev planning stage. Thus increasing the chances of successfully executing the technical part of your product.

But first, I want to make a quick point on when you should (and should not) use one.

.elementor-12941 .elementor-element.elementor-element-e56f4e6{--display:flex;--flex-direction:column;--container-widget-width:100%;--container-widget-height:initial;--container-widget-flex-grow:0;--container-widget-align-self:initial;--background-transition:0.3s;}.elementor-12941 .elementor-element.elementor-element-f8d1905{--box-background-color:var( --e-global-color-f6f9b04 );--box-border-color:var( --e-global-color-secondary );--box-border-width:1px;--box-border-radius:12px;--box-padding:12px;--header-color:var( --e-global-color-text );--separator-width:0px;--item-text-decoration:underline;--item-text-hover-decoration:underline;--marker-color:var( --e-global-color-primary );--marker-size:5px;}.elementor-12941 .elementor-element.elementor-element-f8d1905 .elementor-toc\_\_spinner{color:var( --e-global-color-secondary );fill:var( --e-global-color-secondary );}.elementor-12941 .elementor-element.elementor-element-f8d1905 .elementor-toc\_\_header, .elementor-12941 .elementor-element.elementor-element-f8d1905 .elementor-toc\_\_header-title{font-family:"Poppins", sans-serif;font-size:2.25rem;font-weight:700;text-transform:capitalize;line-height:1.2;}.elementor-12941 .elementor-element.elementor-element-f8d1905 .elementor-toc\_\_list-item{font-family:var( --e-global-typography-45f602c-font-family ), sans-serif;font-size:var( --e-global-typography-45f602c-font-size );font-weight:var( --e-global-typography-45f602c-font-weight );line-height:var( --e-global-typography-45f602c-line-height );letter-spacing:var( --e-global-typography-45f602c-letter-spacing );word-spacing:var( --e-global-typography-45f602c-word-spacing );}.elementor-12941 .elementor-element.elementor-element-f8d1905 > .elementor-widget-container{padding:32px 32px 32px 32px;}@media(max-width:1024px){.elementor-12941 .elementor-element.elementor-element-f8d1905 .elementor-toc\_\_list-item{font-size:var( --e-global-typography-45f602c-font-size );line-height:var( --e-global-typography-45f602c-line-height );letter-spacing:var( --e-global-typography-45f602c-letter-spacing );word-spacing:var( --e-global-typography-45f602c-word-spacing );}}@media(max-width:767px){.elementor-12941 .elementor-element.elementor-element-f8d1905 .elementor-toc\_\_list-item{font-size:var( --e-global-typography-45f602c-font-size );line-height:var( --e-global-typography-45f602c-line-height );letter-spacing:var( --e-global-typography-45f602c-letter-spacing );word-spacing:var( --e-global-typography-45f602c-word-spacing );}} /\*! elementor-pro - v3.19.0 - 07-02-2024 \*/<br /> .elementor-widget-table-of-contents .elementor-toc\_\_header-title{color:var(--header-color)}.elementor-widget-table-of-contents.elementor-toc--collapsed .elementor-toc\_\_toggle-button--collapse,.elementor-widget-table-of-contents:not(.elementor-toc--collapsed) .elementor-toc\_\_toggle-button--expand{display:none}.elementor-widget-table-of-contents .elementor-widget-container{min-height:var(--box-min-height);border:var(--box-border-width,1px) solid var(--box-border-color,#9da5ae);border-radius:var(--box-border-radius,3px);background-color:var(--box-background-color);transition:min-height .4s;overflow:hidden}.elementor-toc\_\_header{display:flex;align-items:center;justify-content:space-between;padding:var(--box-padding,20px);background-color:var(--header-background-color);border-bottom:var(--separator-width,1px) solid var(--box-border-color,#9da5ae)}.elementor-toc\_\_header-title{font-size:18px;margin:0;color:var(--header-color)}.elementor-toc\_\_toggle-button{cursor:pointer;display:inline-flex}.elementor-toc\_\_toggle-button i{color:var(--toggle-button-color)}.elementor-toc\_\_toggle-button svg{height:1em;width:1em;fill:var(--toggle-button-color)}.elementor-toc\_\_spinner-container{text-align:center}.elementor-toc\_\_spinner{font-size:2em}.elementor-toc\_\_spinner.e-font-icon-svg{height:1em;width:1em}.elementor-toc\_\_body{padding:var(--box-padding,20px);max-height:var(--toc-body-max-height);overflow-y:auto}.elementor-toc\_\_body::-webkit-scrollbar{width:7px}.elementor-toc\_\_body::-webkit-scrollbar-thumb{background-color:#babfc5;border-radius:10px}.elementor-toc\_\_list-wrapper{list-style:none;padding:0}.elementor-toc\_\_list-item{margin-bottom:.5em}.elementor-toc\_\_list-item.elementor-item-active{font-weight:700}.elementor-toc\_\_list-item .elementor-toc\_\_list-wrapper{margin-top:.5em;margin-left:var(--nested-list-indent,1em)}.elementor-toc\_\_list-item-text:hover{color:var(--item-text-hover-color);-webkit-text-decoration:var(--item-text-hover-decoration);text-decoration:var(--item-text-hover-decoration)}.elementor-toc\_\_list-item-text.elementor-item-active{color:var(--item-text-active-color);-webkit-text-decoration:var(--item-text-active-decoration);text-decoration:var(--item-text-active-decoration)}.elementor-toc\_\_list-item-text-wrapper{display:flex;align-items:center}.elementor-toc\_\_list-item-text-wrapper:before,.elementor-toc\_\_list-item-text-wrapper i{margin-right:8px;color:var(--marker-color)}.elementor-toc\_\_list-item-text-wrapper svg{margin-right:8px;fill:var(--marker-color);height:var(--marker-size,.5em);width:var(--marker-size,.5em)}.elementor-toc\_\_list-item-text-wrapper i{font-size:var(--marker-size,.5em)}.elementor-toc\_\_list-item-text-wrapper:before{font-size:var(--marker-size,1em)}.elementor-toc--content-ellipsis .elementor-toc\_\_list-item-text{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.elementor-toc\_\_list-items--collapsible>.elementor-toc\_\_list-wrapper>.elementor-toc\_\_list-item>.elementor-toc\_\_list-wrapper{display:none}.elementor-toc\_\_heading-anchor{position:absolute}.elementor-toc\_\_body .elementor-toc\_\_list-item-text{color:var(--item-text-color);-webkit-text-decoration:var(--item-text-decoration);text-decoration:var(--item-text-decoration)}.elementor-toc\_\_body .elementor-toc\_\_list-item-text:hover{color:var(--item-text-hover-color);-webkit-text-decoration:var(--item-text-hover-decoration);text-decoration:var(--item-text-hover-decoration)}.elementor-toc\_\_body .elementor-toc\_\_list-item-text.elementor-item-active{color:var(--item-text-active-color);-webkit-text-decoration:var(--item-text-active-decoration);text-decoration:var(--item-text-active-decoration)}ol.elementor-toc\_\_list-wrapper{counter-reset:item}ol.elementor-toc\_\_list-wrapper .elementor-toc\_\_list-item{counter-increment:item}ol.elementor-toc\_\_list-wrapper .elementor-toc\_\_list-item-text-wrapper:before{content:counters(item,".") ". "}

#### Contents

## Do You Really Need an SRS Document?

The short answer to this question is:

**Usually an early version of a startup product or MVP doesn’t consist of enough features to need an SRS Document**

Thanks to lean and agile methodologies, two kids with little or no experience can literally build an app in their dorm room.

This has caused a paradigm shift. Nowadays startup teams get in the trenches, get hands-on and tend to leave processes like SRS documentation behind.

Even here at Altar, we’ve helped more than a few founders build products that have gone on to raise millions ([like this company for example](https://www.finextra.com/newsarticle/34583/swiss-regtech-apiax-secures-66-million-series-a)) without using an SRS document. We usually only use an SRS document on medium to large projects that consist of over 50 screens and more than two services, for example.

If you’re building a big product, keep reading and I’ll take you through everything you need to write your SRS.

If you’re building a standard MVP or the first iteration of your product, it may be enough to explain your product to your development team in terms of [product scope](https://altar.io/structured-process-develop-mvp/), epics or using a BPMN diagram if you have one or high fidelity prototypes.

.elementor-16418 .elementor-element.elementor-element-fa6400f{--display:flex;--flex-direction:column;--container-widget-width:100%;--container-widget-height:initial;--container-widget-flex-grow:0;--container-widget-align-self:initial;--overflow:hidden;--background-transition:0.3s;--border-radius:12px 12px 12px 12px;}.elementor-16418 .elementor-element.elementor-element-283e311{--display:flex;--flex-direction:row;--container-widget-width:initial;--container-widget-height:100%;--container-widget-flex-grow:1;--container-widget-align-self:stretch;--gap:64px 64px;--background-transition:0.3s;}.elementor-16418 .elementor-element.elementor-element-283e311:not(.elementor-motion-effects-element-type-background), .elementor-16418 .elementor-element.elementor-element-283e311 > .elementor-motion-effects-container > .elementor-motion-effects-layer{background-color:#F4FAFE;}.elementor-16418 .elementor-element.elementor-element-283e311, .elementor-16418 .elementor-element.elementor-element-283e311::before{--border-transition:0.3s;}.elementor-16418 .elementor-element.elementor-element-857117e{--display:flex;--flex-direction:row;--container-widget-width:initial;--container-widget-height:100%;--container-widget-flex-grow:1;--container-widget-align-self:stretch;--background-transition:0.3s;}.elementor-16418 .elementor-element.elementor-element-857117e.e-con{--flex-grow:0;--flex-shrink:0;}.elementor-16418 .elementor-element.elementor-element-e6af329 img{width:100%;max-width:100%;height:100%;object-fit:cover;object-position:bottom right;}.elementor-16418 .elementor-element.elementor-element-e6af329{width:100%;max-width:100%;bottom:-44px;}body:not(.rtl) .elementor-16418 .elementor-element.elementor-element-e6af329{right:0px;}body.rtl .elementor-16418 .elementor-element.elementor-element-e6af329{left:0px;}.elementor-16418 .elementor-element.elementor-element-ec0de51{--display:flex;--flex-direction:column;--container-widget-width:100%;--container-widget-height:initial;--container-widget-flex-grow:0;--container-widget-align-self:initial;--gap:24px 24px;--background-transition:0.3s;--padding-block-start:112px;--padding-block-end:112px;--padding-inline-start:0px;--padding-inline-end:44px;}.elementor-16418 .elementor-element.elementor-element-ec0de51.e-con{--flex-grow:1;--flex-shrink:1;}.elementor-16418 .elementor-element.elementor-element-c168e59{--display:flex;--flex-direction:column;--container-widget-width:100%;--container-widget-height:initial;--container-widget-flex-grow:0;--container-widget-align-self:initial;--background-transition:0.3s;}.elementor-16418 .elementor-element.elementor-element-4aeb8ec .elementor-heading-title{font-family:"Poppins", sans-serif;font-size:32px;font-weight:700;}.elementor-16418 .elementor-element.elementor-element-8e0cd20{color:#000000;}@media(min-width:768px){.elementor-16418 .elementor-element.elementor-element-857117e{--width:360px;}}@media(max-width:767px){.elementor-16418 .elementor-element.elementor-element-283e311{--padding-block-start:40px;--padding-block-end:40px;--padding-inline-start:var(--safe-margin);--padding-inline-end:var(--safe-margin);}.elementor-16418 .elementor-element.elementor-element-857117e{--min-height:300px;}body:not(.rtl) .elementor-16418 .elementor-element.elementor-element-e6af329{right:0px;}body.rtl .elementor-16418 .elementor-element.elementor-element-e6af329{left:0px;}.elementor-16418 .elementor-element.elementor-element-e6af329{bottom:-76px;}.elementor-16418 .elementor-element.elementor-element-ec0de51{--padding-block-start:40px;--padding-block-end:0px;--padding-inline-start:0px;--padding-inline-end:0px;}} 

![Claudio, CTO of Altar, Product and Software development company specialising in building MVPs, full custom software development projects & creating UX/UI that is both functional and beautiful](images/cta-colors-claudio-happy.png)



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

1. Introduction 1.1 Purpose 1.2 Intended Audience 1.3 Intended Use 1.4 Scope 1.5 Definitions and Acronyms
2.  Overall Description 2.1 User Needs 2.2 Assumptions and Dependencies
3.  System Features and Requirements 3.1 Functional Requirements 3.2 External Interface Requirements 3.3 System Features 3.4 Nonfunctional Requirements

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
