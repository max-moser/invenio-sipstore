# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration of Invenio-SIPStore module."""

SIPSTORE_DEFAULT_AGENT_JSONSCHEMA = "sipstore/agent-v1.0.0.json"
"""Default JSON schema for extra SIP agent information.

For more examples, you can have a look at Zenodo's config:
https://github.com/zenodo/zenodo/tree/master/zenodo/modules/sipstore/jsonschemas/sipstore
"""

SIPSTORE_DEFAULT_BAGIT_JSONSCHEMA = "sipstore/bagit-v1.0.0.json"
"""Default JSON schema for BagIt archiver."""

SIPSTORE_AGENT_JSONSCHEMA_ENABLED = True
"""Enable SIP agent validation by default."""

SIPSTORE_AGENT_FACTORY = "invenio_sipstore.api.SIP._build_agent_info"
"""Factory to build the agent, stored for the information about the SIP."""

SIPSTORE_AGENT_TAGS_FACTORY = (
    "invenio_sipstore.archivers.BagItArchiver._generate_agent_tags"
)
"""Factory to build agent information tags."""

SIPSTORE_FILEPATH_MAX_LEN = 1024
"""Max filepath length."""

SIPSTORE_FILE_STORAGE_FACTORY = "invenio_files_rest.storage.pyfs.pyfs_storage_factory"
"""Archived file storage factory."""

SIPSTORE_ARCHIVER_DIRECTORY_BUILDER = (
    "invenio_sipstore.archivers.utils.default_archive_directory_builder"
)
"""Builder for archived SIPs."""

SIPSTORE_ARCHIVER_SIPMETADATA_NAME_FORMATTER = (
    "invenio_sipstore.archivers.utils.default_sipmetadata_name_formatter"
)
"""Filename formatter for archived SIPMetadata."""

SIPSTORE_ARCHIVER_SIPFILE_NAME_FORMATTER = (
    "invenio_sipstore.archivers.utils.default_sipfile_name_formatter"
)
"""Filename formatter for the archived SIPFile."""

SIPSTORE_ARCHIVER_LOCATION_NAME = "archive"
"""Name of the invenio_files_rest.models.Location object, which will specify
to the archive location in its URI."""

SIPSTORE_BAGIT_TAGS = [
    ("Source-Organization", "European Organization for Nuclear Research"),
    ("Organization-Address", "CERN, CH-1211 Geneva 23, Switzerland"),
    ("Bagging-Date", None),  # Autogenerated
    ("Payload-Oxum", None),  # Autogenerated
    ("External-Identifier", None),  # Autogenerated
    ("External-Description", "BagIt archive of SIP."),
]
"""Default list of BagIt tags that will be written."""
