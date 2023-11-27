import math
import random
from PIL import Image


class Filter:
    """
    Базовый класс для создания фильтров.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # Этот метод нужно будет реализовать в новых классах.
        raise NotImplementedError

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        # цикл по всем пикселям
        # img.width - ширина картинки
        # img.height - высота картинки
        for i in range(img.width):
            for j in range(img.height):
                # получаем цвет
                r, g, b = img.getpixel((i, j))

                # как-либо меняем цвет
                new_colors = self.apply_to_pixel(r, g, b)

                # сохраняем пиксель обратно
                img.putpixel((i, j), new_colors)
        return img


class RedFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # плавно усиляет красный
        r = int(math.exp(r / 255) / math.e * 255)
        return r, g, b


class Purple(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        #Фиолетовый фильтр (Сергей)
        r = max(r, g, b)
        g = 0    
        return r, g, b


class GreenFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # плавно усиляет зелёный
        g = int(math.exp(g / 255) / math.e * 255)
        return r, g, b


class BlueFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # плавно усиляет синий
        b = int(math.exp(b / 255) / math.e * 255)
        return r, g, b


class InverseFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # инвертирует цвета
        result = []
        for color in (r, g, b):
            result.append(int((1 - math.exp(color / 255) / math.e) * 255))
        return tuple(result)


class RandomBrightFilter(Filter):
    """
    Фильтр, который зеркалит изображение.
    """
    def __init__(self, img) -> None:
        self.source_img = img.copy()

    def apply_to_pixel(self, r: int, g: int, b: int) -> int:
        new_pixel_r = min(r + random.randrange(100), 255)
        new_pixel_g = min(g + random.randrange(100), 255)
        new_pixel_b = min(b + random.randrange(100), 255)
        return new_pixel_r, new_pixel_g, new_pixel_b
