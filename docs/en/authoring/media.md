---
title: Images & Videos
description: How to embed images and videos, including the bundled image_demo.png and video_demo.mp4.
---

# Images & Videos

## Images

The standard Markdown image syntax is used:

```markdown
![alt text](../assets/images/image_demo.png)
```

![The bundled demo image](../assets/images/image_demo.png)

The `alt` text describes the image for screen readers and is shown if the file cannot be loaded.

### Where to put files

Place images in `docs/assets/images/` (or subfolders). The `assets/` directory is shared between the English and Chinese builds, and MkDocs rewrites relative paths automatically — `../assets/images/…` works from a page in either language.

### Sizing

The `attr_list` extension attaches HTML attributes:

```markdown
![demo](../assets/images/image_demo.png){ width="300" }
```

![demo](../assets/images/image_demo.png){ width="300" }

### Captions

Wrap the image in a figure to add a caption:

```markdown
<figure markdown="span">
  ![The bundled demo image](../assets/images/image_demo.png){ width="480" }
  <figcaption>Figure 1 — The bundled demo image.</figcaption>
</figure>
```

<figure markdown="span">
  ![The bundled demo image](../assets/images/image_demo.png){ width="480" }
  <figcaption>Figure 1 — The bundled demo image.</figcaption>
</figure>

The `markdown="span"` attribute tells the `md_in_html` extension to process the inner content as Markdown.

### External images

Remote URLs work unchanged: `![alt](https://example.com/image.png)`. For images served from your own site, keep them in `docs/assets/` so they survive renames and remain available offline.

## Videos

The `mkdocs-video` plugin converts an image tag whose alt text is `type:video` into an embedded player:

```markdown
![type:video](../assets/videos/video_demo.mp4)
```

![type:video](../assets/videos/video_demo.mp4)

This renders the 30-second bundled demo clip, `docs/assets/videos/video_demo.mp4`. Videos are placed in `docs/assets/videos/`, following the same convention as images.

### Controlling the player

Attributes attached with `attr_list` are copied onto the player. The plugin applies a default style (full width, 16:9-ish height); override it with a `style` attribute:

```markdown
![type:video](../assets/videos/video_demo.mp4){ style="width:640px;height:360px" }
```

To opt out of the plugin's default style entirely (e.g. to set only `width`/`height` attributes), add `disable-global-config`:

```markdown
![type:video](../assets/videos/video_demo.mp4){ disable-global-config width="640" height="360" }
```

### Native player controls

By default the plugin embeds the file in an `<iframe>`. Set `is_video: true` in the plugin configuration to use a native `<video>` element instead, which enables the global options `video_autoplay`, `video_loop`, `video_muted`, and `video_controls`:

```yaml
plugins:
  - mkdocs-video:
      is_video: true
      video_autoplay: true
      video_loop: true
      video_muted: true
```

### External platforms

For YouTube, Bilibili, or similar platforms, paste the platform's embed `<iframe>` directly — the `md_in_html` extension passes it through:

```markdown
<iframe width="560" height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="Video player" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen></iframe>
```

## File size

GitHub Pages has no per-file limit beyond the repository's practical bounds, but large videos slow down cloning and page loads. A guideline:

- under ~10 MB per video: store it in `docs/assets/videos/`;
- above that: upload to an external host (YouTube, Bilibili, a cloud drive) and embed the link or iframe.
