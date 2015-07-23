function fish_user_key_bindings
  fish_vi_key_bindings

  bind --mode insert --sets-mode default kj backward-char force-repaint

  bind -M visual -m insert c kill-selection end-selection force-repaint

  bind \cl 'clear; commandline -f repaint'
  bind -M insert \cl 'clear; commandline -f repaint'

  bind -M insert \ce accept-autosuggestion

  bind \cu backward-kill-line
end
