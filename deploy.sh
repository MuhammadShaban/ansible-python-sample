#!/usr/bin/env bash

ansible-playbook -i ./playbook_hosts --extra-vars '@playbook_vars.json'  playbook.yml
