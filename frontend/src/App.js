import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = 'http://localhost:5002/api';

function App() {
  const [emailText, setEmailText] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!emailText.trim()) {
      setError('Please enter some email text to analyze');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post(`${API_BASE_URL}/classify`, {
        email_text: emailText
      });

      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to classify email');
    } finally {
      setLoading(false);
    }
  };

  const clearForm = () => {
    setEmailText('');
    setResult(null);
    setError(null);
  };

  return (
    <div className="App">
      <div className="container">
        <h1>Email Spam Detector</h1>
        <p className="subtitle">
          Enter your email content below to check if it's spam or legitimate (ham)
        </p>

        <form onSubmit={handleSubmit} className="email-form">
          <div className="form-group">
            <label htmlFor="emailText">Email Content:</label>
            <textarea
              id="emailText"
              value={emailText}
              onChange={(e) => setEmailText(e.target.value)}
              placeholder="Paste your email content here..."
              rows={8}
              disabled={loading}
            />
          </div>

          <div className="button-group">
            <button
              type="submit"
              disabled={loading || !emailText.trim()}
              className="analyze-btn"
            >
              {loading ? 'Analyzing...' : 'Analyze Email'}
            </button>
            
            <button
              type="button"
              onClick={clearForm}
              disabled={loading}
              className="clear-btn"
            >
              Clear
            </button>
          </div>
        </form>

        {error && (
          <div className="error-message">
            <h3>Error</h3>
            <p>{error}</p>
          </div>
        )}

        {result && (
          <div className={`result-card ${result.prediction}`}>
            <h3>Analysis Result</h3>
            <div className="prediction">
              <span className="prediction-label">Prediction:</span>
              <span className={`prediction-value ${result.prediction}`}>
                {result.prediction.toUpperCase()}
              </span>
            </div>
            <div className="description">
              {result.prediction === 'spam' ? (
                <p>This email appears to be spam. Be cautious about clicking links or providing personal information.</p>
              ) : (
                <p>This email appears to be legitimate (ham). It's likely safe to read and respond to.</p>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
