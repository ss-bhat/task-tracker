"""Rename created and updated columns

Revision ID: 8c6efc1104d9
Revises: 45e9abc2a90f
Create Date: 2021-09-18 12:35:39.916339

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8c6efc1104d9'
down_revision = '45e9abc2a90f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('last_updated', sa.DateTime(), nullable=True))
    op.drop_column('task', '_last_updated')
    op.drop_column('task', '_created_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('_created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('task', sa.Column('_last_updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('task', 'last_updated')
    op.drop_column('task', 'created_at')
    # ### end Alembic commands ###
