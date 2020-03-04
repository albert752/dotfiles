" albert752s VIMRC
" Basic configuration

set nu
set rnu
set conceallevel=0
execute pathogen#infect()
syntax on
filetype plugin indent on

" Shortcuts
map <C-t> :NERDTreeToggle<CR>

" Solarized Colour Scheme
syntax enable
set background=dark
colorscheme solarized
