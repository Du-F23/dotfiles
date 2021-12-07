--==[ Material ]==--

-- Global Config
require('material').setup({
	contrast = true,
	borders = false,

	popup_menu = "dark",

	italics = {
		comments = false,
		keywords = false,
		functions = false,
		strings = false,
		variables = false
	},

	contrast_windows = {
		"terminal",
		"packer",
		"qf"
	},

	text_contrast = {
		lighter = false,
		darker = false
	},

	disable = {
		background = false,
		term_colors = false,
		eob_lines = false
	},

	custom_highlights = {}
})

vim.g.material_style = 'deep ocean'
vim.cmd[[colorscheme material]]

-- Styles:
-- darker
-- lighter
-- oceanic
-- palenight
-- deep ocean
