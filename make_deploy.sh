for d in ./tasks/*/ ; do
	e=$(basename $d)
	git stage ./tasks-deploy/$e
done
