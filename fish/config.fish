set DEFAULT_USER jan

if [ -e "$TMUX" ]
  set -gx TERM xterm-256color
else
  set -gx TERM screen-256color
end

function mutt
  bash --login -c '/usr/bin/mutt' $argv;
end
