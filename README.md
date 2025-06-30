#Facial Recognition Advanced Attendance System
This project is a smart attendance management system designed for educational institutions. It uses facial recognition to automate student attendance, enhancing accuracy, security, and efficiency.

📌 Features
🔍 Real-time facial recognition using OpenCV

👩‍💻 User-friendly graphical interface with Tkinter

🗃️ Secure student data management using MySQL database

⏱️ Quick and automatic attendance marking

📊 Attendance records saved and viewable

🛠️ Technologies Used
Python

OpenCV – for face detection and recognition

Tkinter – for GUI

MySQL – for database management

PIL (Pillow) – for image processing

NumPy – for array operations

📁 Project Structure
graphql
Copy
Edit
Facial_Recognition_Attendance_System/
│
├── dataset/                  # Stored face images
├── trainer/                  # Trained model files
├── attendance/               # Attendance CSV logs
├── main.py                   # Main application file
├── database.py               # DB connection and queries
├── train_model.py            # Face model training script
├── face_recognition.py       # Face detection & recognition logic
├── gui.py                    # GUI interface with Tkinter
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
✅ How It Works
Data Collection – Capture student face images using webcam

Model Training – Train the recognition model with collected images

Face Recognition – Recognize faces in real-time and mark attendance

Data Logging – Save attendance details in the database and log files

🚀 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/facial-attendance-system.git
cd facial-attendance-system
Install dependencies

nginx
Copy
Edit
pip install -r requirements.txt
Set up MySQL database

Create a database (e.g., attendance_db)

Run provided SQL scripts (if available) to create necessary tables

Run the application

css
Copy
Edit
python main.py
