from ninja import Schema
from ninja import ModelSchema
from .models import Music

from datetime import datetime


class JointSchema(Schema):
    name:        str
    description: str
    is_active:   bool
    created_at:  datetime
    updated_at:  datetime

class MusicSchema(ModelSchema):
    class Meta:
        model = Music
        fields = "__all__"

class MusicCreateSchema(ModelSchema):
#    class Meta:
    joint_id: int
    class Config:
        model = Music
        model_fields = ['name', 'description', 'url']

class NotFoundSchema(Schema):
    message: str

