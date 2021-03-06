"""empty message

Revision ID: 14b39a4b7eb
Revises: 3274be3cbb8
Create Date: 2015-05-07 22:49:58.403614

"""

# revision identifiers, used by Alembic.
revision = '14b39a4b7eb'
down_revision = '3274be3cbb8'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pending_jobs', 'creation_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pending_jobs', 'creation_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    ### end Alembic commands ###
