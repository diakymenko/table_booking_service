"""empty message

Revision ID: 282964a84d6a
Revises: 
Create Date: 2022-08-15 20:08:02.422169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '282964a84d6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('restaurant_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('tables', sa.Integer(), nullable=True),
    sa.Column('yelp_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('restaurant_id')
    )
    op.create_table('reservation',
    sa.Column('reservation_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('customer_name', sa.String(), nullable=True),
    sa.Column('customer_phone', sa.String(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('guests_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.restaurant_id'], ),
    sa.PrimaryKeyConstraint('reservation_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    op.drop_table('restaurant')
    # ### end Alembic commands ###
