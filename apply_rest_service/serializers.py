from db_tables.models import Player,Items
from rest_framework import serializers


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('url', 'player_name', 'password', 'date_of_registration')

class ItemsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Items
		fields = ('url', 'item_id', 'name', 'description')
