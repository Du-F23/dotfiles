--==[ Plugins ]==--

return require('packer').startup(function()
	-- Performance
	-- use 'dstein64/vim-startuptime'

	-- Color Schemes
	use 'marko-cerovac/material.nvim'
	-- use 'Shatur/neovim-ayu'
	-- use 'RRethy/nvim-base16'
	-- use 'folke/tokyonight.nvim'

	-- Treesitter
	use {
		'nvim-treesitter/nvim-treesitter',
		run = ':TSUpdate'
	}

	-- Lualine
	use {
		'nvim-lualine/lualine.nvim',
		requires = {
			'kyazdani42/nvim-web-devicons',
			opt = true
		}
	}
end)
