# SPDX-FileCopyrightText: 2016-2019 CERN.
# SPDX-License-Identifier: MIT

"""Errors for Submission Information Packages."""

from __future__ import absolute_import, print_function


class SIPError(Exception):
    """Base class for SIPStore errors."""


class SIPUserDoesNotExist(SIPError):
    """User ID for SIP does not exist."""

    def __init__(self, user_id, *args, **kwargs):
        """Initialize exception."""
        self.user_id = user_id
        super(SIPUserDoesNotExist, self).__init__(*args, **kwargs)
