"""Revision note: replaced the flat draft with specific alien grievances
(gravity, rain, filmed tentacles) and a joke turn where the one-star
reviewer would invade again just for the buttered corn, so the food
compliment lands as a real reversal instead of a generic aside.
"""
import os

TEXT = "One star: your planet trapped me in gravity, rain, and a crowd filming my tentacles, but I would invade again tomorrow just to eat your buttered corn."

assert 1 <= len(TEXT) <= 200
assert "\n" not in TEXT and "\r" not in TEXT
assert TEXT == TEXT.strip()

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
