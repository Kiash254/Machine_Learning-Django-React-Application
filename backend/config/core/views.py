import joblib
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Load the saved model from disk
model = joblib.load('model.pkl')

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
