import paddlehub as hub

module = hub.Module(name="ernie_vilg")
text_prompts = ["一群在舞蹈的精灵，数据背景，现实主义风格"]
images = module.generate_image(
    text_prompts=text_prompts, style='探索无限', output_dir='./ernie_vilg_out/')
