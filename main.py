import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from PIL import Image, ImageTk
import requests
import webbrowser

# use: pip install requests pytube Pillow

# Dictionary with exercise details
exercises = {
    'Pull': {
        'Deadlift': {
            'Reps': '5',
            'Sets': '1',
            'Video': 'https://www.youtube.com/watch?v=op9kVnSso6Q'
        },
        'Lat Pulldown': {
            'Reps': '8-12',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=op9kVnSso6Q'
        },
        'Chest Support Row': {
            'Reps': '8-12',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=op9kVnSso6Q'
        },
        'Face Pull': {
            'Reps': '15-20',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=op9kVnSso6Q'
        },
        'Hammer Curl': {
            'Reps': '8-12',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=op9kVnSso6Q'
        },
        'Bicep Curl': {
            'Reps': '15-20',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=op9kVnSso6Q'
        }
},
    'Push': {
        'Bench Press': {
            'Reps': '5',
            'Sets': '5',
            'Video': 'https://www.youtube.com/watch?v=BYKScL2sgCs'
        },
        'Overhead Press': {
            'Reps': '8-12',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=2yjwXTZQDDI'
        },
        'Incline Bench Press': {
            'Reps': '8-12',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=BYKScL2sgCs'
        },
        'Tricep Pushdown': {
            'Reps': '8-12',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=BYKScL2sgCs'
        },
        'Lateral Raise': {
            'Reps': '15-20',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=BYKScL2sgCs'
        },
    },
    'Legs': {
        'Squat': {
            'Reps': '5',
            'Sets': '5',
            'Video': 'https://www.youtube.com/watch?v=BYKScL2sgCs'
        },
        'Romanian Deadlift': {
            'Reps': '8-12',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=BYKScL2sgCs'
        },
        'Leg Press': {
            'Reps': '8-12',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=BYKScL2sgCs'
        },
        'Leg Curl': {
            'Reps': '8-12',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=BYKScL2sgCs'
        },
        'Seated Calf Raise': {
            'Reps': '15-20',
            'Sets': '3',
            'Video': 'https://www.youtube.com/watch?v=BYKScL2sgCs'
        },

    }
}

def show_exercise_details(exercise):
    details = exercises[workout_type.get()][exercise]
    reps_label.config(text='Reps: ' + str(details['Reps']))
    sets_label.config(text='Sets: ' + str(details['Sets']))
    video_url = details['Video']
    video_id = video_url.split('=')[-1]
    video_thumbnail = YouTube(video_url).thumbnail_url
    # Download the thumbnail image
    thumbnail_image = Image.open(requests.get(video_thumbnail, stream=True).raw)
    thumbnail_image = thumbnail_image.resize((320, 240), Image.ANTIALIAS)
    thumbnail = ImageTk.PhotoImage(thumbnail_image)
    video_label.configure(image=thumbnail)
    video_label.image = thumbnail
    # Store the video URL for later use
    video_label.video_url = video_url


def play_video():
    video_url = getattr(video_label, 'video_url', '')
    if video_url:
        webbrowser.open(video_url)
    else:
        messagebox.showinfo('No Video', 'No video URL available.')


def on_start():
    exercise_list.delete(0, tk.END)
    for exercise in exercises[workout_type.get()]:
        exercise_list.insert(tk.END, exercise)

def on_select(event):
    selected_index = exercise_list.curselection()
    if selected_index:
        selected_item = exercise_list.get(selected_index)
        show_exercise_details(selected_item)
    else:
        messagebox.showinfo('No Selection', 'Please select an exercise.')

# Create the main window
window = tk.Tk()
window.title('Gym Workout Planner')


# Set window dimensions and center it on the screen
window_width = 600
window_height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')


# Set window background color
window.configure(bg='#ffffff')

# Set font styles
title_font = ('Arial', 24, 'bold')
label_font = ('Arial', 12)
button_font = ('Arial', 14)

# Create a frame for the workout type selection
type_frame = tk.Frame(window, bg='#ffffff')
type_frame.pack(pady=20)

workout_type = tk.StringVar()
workout_type.set('Push')  # Default workout type

push_radio = tk.Radiobutton(type_frame, text='Push', variable=workout_type, value='Push', command=on_start, bg='#ffffff', font=label_font)
push_radio.pack(side=tk.LEFT)

pull_radio = tk.Radiobutton(type_frame, text='Pull', variable=workout_type, value='Pull', command=on_start, bg='#ffffff', font=label_font)
pull_radio.pack(side=tk.LEFT)

legs_radio = tk.Radiobutton(type_frame, text='Legs', variable=workout_type, value='Legs', command=on_start, bg='#ffffff', font=label_font)
legs_radio.pack(side=tk.LEFT)

# Create a listbox to display the exercises
exercise_list = tk.Listbox(window, width=40, height=10, font=label_font)
exercise_list.pack(pady=10)
exercise_list.bind('<<ListboxSelect>>', on_select)

# Create labels for exercise details
reps_label = tk.Label(window, text='Reps:', bg='#ffffff', font=label_font)
reps_label.pack()

sets_label = tk.Label(window, text='Sets:', bg='#ffffff', font=label_font)
sets_label.pack()

# Create a label for the exercise video
video_label = tk.Label(window, bg='#ffffff')
video_label.pack(pady=10)

# Add a button to play the exercise video
play_button = tk.Button(window, text='Play Video', command=play_video, bg='#4caf50', fg='#ffffff', font=button_font)
play_button.pack(pady=10)

# Add a button to start the workout
start_button = tk.Button(window, text='Start Workout', command=lambda: messagebox.showinfo('Workout', 'Let\'s start the workout!'), bg='#2196f3', fg='#ffffff', font=button_font)
start_button.pack(pady=10)

# Run the application
window.mainloop()