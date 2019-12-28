""" Place for Streamfields """
from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.RichTextBlock(required=True, help_text='Add your text here')

    class Meta:
        icon = "edit"
        label = "Title & Text"


class IntroBlock(blocks.StructBlock):
    intro = blocks.CharBlock(required=True)