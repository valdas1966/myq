from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# create new presentation
prs = Presentation()

# blank slide layout
layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(layout)

# textbox parameters
left = Inches(1)
top = Inches(0)
width = Inches(3)
height = Inches(4)

# add textbox
txBox = slide.shapes.add_textbox(left, top, width, height)
txBox.fill.solid()
txBox.fill.fore_color.rgb = RGBColor(255, 0, 0)

tf = txBox.text_frame
tf.text = "A"

p = tf.add_paragraph()
p.text = "This is a second paragraph that's bold"
p.font.bold = True

p = tf.add_paragraph()
p.text = "This is a third paragraph that's big"
p.font.size = Pt(40)

prs.save('test.pptx')
