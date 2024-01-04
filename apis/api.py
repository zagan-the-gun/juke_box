from ninja import NinjaAPI
from .models import Joint, Music
from .schemas import JointSchema, MusicSchema, MusicCreateSchema, NotFoundSchema
from typing import List, Optional


api = NinjaAPI()

@api.post("/joints", response={201: JointSchema})
def create_joint(request, joint: JointSchema):
    joint = Joint.objects.create(**joint.dict())
    return joint

@api.get("/joints", response=List[JointSchema])
def joints(request, name: Optional[str] = None):
    if name:
        return Joint.objects.filter(name__icontains=name)
    return Joint.objects.all()

@api.get("/joints/{joint_id}", response={200: JointSchema, 404: NotFoundSchema})
def joint(request, joint_id: int):
    try:
        joint = Joint.objects.get(pk=joint_id)
        return 200, joint
    except Joint.DoesNotExist as e:
        return 404, {"message": "Joint does not exist"}

@api.put("/joints/{joint_id}", response={200: JointSchema, 404: NotFoundSchema})
def change_joint(request, joint_id: int, data: JointSchema):
    try:
        joint = Joint.objects.get(pk=joint_id)
        for attribute, value in data.dict().items():
            setattr(joint, attribute, value)
        joint.save()
        return 200, joint
    except Joint.DoesNotExist as e:
        return 404, {"message": "Joint does not exist"}

@api.delete("/joints/{joint_id}", response={200: None, 404: NotFoundSchema})
def delete_joint(request, joint_id: int, data: JointSchema):
    try:
        joint = Joint.objects.get(pk=joint_id)
        joint.delete()
        return 200
    except Joint.DoesNotExist as e:
        return 404, {"message": "Joint does not exist"}



@api.post("/musics", response={201: MusicCreateSchema})
def create_music(request, music: MusicCreateSchema):
    
    music = Music.objects.create(**music.dict())
    return music

@api.get("/musics", response=List[MusicSchema])
def musics(request, name: Optional[str] = None):
    if name:
        return Music.objects.filter(name__icontains=name)
    return Music.objects.all()

@api.get("/musics/{music_id}", response={200: MusicSchema, 404: NotFoundSchema})
def music(request, music_id: int):
    try:
        music = Music.objects.get(pk=music_id)
        return 200, music
    except Music.DoesNotExist as e:
        return 404, {"message": "Music does not exist"}

@api.put("/musics/{music_id}", response={200: MusicCreateSchema, 404: NotFoundSchema})
def change_music(request, music_id: int, data: MusicCreateSchema):
    try:
        music = Music.objects.get(pk=music_id)
        for attribute, value in data.dict().items():
            setattr(music, attribute, value)
        music.save()
        return 200, music
    except Music.DoesNotExist as e:
        return 404, {"message": "Music does not exist"}

@api.delete("/musics/{music_id}", response={200: None, 404: NotFoundSchema})
def delete_music(request, music_id: int, data: MusicSchema):
    try:
        music = Music.objects.get(pk=music_id)
        music.delete()
        return 200
    except Music.DoesNotExist as e:
        return 404, {"message": "Music does not exist"}


