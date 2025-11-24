# 🚀 Streamlit Cloud Deployment Checklist

## ✅ Pre-Deployment (COMPLETED)
- [x] Code pushed to GitHub: https://github.com/vinayredee/AI-Powered-Legal-Chat-Bot
- [x] Requirements.txt created
- [x] Packages.txt created
- [x] App.py is the main file

## 📋 Deployment Steps

### 1. Go to Streamlit Cloud
Visit: **https://share.streamlit.io**

### 2. Sign in with GitHub
Click **"Sign in"** and use your GitHub account (vinayredee)

### 3. Create New App
Click **"New app"** button

### 4. Configure Your App
- **Repository**: `vinayredee/AI-Powered-Legal-Chat-Bot`
- **Branch**: `main`
- **Main file path**: `app.py`

### 5. Add API Secret (IMPORTANT!)
Click **"Advanced settings"** → **"Secrets"**

Paste this EXACTLY:
```toml
GEMINI_API_KEY = "AIzaSyAQtYW_yX_6Xqmlm-AcjMPSqHMoJwUwC50"
```

### 6. Deploy
Click **"Deploy!"** button

Wait 2-3 minutes for deployment to complete.

## 🎉 Your App URL
After deployment, you'll get a URL like:
`https://ai-powered-legal-chat-bot-xxxxxx.streamlit.app`

## ⚠️ Important Notes
- The voice features won't work on cloud (no microphone/speaker)
- The AI will work perfectly using Gemini API
- Database will be reset on each deployment (cloud limitation)

## 🐛 If Deployment Fails
Check the logs in Streamlit Cloud for errors. Common issues:
- Missing API key in secrets
- Typo in repository name
- Wrong main file path (should be `app.py`)
