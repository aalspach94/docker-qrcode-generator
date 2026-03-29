import os
import re
import segno

if not os.path.exists("qrcodes"):
    os.mkdir("qrcodes")


# TODO: Add style options for QR code generation
# STYLES = {
#     "Classic":   dict(dark="#000000", light="#ffffff", finder_dark="#000000"),
#     "Ocean":     dict(dark="#0077b6", light="#caf0f8", finder_dark="#03045e"),
#     "Forest":    dict(dark="#386641", light="#f0f4f0", finder_dark="#1a2e1c"),
#     "Sunset":    dict(dark="#c1121f", light="#fff8f0", finder_dark="#6a0404"),
#     "Midnight":  dict(dark="#e0e0ff", light="#0d0d2b", finder_dark="#a0a0ff"),
# }


def safe_filename(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_-]', '', text)

def generate_qr_code(url: str) -> str:
    qr = segno.make_qr(url, error='h')

    base = safe_filename(url)
    i = 1
    filename = f"qrcodes/qrcode-{base}-{i}.png"
    while os.path.exists(filename):
        i += 1
        filename = f"qrcodes/qrcode-{base}-{i}.png"

    qr.save(filename, scale=10)
    return filename