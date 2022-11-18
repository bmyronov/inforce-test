from menu.models import Menu, MenuMeal

from rest_framework import serializers


class MenuMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuMeal
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    restaurant = serializers.HiddenField(default=serializers.CurrentUserDefault())
    meal = MenuMealSerializer(many=True)

    class Meta:
        model = Menu
        fields = '__all__'

    def create(self, validated_data):
        # Getting restaurant_id
        user = self.context['request'].user

        # Getting meals from the payload
        meals = validated_data.pop('meal')

        menu = self.Meta.model(**validated_data)
        menu.restaurant = user
        menu.save()

        for meal in meals:
            # Adding meals from the payload
            meal_obj = MenuMeal.objects.create(**meal)
            menu.meal.add(meal_obj.id)

        return menu
