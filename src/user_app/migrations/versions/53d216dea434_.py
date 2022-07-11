"""empty message

Revision ID: 53d216dea434
Revises: 
Create Date: 2022-07-11 18:49:42.238429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53d216dea434'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    schema='user_app_schema'
    )
    op.create_index(op.f('ix_user_app_schema_users_email'), 'users', ['email'], unique=True, schema='user_app_schema')
    op.create_index(op.f('ix_user_app_schema_users_username'), 'users', ['username'], unique=True, schema='user_app_schema')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_app_schema_users_username'), table_name='users', schema='user_app_schema')
    op.drop_index(op.f('ix_user_app_schema_users_email'), table_name='users', schema='user_app_schema')
    op.drop_table('users', schema='user_app_schema')
    # ### end Alembic commands ###
