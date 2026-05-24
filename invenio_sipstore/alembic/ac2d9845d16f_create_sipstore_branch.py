# SPDX-FileCopyrightText: 2017-2019 CERN.
# SPDX-License-Identifier: MIT

"""Create sipstore branch."""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ac2d9845d16f'
down_revision = 'dbdbc1b19cf2'
branch_labels = (u'invenio_sipstore',)
depends_on = 'dbdbc1b19cf2'


def upgrade():
    """Upgrade database."""


def downgrade():
    """Downgrade database."""
