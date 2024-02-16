# GPTVideoInsights

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv)
![PIL](https://img.shields.io/badge/PIL-%23FFFFFF?style=for-the-badge&logo=python&logoColor=black)
![Tkinter](https://img.shields.io/badge/Tkinter-%2307405e?style=for-the-badge&logo=python&logoColor=white)

GPTVideoInsights is a cutting-edge application designed to transform the way users interact with video content. By allowing users to upload videos and ask questions about the video content, the application leverages the power of GPT (Generative Pre-trained Transformer) for providing accurate and context-aware insights. This innovative approach to video analysis is both informative and user-friendly, making it an essential tool for educators, content creators, and anyone looking to gain deeper insights into video content.

The application processes videos into image frames, truncates some frames, and sends them to the OpenAI LLM for analysis, ensuring a comprehensive understanding of the video content through advanced AI techniques.

## 🌐 Architecture

GPTVideoInsights employs a sophisticated architecture that includes:

- **cv2 (OpenCV)**: Used for reading frames from videos efficiently.
- **PIL (Python Imaging Library)**: For displaying image frames sequentially.
- **Tkinter**: Provides a robust framework for designing the user interface, including video display and interactive input prompt buttons.
- **Threading**: Ensures smooth operation by allowing two screens to run concurrently; one displays the video, while the other handles input prompts and responses.

This architecture facilitates a seamless and interactive user experience, enabling efficient video analysis and insights generation.

## 🚀 Getting Started

To begin using GPTVideoInsights, follow the steps below:

### 🛠️ Prerequisites

Before you start, ensure you have the following installed:

- Python (version 3.9 or later)
- Git

### 🛠️ Installation

#### Step 1: Clone the Repository

Clone the GPTVideoInsights repository to your local machine:

```bash
git clone https://github.com/RamishUrRehman007/GPTVideoInsights.git

```
#### Step 2: Install Dependencies

Navigate to the project directory and install the required Python packages:

```bash
cd GPTVideoInsights
pip install -r requirements.txt
```

#### Step 3: Replace Default Values and Run

Replace the default values in the code with your own video path and OpenAI API key to personalize the application setup:

```python
12 video_path = "YOUR_VIDEO_PATH_HERE"
13 api_key = "YOUR_API_KEY_HERE"
```


```bash
python gpt_video_insights.py
```