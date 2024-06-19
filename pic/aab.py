from PIL import Image
import os

# 当前目录和输出目录
current_directory = os.getcwd()
output_directory = os.path.join(current_directory, 'thumbnails')

# 如果输出目录不存在，创建它
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# 最大缩略图尺寸
max_size = (300, 300)  # 可根据需要调整最大尺寸

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # 打开图像文件
        with Image.open(filename) as img:
            # 计算缩略图尺寸，保持比例
            img.thumbnail(max_size)
            # 构造输出文件路径
            output_path = os.path.join(output_directory, f'thumbnail_{filename}')
            # 保存缩略图
            img.save(output_path)

print('Thumbnail generation complete.')
