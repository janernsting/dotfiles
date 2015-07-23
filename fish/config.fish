set DEFAULT_USER jan
set fish_greeting # disable fish greeting

if [ -e "$TMUX" ]
  set -gx TERM xterm-256color
else
  set -gx TERM screen-256color
end

function mutt
  bash --login -c '/usr/bin/mutt' $argv;
end

function git
  # inspired by thoughtbot/dotfiles
  if count $argv > /dev/null # alternative: set -q argv
    command git $argv
  else
    command git status -sb
  end
end

set fish_user_abbreviations 'g=git'

# enable vi mode indicator
set -g __fish_vi_mode 1
