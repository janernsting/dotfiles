function git
  # inspired by thoughtbot/dotfiles
  if count $argv > /dev/null # alternative: set -q argv
    command git $argv
  else
    command git status -sb
  end
end
