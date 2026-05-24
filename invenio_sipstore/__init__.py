# SPDX-FileCopyrightText: 2016-2019 CERN.
# SPDX-License-Identifier: MIT

"""Submission Information Package store for Invenio."""

from __future__ import absolute_import, print_function

from .ext import InvenioSIPStore
from .version import __version__
from .proxies import current_sipstore

__all__ = ('__version__', 'current_sipstore', 'InvenioSIPStore')
