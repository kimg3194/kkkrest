from .models import UserPost
from .serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer
    
    filter_backends = [SearchFilter]
    search_fields = ('title',)

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs=qs.none()
        
        # qs = qs.filter(author_id = 1)
        # qs = qs.filter(author=self.request.user)
        return qs