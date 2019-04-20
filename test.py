from PIL import Image, ImageDraw, ImageFont


def merge(background, center, text, target):
    """

    :param background: 背景图
    :param center: 中心图案
    :param text_level: 文本内容
    :return:
    """
    # read file
    background = Image.open(background)
    center = Image.open(center)
    # get target size
    target_size = background.size
    # merge
    background.paste(center, (0, 0), center)

    target_file = background
    target_file.resize(target_size)
    # add text
    target_file, _ = insert_text(text, 'SIMYOU.TTF', 50, target_file, (220, 100))
    # output
    target_file.save(target, 'PNG')


def insert_text(text, fone_type_file, font_size, im, position):
    """
    :param text: 要插入的文字
    :param fone_type_file: 文字类型文件名称
    :param font_size: 文字大小
    :param im: 背景图片
    :param position: 要插入的位置
    :return:
    """

    datas = text.split('\n')
    data = ''
    if not datas:
        datas = [text]
    for d in datas:
        if not d:
            d = ' '
        elif len(d) > 31:
            d1 = d[:30] + '\n'
            d2 = d[30:]
            d = d1 + ' \n'+ d2
        data += (d +'\n')
        data += ' \n'

    data = data[:-1]
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(fone_type_file, font_size)

    dr.text(position, data, font=font, fill="#000000", spacing=0, align='left')
    return im, len(datas)


if __name__ == '__main__':
    merge('background.png', 'content.png', '文本内容', 'out.png')
