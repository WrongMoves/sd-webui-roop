import tempfile
from ifnude import detect

def convert_to_sd(img):
    shapes = []
    min_prob = 2
    chunks = detect(img, min_prob)
    for chunk in chunks:
        shapes.append(chunk["score"] > 2)
    return [any(shapes), tempfile.NamedTemporaryFile(delete=False, suffix=".png")]
