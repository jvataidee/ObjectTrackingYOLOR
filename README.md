![Project Image](capa.png)
# Object Tracking with YOLOR  by João Ataíde

This project is a Streamlit-based object tracking dashboard that utilizes the YOLOR algorithm. It allows you to track objects in a video and provides various settings to customize the tracking process.

# Usage
To run the project, follow these steps:

1. Clone the repository:

# Settings

* `Confidence:` Adjust the confidence level for object detection (range: 0.0 to 1.0).
* `Width:` Specify the desired width for the video (minimum: 300, maximum: 2000).
* `Save Image:` Enable this option to save the processed frames as images.
* `GPU:` Enable GPU acceleration for faster processing.
* `Demo Noturna:` Toggle between night and day mode for the demo video.
* `Use Custom Classes:` Enable this option to select custom classes for tracking.
* `Select The Custom Classes:` Choose the specific custom classes to track (if enabled).
* `Upload video:` Upload a video file for object tracking.

<p align="center">
  <img src="https://github.com/jvataidee/TrakingWithYOLOR/blob/main/layout.png" alt="Demo" width="50%" height="50%">
</p>

# Functionality
The dashboard performs the following tasks:

* Resizes the uploaded video to the specified width and automatically adjusts the height.
* Adds a logo to the sidebar.
* Displays the main title and sidebar title.
* Adjusts the sidebar width based on its expansion state.
* Provides sliders and input fields for various settings.
* Loads the demo video if no video is uploaded.
* Processes the video frames using the YOLOR algorithm and displays the processed frames in real-time.
* Shows key performance indicators (KPIs) such as frame rate, tracked objects, and width.
* Handles exceptions and ensures smooth execution.

Note: The YOLOR algorithm is implemented in the yolor module, which is imported at the beginning of the script.
