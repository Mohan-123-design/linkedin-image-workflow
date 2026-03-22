from sheets import read_rows, update_cell
from prompt_generator import generate_prompt
from image_generator import generate_image

rows = read_rows()

# Skip header row
for idx, row in enumerate(rows[1:], start=2):

    # Ensure row always has 5 columns
    row = row + [""] * (5 - len(row))

    sno, content, prompt, prompt_status, image_status = row[:5]

    # Skip empty rows
    if not sno or not content:
        continue

    # 1️⃣ Prompt generation
    if not prompt_status:
        prompt = generate_prompt(content)
        update_cell(
            f"Sheet1!C{idx}:D{idx}",
            [[prompt, "SUCCESS"]]
        )

    # 2️⃣ Image generation
    if not image_status:
        image_path = generate_image(prompt, f"linkedin_{sno}")
        update_cell(
            f"Sheet1!E{idx}:F{idx}",
            [["SUCCESS", image_path]]
        )
