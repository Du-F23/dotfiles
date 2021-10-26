" Treesitter
let language = ["sh", "c", "css", "haskell", "html", "java", "javascript", "json", "php", "python", "rust", "typescript"]
let file = &filetype
let bool = 0

for x in language
	if file == x
		let bool = 1
	endif
endfor

if bool != 0
lua <<EOF
	bool = true
EOF
else
lua <<EOF
	bool = false
EOF
endif

lua <<EOF
require 'nvim-treesitter.configs'.setup {
	highlight = {
		enable = bool,
		disable = {},
		additional_vim_regex_highlighting = false,
	},

	indent = {
		enable = false,
		disable = {},
	},

	ensure_installed = {
		"bash",
		"c",
		"css",
		"haskell",
		"html",
		"java",
		"javascript",
		"json",
		"php",
		"python",
		"rust",
		"typescript",
	},
}
EOF
