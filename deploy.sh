#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
LAST=$(git log | head -n 1)
git pull
CURR=$(git log | head -n 1)
if [ "$LAST" != "$CURR" ]
then
    tmux kill-session -t unsafepay
    tmux new -ds unsafepay "~/.virtualenvs/unsafepay/bin/python bot.py"
fi
