from tkinter_webcam import webcam
import customtkinter as ctk

BORDER_WIDTH_UNIV = 3

# Set default themes and appearance
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

# Define window size and name
root = ctk.CTk()
root.geometry("1000x500")
root.title("PixelStream")

# Layout setup
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=1)
root.grid_rowconfigure((0, 1, 2), weight=1)

# LEFT SIDEBAR
# create sidebar frame with widgets
sidebar_frame = ctk.CTkFrame(root, width=200)
sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
sidebar_frame.grid_rowconfigure(4, weight=1)

# Sidebar logo
logo_label = ctk.CTkLabel(sidebar_frame, text="PixelStream", font=ctk.CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

divider0_label = ctk.CTkLabel(sidebar_frame, text="_________________________")
divider0_label.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

# Stream / Watch toggle
watch_label = ctk.CTkLabel(sidebar_frame, text="Watch")
watch_label.grid(row=2, column=0, padx=(15, 20), pady=(10, 80), sticky="w")
mode_switch = ctk.CTkSwitch(sidebar_frame, text=" Stream")
mode_switch.grid(row=2, column=0, padx=(65, 15), pady=(10, 80), sticky="e")

# Stream access link
divider2_label = ctk.CTkLabel(sidebar_frame, text="Join Stream\n_________________________")
divider2_label.grid(row=5, column=0, padx=(0, 0), pady=(0, 30), sticky="sew")

stream_link_entry = ctk.CTkEntry(sidebar_frame, width=140, height=20, corner_radius=3, placeholder_text="Stream link", border_color="gray10", border_width=1, bg_color="transparent")
stream_link_entry.grid(row=5, column=0, padx=(5, 5), pady=(5, 2), sticky="sew")

def access_stream_accept_button():
    pass

def clear_fields():
    #stream_link_entry.delete(0, "end")
    pass

join_button = ctk.CTkButton(sidebar_frame, width=70, height=20, fg_color="transparent", border_width=1, text="SEND", text_color=("gray10", "#DCE4EE"), corner_radius=0)
join_button.grid(row=6, column=0, padx=(0, 80), pady=(1, 7))

reset_button = ctk.CTkButton(sidebar_frame, width=70, height=20, fg_color="transparent", border_width=1, text="RESET", text_color=("gray10", "#DCE4EE"), corner_radius=0)
reset_button.grid(row=6, column=0, padx=(80, 0), pady=(1, 7))


# CENTER PART
# Stream video area
video_area = ctk.CTkFrame(root, width=600, height=350, border_width=BORDER_WIDTH_UNIV, corner_radius=5) # , border_color="#4E2173")
video_area.grid(row=0, column=1, columnspan=3, padx=(5, 5), pady=(5, 1), sticky="nsew")

# Stream title
title_label = ctk.CTkLabel(root, width=250, height=50, font=('Courier',30))
title_label.grid(row=2, column=1, columnspan=2, padx=(5, 0), pady=(0, 3), sticky="new")
title_label.configure(text="--Stream Title--")

# Stream Subtitle / Topics
stream_info_label = ctk.CTkLabel(root, width=250, height=20, font=('Courier',20))
stream_info_label.grid(row=3, column=1, columnspan=2, padx=(5, 0), pady=(0, 19), sticky="n")
stream_info_label.configure(text="--Stream Info--")

# Chat text box
send_chat_text = ctk.CTkEntry(root, width=500, height=25, corner_radius=5, placeholder_text="Enter message...", border_color="white", border_width=1)
send_chat_text.grid(row=6, column=1, padx=(10, 0), pady=(1, 5), sticky="e")

# Chat send button
send_chat_enter = ctk.CTkButton(root, width=75, height=25, fg_color="transparent", border_width=2, text="SEND", text_color=("gray10", "#DCE4EE"))
send_chat_enter.grid(row=6, column=3, padx=(0, 1), pady=(1, 10))

# RIGHT SIDEBAR
# Chat view
chat_frame = ctk.CTkFrame(root, width=200, border_width=BORDER_WIDTH_UNIV, corner_radius=5) # , border_color="#271C73")
chat_frame.grid(row=0, column=4, rowspan=6, padx=(0,5), pady=(5, 0), sticky="nsew")

# Set/Enter username button
def username_input_dialog_event():
    dialog = ctk.CTkInputDialog(text="Enter your Username", title="Username")
    print("CTkInputDialog:", dialog.get_input())

enter_username = ctk.CTkButton(root, text="-- Username --", command=username_input_dialog_event)
enter_username.grid(row=6, column=4, padx=(5, 5), pady=(2, 0), sticky="ew")

root.mainloop()