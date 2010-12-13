#!/bin/bash

[ -d raw-eggs ] || exit 0

ls `pwd`/raw-eggs/*egg | while read egg
do
    sed -i "s#\(find-links.\+\)#\1\n    $egg#" buildout.cfg
done

