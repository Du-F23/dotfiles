set number
set relativenumber
set mouse=i
set clipboard=unnamed
set encoding=utf-8
set tabstop=4
set shiftwidth=4
set laststatus=2
set noshowmode
set showcmd
set showmatch
set ruler
set termguicolors
syntax on
filetype plugin on

let $path = "~/.config/nvim/sources"

" Syntax
so $path/polygot.vim

" Plugins
so $path/vim-plug.vim

" Colorschemes
so $path/colorscheme.vim

" Treesitter
so $path/treesitter.vim

" Nerdtree & Nerdcommenter
so $path/nerd.vim

" Keyboard shortcuts
so $path/maps.vim

" CoC
so $path/coc.vim
