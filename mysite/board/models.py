from django.db import models

class Board(models.Model):
    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField(verbose_name="내용")
    passwd = models.CharField(verbose_name="비밀번호", max_length=100)
    username = models.CharField(verbose_name="글쓴이", max_length=10)
    filename = models.CharField(verbose_name="파일명", max_length=100, null=True, blank=True)
    original_filename = models.CharField(verbose_name="원본파일명", max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    
    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'

    def __str__(self):
        return self.title