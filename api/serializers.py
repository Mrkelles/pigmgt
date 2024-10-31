# api/serializers.py
from rest_framework import serializers

class DummyDataSerializer(serializers.Serializer):
    week = serializers.IntegerField()
    number_of_pigs = serializers.IntegerField()
    age = serializers.IntegerField()
    start_weight = serializers.FloatField()
    end_weight = serializers.FloatField()
    average_weekly_weight_gain = serializers.FloatField()
    cumulative_weight_gain = serializers.FloatField()
    adg = serializers.FloatField()
    adfi = serializers.FloatField()
    average_weekly_feed_intake = serializers.FloatField()
    cumulative_feed_intake = serializers.FloatField()
    fcr = serializers.FloatField()
    cumulative_fcr = serializers.FloatField()
    feed_cost_per_kg = serializers.FloatField()
    average_weekly_feed_cost = serializers.FloatField()
    cumulative_feed_cost = serializers.FloatField()
    feed_class = serializers.CharField()
    protein_content = serializers.FloatField()
    energy_content = serializers.FloatField()
    health_interventions = serializers.CharField()
    environmental_temp = serializers.FloatField()
    environmental_humidity = serializers.FloatField()
    notes = serializers.CharField()