from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_title_event_titulo_remove_event_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='eventos/'),
        ),
    ]
