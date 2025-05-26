# NoteLet - FastAPI Note Taking Application

A modern, responsive note-taking application built with FastAPI, MongoDB, and Bootstrap 5.

## Features

- Create, Read, Update, and Delete notes
- Mark notes as important
- Search notes by title or description
- Responsive design
- Modern UI with Bootstrap 5
- Real-time updates
- MongoDB database integration

## Tech Stack

- FastAPI - Modern Python web framework
- MongoDB - NoSQL Database
- Bootstrap 5 - Frontend framework
- Jinja2 Templates - Server-side templating
- Python 3.8+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/notelet.git
cd notelet
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up MongoDB:
- Create a MongoDB Atlas account or use local MongoDB
- Update the connection string in `config/db.py`

5. Run the application:
```bash
uvicorn main:app --reload
```

6. Open your browser and navigate to `http://localhost:8000`

## Project Structure

```
notelet/
├── config/
│   └── db.py
├── models/
│   └── note.py
├── routes/
│   └── note.py
├── schemas/
│   └── note.py
├── static/
├── templates/
│   ├── index.html
│   └── edit.html
├── main.py
├── requirements.txt
└── README.md
```

## Environment Variables

Create a `.env` file in the root directory and add your MongoDB connection string:
```
MONGO_URI=your_mongodb_connection_string
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 