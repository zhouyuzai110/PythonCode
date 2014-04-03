# Sublime Text README



## 插件
### 通用插件
- **[Package Control](https://sublime.wbond.net/)：**

	>import urllib2,os; pf='Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler( ))); open( os.path.join( ipp, pf), 'wb' ).write( urllib2.urlopen( 'http://sublime.wbond.net/' +pf.replace( ' ','%20' )).read()); print( 'Please restart Sublime Text to finish installation')


- **[Sublime Linter](https://github.com/kronuz/SublimeLinter/)：**一个支持lint语法的插件，可以高亮linter认为有错误的代码行，也支持高亮一些特别的注释，比如“TODO”，这样就可以被快速定位。（IntelliJ IDEA的TODO功能很赞，这个插件虽然比不上，但是也够用了吧）

- **[Sublime Alignment](https://github.com/wbond/sublime_alignment)：**用于代码格式的自动对齐。传说最新版Sublime 已经集成。

- **[Clipboard History](https://github.com/kemayo/sublime-text-2-clipboard-history)：**粘贴板历史记录，方便使用复制/剪切的内容。

- **[Sublime CodeIntel](https://github.com/Kronuz/SublimeCodeIntel)：**代码自动提示,尚待考察

- **[Bracket Highlighter](https://github.com/facelessuser/BracketHighlighter)：**类似于代码匹配，可以匹配括号，引号等符号内的范围。

- **[SideBarEnhancements]()：**侧边栏增强。
- **[GBK Encoding Support]()：**支持GBK编码。
- **[Sublime CodeIntel](https://github.com/Kronuz/SublimeCodeIntel)：**代码自动提示,尚待考察

### MARKDOWN插件
- **[Markdown Preview]()：**推荐，我最常用的Markdown插件，写完之后可以在浏览器中浏览。还可以导出成HTMl代码，直接发布到WordPress中。
- **[Markdown Editing]()：**待选，如果在某个标题上按Tab键，它可以帮你折叠这个标题下的内容。而在文档的任何一个位置按下'Shift + Tab'，会折叠起来整个文档。这对分章节的长文档很有用。按下`Control+C`然后按`Control + N`能跳转到下一个标题，按下`Control + C`然后按`Control + P`能跳转到下一个标题。
- **[Smart Markdown]()：**待选 

### latex插件
- **[LateTools]()：**
>找到 ...\Sublime Text 2\Data\Packages\LaTeXTools\LaTeX.sublime-build 文件，用文本编辑器打开；
将
"cmd": ["texify","-b","-p","--tex-option=\"--synctex=1\""]
修改为
"cmd": ["texify","-b","-p","--engine=xetex","--tex-option=\"--synctex=1\""]
保存重新启动 Sublime Text 编译就转换为 XeTeX 引擎。

### R插件
- **[]()：**
- **[]()：**
- **[]()：**
- **[]()：**
- **[]()：**
- **[]()：**





### Python插件
- **[All Autocomplete]()：**
- **[]()：**
- **[]()：**
- **[]()：**
- **[]()：**
- **[]()：**




### 主题
- **[FlatLand]():














## 多行选择和多行编辑

-  鼠标选中多行，按下 `Ctrl+Shift+L (Command+Shift+L)` 即可同时编辑这些行；
-  鼠标选中文本，反复按 `CTRL+D (Command+D)` 即可继续向下同时选中下一个相同的文本进行同时编辑；
-  鼠标选中文本，按下 `Alt+F3 (Win)` 或 `Ctrl+Command+G(Mac)` 即可一次性选择全部的相同文本进行同时编辑；
-  Shift+鼠标右键 (Win) 或 Option+鼠标左键 (Mac) 或使用鼠标中键可以用鼠标进行竖向多行选择；
-  Ctrl+鼠标左键(Win) 或 Command+鼠标左键(Mac) 可以手动选择同时要编辑的多处文本




## 配置文件

	{
		"color_scheme": "Packages/Color Scheme - Default/Made of Code.tmTheme",
		"font_face": "Microsoft YaHei Mono",
		"font_size": 12,
		"ignored_packages":
		[
			"Vintage"
		],
		"line_padding_bottom": 1,
		"line_padding_top": 1,
		"theme": "Flatland Dark.sublime-theme",
		"update_check": false
	}
