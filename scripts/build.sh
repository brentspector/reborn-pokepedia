#!/bin/bash
ionic build
ionic cap copy
cordova-res android --skip-config --copy