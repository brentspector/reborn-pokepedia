<h1 align="center"> Reborn Pokepedia </h1> <br>
<h2 align="center">Built for</h@> <br>
<p align="center">
  <a href="https://www.rebornevo.com/">
    <img alt="PokemonReborn" title="PokemonReborn" src="https://www.rebornevo.com/images/pr/rebornsmall.png" width="450">
  </a>
</p>

<p align="center">Guide for Pokemon Based on Progress in Game</p>

<p align="center">
  <a href="https://play.google.com/store/apps/details?id=com.brentspector.rebornpokepedia">
    <img alt="Get it on Google Play" title="Google Play" src="https://pluspng.com/img-png/get-it-on-google-play-badge-png--2194.png" width="140">
  </a>
</p>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Feedback](#feedback)
- [Build Process](#build-process)
- [Committing](#committing)
- [Acknowledgments](#acknowledgments)

## Introduction

[![Build Status](https://github.com/brentspector/reborn-pokepedia/actions/workflows/webApp.yml/badge.svg)](https://github.com/brentspector/reborn-pokepedia/actions/workflows/webApp.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg?style=flat-square)](http://commitizen.github.io/cz-cli/)

Reborn Pokepedia allows players to filter for Pokemon that are available based on their progress in game. It will show all wild, event, and gift Pokemon that can be obtained at a given point in the game, and details what moves, tutors, and TM/HM are available to them.

This application is available on web, iOS, and Android.

**Available for Android.**

Android: https://play.google.com/store/apps/details?id=com.brentspector.rebornpokepedia

### What Happened to iOS?

While there is an iOS app available in this codebase, the actual distribution to the App Store is too expensive. If you are interested in the iOS app, follow [these instructions](https://developer.apple.com/documentation/xcode/distributing-your-app-to-registered-devices).

The app to load in XCode can be found at `ios/App/App.xcworkspace`

You will likely need [NodeJS and npm](https://nodejs.org/en/download/), [Ionic CLI](https://ionicframework.com/docs/cli), and [cordova-res](https://capacitorjs.com/docs/guides/splash-screens-and-icons) to collect the node modules and build artifacts that Capacitor relies on in order to properly build the iOS app.

Once that's taken care of, run `scripts/ios_build.sh` to create the build artifacts that XCode will use to make the `.ipa` file that gets installed on Apple devices.

This app has been tested on `Monterey 12.1` and `Xcode 13.2.1` and various virtual devices, including `iPhone 13`.

## Features

A few of the things you can do with Reborn Pokepedia:

- Look up Pokemon by major battle (Gym, Rival, PULSE, or Major NPC)
- Look up Pokemon by location
- Look up details for individual Pokemon

## Feedback

Feel free to send us feedback by [Email](bspector20170@yahoo.com) or [file an issue](https://github.com/brentspector/reborn-pokepedia/issues/new). Feature requests are always welcome, although not guaranteed to be fulfilled. If you wish to contribute, please submit a pull request.

## Build Process

- Follow the [Ionic Guide](https://ionicframework.com/docs/intro/environment) for getting started building the project. **A Mac is required if you wish to develop for iOS.**
- Clone or download the repo
- `npm install` to install dependencies
- `ionic serve` to spin up the web-app
- `ionic capacitor open ios` requires appropriate setup in a [Mac Environment](https://ionicframework.com/docs/developing/ios)
- `ionic capacitor open andriod` requires appropriate setup with [Android Studio](https://ionicframework.com/docs/developing/android)

### Production Build

Any commit to the `master` branch triggers a Github Action that rebuilds the project and updates https://brentspector.github.io/reborn-pokepedia/.

However, if you wish to preview the production build locally, a Dockerfile has been created to do just that!

From the project root, run the following commands

```
scripts/docker_build.sh
scripts/docker_run.sh
```

Then navigate to `localhost:8080` to see the product.

## Single File Component

Vue.js recommends combining HTML, CSS, and Javascript into one file, represented with the `.vue` file extension. More details on the rationale behind this can be found at https://v3.vuejs.org/guide/single-file-component.html#how-it-works

## Pokemon Data

Data has been broken down into each generation, and some generations have been broken down into multiple portions. This is due to Babel (a compatibility library) deoptimizing files that exceed 500 kB. In order to keep build times short, files should be less than 500 kB if possible.

`Point in Game` is defined as the point you have not crossed yet. For instance, If you beat Julia but have not gotten through Pulse Tangrowth 1, then your `Point in Game` would be `ZEL/Pulse Tangrowth 1`.

Points in game require the following criteria:

- Points of importance where player might get stuck and need to rework team
- 2 or more evolutionary lines are made available between any two consecutive points (i.e. if Zubat and Golbat are unlocked at the same time, it gets lumped with the next batch instead of getting a separate `Point in Game`)

`Location in Game` require the following criteria:

- Unique in-game location (i.e location printed in `Trainer Memo` on Pokemon details screen)
- Sufficiently relevant encounters

The initial pass attempts to lump as many similar areas together as possible (i.e `Glitch World`) even if they may have different `Trainer Memo` locations. This can be adjusted later if requested.

Some Pokemon (like `Alolan Raichu` or `Mega Venusaur`) were given a location even though you can't find them in the wild. This was done when an evolution is available based on a location or item that is not available until after the earliest time to obtain. Thus `Clefable` is listed as having no locations since the `Moon Stone` is available prior to the point you get `Clefairy`. NOTE: Random potential events like Mystery Egg are not considered "earliest".

## Committing

Run `npm run commit` to automatically use `Commitizen`.

## Acknowledgments

Thanks to `Amethyst` for the great game!
Support her work on Patreon
<br>
<a href="https://www.patreon.com/amethystvl">
<img src="https://www.licographics.com/wp-content/uploads/2020/07/become_a_patron_button@2x-300x71.png" width=200>
</a>
<br>

- Thanks to [PokeAPI](https://pokeapi.co) for the sprites on [GitHub](https://github.com/PokeAPI/sprites/tree/master/sprites/Pokemon/other/official-artwork)
- Thanks to [AlphaXXI](https://www.deviantart.com/alphaxxi) for the Floette Eternal Flower form [art](https://www.deviantart.com/alphaxxi/art/Eternal-Flower-Floette-561498099)
- Thanks to [Starry Knight](https://www.rebornevo.com/forums/profile/73296-starry-knight/) for [E18 Pokemon Locations](https://www.rebornevo.com/forums/topic/42836-void-kissed-Pokemon-location-guide/)
- Thanks to [Aegisth](https://www.rebornevo.com/forums/profile/77714-aegisth/) for [E18 Pokemon Spreadsheet](https://www.rebornevo.com/forums/topic/43367-e18-Pokemon-locations-spreadsheet-all-wild-and-event-Pokemon-plus-more/)
- Thanks to [Aboodie](https://www.rebornevo.com/forums/profile/65028-aboodie/) for [E18 Item Guide](https://www.rebornevo.com/forums/topic/41661-item-guide-v18-void-kissed/)
- Thanks to [AyTales](https://www.rebornevo.com/forums/profile/77714-aytales/) for [E19 Pokemon Spreadsheet](https://docs.google.com/spreadsheets/d/1NmNBklcSI_OqWKMAaJ_WyqjBJ5J7lo3IuwTftIaJlIw/edit#gid=1921351918)
- Thanks to [Ngoc Nguyen](nguyen.gia.ngoc.2710@gmail.com) for [E19 Move Tutors](https://docs.google.com/spreadsheets/d/1ZaS7Vs-CWfFojVxeii8D7S4GbZWlwcNspb7zQkqMmUk/edit#gid=0)
- Thanks to [Bradley Mc-Avoy-James](https://videogamesuncovered.com/author/bsjkupo/) for the [Pokemon type sprites](https://videogamesuncovered.com/features/Pokemon-sun-and-moon-tips-and-tricks-guide/Pokemon-types/)
- Thanks to [James Shvarts](https://www.linkedin.com/in/jshvarts) for the [Android CICD](https://www.valueof.io/blog/deploying-to-google-play-using-github-actions)
