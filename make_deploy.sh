for d in ./tasks/*/ ; do
	e=$(basename $d)
	cp -r ./tasks-deploy/_template ./tasks-deploy/$e
done