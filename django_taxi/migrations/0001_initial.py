# Generated by Django 4.1 on 2022-08-20 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Taxonomy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("meta", models.JSONField(blank=True, default=dict, null=True)),
                ("name", models.CharField(max_length=128, verbose_name="Name")),
                ("slug", models.SlugField()),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="django_taxi.taxonomy",
                        verbose_name="Parent",
                    ),
                ),
            ],
            options={
                "verbose_name": "Taxonomy",
                "verbose_name_plural": "Taxonomies",
            },
        ),
        migrations.CreateModel(
            name="Term",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("meta", models.JSONField(blank=True, default=dict, null=True)),
                ("name", models.CharField(max_length=128, verbose_name="Name")),
                ("slug", models.SlugField()),
            ],
            options={
                "verbose_name": "Term",
                "verbose_name_plural": "Terms",
            },
        ),
        migrations.CreateModel(
            name="TermTaxonomy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("meta", models.JSONField(blank=True, default=dict, null=True)),
                (
                    "taxonomy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="terms",
                        to="django_taxi.taxonomy",
                        verbose_name="Taxonomy",
                    ),
                ),
                (
                    "term",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taxonomies",
                        to="django_taxi.term",
                        verbose_name="Term",
                    ),
                ),
            ],
            options={
                "verbose_name": "Term Taxonomy",
                "verbose_name_plural": "Term Taxonomies",
            },
        ),
        migrations.CreateModel(
            name="TermTaxonomyItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("meta", models.JSONField(blank=True, default=dict, null=True)),
                ("object_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "term_taxonomy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_taxi.termtaxonomy",
                        verbose_name="Taxi",
                    ),
                ),
            ],
            options={
                "verbose_name": "Term Taxonomy Item",
                "verbose_name_plural": "Term Taxonomy Items",
            },
        ),
    ]
