import fontforge

# 字体路径
font_a_path = "HarmonyOS_Sans_SC_Regular.ttf"     # 主字体（被修改）
font_b_path = "JetBrainsMono-Regular.ttf"         # 来源字体（提供拉丁字形等）
output_path = "HarmonyOS_JetBrains_Mono.ttf"      # 输出文件

# 打开字体
font_a = fontforge.open(font_a_path)
font_b = fontforge.open(font_b_path)

# 合并 glyphs
for glyph in font_b.glyphs():
    if glyph.unicode == -1:
        continue  # 跳过无 Unicode 编码的字形

    unicode_char = chr(glyph.unicode)
    glyph_name = glyph.glyphname

    if unicode_char in font_a:
        print(f"🔁 替换: U+{glyph.unicode:04X} '{unicode_char}'")
        font_a.removeGlyph(unicode_char)
    else:
        print(f"➕ 添加: U+{glyph.unicode:04X} '{unicode_char}'")

    # 创建新字形
    font_a.createChar(glyph.unicode, glyph_name)

    # 使用复制粘贴方式确保轮廓/组件完整
    font_b.selection.none()
    font_b.selection.select(glyph_name)
    font_b.copy()

    font_a.selection.none()
    font_a.selection.select(glyph_name)
    font_a.paste()

    # 保留源字体宽度
    font_a[glyph_name].width = font_b[glyph_name].width

# 设置字体名称
font_a.familyname = "HarmonyOS JetBrains Mono"
font_a.fullname = "HarmonyOS JetBrains Mono"
font_a.fontname = "HarmonyOSJetBrainsMono"  # 确保 PostScript 名没有空格

# 设置 SFNT 名称（用于 OpenType 等）
font_a.appendSFNTName('English (US)', 'Preferred Family', 'HarmonyOS JetBrains Mono')
font_a.appendSFNTName('Chinese (PRC)', 'Family', 'HarmonyOS JetBrains Mono')
font_a.appendSFNTName('Chinese (PRC)', 'Fullname', 'HarmonyOS JetBrains Mono')
font_a.appendSFNTName('English (US)', 'Preferred Styles', 'Regular')

# 导出字体并保存
font_a.generate(output_path)
print(f"\n✅ 字体合并完成，输出文件：{output_path}")
