# add paths
for ITEM in $HOME/.sdkman/candidates/* ;
	set -gx PATH $PATH $ITEM/current/bin
end
