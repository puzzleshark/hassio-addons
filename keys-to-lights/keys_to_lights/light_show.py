import time
import asyncio

from keys_to_lights import color_association
from keys_to_lights import change_color




async def turn_on_lights_at(note, when, until):
    rgb = color_association.note_to_rgb2(note)
    if until > time.time():
        if when > time.time():
            print(f"sleeping for {when - time.time()} seconds. Then changing to {note}")
            await asyncio.sleep(when - time.time())
        print(f"changing to {note}")
        change_color.change_color(rgb[0], rgb[1], rgb[2])



async def light_show(info, song):
    light_segments = []
    print(f"####### light show for '{song['item']['name']}' ########")
    for i, section in enumerate(info["sections"]):

        mode = section["mode"]
        if mode == 0:
            corrected_key = (section["key"] + 3) % 12
            main_key = (corrected_key * 7) % 12
        else:
            main_key = (section["key"] * 7) % 12

        note = color_association.Note(main_key)
        print(f"section {i + 1} is in key of {note}")
        light_segments.append(
            asyncio.create_task(
                turn_on_lights_at(
                    note,
                    (song["timestamp"]-song["progress_ms"])/1000.0 + section["start"],
                    (song["timestamp"]-song["progress_ms"])/1000.0 + section["start"] + section["duration"]
                )
            )
        )
    await asyncio.gather(*light_segments)