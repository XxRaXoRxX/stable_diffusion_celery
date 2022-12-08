# stable_diffusion_celery
Stable diffusion with Celery and Redis technology. Mixing both technologies using a client to make prompts and a worker to do the hard work generating images.
## Stable Diffusion:
**Stable Diffusion** is a [deep learning](https://en.wikipedia.org/wiki/Deep_learning "Deep learning"), [text-to-image model](https://en.wikipedia.org/wiki/Text-to-image_model "Text-to-image model") released in 2022. It is primarily used to generate detailed images conditioned on text descriptions, though it can also be applied to other tasks such as [inpainting](https://en.wikipedia.org/wiki/Inpainting "Inpainting"), outpainting, and generating image-to-image translations guided by a [text prompt](https://en.wikipedia.org/wiki/Prompt_engineering "Prompt engineering").
## Celery and Redis:
*Distributed task queue*. **Celery** is an [asynchronous task](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)) queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well.
*An in-memory database that persists on disk*. Redis is an open source, BSD licensed, advanced [key-value store](https://en.wikipedia.org/wiki/Key%E2%80%93value_database). It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets and sorted sets.

*Thanks to [stable-diffusion](https://github.com/CompVis/stable-diffusion), [stable-diffusion-optimized](https://github.com/basujindal/stable-diffusion), [Stability AI](https://stability.ai/), [Runway](https://runwayml.com/) and [d1cor](https://github.com/d1cor)* for helping to make this project a reality.
