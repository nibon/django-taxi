from django import forms
from django.apps import apps
from django.contrib.contenttypes.fields import GenericRelation

app_name = apps.get_app_config("django_taxi").name


print("app_name", app_name)


class TaxiBaseField:
    taxonomy_slug = None

    def __init__(self, taxonomy_slug, *args, **kwargs):
        self.taxonomy_slug = taxonomy_slug
        super().__init__(*args, **kwargs)


class TaxiField(TaxiBaseField, forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple


class TaxiSingleField(TaxiBaseField, forms.ChoiceField):
    widget = forms.Select


class TaxiRelation(GenericRelation):
    taxonomy = f"{app_name}.TermTaxonomyItem"

    def __init__(self, taxonomy=None, **kwargs):
        if taxonomy:
            self.taxonomy = taxonomy
        super().__init__(self.taxonomy, **kwargs)