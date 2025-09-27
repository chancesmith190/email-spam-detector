# Email Spam Detector

A full-stack web application that uses machine learning to detect email spam. Built with Flask (backend API) and React (frontend).

## Architecture

- **Backend**: Flask API with Random Forest classifier using scikit-learn
- **Frontend**: Modern React application with responsive design
- **ML Model**: Random Forest trained on the spam/ham dataset with text preprocessing

## Features

- Real-time email classification (spam vs ham)
- Confidence scoring for predictions
- Modern, responsive React UI
- RESTful API design
- Text preprocessing with NLTK (stemming, stopword removal)

## Quick Start

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd email-spam-detector
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask API server:
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The React app will be available at `http://localhost:3000`

## API Endpoints

- `GET /api/health` - Health check
- `GET /api/info` - Model information
- `POST /api/classify` - Classify email text

### Classification Request Format

```json
{
  "email_text": "Your email content here..."
}
```

### Classification Response Format

```json
{
  "prediction": "spam" | "ham",
  "confidence": 0.95,
  "email_text": "Your email content here..."
}
```
