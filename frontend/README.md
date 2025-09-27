# Email Spam Detector - Frontend

React app for detecting spam emails.

## What it does

- Takes email text and tells you if it's spam or not
- Works on desktop and mobile
- Shows errors if something goes wrong

## Setup

You need Node.js installed.

1. Install stuff:
   ```bash
   npm install
   ```

2. Run it:
   ```bash
   npm start
   ```

3. Go to [http://localhost:3000](http://localhost:3000)

## Build for production

```bash
npm run build
```

## Backend

This talks to a Flask API at `http://localhost:5002/api`. Start the backend first.

## How to use

1. Paste email text in the box
2. Hit "Analyze Email" 
3. See if it's spam or ham (not spam)
4. Hit "Clear" to start over

## What's inside

- **App.js** - Main React component
- **App.css** - Blue and white styling

## Tech used

- React
- Axios for API calls
- CSS

## Scripts

- `npm start` - Dev server
- `npm test` - Run tests  
- `npm run build` - Production build
- `npm run eject` - Eject from Create React App
