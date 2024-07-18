import os

def split_file(input_file_path: str, chunk_size_mb=80, output_dir='slices') -> None:
    """
    将大文件按照指定大小切分为多个小文件。
    
    :param input_file_path: 要分割的原始文件路径
    :param chunk_size_mb: 每个切片的大小，单位为MB
    :param output_dir: 输出切片文件的目录
    """
    chunk_size = chunk_size_mb * 1024 * 1024
    with open(input_file_path, 'rb') as file:
        chunk_num = 0
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            # rname = (6 - len(str(chunk_num))*"0"+str(chunk_num)
            chunk_filename = f'{output_dir}/slice_{chunk_num}.bin'
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(data)
                print(f"{chunk_filename} 已切片完成")
            chunk_num += 1
    print(f'文件已分割成{chunk_num}个部分，每个大小约为{chunk_size_mb}MB。')

input_file_path = input("请输入大文件路径> ")
chunk_size_mb = int(input("请输入每个文件的最大大小> "))
output_dir = input("请输入输出文件夹> ")
os.makedirs(output_dir, exist_ok=True)
split_file(input_file_path, chunk_size_mb, output_dir)
