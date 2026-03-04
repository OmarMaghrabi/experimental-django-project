# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TableLikesSaves(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_user = models.ForeignKey('TableUser', models.DO_NOTHING, blank=True, null=True)
    fk_post = models.ForeignKey('TablePost', models.DO_NOTHING, blank=True, null=True)
    liked = models.IntegerField(blank=True, null=True)
    saved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_likes_saves'


class TablePost(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_user = models.ForeignKey('TableUser', models.DO_NOTHING, blank=True, null=True)
    post_text = models.CharField(max_length=255, blank=True, null=True)
    time_posted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_post'


class TablePostComments(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_user = models.ForeignKey('TableUser', models.DO_NOTHING, blank=True, null=True)
    fk_post = models.ForeignKey(TablePost, models.DO_NOTHING, blank=True, null=True)
    comment_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_post_comments'


class TablePostImg(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_post = models.ForeignKey(TablePost, models.DO_NOTHING, blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_post_img'


class TablePostVid(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_post = models.ForeignKey(TablePost, models.DO_NOTHING, blank=True, null=True)
    vid_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_post_vid'


class TableUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    passkey = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_user'
