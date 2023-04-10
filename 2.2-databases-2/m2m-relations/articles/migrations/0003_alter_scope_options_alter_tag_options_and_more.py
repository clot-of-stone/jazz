# Generated by Django 4.1.7 on 2023-04-10 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_scope_tag_scope_tag"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="scope",
            options={
                "ordering": ("-is_main", "tag"),
                "verbose_name": "Тематика статьи",
                "verbose_name_plural": "Тематики статьи",
            },
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Раздел", "verbose_name_plural": "Разделы"},
        ),
        migrations.AlterField(
            model_name="scope",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.article",
                verbose_name="Статья",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="scope",
            unique_together={("article", "tag")},
        ),
    ]
