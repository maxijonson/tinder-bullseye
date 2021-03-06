# Tinder Bullseye

A Python script that searches for people who liked you and likes them back (if you want to).

### Disclaimer

As per Tinder's Terms, under section 6 "Rights Tinder Grants You.":

> [...] you agree not to:
>
> - use any robot, bot, spider, crawler, scraper, site search/retrieval application, proxy or other manual or automatic device, method or process to access, retrieve, index, “data mine,” or in any way reproduce or circumvent the navigational structure or presentation of the Service or its contents.
> - modify, adapt, sublicense, translate, sell, reverse engineer, decipher, decompile or otherwise disassemble any portion of the Service, or cause others to do so.
> - use or develop any third-party applications that interact with the Service or other users’ Content or information without our written consent.
> - use, access, or publish the Tinder application programming interface without our written consent.
> - encourage or promote any activity that violates this Agreement.

That said, I do not encourage anyone to use this tool to their advantage, as it would break their terms of service and could result in a ban and/or legal actions. If you wish to achieve the benefits this app has, **YOU SHOULD BUY TINDER GOLD**. I take no responsability on the consequences you may suffer from using this app.

##### "Why was this app made?"

This tool was solely made to gain experience with the Python programming language and is not intended for actual use. It uses API endpoints that are exposed by the traditionnal use case of Tinder (i.e using their web app to swipe people). It does not attempt to bypass Tinder's systems: \
**The app does not forge fake headers:** Your X-AUTH-TOKEN has to be manually added by grabbing it from the actual web app's network requests. Tinder Bullseye fully shows itself in the User-Agent header (TinderBullseye/1.0.0) \
**The app does not spam endpoints:** The `recs` and `teasers` are called only once during the lifecycle of the app. No loops refetch `recs` specifically to prevent a spamming behaviour. 

##### "How was this app tested?"

On Tinder's official web app, I simply took the response data from my browser's (Chrome) network tab (recs and teasers). After that, I kept that data during development to test the app and its functionnality. Once I was confident the app worked, I added the real endpoints, assuming the data format did not change. \
There is a case that I've tought of where the app could fail: the `teasers` photos do not come from the same source as the `recs` source. This means that if a `teaser`'s photo is not exactly the same as the `rec`'s photo, even if it is the same person, the app will fail.

##### "I am a Tinder representative. I want this app to be removed."

This app is purely for educationnal purposes. If you are a Tinder representative and wish for this app to be removed, you should send an email to tristan.chin@chintristan.io with some proof of your affiliation and it will be removed as soon as possible. However, I do not take responsability for forks. **By forking this project, you assume the risks.**

### Background

A while back, I noticed that the unblurred photos of the people who liked me were fully visible from the network panel in Chrome, even without Gold. I contacted Tinder's security team to tell them. Due to the simplicity of the issue, I wasn't surprised by their answer: they know about it, they just choose not to do anything about it (yet). So, until that "yet" comes, if ever, and since I got a competition (CS Games 2020) to prepare for, I decided to make Tinder Bullseye!

*Update: due to COVID-19 concerns, the CS Games 2020 that were to happen on March 13th 2020 has been postponed until the pandemic threat decreases*

### How does it work?

The process is fairly simple. Note that I am not using any existing Tinder unofficial API. I know they exist, but I need practice in Python, so I try to do it by myself.

1.  I fetch people who liked me on the `teasers` endpoint. This gives me access to their photos (unblurred) as well as some other information which is not really useful to me. Note that the `id` is not the actual user account id, otherwise we would already be done!
2.  The `recs` (recommendations) endpoint gives us 20 recommendations. These people's `id` are their actual account `id` which we will pass to the `like` or `pass` endpoint. They also come with their pictures, which we will be using to compare with our teasers.
3.  Compare the picture(s) from the recommendation with the picture(s) from our teasers. If they kind of match (accuracy doesn't need to be perfect), it is a good chance we got that person! We can now ask if we wish to "like" or "pass" this person and poll the `like` (press 'L'), `pass` (press 'P') or `superlike` (press 'S') endpoint accordingly.
4.  ~~Repeat from step 2 until we found all the matches.~~ to prevent abuse, this step has been disabled.

### Endpoints

These are not secret endpoints. They are the very same endpoints that are called when interacting with the app.

| Method | Path                     | Description                                                                                                                                                       |
| ------ | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GET    | `/v2/recs/core`          | Gets 20 recommendations. These contain the account id and pictures. _Has optional query param `?locale=en`._                                                      |
| GET    | `/v2/fast-match/teasers` | Gets the people who likes you. These contain a single picture and an id (which I am guessing is some sort of "preview" account id to hide the actual account id). |
| GET    | `/like/{userId}`         | Provided the `userId` is the account id of the person, likes that person.                                                                                             |
| GET    | `/pass/{userId}`         | Provided the `userId` is the account id of the person, passes (dislike) that person.                                                                                  |
| POST   | `/like/{userId}/super`   | Provided the `userId` is the account id of the person, superlikes the person.                                                                                         |
| GET    | `/v2/fast-match/teasers` | Gets the people who liked you.                                                                                                                                    |
| GET    | `/v2/fast-match/count`   | Gets the number of people who liked you.                                                                                                                          |

_Endpoints' base is `https://api.gotinder.com`_

### Fun Fact

The name comes from a field `processed_by_bullseye` seen while inspecting response payloads of the `recs` endpoint. It is one of the few fields that I am not sure about its purpose and found it mysterious. So I named my project on that mystery. Please be the first to break the magic and tell me what it does 🙂

### Go easy on me

This is my first personnal project in Python with about 1 month of training 🙂 Please report in a constructive way any mistakes I might have made. At the end of the day, I'm a JS dev, so I think in JS, which is probably not always the best approach for Python.

### Contributing

Since this is purely for educationnal purposes, the project will be archived as soon as it is published. It will not be updated and no additionnal features should come. For that reason, contributions will not be accepted for this project. However, feel free to point out mistakes/bad design/etc, as I would love feedback on my Python beginner skills 🙂 