function fish_user_key_bindings
  bind --mode insert --sets-mode default kj backward-char force-repaint

  bind -M visual -m insert c kill-selection end-selection force-repaint

  bind \cl 'clear; commandline -f repaint'
  bind -M insert \cl 'clear; commandline -f repaint'

  bind -M insert \cf forward-word

  bind \cu backward-kill-line

  bind -M default V edit_command
  bind -M default K commandline_man

  bind \cr search_history
  bind -M insert \cr search_history
end
