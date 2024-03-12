"""adding education table

Revision ID: 11779e1fd8d5
Revises: 0fe3f82302c2
Create Date: 2024-03-12 22:19:30.576101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11779e1fd8d5'
down_revision = '0fe3f82302c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_email', sa.String(length=255), nullable=False),
    sa.Column('course_title', sa.String(length=255), nullable=True),
    sa.Column('institution', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('education')
    # ### end Alembic commands ###