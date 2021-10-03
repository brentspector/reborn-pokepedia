root_dir="$(dirname $(dirname $(realpath $0)) )"
docker build $root_dir -t reborn-pokepedia