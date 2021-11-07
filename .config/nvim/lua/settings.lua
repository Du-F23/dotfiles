--==[ Settings ]==--
local set = vim.opt

-- Performance
set.lazyredraw = true
local disabled_built_ins = {
    "2html_plugin",
    "getscript",
    "getscriptPlugin",
    "gzip",
    "logipat",
    "netrw",
    "netrwPlugin",
    "netrwSettings",
    "netrwFileHandlers",
    "matchit",
    "tar",
    "tarPlugin",
    "rrhelper",
    "spellfile_plugin",
    "vimball",
    "vimballPlugin",
    "zip",
    "zipPlugin",
}

for _, plugin in pairs(disabled_built_ins) do
    vim.g["loaded_" .. plugin] = 1
end

-- System Utilities
set.clipboard = 'unnamedplus'
set.encoding = 'utf-8'
set.backup = false
set.swapfile = false

-- Interface
set.number = true
set.relativenumber = true
set.hidden = true
set.showmode = false
set.showcmd = true
set.termguicolors = true

-- Mouse Support
set.mouse = 'i'
set.cursorline = false

-- Spaces & Tabs
set.tabstop = 4
set.shiftwidth = 4
set.expandtab = true
