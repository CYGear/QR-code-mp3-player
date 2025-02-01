import qrcode
import os

try:
    # Path to your MP3 file (local file on your PC)
    mp3_url = "http://localhost:8000/HappyBirthday.mp3"  # Replace with your MP3 file's name if needed

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(mp3_url)
    qr.make(fit=True)

    # Get the path to the Documents folder
    save_path = os.path.join(os.path.expanduser("~"), "Documents", "music_qr_code.png")

    # Create an image from the QR code and save it in the Documents folder
    img = qr.make_image(fill="black", back_color="white")
    img.save(save_path)
    print(f"QR code saved as '{save_path}'")

except Exception as e:
    print(f"An error occurred: {e}")

# Keep the script running to prevent closing automatically
input("Press Enter to exit.")
