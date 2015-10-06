from uuid import uuid4
from django.db.models import Model, ForeignKey, CharField, UUIDField


class BaseModel(Model):
    uuid = UUIDField(default=uuid4, unique=True)
    name = CharField(max_length=255)

    class Meta:
        abstract = True

    def to_dict(self):
        return {
            'type': 'base',
            'id': self.id,
            'uuid': str(self.uuid),
            'name': self.name,
        }

    def __str__(self):
        return "%s - %s" % (self.uuid, self.name)

    def __repr__(self):
        return "<BaseModel: %s>" % self.__str__()


class Project(BaseModel):

    def to_dict(self):
        d = super(Project, self).to_dict()
        d.update({
            "type": "project",
        })
        return d

    def __repr__(self):
        return "<Project: %s>" % self.__str__()


class File(BaseModel):
    project = ForeignKey(Project, related_name='files')

    def to_dict(self):
        d = super(File, self).to_dict()
        d.update({
            "type": "file",
            "project": self.project_id,
        })
        return d

    def __repr__(self):
        return "<File: %s>" % self.__str__()


class Page(BaseModel):
    file = ForeignKey(File, related_name='pages')

    def to_dict(self):
        d = super(Page, self).to_dict()
        d.update({
            "type": "page",
            "file": self.file_id,
        })
        return d

    def __repr__(self):
        return "<Page: %s>" % self.__str__()
