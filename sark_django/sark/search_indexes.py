from haystack import indexes

from . import models

class ProgramIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date = indexes.DateField(model_attr="date")
    host = indexes.CharField(model_attr="host", faceted=True)
    # performers = indexes.MultiValueField(faceted=True)
    # instruments = indexes.MultiValueField(faceted=True)

    def get_model(self):
        return models.RadioShow

    # def prepare_performers(self, obj):
    #     return [performer.name for performer in obj.performers.all()]
    #
    # def prepare_instruments(self, obj):
    #     return [instrument.name for instrument in obj.instruments.all()]

    def index_queryset(self, using=None):
        return self.get_model().objects

class FieldRecordingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date = indexes.DateField(model_attr="date")
    performers = indexes.MultiValueField(faceted=True)
    instruments = indexes.MultiValueField(faceted=True)

    def get_model(self):
        return models.FieldRecording

    def prepare_performers(self, obj):
        performances = [performance for performance in obj.performances.all()]
        performers = []
        for performance in performances:
            for performer in performance.performers.all():
                performers.append(performer)
        return performers

    def prepare_instruments(self, obj):
        performances = [performance for performance in obj.performances.all()]
        instruments = []
        for performance in performances:
            for instrument in performance.instruments.all():
                instruments.append(instrument.name)
        return instruments

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class AgentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr="name", faceted=True)

    def get_model(self):
        return models.Agent

    def index_queryset(self, using=None):
        return self.get_model().objects

