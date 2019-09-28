# Makefile for dotfiles in the style of
# http://github.com/mitsuhiko/dotfiles/blob/master/Makefile
# found in https://github.com/sanitz/dotfiles/blob/master/Makefile

install: install-vim install-mutt install-git install-fish install-peco install-misc-rcs

install-vim:
	rm -rf ~/.vim ~/.vimrc
	ln -s `pwd`/vim ~/.vim
	ln -s ~/.vim/vimrc ~/.vimrc

install-mutt:
	rm -rf ~/.mutt ~/.muttrc ~/.msmtprc ~/.goobookrc ~/.offlineimaprc
	ln -s `pwd`/mutt ~/.mutt
	ln -s ~/.mutt/muttrc ~/.muttrc
	ln -s ~/.mutt/msmtprc ~/.msmtprc
	ln -s ~/.mutt/goobookrc ~/.goobookrc
	ln -s ~/.mutt/offlineimaprc ~/.offlineimaprc

install-git:
	rm -rf ~/.gitconfig ~/.gitignore_global
	ln -s `pwd`/git/gitconfig ~/.gitconfig
	ln -s `pwd`/git/gitignore_global ~/.gitignore_global

install-fish:
	rm -rf ~/.config/fish
	ln -s `pwd`/fish ~/.config/fish

install-peco:
	rm -rf ~/.config/peco
	ln -s `pwd`/peco ~/.config/peco

install-misc-rcs:
	rm -rf ~/.wgetrc ~/.ctags
	ln -s `pwd`/wgetrc ~/.wgetrc
	ln -s `pwd`/ctags ~/.ctags

