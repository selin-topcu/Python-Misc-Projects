import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

app = tk.Tk()
app.geometry("532x622")
app.title("Text to Image App")
ctk.set_appearance_mode("dark")

input = ctk.CTkEntry(height=40, width=512, text_font=("Arial", 20), text_color="black", fg_color="white")
input.place(x=10, y=10)

body = ctk.CTkLabel(height=512, width=512)
body.place(x=10, y=110)

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16,
                                               use_auth_token=auth_token)
pipe.to(device)


def create():
    with autocast(device):
        img = pipe(input.get(), guidance_scale=8.5)["sample"][0]

    img.save('createImage.png')
    imgShow = ImageTk.PhotoImage(img)
    body.configure(img=imgShow)


trigger = ctk.CTkButton(height=40, width=120, text_font=("Arial", 20), text_color="black", fg_color="green",
                        command=create)
trigger.configure(text="Create")
trigger.place(x=200, y=60)

app.mainloop()
