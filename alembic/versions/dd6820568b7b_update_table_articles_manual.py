"""update table articles - manual

Revision ID: dd6820568b7b
Revises: 8a36b7e8ae10
Create Date: 2024-09-18 08:56:50.230503

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd6820568b7b'
down_revision: Union[str, None] = '8a36b7e8ae10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False))
    op.add_column('articles', sa.Column('updated_at', sa.DateTime(), nullable=True, onupdate=sa.text('NOW()')))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
