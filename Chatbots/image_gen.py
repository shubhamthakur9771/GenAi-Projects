import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)

pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

prompt = "A futuristic AI hospital with robots, 4k"
image = pipe(prompt).images[0]

image.save("output.png")

print("✅ Image generated successfully")