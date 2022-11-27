"""New Migration

Revision ID: 13a7db048542
Revises: 
Create Date: 2022-11-27 17:40:54.643845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13a7db048542'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notebook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('notebook_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['notebook_id'], ['notebook.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_note_id'), 'note', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_note_id'), table_name='note')
    op.drop_table('note')
    op.drop_table('notebook')
    # ### end Alembic commands ###
