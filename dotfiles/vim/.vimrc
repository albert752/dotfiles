" albert752s VIMRC
" Basic configuration
set nu
set rnu
set conceallevel=0
set encoding=UTF-8
set tabstop=4
set shiftwidth=4
set expandtab
" set cursorline
let mapleader = ","

" Quick vimrc edit
nnoremap <Leader>ve :tabnew<CR>:e $MYVIMRC<CR>
nnoremap <Leader>vr :source $MYVIMRC<CR>

" Pathogen
execute pathogen#infect()
syntax on
filetype plugin indent on

" Shortcuts
map <C-t> :NERDTreeToggle<CR>
imap <C-e> <C-o>A
nmap <C-n> :tabnew<CR>

" Python syntax
let g:python_highlight_all = 1

" Solarized Colour Scheme
"let g:solarized_termcolors=16
"syntax enable
"set background=dark
"colorscheme solarized

" Status bar
set laststatus=2


"" Custom colours
highlight LineNr ctermfg=darkgrey
"highlight String ctermfg=darkgreen
"highlight Function ctermfg=blue
"highlight Import ctermfg=darkyellow
"highlight Boolean ctermfg=magenta
""highlight Comment ctermfg,green
"highlight Normal ctermfg=grey
"highlight pythonImport ctermfg=darkyellow
