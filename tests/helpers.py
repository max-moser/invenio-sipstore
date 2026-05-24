# SPDX-FileCopyrightText: 2017-2019 CERN.
# SPDX-License-Identifier: MIT


"""Pytest helpers."""

from __future__ import absolute_import, print_function


def get_file(filename, result):
    """Get a file by its filename from the results list."""
    return next((f for f in result if f['filename'] == filename), None)
