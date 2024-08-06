"""Added WalletEntry table

Revision ID: af0196fa1984
Revises: 96ac09edcdf2
Create Date: 2024-08-06 14:32:35.304011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af0196fa1984'
down_revision = '96ac09edcdf2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wallet_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_user_id', sa.Integer(), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('seal_number', sa.Integer(), nullable=False),
    sa.Column('cash_amount', sa.Float(), nullable=False),
    sa.Column('bank_amount', sa.Float(), nullable=False),
    sa.Column('cash_out', sa.Float(), nullable=True),
    sa.Column('cash_in', sa.Float(), nullable=True),
    sa.Column('bank_card_removed', sa.Boolean(), nullable=False),
    sa.Column('money_spent', sa.Float(), nullable=True),
    sa.Column('money_spent_description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['service_user_id'], ['service_user.id'], ),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallet_entry')
    # ### end Alembic commands ###
