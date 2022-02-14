"""new row

Revision ID: 5dbf65e8dc2d
Revises: 72340dc1fa24
Create Date: 2022-02-14 12:58:52.351265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dbf65e8dc2d'
down_revision = '72340dc1fa24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('listings', sa.Column('number_of_views', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('listings', 'number_of_views')
    # ### end Alembic commands ###
