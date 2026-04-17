# 📚 AI-Powered Book Insight Platform

An AI-powered full-stack web application that provides book summaries, recommendations, sentiment/genre insights, and intelligent Q&A using a RAG (Retrieval-Augmented Generation) pipeline.

## 🚀 Features

- 📖 Book Listing and Details
- ✨ AI-generated Summaries
- 🤖 Ask AI (RAG-based Q&A)
- 📊 Genre and Sentiment Insights
- 📚 Book Recommendations
- 💎 Premium React UI

## 🛠 Tech Stack

### Frontend
- React.js
- Tailwind CSS

### Backend
- Django
- Django REST Framework

### AI / ML
- LM Studio (Local LLM)
- Sentence Transformers
- ChromaDB Vector Database

## 🧠 How RAG Works

1. Book descriptions are converted into embeddings.
2. Stored in ChromaDB vector database.
3. User asks a question.
4. Relevant chunks are retrieved.
5. LLM generates contextual answer.

## 📂 Project Structure

backend/ → Django API  
frontend/ → React App

## ▶️ Run Locally

### Backend

```bash
cd backend
python manage.py runserver

```
### Frontend

```bash
cd frontend
npm install
npm start
```
## 📌 API Endpoints

### GET APIs

- `/api/books/`
- `/api/books/<id>/`
- `/api/summary/<id>/`
- `/api/insights/<id>/`
- `/api/recommend/<id>/`

### POST APIs

- `/api/ask/`
- `/api/load-vectors/`

## 📌 Sample Questions

- What is Atomic Habits about?
- Recommend books like The Alchemist
- Which books are self-help related?
- Give summary of Deep Work
- Which book has motivational tone?

## 📸 Screenshots

<img width="1910" height="915" alt="screenshot-1776441773011" src="https://github.com/user-attachments/assets/492484e1-5444-4a22-9144-4fc282a329f4" />
---
<img width="1600" height="766" alt="WhatsApp Image 2026-04-17 at 9 24 13 PM" src="https://github.com/user-attachments/assets/583406f1-a89e-490c-9f79-7c6727162fdd" />
---
<img width="1600" height="766" alt="WhatsApp Image 2026-04-17 at 9 16 32 PM" src="https://github.com/user-attachments/assets/b2f69a1c-a223-4991-817d-2e620195fb10" />
---
<img width="1600" height="766" alt="WhatsApp Image 2026-04-17 at 9 25 02 PM" src="https://github.com/user-attachments/assets/f962d7b8-4732-447d-a8cd-275c3409bbdd" />
---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
npm install
```
Backend Requirements
- Python 3.x
- Django
- Django REST Framework
- sentence-transformers
- chromadb
- requests
- beautifulsoup4
  
Frontend Requirements
- Node.js
- npm
- React.js
- Tailwind CSS

## 👨‍💻 Author
Adarsh Ranjan Rout

