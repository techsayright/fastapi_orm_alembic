"""add phone_number column in users

Revision ID: 2d8c35d0dba8
Revises: 
Create Date: 2023-05-26 18:25:17.381806

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2d8c35d0dba8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('post')
    # op.drop_table('products')
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # op.create_table('products',
    # sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    # sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.PrimaryKeyConstraint('id', name='products_pkey')
    # )
    # op.create_table('post',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    # sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False),
    # sa.Column('published', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False),
    # sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('id', name='post_pkey')
    # )
    # ### end Alembic commands ###
