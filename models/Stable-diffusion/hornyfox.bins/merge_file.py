import argparse
import os
import sys

def handle_commandline():
    """
 .  负责解析命令行模式的传参
    """
    parser = argparse.ArgumentParser(description="Processing large files that have been segmented using form files.\nAuthor: chengfeng30121@github.com")
    parser.add_argument("-l", "--list", type=str, required=True, help=" specify the list file path.")
    parser.add_argument("-o", "--output", type=str, required=True, help=" specify the output file name")
    args = parser.parse_args()
    judgment_args = (args.list, args.output)
    for arg in judgment_args:
        if arg is None:
            print(f"merge_file: too few argument. Please type '{os.path.basename(__file__)} -h' to read the usage.")
            exit(1)
    merge_slices(args.list, args.output)

def merge_slices(output_txt_path, output_file_name):
    """
    根据 <output_txt_path> 中的文件列表合并所有切片到一个文件中。
    
    :param output_txt_path: 包含切片文件名的文本文件路径
    :param output_file_name: 合并后文件的名称
    """
    with open(output_txt_path, 'r') as file_list:
        slice_files = file_list.readlines()
        
    with open(output_file_name, 'wb') as merged_file:
        for slice_file in slice_files:
            slice_file = slice_file.strip()
            if slice_file == "":
                continue
            with open(slice_file, 'rb') as current_slice:
                merged_file.write(current_slice.read())
                print(f"正在整合 {slice_file}")
    print(f'切片文件已成功合并至 {output_file_name}')

def main():
    if len(sys.argv) > 1:
        handle_commandline()
    else:
        output_txt_path = input("请输入清单文件路径> ")
        output_file_name = input("请输入合并后文件名> ")
        merge_slices(output_txt_path, output_file_name)

if __name__ == "__main__":
    main()
