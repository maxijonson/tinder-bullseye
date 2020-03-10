# Tinder Bullseye

A Python script that searches for people who liked you and likes them back (if you want to).

### Background

A while back, I noticed that the unblurred photos of the people who liked me were fully visible from the network panel in Chrome, even without Gold. I contacted Tinder's security team to tell them. Due to the simplicity of the issue, I wasn't surprised by their answer: they know about it, they just choose not to do anything about it (yet). So, until that "yet" comes, if ever, and since I got a competition (CS Games 2020) to prepare for, I decided to make Tinder Bullseye!

### How does it work?

The process is fairly simple. Note that I am not using any existing Tinder unofficial API. I know they exist, but I need practice in Python, so I try to do it by myself.

1.  I fetch people who liked me on the `teasers` endpoint. This gives me access to their photos (unblurred) as well as some other information which is not really useful to me. Note that the `id` is not the actual user account id, otherwise we would already be done!
2.  The `recs` (recommendations) endpoint gives us 20, you guessed it, recommendations. These people's `id` are their actual account `id` which we will pass to the `like` or `pass` endpoint. They also come with their pictures, which we will be using to compare with our teasers.
3.  Compare the picture(s) from the recommendation with the picture(s) from our teasers. If they kind of match (accuracy doesn't need to be perfect), it is a good chance we got that person! We can now ask if we wish to "like" or "pass" this person and poll the `like` or `pass` endpoint accordingly.
4.  Repeat from step 2 until we found all the matches.

### Endpoints

| Method | Path                     | Description                                                                                                                                                       |
| ------ | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GET    | `/v2/recs/core`          | Gets 20 recommendations. These contain the account id and pictures. _Has optional query param `?locale=en`._                                                      |
| GET    | `/v2/fast-match/teasers` | Gets the people who likes you. These contain a single picture and an id (which I am guessing is some sort of "preview" account id to hide the actual account id). |
| GET    | `/like/{userId}`         | Provided the `id` is the account id of the person, likes that person.                                                                                             |
| GET    | `/pass/{userId}`         | Provided the `id` is the account id of the person, passes (dislike) that person.                                                                                  |
| POST   | `/like/{userId}/super`   | Provided the `id` is the account id of the person, superlikes the person.                                                                                         |
| GET    | `/v2/fast-match/teasers` | Gets the people who liked you.                                                                                                                                    |
| GET    | `/v2/fast-match/count`   | Gets the number of people who liked you.                                                                                                                          |

_Endpoints' base is `https://api.gotinder.com`_
_Model always has the shape `{ meta: { status: number }, data: { ... } }`. The models in that column only represent the `data` object_

### Fun Fact

The name comes from a field `processed_by_bullseye` seen while inspecting response payloads of the `recs` endpoint. It is one of the few fields that I am not sure about its purpose and found it mysterious. So I named my project on that mystery. Please be the first to break the magic and tell me what it does 🙂

### Go easy on me

This is my first personnal project in Python with about 1 month of training 🙂 Pull requests will be accepted after the initial project requirements are met. However, I most likely won't publish this unless it works 😜