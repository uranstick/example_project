from drf_haystack.serializers import HaystackSerializerMixin
from rest_framework import serializers

from example.models import WeaponFilterValue, WeaponFilter, Weapon


class WeaponFilterValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeaponFilterValue
        fields = ('id', 'name', 'icon')


class WeaponFilterSerializer(serializers.ModelSerializer):

    values = WeaponFilterValueSerializer(
        source='armslineweaponfiltervalue_set', many=True
    )

    class Meta:
        model = WeaponFilter
        fields = (
            'id', 'name', 'values', 'is_show_catalogue_weapon',
            'is_show_catalogue_reloading', 'is_show_our_work',
            'show_if_selected'
        )


class WeaponSerializer(serializers.ModelSerializer):

    filters = serializers.WeaponFilterSerializer(
        source='weaponfilter_set', many=True
    )
    url = serializers.SerializerMethodField()
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    caliber_name = serializers.CharField(source='caliber.name', read_only=True)
    adaptability_name = serializers\
        .CharField(source='adaptability.name', read_only=True)
    stock = serializers.SerializerMethodField()

    class Meta:
        model = Weapon
        fields = (
            'name', 'img', 'img_center', 'img_right', 'img_pistol', 'price',
            'brand', 'caliber', 'adaptability', 'filters', 'url', 'brand_name',
            'caliber_name', 'adaptability_name', 'catalogue', 'quantity',
            'stock', 'catalogue_video', 'seo_description', 'seo_keywords',
            'is_show_our_work'
        )

    def get_filters(self, obj):
        return obj.filters.values_list('id', flat=True)

    def get_url(self, obj):
        return obj.get_absolute_url()
