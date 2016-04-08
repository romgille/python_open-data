read -p "Voulez-vous récupérer les dernières données disponibles ? [y/n]" choice
case "$choice" in
  y|Y ) ./getdata.sh;;
  n|N ) echo "ok, on utilisera les dernières données récupérées.";;
  * ) echo "ok, on utilisera les dernières données récupérées.";;
esac
