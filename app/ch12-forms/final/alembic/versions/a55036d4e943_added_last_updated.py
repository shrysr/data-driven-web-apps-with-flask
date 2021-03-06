"""Added last updated

Revision ID: a55036d4e943
Revises: 
Create Date: 2019-05-16 10:55:28.413573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a55036d4e943'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('packages', sa.Column('last_updated', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_packages_last_updated'), 'packages', ['last_updated'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_packages_last_updated'), table_name='packages')
    op.drop_column('packages', 'last_updated')
    # ### end Alembic commands ###
