# ECE USC Server :rocket:

## About

## Getting Started

### Prerequisites

1. Have git installed
2. Have python3, pip3 installed
3. Run these commands:

```bash

git clone https://github.com/ucsdeceusc/server.git
cd server/
make init
make install
make run
```

Then visit [http://localhost:8000](http://localhost:8000) to see the front page!

## Quick Overview

This server is a [Django app](https://www.djangoproject.com/) written in Python that hosts many endpoints that the ECE USC at UC San Diego uses in their projects.

Whatever is on the `master` branch on this repo gets directly pushed to our public [heroku app](https://www.heroku.com/what) found [here](http://eceusc.herokuapp.com/).

### Current Projects


#### [Slack Bot](slack/)

#### [Messenger Bot](messengerbot/)


## Contributing

Want to contribute to our projects? Awesome! Follow these instructions to make sure it goes smoothly:

1. Fork this repo (upper right hand corner)
2. `git clone` your new forked repo on your computer.
3. Make whatever edits you want.
4. Create a new [Pull Request](https://help.github.com/articles/creating-a-pull-request/) to this repo's `integration` branch.
5. Your PR will be reviewed and hopefully merged in! 

## Todo (and in progress)
- [ ] Get a HelloWorld Messenger Bot up
- [ ] Create template for Slack Messages
