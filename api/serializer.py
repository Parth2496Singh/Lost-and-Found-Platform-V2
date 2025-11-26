from rest_framework import serializers
from reports.models import LostItems, FoundItem, Claim
from django.contrib.auth.models import User

class LostItemSerializer(serializers.ModelSerializer):
    has_approved_claim = serializers.SerializerMethodField()

    class Meta:
        model = LostItems
        fields = '__all__'

    def get_has_approved_claim(self, obj):
        # Check if any claim for this lost item has status 'Approved'
        return Claim.objects.filter(lost_item=obj, status='Approved').exists()

class FoundItemSerializer(serializers.ModelSerializer):
    has_approved_claim = serializers.SerializerMethodField()
    class Meta:
        model = FoundItem
        fields = '__all__'

    def get_has_approved_claim(self, obj):
        # Check if any claim for this found item has status 'Approved'
        return Claim.objects.filter(found_item=obj, status='Approved').exists()

from rest_framework import serializers
from reports.models import Claim

class ClaimSerializer(serializers.ModelSerializer):
    # For POST (input only)
    lost_item = serializers.PrimaryKeyRelatedField(
        queryset=LostItems.objects.all(),
        write_only=True
    )
    found_item = serializers.PrimaryKeyRelatedField(
        queryset=FoundItem.objects.all(),
        write_only=True
    )

    # For GET (output only — nested item details)
    lost_item_detail = LostItemSerializer(source='lost_item', read_only=True)
    found_item_detail = FoundItemSerializer(source='found_item', read_only=True)

    # Owner IDs
    lost_item_owner_id = serializers.SerializerMethodField()
    found_item_owner_id = serializers.SerializerMethodField()

    # Owner emails
    lost_owner_email = serializers.SerializerMethodField()
    found_owner_email = serializers.SerializerMethodField()

    status = serializers.CharField(read_only=True)

    class Meta:
        model = Claim
        fields = [
            'id',
            'lost_item',
            'found_item',
            'lost_item_detail',
            'found_item_detail',
            'status',
            'created_at',
            'lost_owner_email',
            'found_owner_email',
            'lost_item_owner_id',
            'found_item_owner_id'
        ]

    def get_lost_item_owner_id(self, obj):
        return obj.lost_item.user.id if obj.lost_item and obj.lost_item.user else None

    def get_found_item_owner_id(self, obj):
        return obj.found_item.user.id if obj.found_item and obj.found_item.user else None

    def get_lost_owner_email(self, obj):
        return obj.lost_item.user.email if obj.lost_item and obj.lost_item.user else None

    def get_found_owner_email(self, obj):
        return obj.found_item.user.email if obj.found_item and obj.found_item.user else None
    

 
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
