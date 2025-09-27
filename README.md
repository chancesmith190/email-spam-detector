# Email Spam Detection System

A web application that classifies emails as spam or legitimate using machine learning. Built with Flask backend and React frontend.

## Overview

This application uses a Random Forest classifier to analyze email text and determine if it's spam. The model processes text using natural language processing techniques including stemming and stopword removal.

## Tech Stack

**Backend:**
- Flask web framework
- scikit-learn for machine learning
- NLTK for text processing
- pandas and numpy for data handling

**Frontend:**
- React
- Axios for API calls
- CSS for styling

## Setup

### Requirements
- Python 3.8+
- Node.js 16+

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
```bash
python app.py
```

The API runs on `http://localhost:5002`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The app runs on `http://localhost:3000`

## API Endpoints

- `GET /api/health` - Check if the API is running
- `GET /api/info` - Get model information
- `POST /api/classify` - Classify email text

### Classification Request

Send a POST request to `/api/classify` with:

```json
{
  "email_text": "Your email content here"
}
```

### Response

```json
{
  "prediction": "spam",
  "confidence": 0.85,
  "email_text": "Your email content here"
}
```

## How It Works

1. **Text Preprocessing**: Email text is cleaned by removing punctuation, converting to lowercase, removing stopwords, and applying stemming
2. **Vectorization**: Processed text is converted to numerical features using CountVectorizer
3. **Classification**: Random Forest model predicts spam/ham with confidence score
4. **Response**: Result is returned via REST API

## Model Details

- **Algorithm**: Random Forest Classifier
- **Training Data**: 5,572 emails from spam/ham dataset
- **Text Processing**: NLTK stemming and stopword removal
- **Accuracy**: Approximately 95% on test data

## Project Structure

```
email-spam-detector/
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── spam_ham_dataset.csv # Training data
├── frontend/
│   ├── src/
│   │   ├── App.js         # Main React component
│   │   └── App.css        # Styles
│   └── package.json       # Node dependencies
└── README.md              # This file
```

## Usage

1. Start both backend and frontend servers
2. Open browser to `http://localhost:3000`
3. Enter email text in the textarea
4. Click "Analyze Email" to get classification
5. View spam/ham prediction with confidence score

## Development

To modify the model, edit the preprocessing or classification logic in `backend/app.py`. For UI changes, modify the React components in `frontend/src/`.

The model retrains automatically when the application starts using the provided dataset.