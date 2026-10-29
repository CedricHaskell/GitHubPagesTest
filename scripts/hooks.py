import shutil
from pathlib import Path

def on_post_build(config, **kwargs):
    site_dir = Path(config.site_dir)
    root_sitemap = site_dir / "sitemap.xml"
    if not root_sitemap.exists():
        return

    # copy sitemap into every language that is not default
    for lang in ["zh"]:
        lang_dir = site_dir / lang
        if lang_dir.is_dir():
            shutil.copy(root_sitemap, lang_dir / "sitemap.xml")