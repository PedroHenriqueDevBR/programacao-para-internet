from rest_framework import serializers
from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category', 'created')

    def validate_name(self, value):
        game = Game.objects.filter(name=value)
        if game:
            raise serializers.ValidationError("Não pode ter dois jogos com o mesmo nome.")
        return value
