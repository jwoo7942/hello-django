from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_content', 'is_publish', 'tags', 'created_at'] #게시판 항목 수정
    list_display_links = ['title']   #title 부분에 링크를 걸 수 있도록. 이거 안해주면 디폴트는 첫번째 컬럼(id)이 링크
    list_filter = ['is_publish']
    search_fields = ['title']        #title을 검색할 수 있도록 검색필드 추가

    def short_content(self, post):
        return post.content[:20] + ' ...'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

