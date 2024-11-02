import React, { useState } from 'react';
import axios from 'axios';

function PredictionForm() {
  const [height, setHeight] = useState('');
  const [weight, setWeight] = useState('');
  const [prediction, setPrediction] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!height || !weight) {
      setError('Please enter both height and weight.');
      return;
    }

    try {
      const response = await axios.post('http://localhost:8000/api/predict/', {
        height: parseFloat(height),
        weight: parseFloat(weight),
      });

      setPrediction(response.data.prediction);
      setError('');
    } catch (error) {
      console.error(error);
      setError('Error making prediction. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Height (cm):
        <input
          type="number"
          value={height}
          onChange={(event) => setHeight(event.target.value)}
        />
      </label>
      <br />
      <label>
        Weight (kg):
        <input
          type="number"
          value={weight}
          onChange={(event) => setWeight(event.target.value)}
        />
      </label>
      <br />
      <button type="submit">Predict</button>
      {prediction && <p>Prediction: {prediction}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
}

export default PredictionForm;
