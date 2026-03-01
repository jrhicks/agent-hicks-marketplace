#!/usr/bin/env python3
"""
Nano Banana Image Generator
Uses Google's Gemini and Imagen models for dev-time asset generation.

Model Architecture Guide:
- Gemini models (Nano Banana) → use generate_content() [multimodal LLM]
- Imagen models → use generate_images() [diffusion model]
"""
import os
import sys
import argparse
from pathlib import Path
from PIL import Image

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("ERROR: google-genai package not installed.")
    print("Install with: pip install google-genai")
    sys.exit(1)

# Model configurations
MODELS = {
    "nano-banana": {
        "id": "gemini-2.5-flash-image",
        "type": "gemini",
        "description": "Nano Banana (fast, versatile, good for iteration)"
    },
    "nano-banana-pro": {
        "id": "gemini-3-pro-image-preview",
        "type": "gemini",
        "description": "Nano Banana Pro (higher quality, more creative controls)"
    },
    "imagen-fast": {
        "id": "imagen-4.0-fast-generate-001",
        "type": "imagen",
        "description": "Imagen 4 Fast (good photorealism, faster generation)"
    },
    "imagen": {
        "id": "imagen-4.0-generate-001",
        "type": "imagen",
        "description": "Imagen 4 (better photorealism, balanced)"
    }
}

DEFAULT_MODEL = "nano-banana"

