from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from user.models import User

from comment.models import PostType, Comment, Like
from comment.serializers import CommentSerializer, LikeSerializer

class CommentView(APIView):
    # 댓글 조회 : /comment/<posttype_id>/<post_id>/
    def get(self, request, posttype_id, post_id):
        comments = Comment.objects.filter(posttype=posttype_id, post_id=post_id)

        comment_serializer = CommentSerializer(comments, many=True).data

        return Response(comment_serializer, status=status.HTTP_200_OK)

    # 댓글 작성 : /comment/
    def post(self, request):
        # print(request.data)
        request_user = request.data.get("user", "")
        request_posttype = request.data.get("posttype", "")

        user = User.objects.get(id=request_user)
        posttype = PostType.objects.get(id=request_posttype)

        comment_serializer = CommentSerializer(data=request.data)

        if comment_serializer.is_valid():
            comment_serializer.save(user=user, posttype=posttype)
            return Response({"message": "댓글 작성 성공"}, status=status.HTTP_200_OK)

        return Response({"error": "댓글 작성 실패"}, status=status.HTTP_400_BAD_REQUEST)

    # 댓글 수정 : /comment/<comment_id>
    def put(self, request):
        return Response({})

    # 댓글 삭제 : /comment/<comment_id>
    def delete(self, request):
        return Response({})

class LikeView(APIView):
    # 좋아요 등록 : /like/
    def post(self, request):
        return Response({})

    # 좋아요 취소 : /like/
    def delete(self, request):
        return Response({})
