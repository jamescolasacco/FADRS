"""Render named views from the open FADRS-Studio.blend using Blender's Python."""
import argparse
from pathlib import Path
import sys

import bpy


SHOTS = {
    "hero": ("01   Hero | front three-quarter", "FADRS-Hero.png", 3840, 2560),
    "panel": ("02   Panel | elevated", "FADRS-Panel.png", 3200, 1980),
    "faders": ("03   Control detail | channel bank", "FADRS-Faders.png", 2880, 1800),
    "transport": ("04   Control detail | transport", "FADRS-Transport.png", 2700, 1800),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shot", choices=SHOTS, nargs="+", default=list(SHOTS))
    parser.add_argument("--output", type=Path, default=Path(bpy.data.filepath).parent)
    parser.add_argument("--preview", action="store_true")
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    args = parser.parse_args(argv)
    args.output.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    for key in args.shot:
        camera, filename, width, height = SHOTS[key]
        scene.camera = bpy.data.objects[camera]
        scene.render.resolution_x = width
        scene.render.resolution_y = height
        scene.render.resolution_percentage = 30 if args.preview else 100
        scene.cycles.samples = 12 if args.preview else 64
        scene.cycles.adaptive_threshold = 0.10 if args.preview else 0.035
        scene.render.filepath = str(args.output.resolve() / filename)
        result = bpy.ops.render.render(write_still=True)
        if "FINISHED" not in result or not Path(scene.render.filepath).is_file():
            raise RuntimeError(f"Render did not finish for {filename}")
        print(f"Saved {filename}", flush=True)


if __name__ == "__main__":
    main()
