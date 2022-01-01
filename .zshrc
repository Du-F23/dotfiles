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
alias pacman='sudo pacman'

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
        vcs_status[1]=$VCS_STATUS_COMMITS_BEHIND
        vcs_status[2]=$VCS_STATUS_COMMITS_AHEAD
        vcs_status[3]=$VCS_STATUS_STASHES
        vcs_status[4]=$VCS_STATUS_NUM_CONFLICTED
        vcs_status[5]=$VCS_STATUS_NUM_STAGED
        vcs_status[6]=$VCS_STATUS_NUM_UNSTAGED
        vcs_status[7]=$VCS_STATUS_NUM_UNTRACKED
    
    local git_status=0;
    local git_color=0;

    PROMPT='%B %F{blue}%1~%f %F{magenta}%f%b '
	
    function preexec() {
        timer=$(($(date +%s%0N)/1000000))
    }

    function precmd() {
        RPROMPT=''
        if [ $timer ]; then
            now=$(($(date +%s%0N)/1000000))
            ms=$(($now-$timer))
            text='ms'

            if (( $ms > 99 )); then
                if (( $ms < 999 )); then
                    elapsed=$(bc <<< "scale=1; $ms / 1000" | sed "s/^\./0./")
                else
                    elapsed=$(bc <<< "scale=1; $ms / 1000" | sed "s/\.0$//")
                fi
                text='s'
            else
                elapsed=$ms
            fi

            last_exit='%F{%(?.green.red)}%(?.✔.✘)  %f'
            time_elapsed="%F{cyan}${elapsed}${text}%f"
            export RPROMPT="%B${last_exit}${time_elapsed}%b"
            unset timer
        fi
    }
    
    if gitstatus_query MY && [[ $VCS_STATUS_RESULT == ok-sync ]]; then
        RPROMPT+='%B'
        for value in ${vcs_status[@]}; do
            if [[ $value != 0 ]]; then
                local git_status=1;
                break
            fi
        done

        if [[ $git_status == 1 ]]; then
            local array=(4 1 5 7 6 3 2 0)
            for i in ${array[@]}{; do
                if [[ $vcs_status[$i] != 0 ]]; then
                    case $i in
                        1) local git_color=3; ;; # commits behind
                        2) local git_color=1; ;; # commits ahead
                        3) local git_color=2; ;; # stashes
                        4) local git_color=3; ;; # conflicted
                        5) local git_color=3; ;; # staged
                        6) local git_color=2; ;; # unstaged
                        7) local git_color=2; ;; # untracked
                    esac
                    break
                fi
            done
        fi

        case $git_color in
            3) RPROMPT+='%F{red}' ;;
            2) RPROMPT+='%F{yellow}' ;;
            1) RPROMPT+='%F{magenta}' ;;
            0) RPROMPT+='%F{magenta}' ;;
        esac

        RPROMPT+=' ('
        RPROMPT+=${${VCS_STATUS_LOCAL_BRANCH:-@${VCS_STATUS_COMMIT}}//\%/%%}
        (( VCS_STATUS_STASHES )) && RPROMPT+=' *'
        RPROMPT+=')%f%b'
    fi

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
