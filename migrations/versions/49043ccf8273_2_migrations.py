"""2 migrations

Revision ID: 49043ccf8273
Revises: 
Create Date: 2024-12-05 19:28:39.921538

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '49043ccf8273'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('homework')
    op.drop_table('report')
    op.drop_table('attendance')
    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lesson_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'lesson', ['lesson_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('class_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'class', ['class_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('class_id')

    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('lesson_id')

    op.create_table('attendance',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('lesson_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], name='attendance_lesson_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], name='attendance_student_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='attendance_pkey')
    )
    op.create_table('report',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('pair_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('attendance', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('grades', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pair_id'], ['parent_student.id'], name='report_pair_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='report_pkey')
    )
    op.create_table('homework',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name='homework_subject_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='homework_pkey')
    )
    # ### end Alembic commands ###
