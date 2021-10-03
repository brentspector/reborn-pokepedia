<h1 align="center"> Reborn Pokepedia </h1> <br>
<h2 align="center">Built for</h@> <br>
<p align="center">
  <a href="https://www.rebornevo.com/">
    <img alt="RebornPokepedia" title="RebornPokepedia" src="https://www.rebornevo.com/images/pr/rebornsmall.png" width="450">
  </a>
</p>

<p align="center">Guide for Pokemon Based on Progress in Game</p>

<p align="center">
  <a href="https://img3.stockfresh.com/files/k/kikkerdirk/m/81/4759970_stock-photo-coming-soon.jpg">
    <img alt="Download on the App Store" title="App Store" src="http://i.imgur.com/0n2zqHD.png" width="140">
  </a>

  <a href="https://img3.stockfresh.com/files/k/kikkerdirk/m/81/4759970_stock-photo-coming-soon.jpg">
    <img alt="Get it on Google Play" title="Google Play" src="http://i.imgur.com/mtGRPuM.png" width="140">
  </a>
</p>

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Feedback](#feedback)
- [Build Process](#build-process)
- [Committing](#committing)
- [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

[![Build Status](https://img.shields.io/travis/gitpoint/git-point.svg?style=flat-square)](https://travis-ci.org/gitpoint/git-point)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg?style=flat-square)](http://commitizen.github.io/cz-cli/)

Reborn Pokepedia allows players to filter for pokemon that are available based on their progress in game. It will show all wild, event, and gift pokemon that can be obtained at a given point in the game, and details what moves, tutors, and TM/HM are available to them.

This application is available on web, iOS, and Android.

**Available for both iOS and Android.**

<p align="center">
  <img src = "https://img3.stockfresh.com/files/k/kikkerdirk/m/81/4759970_stock-photo-coming-soon.jpg" width=350>
</p>

## Features

A few of the things you can do with Reborn Pokepedia:

- Look up pokemon by major battle (Gym, Rival, PULSE, or Major NPC)

## Feedback

Feel free to send us feedback by [Email](brent.spector@yahoo.com) or [file an issue](https://github.com/brentspector/reborn-pokepedia/issues/new). Feature requests are always welcome, although not guaranteed to be fulfilled. If you wish to contribute, please submit a pull request.

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
Thanks to [PokeAPI](https://pokeapi.co) for the sprites on [GitHub](https://github.com/PokeAPI/sprites/tree/master/sprites/pokemon/other/official-artwork)
Thanks to [Fuyutarow](https://github.com/fuyutarow) for the Pokemon JSON data on [GitHub](https://github.com/fuyutarow/pokemon.json/blob/master/en/pokemon.json)
