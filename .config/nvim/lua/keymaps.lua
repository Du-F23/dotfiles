--==[ Key Bindings ]==--

-- Set new keymap
local map = function(key)
	local opts = {noremap = true}
	for i, v in pairs(key) do
		if type(i) == 'string' then
			opts[i] = v
		end
	end

	vim.api.nvim_set_keymap(
		key[1],
		key[2],
		key[3],
		opts
	)
end

-- Leader Key
vim.g.mapleader = ' '

-- Save & Quit
map{'n', '<Leader>w', ':w<cr>'}
map{'n', '<Leader>q', ':q<cr>'}

-- Reload
map{'n', '<Leader>r', ':source %'}
