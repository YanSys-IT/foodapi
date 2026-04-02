from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Prefetch
from .models import Food, FoodCategory
from .serializers import FoodListSerializer


class FoodListView(APIView):
    def get(self, request):
        published_foods = Food.objects.filter(is_publish=True).prefetch_related(
            Prefetch('additional', queryset=Food.objects.filter(is_publish=True))
        )

        categories = (
            FoodCategory.objects
            .prefetch_related(Prefetch('food', queryset=published_foods))
            .filter(food__is_publish=True)
            .distinct()
        )

        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)
