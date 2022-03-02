#!/usr/bin/env bash

set -o errexit
set -o nounset

allYears="2019 2021 2022"

cd $(dirname $0)
echo "" > index.md
echo -e "# Index" > index.md

for year in $allYears; do
    echo "$year"
    echo -e "\n## $year\n" >> index.md
    git ls-files -z $year | tr '\0' '\n' | grep -E "\.(pdf|html)$" | sed -E "s/$year\/(.*)/- [\1]($year\/\1)/" >> index.md
done
