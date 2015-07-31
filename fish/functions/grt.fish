function grt -d "Change to top of the current repository or submodule"
  cd (git rev-parse --show-toplevel; or echo ".") 
end
