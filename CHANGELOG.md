# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## 1.0.0 (2021-12-15)


### ⚠ BREAKING CHANGES

* updates package.json

* build(android): remove ios add android

remove ios; add android; fix lint errors;
* remove ios

* fix(android): fix android build issues and public path

update android gradle version variables to use publicly available versions; update public path to be
root unless overriden; provide ghpages override to build target in package.json;

* style(eslint): fix eslint errors

replace all variables with camelCase; add ignores for unused variables in locations and points
views; fix fsevent dependency to be optional in package-lock.json;

* fix(pokemon details): fix details to use new variable names

replaces converted variable names with their new camelCase version;

* fix(pokemon details): fix click command for fab

the fab's click property now uses a wrapper around the modalCallback so that typescript knows it's a
function;

* feat(android app): add splash screen and icons for android

adds base splash screen, icons, and adaptive icons for android; adds new build script for android;
updates generic build script to copy cordova-res assets to the correct locations;

* fix(build.gradle): add unique package id for android app

replaces io.ionic.starter with the correct package name

* docs(privacy policy): add privacy policy

adds a privacy policy
* replaces old routing with new routing

* feat(pokemon details): display pokemon details

adds list of pokemon data when selecting a pokemon to view;

### Features

* **details:** migrate details dropdowns to searchlist ([2bc4d66](https://github.com/brentspector/reborn-pokepedia/commit/2bc4d66478c7e22a896ba242db43a336955d2b13))
* **locations:** migrate locations to searchlist ([f7f40c4](https://github.com/brentspector/reborn-pokepedia/commit/f7f40c4d24ad70b0beabfd6fd365db1d7d60641c))
* **main view:** layout a framework for two-way binding and loading an image ([f3119c9](https://github.com/brentspector/reborn-pokepedia/commit/f3119c91a6611689a4d79ad344e627fd41172812))
* **points:** complete game points transition to new searchlist utility ([350b8b4](https://github.com/brentspector/reborn-pokepedia/commit/350b8b46a725d06047eb31a3f097272c60dab6d1))
* **pokemon details:** allow routing based on index id ([#10](https://github.com/brentspector/reborn-pokepedia/issues/10)) ([64c01a9](https://github.com/brentspector/reborn-pokepedia/commit/64c01a994876c3244d89e562a26279f3ce6c806e))
* **searchlist:** add searchlist view ([57f2995](https://github.com/brentspector/reborn-pokepedia/commit/57f2995e300a30979d724a504d6cf4a83caacb30))


* Feature/android app (#19) ([05d2d49](https://github.com/brentspector/reborn-pokepedia/commit/05d2d49911ee3d8705a4b48c6336d6d6509cb261)), closes [#19](https://github.com/brentspector/reborn-pokepedia/issues/19) [#18](https://github.com/brentspector/reborn-pokepedia/issues/18)
* Feature/view pokemon data (#7) ([5565bd9](https://github.com/brentspector/reborn-pokepedia/commit/5565bd96ea977fc13d6513537cdd5bb76ee5652f)), closes [#7](https://github.com/brentspector/reborn-pokepedia/issues/7)

### [0.1.4](https://github.com/brentspector/reborn-pokepedia/compare/v0.1.3...v0.1.4) (2021-12-10)


### Bug Fixes

* **android:** automatically increment android version ([30c81cc](https://github.com/brentspector/reborn-pokepedia/commit/30c81cc2e7ab7a3db18566377cc0d58f069e0639))
* **android:** dynamically change version name ([22fb529](https://github.com/brentspector/reborn-pokepedia/commit/22fb529c372fe3b359d9e09582ba49ee937a9a6f))
* **workflow:** downgrade upload google play to 1.0.15 ([c755417](https://github.com/brentspector/reborn-pokepedia/commit/c75541755cadc2aad714a18d1c7be38c541caa80))

### [0.1.3](https://github.com/brentspector/reborn-pokepedia/compare/v0.1.2...v0.1.3) (2021-12-10)

### [0.1.2](https://github.com/brentspector/reborn-pokepedia/compare/v0.1.1...v0.1.2) (2021-12-10)

### [0.1.1](https://github.com/brentspector/reborn-pokepedia/compare/v0.1.0...v0.1.1) (2021-12-10)


### Bug Fixes

* **workflow:** remove tag from android workflow ([8b794c1](https://github.com/brentspector/reborn-pokepedia/commit/8b794c168168f814c451031ccf23322e95aa3811))

## 0.1.0 (2021-12-10)


### ⚠ BREAKING CHANGES

* updates package.json

* build(android): remove ios add android

remove ios; add android; fix lint errors;
* remove ios

* fix(android): fix android build issues and public path

update android gradle version variables to use publicly available versions; update public path to be
root unless overriden; provide ghpages override to build target in package.json;

* style(eslint): fix eslint errors

replace all variables with camelCase; add ignores for unused variables in locations and points
views; fix fsevent dependency to be optional in package-lock.json;

* fix(pokemon details): fix details to use new variable names

replaces converted variable names with their new camelCase version;

* fix(pokemon details): fix click command for fab

the fab's click property now uses a wrapper around the modalCallback so that typescript knows it's a
function;

* feat(android app): add splash screen and icons for android

adds base splash screen, icons, and adaptive icons for android; adds new build script for android;
updates generic build script to copy cordova-res assets to the correct locations;

* fix(build.gradle): add unique package id for android app

replaces io.ionic.starter with the correct package name

* docs(privacy policy): add privacy policy

adds a privacy policy
* replaces old routing with new routing

* feat(pokemon details): display pokemon details

adds list of pokemon data when selecting a pokemon to view;

### Features

* **main view:** layout a framework for two-way binding and loading an image ([f3119c9](https://github.com/brentspector/reborn-pokepedia/commit/f3119c91a6611689a4d79ad344e627fd41172812))
* **pokemon details:** allow routing based on index id ([#10](https://github.com/brentspector/reborn-pokepedia/issues/10)) ([64c01a9](https://github.com/brentspector/reborn-pokepedia/commit/64c01a994876c3244d89e562a26279f3ce6c806e))


### Bug Fixes

* **workflow:** add capacitor update android to build steps ([f5274a9](https://github.com/brentspector/reborn-pokepedia/commit/f5274a920975ca29760861998f1886a66c761f1b))
* **workflow:** add debug statements ([2126542](https://github.com/brentspector/reborn-pokepedia/commit/2126542ec6702fd7ec9426f6aa43434cf1161ec0))
* **workflow:** add more ignore options for gradle build ([d4d002e](https://github.com/brentspector/reborn-pokepedia/commit/d4d002e8ba28e6ec1a647a9afc814ad2366c3fbd))
* **workflow:** create environment for android ([0cb57e6](https://github.com/brentspector/reborn-pokepedia/commit/0cb57e62a0f1f7c4bf1393d1995abc20646d608e))
* **workflow:** downgrade java to 16 in android workflow ([bef895a](https://github.com/brentspector/reborn-pokepedia/commit/bef895a9e2a9fa9cb6c6e2cbc50a0e1e7e985647))
* **workflow:** downgrade min sdk to 22 ([cf8f4fc](https://github.com/brentspector/reborn-pokepedia/commit/cf8f4fc3d555332439b20645667d20d91e368e88))
* **workflow:** downgrade workflow to jdk 11 ([bf124e7](https://github.com/brentspector/reborn-pokepedia/commit/bf124e7839e6ee20a785584cb427c8ea81680017))
* **workflow:** fix the fix ([5944dc9](https://github.com/brentspector/reborn-pokepedia/commit/5944dc910b68778f6241b0dc35e659d7442be5de))
* **workflow:** remove gradle cache ([911b513](https://github.com/brentspector/reborn-pokepedia/commit/911b51385eddfb734d04a659c960955f34e3a18f))
* **workflow:** run java in android dir ([b04f16c](https://github.com/brentspector/reborn-pokepedia/commit/b04f16c53fc86aab8ece133d790ef2efa43640a1))
* **workflow:** skip building dependencies ([228de07](https://github.com/brentspector/reborn-pokepedia/commit/228de07270eb1eacfbaf13a7a884296cdbd56cea))
* **workflow:** skip failure on android lint ([25e5d46](https://github.com/brentspector/reborn-pokepedia/commit/25e5d465c0f772cdb674222c74dcdfe52b991e2e))


* Feature/android app (#19) ([05d2d49](https://github.com/brentspector/reborn-pokepedia/commit/05d2d49911ee3d8705a4b48c6336d6d6509cb261)), closes [#19](https://github.com/brentspector/reborn-pokepedia/issues/19) [#18](https://github.com/brentspector/reborn-pokepedia/issues/18)
* Feature/view pokemon data (#7) ([5565bd9](https://github.com/brentspector/reborn-pokepedia/commit/5565bd96ea977fc13d6513537cdd5bb76ee5652f)), closes [#7](https://github.com/brentspector/reborn-pokepedia/issues/7)
