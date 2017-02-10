"""Add soundcloud upload try logging table

Revision ID: 46085f5c8e36
Revises: 1e3be3ff186d
Create Date: 2017-02-10 11:20:12.308503

"""

# revision identifiers, used by Alembic.
revision = '46085f5c8e36'
down_revision = '1e3be3ff186d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('soundcloud_track_retry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('soundcloud_track_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['soundcloud_track_id'], ['soundcloud_track.id'], name=op.f('fk_soundcloud_track_retry_soundcloud_track_id_soundcloud_track')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_soundcloud_track_retry'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('soundcloud_track_retry')
    ### end Alembic commands ###