def get_client():
    """Get authenticated Google GenAI client."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: GOOGLE_API_KEY environment variable not set.")
        print("Get your key at: https://aistudio.google.com/apikey")
        sys.exit(1)
    return genai.Client(api_key=api_key)

def generate_image_gemini(client, model_id: str, prompt: str, output_path: str,
                          num_images: int = 1, aspect_ratio: str = None) -> list[str]:
    """Generate image using Gemini multimodal approach (Nano Banana)."""
    if num_images > 1:
        print("WARNING: Gemini models generate one image at a time via generate_content()")
        print(f"Generating {num_images} images sequentially...")

    saved_paths = []
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    base = Path(output_path)

    # Build config with optional native aspect ratio
    image_config = None
    if aspect_ratio:
        image_config = types.ImageConfig(aspect_ratio=aspect_ratio)

    for i in range(num_images):
        response = client.models.generate_content(
            model=model_id,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=image_config,
            )
        )

        # Extract image from response
        image_saved = False
        for part in response.candidates[0].content.parts:
            if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                if num_images == 1:
                    path = output_path
                else:
                    path = str(base.parent / f"{base.stem}_{i+1}{base.suffix}")

                with open(path, "wb") as f:
                    f.write(part.inline_data.data)
                saved_paths.append(path)
                print(f"Saved: {path}")
                image_saved = True
                break

        if not image_saved:
            print(f"ERROR: No image in response for generation {i+1}")
            sys.exit(1)

    return saved_paths

def generate_image_imagen(client, model_id: str, prompt: str, output_path: str,
                          aspect_ratio: str = "1:1", num_images: int = 1) -> list[str]:
    """Generate image using Imagen diffusion approach."""
    response = client.models.generate_images(
        model=model_id,
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=num_images,
            aspect_ratio=aspect_ratio,
            output_mime_type="image/png"
        )
    )

    saved_paths = []
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    if num_images == 1:
        if response.generated_images and len(response.generated_images) > 0:
            response.generated_images[0].image.save(output_path)
            saved_paths.append(output_path)
            print(f"Saved: {output_path}")
        else:
            print("ERROR: No image generated")
            sys.exit(1)
    else:
        base = Path(output_path)
        for i, img in enumerate(response.generated_images or []):
            path = base.parent / f"{base.stem}_{i+1}{base.suffix}"
            img.image.save(str(path))
            saved_paths.append(str(path))
            print(f"Saved: {path}")

    return saved_paths

def generate_image(prompt: str, output_path: str, model_key: str = DEFAULT_MODEL,
                   aspect_ratio: str = "1:1", num_images: int = 1) -> list[str]:
    """Generate image(s) from text prompt using auto-routed method."""
    if model_key not in MODELS:
        print(f"ERROR: Unknown model '{model_key}'")
        print(f"Available models: {', '.join(MODELS.keys())}")
        sys.exit(1)

    model_config = MODELS[model_key]
    model_id = model_config["id"]
    model_type = model_config["type"]

    client = get_client()

    print(f"Using {model_config['description']}")

    if model_type == "gemini":
        return generate_image_gemini(client, model_id, prompt, output_path, num_images, aspect_ratio)
    elif model_type == "imagen":
        return generate_image_imagen(client, model_id, prompt, output_path, aspect_ratio, num_images)
    else:
        print(f"ERROR: Unknown model type '{model_type}'")
        sys.exit(1)

ASPECT_RATIOS = {
    "1:1": (1, 1),
    "16:9": (16, 9),
    "9:16": (9, 16),
    "4:3": (4, 3),
    "3:4": (3, 4),
}

def crop_to_aspect(image_path: str, aspect: str) -> None:
    """Center-crop an image to the target aspect ratio. Removes content."""
    if aspect not in ASPECT_RATIOS:
        print(f"WARNING: Unknown aspect ratio '{aspect}', skipping crop")
        return

    target_w, target_h = ASPECT_RATIOS[aspect]
    target_ratio = target_w / target_h

    img = Image.open(image_path)
    w, h = img.size
    current_ratio = w / h

    if abs(current_ratio - target_ratio) < 0.01:
        return

    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))

    img.save(image_path)
    print(f"Cropped to {aspect}: {img.size[0]}x{img.size[1]}")

def pad_to_aspect(image_path: str, aspect: str) -> None:
    """Pad an image to the target aspect ratio using edge colors. Preserves all content."""
    if aspect not in ASPECT_RATIOS:
        print(f"WARNING: Unknown aspect ratio '{aspect}', skipping pad")
        return

    target_w, target_h = ASPECT_RATIOS[aspect]
    target_ratio = target_w / target_h

    img = Image.open(image_path)
    w, h = img.size
    current_ratio = w / h

    if abs(current_ratio - target_ratio) < 0.01:
        return

    import numpy as np

    if current_ratio < target_ratio:
        new_w = int(h * target_ratio)
        pad_left = (new_w - w) // 2
        pad_right = new_w - w - pad_left

        strip_w = min(10, w // 4)
        arr = np.array(img)
        left_color = arr[:, :strip_w, :].mean(axis=(0, 1)).astype(np.uint8)
        right_color = arr[:, -strip_w:, :].mean(axis=(0, 1)).astype(np.uint8)

        left_pad = np.broadcast_to(left_color, (h, pad_left, arr.shape[2])).copy()
        right_pad = np.broadcast_to(right_color, (h, pad_right, arr.shape[2])).copy()
        result = np.concatenate([left_pad, arr, right_pad], axis=1)
        img = Image.fromarray(result)
    else:
        new_h = int(w / target_ratio)
        pad_top = (new_h - h) // 2
        pad_bottom = new_h - h - pad_top

        strip_h = min(10, h // 4)
        arr = np.array(img)
        top_color = arr[:strip_h, :, :].mean(axis=(0, 1)).astype(np.uint8)
        bottom_color = arr[-strip_h:, :, :].mean(axis=(0, 1)).astype(np.uint8)

        top_pad = np.broadcast_to(top_color, (pad_top, w, arr.shape[2])).copy()
        bottom_pad = np.broadcast_to(bottom_color, (pad_bottom, w, arr.shape[2])).copy()
        result = np.concatenate([top_pad, arr, bottom_pad], axis=0)
        img = Image.fromarray(result)

    img.save(image_path)
    print(f"Padded to {aspect}: {img.size[0]}x{img.size[1]}")

def fit_to_aspect(image_path: str, aspect: str, method: str = "pad") -> None:
    """Fit image to target aspect ratio. Method: 'pad' (default, preserves content) or 'crop'."""
    if method == "crop":
        crop_to_aspect(image_path, aspect)
    else:
        pad_to_aspect(image_path, aspect)

def transform_image(input_path: str, prompt: str, output_path: str,
                    model_key: str = DEFAULT_MODEL, aspect_ratio: str = None) -> str:
    """Transform an existing image based on prompt (Gemini only)."""
    if model_key not in MODELS:
        print(f"ERROR: Unknown model '{model_key}'")
        sys.exit(1)

    model_config = MODELS[model_key]

    if model_config["type"] != "gemini":
        print(f"ERROR: Image transformation only supported by Gemini models")
        print(f"Try: nano-banana or nano-banana-pro")
        sys.exit(1)

    client = get_client()

    with open(input_path, "rb") as f:
        image_data = f.read()

    ext = Path(input_path).suffix.lower()
    mime_types = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                  ".webp": "image/webp", ".gif": "image/gif"}
    mime_type = mime_types.get(ext, "image/png")

    print(f"Using {model_config['description']}")

    image_config = None
    if aspect_ratio:
        image_config = types.ImageConfig(aspect_ratio=aspect_ratio)

    response = client.models.generate_content(
        model=model_config["id"],
        contents=[
            types.Part.from_bytes(data=image_data, mime_type=mime_type),
            prompt
        ],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
            image_config=image_config,
        )
    )

    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            with open(output_path, "wb") as f:
                f.write(part.inline_data.data)
            print(f"Saved: {output_path}")

            if aspect_ratio:
                from PIL import Image as PILImage
                check = PILImage.open(output_path)
                cw, ch = check.size
                target_ratio = ASPECT_RATIOS[aspect_ratio][0] / ASPECT_RATIOS[aspect_ratio][1]
                actual_ratio = cw / ch
                if abs(actual_ratio - target_ratio) > 0.05:
                    print(f"WARNING: Model output {cw}x{ch} (ratio {actual_ratio:.2f}), expected {aspect_ratio} ({target_ratio:.2f})")
                    print(f"Falling back to post-process crop...")
                    fit_to_aspect(output_path, aspect_ratio, "crop")
                else:
                    print(f"Native aspect ratio: {cw}x{ch} ({aspect_ratio})")

            return output_path

    print("ERROR: No image in response")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Nano Banana Image Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available models:
  nano-banana       Gemini 2.5 Flash Image (default, fast & versatile)
  nano-banana-pro   Gemini 3 Pro Image (higher quality)
  imagen-fast       Imagen 4 Fast (good photorealism, faster)
  imagen            Imagen 4 (better photorealism)

Examples:
  # Generate with default Nano Banana
  python generate_image.py generate "cute crab icon" output.png

  # Generate with Imagen for photorealism
  python generate_image.py generate "realistic sunset" output.png --model imagen-fast

  # Transform an image
  python generate_image.py transform input.png "make it pixel art" output.png
        """
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    gen_parser = subparsers.add_parser("generate", help="Generate image from text prompt")
    gen_parser.add_argument("prompt", help="Text prompt for image generation")
    gen_parser.add_argument("output", help="Output file path")
    gen_parser.add_argument("--model", default=DEFAULT_MODEL,
                           choices=list(MODELS.keys()),
                           help=f"Model to use (default: {DEFAULT_MODEL})")
    gen_parser.add_argument("--aspect", default="1:1",
                           choices=["1:1", "16:9", "9:16", "4:3", "3:4"],
                           help="Aspect ratio (default: 1:1)")
    gen_parser.add_argument("--count", type=int, default=1,
                           help="Number of images to generate (default: 1)")

    trans_parser = subparsers.add_parser("transform", help="Transform existing image")
    trans_parser.add_argument("input", help="Input image path")
    trans_parser.add_argument("prompt", help="Transformation prompt")
    trans_parser.add_argument("output", help="Output file path")
    trans_parser.add_argument("--model", default=DEFAULT_MODEL,
                             choices=list(MODELS.keys()),
                             help=f"Gemini model to use (default: {DEFAULT_MODEL})")
    trans_parser.add_argument("--aspect", default=None,
                             choices=["1:1", "16:9", "9:16", "4:3", "3:4"],
                             help="Output aspect ratio")

    args = parser.parse_args()

    if args.command == "generate":
        generate_image(args.prompt, args.output, args.model, args.aspect, args.count)
    elif args.command == "transform":
        transform_image(args.input, args.prompt, args.output, args.model, args.aspect)

if __name__ == "__main__":
    main()
