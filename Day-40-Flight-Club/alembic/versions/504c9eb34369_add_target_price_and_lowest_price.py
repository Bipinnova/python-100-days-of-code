"""add target price and lowest price

Revision ID: 504c9eb34369
Revises: 31746e1098b2
Create Date: 2026-08-16
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "504c9eb34369"
down_revision: Union[str, Sequence[str], None] = "31746e1098b2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # 1. Add target_price temporarily as nullable.
    op.add_column(
        "flight_routes",
        sa.Column(
            "target_price",
            sa.Float(),
            nullable=True
        )
    )

    # 2. Copy the existing lowest_price
    #    into target_price.
    op.execute(
        """
        UPDATE flight_routes
        SET target_price = lowest_price
        WHERE target_price IS NULL
        """
    )

    # 3. Make target_price required.
    op.alter_column(
        "flight_routes",
        "target_price",
        existing_type=sa.Float(),
        nullable=False
    )


def downgrade() -> None:

    op.drop_column(
        "flight_routes",
        "target_price"
    )