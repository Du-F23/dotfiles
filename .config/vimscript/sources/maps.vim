" Keyboard shortcuts
let mapleader = " "

nmap <Leader>w :w<cr>
nmap <Leader>q :q<cr>

nmap <Leader>s <Plug>(easymotion-s2)

nmap <Leader>o :NERDTreeToggle %<cr>
nmap <Leader>c<space> NERDCommenterToggle

nmap <Leader>f :Files<cr>
nmap <Leader>b :Buffers<cr>

nmap <Leader>ce :CocEnable<cr>
nmap <Leader>cd :CocDisable<cr>
nmap <Leader>cx :CocList extensions<cr>
nmap <Leader>cnc :CocUpdateSync

nmap <Leader>r :source %

nmap <Leader>pl :PlugInstall
nmap <Leader>pd :PlugUpdate
