# --==[ Autoload ]==--
# zmodload zsh/zprof
autoload -U colors && colors
# autoload -Uz compinit
# zmodload zsh/complist
autoload -Uz add-zsh-hook

# --==[ History File ]==--
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history
setopt appendhistory

# --==[ Alias ]==--
# System
alias cd..='cd ..'
alias c='clear'
alias tar='tar -xf'
alias dload='curl -O'
alias grep='grep --color=auto'

# Files
alias ls='exa --group-directories-first'
alias ll='exa -la --group-directories-first'
alias tree='exa -T'

# Development
alias cat='bat'
alias vim='nvim'

# Info
alias fetch='neofetch'
alias usage='du -sh'

# --==[ Autocomplete ]==--
# - Option 1
# zstyle ':completion:*' menu select=0
# zstyle ':completion:*' format '  %d'
# compinit

# - Option 2
# setopt autocd
# zstyle ':completion:*' menu select
# zstyle ':completion:*' matcher-list '' \
#   'm:{a-z\-}={A-Z\_}' \
#   'r:[^[:alpha:]]||[[:alpha:]]=** r:|=* m:{a-z\-}={A-Z\_}' \
#   'r:|?=** m:{a-z\-}={A-Z\_}'
# compinit

# --==[ Plugins ]==--
# Highlighting
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Autosuggestions
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# Git Status
source /usr/share/gitstatus/gitstatus.prompt.zsh

# --==[ Prompt + Git ]==--
function set_prompt() {
    declare -A vcs_status
        vcs_status[0]=$VCS_STATUS_COMMITS_BEHIND
        vcs_status[1]=$VCS_STATUS_COMMITS_AHEAD
        vcs_status[2]=$VCS_STATUS_STASHES
        vcs_status[3]=$VCS_STATUS_NUM_CONFLICTED
        vcs_status[4]=$VCS_STATUS_NUM_STAGED
        vcs_status[5]=$VCS_STATUS_NUM_UNSTAGED
        vcs_status[6]=$VCS_STATUS_NUM_UNTRACKED

    let x=0;

    for i in ${vcs_status[@]}; do
        if [[ $i != 0 ]]; then
            let x=1;
        fi
    done

    PROMPT='%B%F{green}%n%f%F{yellow}:%f%F{blue}[%1d]%f '
	
    if gitstatus_query MY && [[ $VCS_STATUS_RESULT == ok-sync ]]; then
        PROMPT+='%bon%B %F{magenta} '
        PROMPT+=${${VCS_STATUS_LOCAL_BRANCH:-@${VCS_STATUS_COMMIT}}//\%/%%}
        PROMPT+='%f '

        if [[ $x != 0 ]]; then
            PROMPT+='%F{red}['
        fi

        (( VCS_STATUS_COMMITS_BEHIND )) && PROMPT+=''
        (( VCS_STATUS_COMMITS_AHEAD  )) && PROMPT+=''
        (( VCS_STATUS_STASHES        )) && PROMPT+='*'
        (( VCS_STATUS_NUM_CONFLICTED )) && PROMPT+='~'
        (( VCS_STATUS_NUM_STAGED     )) && PROMPT+='+'
        (( VCS_STATUS_NUM_UNSTAGED   )) && PROMPT+='!'
        (( VCS_STATUS_NUM_UNTRACKED  )) && PROMPT+='?'

        if [[ $x != 0 ]]; then
            PROMPT+=']%f'
        fi
    fi

    PROMPT+=$'\n'
    PROMPT+='%b%F{yellow} ﬌%f '

    setopt no_prompt_{bang,subst} prompt_percent
}

gitstatus_stop 'MY' && gitstatus_start -s -1 -u -1 -c -1 -d -1 'MY'
add-zsh-hook precmd set_prompt

# --==[ Highlighting ]==--
typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=magenta'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=magenta'
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=magenta'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=red'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=cyan'
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=cyan'
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=blue'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=blue'
ZSH_HIGHLIGHT_STYLES[path]='fg=blue'

# --==[ Key bindings ]==--
bindkey '^ ' autosuggest-accept                    # ctrl + space
bindkey '^[[7~' beginning-of-line                  # ctrl + a
bindkey '^[[8~' end-of-line                        # ctrl + e
bindkey '^[[2~' overwrite-mode                     # insert
bindkey '^[[3~' delete-char                        # delete
bindkey '^[[C'  forward-char                       # right
bindkey '^[[D'  backward-char                      # left
bindkey '^[[5~' history-beginning-search-backward  # page up
bindkey '^[[6~' history-beginning-search-forward   # page down
bindkey '^[[1;5D' backward-word                    # ctrl + right
bindkey '^[[1;5C' forward-word                     # ctrl + left
bindkey '^H' backward-kill-word                    # ctrl + backspace
bindkey '^K' backward-kill-line                    # ctrl + k
bindkey '^[[Z' undo                                # shift + tab
bindkey '^L' clear-screen                          # ctrl + l

# - Keycode
# (crtl + v) + (key combo)
# - Source
# https://linux.die.net/man/1/zshzle

# --==[ Exports ]==--
export PATH="${PATH}:${HOME}/.local/bin"

# --==[ Autostart ]==--
# neofetch

# --==[ Performance ]==--
# /usr/bin/time zsh -i -c exit
# zprof
