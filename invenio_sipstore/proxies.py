# SPDX-FileCopyrightText: 2017-2019 CERN.
# SPDX-License-Identifier: MIT

"""Proxy definitions."""

from __future__ import absolute_import, print_function

from flask import current_app
from werkzeug.local import LocalProxy

current_sipstore = LocalProxy(
    lambda: current_app.extensions['invenio-sipstore'])
"""Helper proxy to access the SIPStore state object."""
