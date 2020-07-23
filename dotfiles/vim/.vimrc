" albert752s VIMRC
" Basic configuration
set nu
set rnu
set conceallevel=0
set encoding=UTF-8
set tabstop=4
set shiftwidth=4
set expandtab
set colorcolumn=80
 "set textwidth=80
set cursorline
let mapleader = ","

" Quick vimrc edit
nnoremap <Leader>ve :tabnew<CR>:e $MYVIMRC<CR>
nnoremap <Leader>vr :source $MYVIMRC<CR>

" Pathogen
execute pathogen#infect()
syntax on
filetype plugin indent on

" Shortcuts
"let search_and_destroy = "/<++><Enter>"_c4l"
map <C-t> :NERDTreeToggle<CR>
imap <C-e> <C-o>A
nmap <C-n> :tabnew<CR>
map <C-i> /<++><Enter>"_c4l
imap ;pl <++>


" Python syntax
let g:python_highlight_all = 1

" LaTeX
let g:vimtex_view_method = 'zathura'
autocmd FileType *tex* inoremap ;i \textit{}<Esc>i
autocmd FileType *tex* inoremap ;b \textbf{}<Esc>i
autocmd FileType *tex* inoremap ;s \underline{}<Esc>i
autocmd FileType *tex* inoremap ;t \texttt{}<Esc>i
autocmd FileType *tex* inoremap ;f \footnote{}<Esc>i
autocmd FileType *tex* set spell spelllang=en_us

" HTML and HTMLDJANGO
autocmd FileType *html* setlocal tabstop=2
autocmd FileType *html* setlocal shiftwidth=2
autocmd FileType *html* inoremap ;div <div><++></div><Esc>/<++><Enter>"_c4l
autocmd FileType *html* inoremap ;p <p><++></p><Esc>/<++><Enter>"_c4l

" Solarized Colour Scheme
let g:solarized_termcolors=16
syntax enable
set background=dark
colorscheme solarized

" Status bar
set laststatus=2

