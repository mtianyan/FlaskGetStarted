# encoding: utf-8
import os
import uuid
__author__ = 'mtianyan'
__date__ = '2018/2/17 0017 02:10'
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class Captcha:
    """
    验证码功能类
    """
    # 随机一个字母或者数字

    def random_char(self):
        num = random.randint(1, 3)
        if num == 1:
            # 随机一个0-9之间数字: ascii码
            char = random.randint(48, 57)
        elif num == 2:
            # 随机一个a-z之间字母
            char = random.randint(97, 122)
        else:
            # 随机一个A-Z之间字母
            char = random.randint(65, 90)
        # chr将数字转换为对应ASCII码数字字母
        return chr(char)

    # 随机一个干扰字符
    def random_diss(self):
        arr = ["^", "_", "-", ".", "~"]
        return arr[random.randint(0, len(arr) - 1)]

    # 定义干扰字符颜色,干扰字符与字符颜色在不同区间
    def random_char_color(self):
        return (
            random.randint(
                65, 255), random.randint(
                65, 255), random.randint(
                65, 255))

    # 定义字符颜色, 三原色 RGB
    def random_diss_color(self):
        return (
            random.randint(
                32, 127), random.randint(
                32, 127), random.randint(
                32, 127))

    # 生成验证码:
    def create_captcha(self):
        width = 240  # 240px
        height = 60  # 60px

        # 创建一个图片
        image = Image.new("RGB", (width, height), (255, 255, 255))

        # 创建font对象，定义字体和大小
        font_name = random.randint(1, 3)
        font_file = os.path.join(
            os.path.dirname(__file__),
            "static/fonts") + "/%d.ttf" % font_name
        font = ImageFont.truetype(font_file, 40)

        # 创建draw画布使图片可编辑，填充像素点
        draw = ImageDraw.Draw(image)
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                draw.point((x, y), fill=self.random_diss_color())

        # 填充干扰字符
        for v in range(0, width, 30):
            dis = self.random_diss()
            w = 5 + v
            # 距离图片上边距最多15个像素， 最低五个像素
            h = random.randint(5, 15)
            draw.text((w, h), dis, font=font, fill=self.random_diss_color())
        # 填充字符
        chars = ""
        for v in range(4):
            c = self.random_char()
            chars += str(c)
            # 距离图片上边距最多15个像素， 最低五个像素
            h = random.randint(5, 15)
            # 占图片宽度1/4， 10px间距, 顺序平移
            w = width / 4 * v + 10
            draw.text((w, h), c, font=font, fill=self.random_char_color())
        # 模糊效果:
        image.filter(ImageFilter.BLUR)
        image_name = "%s.jpg" % uuid.uuid4().hex
        save_dir = os.path.join(
            os.path.dirname(__file__),
            "static/captcha")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        image.save(save_dir + '/' + image_name, "jpeg")
        return dict(
            image_name=image_name,
            captcha=chars
        )
        image.show()


if __name__ == "__main__":
    c = Captcha()
    print(c.random_char())
    print(c.random_diss())
    print(c.random_char_color())
    print(c.random_diss_color())
    c.create_captcha()
