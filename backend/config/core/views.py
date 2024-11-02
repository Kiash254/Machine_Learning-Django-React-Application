import joblib
import numpy as np
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Load the saved model from disk using an absolute path
model_path = os.path.join('model.pkl')
model = joblib.load(model_path)

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        data = request.POST.dict()
        
        try:
            height = float(data.get('height'))
            weight = float(data.get('weight'))
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid input values'}, status=400)
        
        X = np.array([[height, weight]])
        
        # Make a prediction
        y_pred = model.predict(X)
        return JsonResponse({'prediction': str(y_pred[0])})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
