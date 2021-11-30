#!/bin/bash
if [ -z $1 ]; then
 echo "please provide a target copy path as the first argument"
 exit 1
fi
TARGET_DIR=$1/reborn-pokepedia
root_dir="$(dirname $(dirname $(realpath $0)) )"
$root_dir/scripts/build.sh
mkdir $TARGET_DIR
cp -r android $TARGET_DIR
mkdir $TARGET_DIR/node_modules
cp -r node_modules/@capacitor $TARGET_DIR/node_modules