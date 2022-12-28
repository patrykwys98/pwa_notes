"""shared notes

Revision ID: 9834acc573ea
Revises: 715eb1b61fa0
Create Date: 2022-12-20 22:35:14.807037

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '9834acc573ea'
down_revision = '715eb1b61fa0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('share',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('note', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('shared_by', sa.Integer(), nullable=False),
    sa.Column('can_edit', sa.Boolean(), nullable=True),
    sa.Column('can_delete', sa.Boolean(), nullable=True),
    sa.Column('can_share', sa.Boolean(), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['note'], ['note.id'], ),
    sa.ForeignKeyConstraint(['shared_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'note', 'user')
    )
    op.create_index(op.f('ix_share_id'), 'share', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_share_id'), table_name='share')
    op.drop_table('share')
    # ### end Alembic commands ###
