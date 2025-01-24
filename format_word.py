from docx import Document
from docx.shared import Pt, Inches


def apply_styles_and_remove_markers(doc_path):
    # 打开Word文档
    doc = Document(doc_path)

    # 获取或创建样式（假设已存在）
    try:
        article_title_style = doc.styles['文章标题']
        bold_subtitle_style = doc.styles['黑体小标题']
    except KeyError:
        print("样式'文章标题'或'黑体小标题'不存在于文档中，请先确保它们已经定义。")
        return

    for para in doc.paragraphs:
        text = para.text.strip()

        if text.startswith('aaa') and text.endswith('aaa'):
            # 清除原有缩进
            para.paragraph_format.left_indent = Inches(0)
            para.paragraph_format.first_line_indent = Pt(0)
            # 应用文章标题样式
            para.style = article_title_style
            # 删除aaa标记
            para.text = text[3:-3]
        elif text.startswith('bbb') and text.endswith('bbb'):
            # 清除原有缩进
            para.paragraph_format.left_indent = Inches(0)
            para.paragraph_format.first_line_indent = Pt(0)
            # 应用黑体小标题样式
            para.style = bold_subtitle_style
            # 删除bbb标记
            para.text = text[3:-3]

    # 保存更改后的文档
    doc.save(doc_path)


# 调用函数
doc_path = r"D:\OneDrive\党建政治\文档模版.docx"
apply_styles_and_remove_markers(doc_path)
