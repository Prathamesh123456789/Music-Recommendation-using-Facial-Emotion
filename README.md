Here's the updated README with your GitHub username included:

---

# Emotion-Based Music Recommendation System 🎵🎭  

An innovative system that recommends music based on facial emotions. By leveraging **Haar Cascade Classifiers** for facial detection and emotion recognition, this project offers personalized music suggestions to enhance the user's mood.

## 🚀 Features  
- Real-time facial emotion detection.  
- Emotion-based music recommendation.  
- User-friendly interface for seamless interaction.  
- Experience feedback form for collecting user input.  

## 🛠️ Technology Stack  
- **Programming Language**: Python  
- **Libraries Used**:  
  - `OpenCV` for facial detection.  
  - `pandas` for data handling.  
  - `TensorFlow` for emotion recognition.
  - `WebBrowser` for opening URLs in the default web browser.
  - `Spotipy`     for integrating Spotify API to fetch music recommendations.
- **Frameworks**: Haar Cascade Classifiers for facial detection.


## 📂 Project Structure  
```
Emotion-Based-Music-Recommendation/
├── .devcontainer/            # Development container configuration  
├── .gitignore                # Git ignore file  
├── detect.py                 # Main script for facial emotion detection and music recommendation
├── requirements.txt          # Dependencies  
├── README.md                 # Project documentation  
└── LICENSE                   # License for the project  

```  

## ⚡ Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/prathmeshsagole/.git  
   ```  

2. Navigate to the project directory:  
   ```bash  
   cd Music-Recommendation-using-Facial-Emotion
   ```  

3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Run the application:  
   ```bash  
   python src/detect.py  
   ```  

## 🎨 How It Works  
1. The system uses Haar Cascade Classifiers to detect facial regions from webcam input.  
2. Emotions like *happy*, *sad*, *neutral*, etc., are recognized using facial landmarks.  
3. Based on the detected emotion, a curated playlist of songs is fetched and displayed.  
4. Users can provide feedback through an embedded form, helping improve the system.  

## 🌟 Features to Explore  
- **Emotion Detection**: Ensure your webcam is functional to capture real-time emotions.  
- **Customizable Playlists**: Update the `dataset/` folder with your own music for personalized recommendations.  
- **Feedback Integration**: Share your experience via the feedback form!  

## 🤝 Contribution  
Contributions are welcome! If you'd like to improve the project, please:  
- Fork the repository.  
- Create a feature branch: `git checkout -b feature-name`.  
- Commit your changes: `git commit -m 'Add feature-name'`.  
- Push to the branch: `git push origin feature-name`.  
- Open a pull request.  


## 💬 Feedback  
Have feedback or suggestions? Feel free to open an issue on the (https://github.com/prathmeshsagole/Music-Recommendation-using-Facial-Emotion) or drop a message!  

---

Let me know if there’s anything else you’d like to add or modify!
