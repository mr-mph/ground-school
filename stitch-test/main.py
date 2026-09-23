import cv2
import numpy as np
from tqdm import tqdm

filename = "vid.mp4"
cap = cv2.VideoCapture(filename)

scale = 0.5
max_shift = 10

n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

frames = []
for _ in tqdm(range(n), desc="extract"):
    ok, frame = cap.read()
    if not ok:
        break

    small_frame = cv2.resize(
        frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA
    )
    frames.append(small_frame)

cap.release()

print("finished extracting frames")


strips = [frames[0]]

for previous, current in tqdm(
    zip(frames, frames[1:]), total=len(frames) - 1, desc="stitch"
):
    height = current.shape[0]
    previous_f = previous.astype(np.float32)
    current_f = current.astype(np.float32)

    if (
        np.mean(np.abs(current_f - previous_f)) < 1.0
    ):  # discard frame if too similar to last
        continue

    max_scroll = min(max_shift, height - 1)
    errors = [
        np.mean(np.abs(current_f[scroll:] - previous_f[: height - scroll]))
        for scroll in range(0, max_scroll + 1)  # include 0 for no scroll
    ]
    scroll = int(np.argmin(errors))
    if scroll > 0:
        strips.append(current[:scroll])


stitched_img = np.vstack(strips[::-1])
cv2.imwrite("stitched.png", stitched_img)
