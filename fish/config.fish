set DEFAULT_USER jan

if [ -e "$TMUX" ]
  set -gx TERM xterm-256color
else
  set -gx TERM screen-256color
end

set -gx EDITOR vim

set fish_key_bindings fish_vi_key_bindings
eval (perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)
export PATH="/usr/local/opt/coreutils/libexec/gnubin:/usr/local/opt/python/libexec/bin:$PATH"
export MANPATH="/usr/local/opt/coreutils/libexec/gnuman:$MANPATH"
export BYOBU_PREFIX=/usr/local
export GPG_TTY=(tty)
