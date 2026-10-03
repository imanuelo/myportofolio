import uuid
from django.db import migrations, models


def change_education_id(apps, schema_editor):
    Education = apps.get_model('main', 'Education')

    old_field = Education._meta.get_field('id')

    new_field = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        serialize=False,
    )

    # Hubungkan field baru dengan model dan nama kolomnya.
    new_field.model = Education
    new_field.set_attributes_from_name('id')

    if schema_editor.connection.vendor == 'sqlite':
        schema_editor.alter_field(
            Education,
            old_field,
            new_field,
            strict=True,
        )
    else:
        schema_editor.execute(
            'ALTER TABLE main_education DROP COLUMN id;'
        )
        schema_editor.execute(
            'ALTER TABLE main_education '
            'ADD COLUMN id uuid NOT NULL PRIMARY KEY;'
        )


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_project_starred_by'),
    ]

    operations = [
        migrations.RunPython(
            change_education_id,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name='education',
                    name='id',
                    field=models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
            database_operations=[],
        ),
    ]
