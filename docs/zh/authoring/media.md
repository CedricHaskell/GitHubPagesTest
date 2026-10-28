---
title: 图片与视频
description: 如何嵌入图片与视频，包括模板自带的 image_demo.png 与 video_demo.mp4。
---

# 图片与视频

## 图片

使用标准 Markdown 图片语法：

```markdown
![替代文本](../assets/images/image_demo.png)
```

![模板自带的示例图片](../assets/images/image_demo.png)

`alt` 文本供屏幕阅读器使用，文件加载失败时也会显示。

### 文件放在哪里

图片放在 `docs/assets/images/`（或其子目录）中。`assets/` 目录由中英文构建共享，MkDocs 会自动重写相对路径——`../assets/images/…` 在两种语言的页面中都有效。

### 调整尺寸

`attr_list` 扩展可以附加 HTML 属性：

```markdown
![示例](../assets/images/image_demo.png){ width="300" }
```

![示例](../assets/images/image_demo.png){ width="300" }

### 图注

用 figure 包裹图片以添加图注：

```markdown
<figure markdown="span">
  ![模板自带的示例图片](../assets/images/image_demo.png){ width="480" }
  <figcaption>图 1——模板自带的示例图片。</figcaption>
</figure>
```

<figure markdown="span">
  ![模板自带的示例图片](../assets/images/image_demo.png){ width="480" }
  <figcaption>图 1——模板自带的示例图片。</figcaption>
</figure>

`markdown="span"` 属性告诉 `md_in_html` 扩展把内部内容作为 Markdown 处理。

### 外部图片

远程 URL 直接可用：`![替代文本](https://example.com/image.png)`。站点自身使用的图片建议放入 `docs/assets/`，以便在文件重命名后依然可用，且离线时仍能访问。

## 视频

`mkdocs-video` 插件把 alt 文本为 `type:video` 的图片标签转换为内嵌播放器：

```markdown
![type:video](../assets/videos/video_demo.mp4)
```

![type:video](../assets/videos/video_demo.mp4)

以上渲染的是模板自带的 30 秒示例视频 `docs/assets/videos/video_demo.mp4`。视频放入 `docs/assets/videos/`，与图片遵循相同的约定。

### 控制播放器

通过 `attr_list` 附加的属性会复制到播放器上。插件默认应用一套样式（全宽、约 16:9 的高度）；用 `style` 属性覆盖：

```markdown
![type:video](../assets/videos/video_demo.mp4){ style="width:640px;height:360px" }
```

要完全放弃插件的默认样式（例如只设置 `width`/`height` 属性），加上 `disable-global-config`：

```markdown
![type:video](../assets/videos/video_demo.mp4){ disable-global-config width="640" height="360" }
```

### 原生播放器控件

插件默认用 `<iframe>` 嵌入文件。在插件配置中设置 `is_video: true` 可改用原生 `<video>` 元素，此时全局选项 `video_autoplay`、`video_loop`、`video_muted`、`video_controls` 生效：

```yaml
plugins:
  - mkdocs-video:
      is_video: true
      video_autoplay: true
      video_loop: true
      video_muted: true
```

### 外部平台

对于 YouTube、Bilibili 等平台，直接粘贴平台提供的 `<iframe>` 嵌入代码——`md_in_html` 扩展会原样传递：

```markdown
<iframe width="560" height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="Video player" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen></iframe>
```

## 文件大小

GitHub Pages 对单个文件没有硬性限制，但大视频会拖慢克隆与页面加载。建议：

- 单个视频约 10 MB 以内：存放在 `docs/assets/videos/`；
- 超过该大小：上传到外部平台（YouTube、Bilibili、云盘），嵌入链接或 iframe。
