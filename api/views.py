from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DummyDataSerializer
import pandas as pd
from .pigmgt import perform_analysis  # Import your analysis function

REFERENCE_PATH = "Reference Pig Data.csv"  # Path to reference data CSV

@api_view(['POST'])
def analyze_pig_data(request):
    serializer = DummyDataSerializer(data=request.data, many=True)  # Expecting a list of entries
    if serializer.is_valid():
        # Load the reference data
        pig_data = pd.read_csv(REFERENCE_PATH)
        
        # Convert incoming dummy data to a DataFrame for compatibility with perform_analysis
        dummy_data = pd.DataFrame(serializer.validated_data)
        
        # Call the perform_analysis function
        predictions = perform_analysis(pig_data, dummy_data)
        
        # Return JSON response with the analysis results
        return Response(predictions)
    return Response(serializer.errors, status=400)
