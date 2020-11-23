#!/usr/bin/env bash

export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin

script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
PIPENV_EXEC=$(which pipenv)
PIPFILE=$script_dir/Pipfile
export PIPENV_PIPFILE=$PIPFILE
export PIPENV_VERBOSITY=-1

$PIPENV_EXEC run python $script_dir/monitor.py
