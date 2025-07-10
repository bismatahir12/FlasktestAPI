# Flask Text API  
A simple Flask API that processes text via JSON POST requests.  

## Features  
1. **Task 1**: Count words in a string.  
2. **Task 2**: Calculate character frequencies (ignoring spaces).  

## How to Test  
### Prerequisites  
- Python 3.x  
- Flask (`pip install flask`)  

### Steps  
1. **Run the Flask server**:  
   ```bash
   python app.py
   ```
   ![Flask Server Running](/screenshots/flask_server.png)  

2. **Test Task 1 (Word Count)**:  
   ```powershell
   curl -Uri "http://127.0.0.1:5000/task01" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"text": "hello world from flask"}'
   ```
   ![Task 1 Output](/screenshots/task1_wordcount.png)  

3. **Test Task 2 (Character Frequency)**:  
   ```powershell
   curl -Uri "http://127.0.0.1:5000/task02" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"text": "banana"}'
   ```
   ![Task 2 Output](/screenshots/task2_frequency.png)  

## Code  
See [app.py](app.py) for the implementation.  