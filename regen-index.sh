#!/usr/bin/env bash

set -o errexit
set -o nounset

cd $(dirname $0)

echo -e "# Index\n" > index.md

echo -e "## 2019\n" >> index.md

git ls-files -z 2019 | tr '\0' '\n' | grep -E "\.pdf$" | sed -E "s/2019\/(.*)/- [\1](2019\/\1)/" >> index.md
