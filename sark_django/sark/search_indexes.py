from haystack import indexes

from . import models

class ProgramIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    broadcast_date = indexes.DateField(model_attr="broadcast_date")
    host = indexes.CharField(model_attr="host", faceted=True)

    def get_model(self):
        return models.RadioShow

    def index_queryset(self, using=None):
        return self.get_model().objects


class AgentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr="name", faceted=True)

    def get_model(self):
        return models.Agent

    def index_queryset(self, using=None):
        return self.get_model().objects

