from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _


class MetaMixin(models.Model):
    meta = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        abstract = True


class Taxonomy(MetaMixin, models.Model):
    """ """

    name = models.CharField(max_length=128, verbose_name=_("Name"))
    slug = models.SlugField()
    parent = models.ForeignKey(
        "Taxonomy",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.SET_NULL,
        verbose_name=_("Parent"),
    )

    class Meta:
        verbose_name = _("Taxonomy")
        verbose_name_plural = _("Taxonomies")

    def __str__(self):
        return self.name


class Term(MetaMixin, models.Model):
    name = models.CharField(max_length=128, verbose_name=_("Name"))
    slug = models.SlugField()

    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Terms")

    def __str__(self):
        return self.name


class TermTaxonomy(MetaMixin, models.Model):
    term = models.ForeignKey(
        Term,
        on_delete=models.SET_NULL,
        related_name="taxonomies",
        null=True,
        verbose_name=_("Term"),
    )
    taxonomy = models.ForeignKey(
        Taxonomy,
        null=True,
        on_delete=models.SET_NULL,
        related_name="terms",
        verbose_name=_("Taxonomy"),
    )

    def __str__(self):
        return f"{self.taxonomy} / {self.term}"

    class Meta:
        verbose_name = _("Term Taxonomy")
        verbose_name_plural = _("Term Taxonomies")


class TermTaxonomyItem(MetaMixin, models.Model):
    term_taxonomy = models.ForeignKey(
        TermTaxonomy, null=True, on_delete=models.SET_NULL, verbose_name=_("Taxi")
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = _("Term Taxonomy Item")
        verbose_name_plural = _("Term Taxonomy Items")
