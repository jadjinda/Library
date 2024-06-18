"""Initial migration .

Revision ID: 1fdb71a99d53
Revises: 
Create Date: 2024-06-18 13:02:10.475905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fdb71a99d53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('statut', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titre', sa.String(length=255), nullable=False),
    sa.Column('auteur', sa.String(length=255), nullable=False),
    sa.Column('codeISBN', sa.String(length=255), nullable=False),
    sa.Column('datePublication', sa.Integer(), nullable=False),
    sa.Column('nombreExemplaires', sa.Integer(), nullable=False),
    sa.Column('imageCouverture', sa.String(length=255), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('emprunt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nomEmprunteur', sa.String(length=255), nullable=False),
    sa.Column('dateEmprunt', sa.String(length=255), nullable=False),
    sa.Column('dateRetour', sa.String(length=255), nullable=False),
    sa.Column('observation', sa.String(length=255), nullable=True),
    sa.Column('livre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['livre_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emprunt')
    op.drop_table('book')
    op.drop_table('category')
    # ### end Alembic commands ###