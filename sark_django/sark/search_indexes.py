from haystack import indexes

from . import models

class ProgramIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date = indexes.DateField(model_attr="broadcast_date")

    def get_model(self):
        return models.RadioShow

    def index_queryset(self, using=None):
        return self.get_model().objects


