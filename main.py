from tkinter import *
from webcam import capture_face
from faces import recognise_face
# Initializing the GUI window
root = Tk()
root.title("My Face Recognition App")
root.geometry('700x550')
root.resizable(0, 0)

# Creating the color and font variables
lf_bg = 'Gray70'  # Lightest Shade
cf_bg = 'Gray57'
rf_bg = 'Gray35'  # Darkest Shade
frame_font = ("Garamond", 14)

# Creating the StringVar variables
name_strvar = StringVar()
phone_strvar = StringVar()
email_strvar = StringVar()
search_strvar = StringVar()



center_frame = Frame(root, bg=cf_bg)
center_frame.place(relx=0.3, relheight=1, y=30, relwidth=0.3)


Button(center_frame, text='CAPTURE FACE', font=frame_font, width=15, command=capture_face).place(relx=0.13, rely=0.1)
# Button(center_frame, text='CANCEL CAPTURE FACE', font=frame_font, width=15, command=submit_record).place(relx=0.13, rely=0.2)
Button(center_frame, text='START FACE MOTION DECTECTING', font=frame_font, width=15, command=recognise_face).place(relx=0.13, rely=0.3)

root.update()
root.mainloop()
