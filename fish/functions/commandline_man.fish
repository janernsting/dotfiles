function commandline_man
  set cmd (echo (commandline)|cut -f 1 -d " ")

  switch $cmd
    case openssl -o sudo
      set c (echo (commandline)|cut -f 2 -d " ")
    case git -o btrfs -o ip
      set c (echo (commandline)|cut -f 1 -d " ")-(echo (commandline)|cut -f 2 -d " ")
  end
  if test ! $c = ""
    set cmd $c
  end

  man $cmd
end
