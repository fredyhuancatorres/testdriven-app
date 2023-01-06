"""empty message

Revision ID: c8efb0de0fa7
Revises: 
Create Date: 2023-01-06 01:01:44.591377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8efb0de0fa7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255)))
    op.execute('UPDATE users SET password=email')
    op.alter_column('users', 'password', nullable=False)
    #op.create_unique_constraint(None, 'users', ['email'])
    #op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###