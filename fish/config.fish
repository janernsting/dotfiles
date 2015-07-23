set DEFAULT_USER jan
set fish_greeting # disable fish greeting

set __fish_vi_mode 1
set fish_key_bindings fish_vi_key_bindings

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

set -U fish_user_abbreviations 'g=git'
