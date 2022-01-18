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
alias cat='bat'
alias vim='nvim'

# Development
alias github='eval "$(ssh-agent -s)" && github'
alias gpsh='git push'
alias gpll='git pull'
alias gs='git status'
alias gr='git restore'
alias gd='git diff'
alias ga='git add'
alias gb='git branch'
alias gck='git checkout'
alias gsw='git switch'
alias gcm='git commit -m'
alias gcam='git commit -a -m'

# Info
alias google.com='ping -c 5 google.com'
alias archlinux.org='ping -c 5 archlinux.org'
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

# --==[ Key Bindings ]==--
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

# --==[ Prompt + Git ]==--
function preexec() {
  timer=$(($(date +%s%0N) / 1000000))
}

function elapsed_time() {
  function precmd() {
    RPROMPT=''
    if [ $timer ]; then
      local now=$(($(date +%s%0N) / 1000000))
      local ms=$(($now - $timer))
      local time=''

      if (( $ms > 99 )); then
        if (( $ms < 999 )); then
          seconds=$(bc <<< "scale=1; $ms / 1000" | sed "s/^\./0./")
          time=($seconds's')

        else
          seconds=$(($ms / 1000))

          if (( $seconds > 59 )); then
            minutes=$(($seconds / 60))

            if (( $minutes > 59 )); then
              hours=$(($minutes / 60))
              minutes=$(($minutes - ($hours * 60)))
              time=$(print $hours'h' $minutes'm' | sed "s/\s0m$//")

            else
              seconds=$(($seconds - ($minutes * 60)))
              time=$(print $minutes'm' $seconds's' | sed "s/\s0s$//")
            fi

          else
            time=($seconds's')
          fi

        fi
      else
        time=($ms'ms')
      fi

      RPROMPT+="%B%F{yellow}${time}%f%b"
      unset timer
    fi
  }
}

function git_sign() {
  if gitstatus_query MY && [[ $VCS_STATUS_RESULT == ok-sync ]]; then
    declare -A vcs_status
      vcs_status[1]=$VCS_STATUS_COMMITS_BEHIND
      vcs_status[2]=$VCS_STATUS_COMMITS_AHEAD
      vcs_status[3]=$VCS_STATUS_HAS_CONFLICTED
      vcs_status[4]=$VCS_STATUS_HAS_UNSTAGED
      vcs_status[5]=$VCS_STATUS_HAS_STAGED
      vcs_status[6]=$VCS_STATUS_HAS_UNTRACKED

    for value in ${vcs_status[@]}; do
      if [[ $value > 0 ]]; then
        RPROMPT+='%B%F{magenta} *%f%b'
        break
      fi
    done
  fi
}

function git_prompt() {
  if gitstatus_query MY && [[ $VCS_STATUS_RESULT == ok-sync ]]; then
    declare -A vcs_status
      vcs_status[1]=$VCS_STATUS_NUM_UNSTAGED_DELETED
      vcs_status[2]=$VCS_STATUS_NUM_STAGED_DELETED
      vcs_status[3]=$VCS_STATUS_HAS_UNSTAGED
      vcs_status[4]=$VCS_STATUS_HAS_STAGED
      vcs_status[5]=$VCS_STATUS_HAS_UNTRACKED

    for value in ${vcs_status[@]}; do
      if [[ $value > 0 ]]; then
        local git_status=1
        break
      fi
    done

    if [ $git_status ]; then
      local simbols=''
      
      (( $vcs_status[1] )) ||
      (( $vcs_status[2] )) && simbols+='-'
      (( $vcs_status[3] )) && simbols+='!'
      (( $vcs_status[4] )) && simbols+='+'
      (( $vcs_status[5] )) && simbols+='?'

      local STATUS="%B%F{red}[${simbols}]%f%b"
    fi

    if (( VCS_STATUS_HAS_CONFLICTED )); then
      local color='red'
      local icon='%F{red}✘ %f'
    else
      local color='magenta'
    fi

    PROMPT+="%F{white}at%f %B%F{magenta} "
    PROMPT+="${VCS_STATUS_LOCAL_BRANCH}%f%b "
    (( $git_status )) && PROMPT+=${STATUS}

    (( VCS_STATUS_HAS_CONFLICTED )) && LAST_COMMIT+=$icon
    LAST_COMMIT+="%B%F{${color}}@"
    LAST_COMMIT+=${VCS_STATUS_COMMIT[1,7]}
    LAST_COMMIT+='%f%b'
  fi
}

function set_prompt() {
  ZLE_RPROMPT_INDENT=0
  PROMPT='%B%F{cyan}%2~%f%b '
  RPROMPT=''

  if [[ $(pwd) == $HOME ]] || [[ $(pwd) == '/' ]]; then
    PROMPT+='%F{%(?.magenta.red)}❯ %f'
    git_sign
    # elapsed_time

  else
    LAST_COMMIT=''
    git_prompt

    RPROMPT=%{$'\e[1A'%}"${LAST_COMMIT}"%{$'\e[1B'%}

    PROMPT+=$'\n'
    PROMPT+='%F{%(?.yellow.red)}λ%f '
  fi

  setopt no_prompt_{bang,subst} prompt_percent
}

gitstatus_stop 'MY' && gitstatus_start -s -1 -u -1 -c -1 -d -1 'MY'
add-zsh-hook precmd set_prompt

# --==[ Exports ]==--
export PATH="${PATH}:${HOME}/.local/bin"
export PATH="${PATH}:${HOME}/.resources/scripts"

# --==[ Autostart ]==--
# neofetch

# --==[ Performance ]==--
# /usr/bin/time zsh -i -c exit
# zprof
