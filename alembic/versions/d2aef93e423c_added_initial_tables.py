"""Added initial tables

Revision ID: d2aef93e423c
Revises: 
Create Date: 2025-05-28 00:05:09.023162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2aef93e423c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('character', sa.String(length=100), nullable=True),
    sa.Column('power_level', sa.String(length=100), nullable=True),
    sa.Column('saga_or_movie', sa.String(length=100), nullable=True),
    sa.Column('dragon_ball_series', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api_data')
    # ### end Alembic commands ###
