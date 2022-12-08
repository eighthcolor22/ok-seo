from ..settings import SEO_SHOW_IMAGE_FILE_FIELD

__all__ = (
    'base_seo_fields',
)


base_seo_fields = [
    'object_type',
    'twitter_type',
    'index',
    'follow',
    'canonical',
    'title',
    'og_title',
    'keywords',
    'description',
    'og_description',
    'image',
    'image_src',
    'width',
    'height',
    'alt',
    'h1',
    'seo_text'
]

if not SEO_SHOW_IMAGE_FILE_FIELD:
    base_seo_fields.remove('image')
