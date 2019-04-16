#!/bin/bash
gh_token=$1
random_string=$(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

git checkout -b branch-$random_string
echo "Hello Im a new change"
touch yadda-$random_string.out
echo "yadda" >> yadda-$random_string.oin
git add yadda-$random_string.out
git commit -m "random string for commit messages $random_string"
git push origin branch-$random_string
git checkout master
git branch

curl -X POST \
  https://api.github.com/repos/jwalczyk/test_repo/pulls \
  -H 'authorization: tokens '"$gh_token"' ' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "title": "pr_for_branch-'"$random_string"'",
  "head": "branch-'"$random_string"'",
  "base": "master"
}'
