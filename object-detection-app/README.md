# Object Detection App

This project is designed to detect specific objects (in this case, chair seats) in real-time video streams. The application allows users to define a region of interest (ROI) for detection using a graphical interface.

## Project Structure

```
object-detection-app
├── src
│   ├── controllers
│   │   └── roi_selector.py  # Contains the ROISelector class for selecting the region of interest.
│   ├── models
│   │   └── __init__.py       # Placeholder for future data models related to object detection.
│   ├── views
│   │   └── __init__.py       # Placeholder for future view-related functions or classes.
│   └── app.py                # Main entry point of the application.
├── requirements.txt           # Lists the dependencies required for the project.
└── README.md                  # Documentation for the project.
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/object-detection-app.git
   cd object-detection-app
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   Execute the following command to start the application:
   ```bash
   python src/app.py
   ```

2. **Select the Region of Interest (ROI):**
   - A window will open displaying the video feed.
   - Use your mouse to click and drag to define a rectangle around the area where the chair seats will pass.
   - Press 'q' to finalize the selection.

3. **Object Detection:**
   - Once the ROI is selected, the application will begin detecting and marking the chair seats within the defined area.

## Future Enhancements

- Implement a training mechanism to improve the detection accuracy for the specific object (chair seats).
- Add functionality to save and load trained models.
- Enhance the user interface for better interaction and visualization of results.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.