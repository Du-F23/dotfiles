#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias cd..='cd ..'
alias c='clear'
alias tar='tar -xf'
alias dload='curl -O'
alias grep='grep --color=auto'
alias ls='ls --color=auto'
alias all='ls -ahls'
alias vim='nvim'
alias usage='du -sh'

PS1='[\u@\h \W]\$ '
