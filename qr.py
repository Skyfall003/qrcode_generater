import qrcode
from tkinter import Tk, Label, Entry, Button
from tkinter import filedialog

def generate_qr_code():
    data = data_entry.get()
    file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    
    if data and file_name:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_name)
        status_label.config(text="QR code generated!")
    else:
        status_label.config(text="Please enter data and select a file name.")

# Create GUI window
window = Tk()
window.title("QR Code Generator")

# Data Label and Entry
data_label = Label(window, text="Data:")
data_label.pack()
data_entry = Entry(window, width=50)
data_entry.pack()

# Generate button
generate_button = Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Status Label
status_label = Label(window, text="")
status_label.pack()

# Run the GUI window
window.mainloop()
