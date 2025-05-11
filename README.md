# Merge fonts

## 更新逻辑

我们将脚本更新为 **合并 + 替换所有 B 中的字形到 A 中**：

| 条件        | 操作                 |
|-----------|--------------------|
| A 中已有对应字符 | 删除 A 中字形 → 用 B 中替换 |
| A 中没有该字符  | 直接从 B 中添加到 A       |

## 使用方式

1. 安装 FontForge（必须安装带有 Python 支持的版本）：

    * macOS：`brew install fontforge`
    * Linux：`sudo apt install fontforge`
    * Windows：安装 [FontForge with Python](https://fontforge.org/en-US/downloads/)

2. 将脚本保存为 `merge_fonts.py`

3. 在命令行运行：

```bash
fontforge -script merge_fonts.py
```
