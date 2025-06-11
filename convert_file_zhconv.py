import zhconv  # 或使用 opencc


def convert_file(input_path, output_path):
    """
    转换文本文件从繁体到简体
    :param input_path: 输入文件路径
    :param output_path: 输出文件路径
    """
    try:
        # 读取繁体文本
        with open(input_path, 'r', encoding='utf-8') as f:
            traditional_text = f.read()

        # 转换简体（zhconv方案）
        simplified_text = zhconv.convert(traditional_text, 'zh-cn')

        # 写入简体文本
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(simplified_text)

        print(f"转换成功！结果已保存到 {output_path}")

    except Exception as e:
        print(f"转换失败: {str(e)}")


if __name__ == "__main__":
    input_file = "zheyao.txt"  # 替换为你的输入文件路径
    output_file = "output_simplified.txt"  # 输出文件路径
    convert_file(input_file, output_file)
