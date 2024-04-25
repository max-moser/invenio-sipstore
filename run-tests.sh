#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2019 CERN.
# Copyright (C) 2024 TU Wien.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

export LC_TIME=en_US.UTF-8
python -m check_manifest
python -m sphinx.cmd.build -qnN docs docs/_build/html

# Forward all arguments to this script to pytest
python -m pytest "${@}"
