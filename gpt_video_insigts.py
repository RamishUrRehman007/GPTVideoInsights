import tkinter as tk
from tkinter import scrolledtext, Toplevel
from PIL import Image, ImageTk
import base64
import cv2
import io
import queue
from threading import Thread
from openai import OpenAI

base64Frames = list()
video_path = "data/sample_video.mp4"
api_key = "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"

def center_window(window, width=800, height=1000):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    center_x = int(screen_width/2 - width / 2)
    center_y = int(screen_height/2 - height / 2)

    window.geometry(f'{width}x{height}+{center_x}+{center_y}')

class VideoPlayer:
    def __init__(self, video_path, frame_queue, label, callback):
        self.video_path = video_path
        self.frame_queue = frame_queue
        self.label = label
        self.callback = callback 

    def load_video_frames(self):
        video = cv2.VideoCapture(self.video_path)
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
            _, buffer = cv2.imencode('.jpg', frame)
            encoded_frame = base64.b64encode(buffer)
            base64Frames.append(encoded_frame.decode("utf-8"))
            self.frame_queue.put(encoded_frame)
        self.frame_queue.put(None)
        video.release()

    def display_next_frame(self):
        if not self.frame_queue.empty():
            frame_data = self.frame_queue.get()
            if frame_data is None: 
                self.callback()  
                return
            image = Image.open(io.BytesIO(base64.b64decode(frame_data)))
            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo
            self.label.after(42, self.display_next_frame)
        else:
            self.label.after(10, self.display_next_frame)

def open_query_screen():
    query_window = Toplevel()
    query_window.title("Get GPT Insights")
    
    center_window(query_window, 500, 300)

    input_text = scrolledtext.ScrolledText(query_window, height=4)
    input_text.pack()

    response_text_box = scrolledtext.ScrolledText(query_window, height=8)
    response_text_box.pack()

    submit_button = tk.Button(query_window, text="Get GPT Insights", command=lambda: gpt_insights(input_text, response_text_box))
    submit_button.pack()

def gpt_insights(input_text_widget, response_text_box):
    prompt = input_text_widget.get("1.0", tk.END).strip()
    gpt_response = openai_call(prompt)
    response_text_box.insert(tk.END, gpt_response + "\n")


def openai_call(prompt: str):
    client = OpenAI(api_key=api_key)
    PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": [
                prompt,
                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::50]),
            ],
        },
    ]
    params = {
        "model": "gpt-4-vision-preview",
        "messages": PROMPT_MESSAGES,
        "max_tokens": 512,
    }


    result = client.chat.completions.create(**params)
    return result.choices[0].message.content

def main():
    root = tk.Tk()
    root.title("GPT Video Insights")

    center_window(root, 1000, 850)
    
    label = tk.Label(root)
    label.pack()
    
    frame_queue = queue.Queue()
    
    video_player = VideoPlayer(video_path, frame_queue, label, open_query_screen)
    Thread(target=video_player.load_video_frames).start()
    video_player.display_next_frame()

    root.mainloop()

if __name__ == "__main__":
    
    main()
