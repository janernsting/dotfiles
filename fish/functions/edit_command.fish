function edit_command --description "Edit the current command in your $EDITOR"
  set -q EDITOR; or return 1
  set -l tmpfile (mktemp -t "fish_edit_command.XXXXXXXXXX.fish"); or return 1
  commandline > $tmpfile
  eval $EDITOR $tmpfile
  commandline -r -- (cat $tmpfile)
  rm $tmpfile
end
