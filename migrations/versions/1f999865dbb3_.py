"""empty message

Revision ID: 1f999865dbb3
Revises: 5ce2d484925a
Create Date: 2023-02-03 00:01:17.876829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f999865dbb3'
down_revision = '5ce2d484925a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    op.drop_table('characters')
    op.drop_table('vehicles')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    op.create_table('vehicles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('length', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('crew', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('passengers', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('classification', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='vehicles_pkey'),
    sa.UniqueConstraint('name', name='vehicles_name_key')
    )
    op.create_table('characters',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('birth_year', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('height', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('homeworld', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='characters_pkey'),
    sa.UniqueConstraint('homeworld', name='characters_homeworld_key'),
    sa.UniqueConstraint('name', name='characters_name_key')
    )
    op.create_table('planets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('diameter', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('population', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('climate', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('terrain', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='planets_pkey'),
    sa.UniqueConstraint('climate', name='planets_climate_key'),
    sa.UniqueConstraint('name', name='planets_name_key'),
    sa.UniqueConstraint('terrain', name='planets_terrain_key')
    )
    # ### end Alembic commands ###
