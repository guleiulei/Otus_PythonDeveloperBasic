"""add description column to products table

Revision ID: fed36c1ece08
Revises: 8284168bffad
Create Date: 2022-12-02 20:49:16.071545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fed36c1ece08"
down_revision = "8284168bffad"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("product", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "description",
                sa.Text(),
                server_default="",
                nullable=False,
            ),
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("product", schema=None) as batch_op:
        batch_op.drop_column("description")

    # ### end Alembic commands ###
