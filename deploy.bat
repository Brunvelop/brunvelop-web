hugo -D
git checkout deploy
git checkout main -- public
xcopy /s public . /Y
rmdir /s /q public
git add .
git commit -m 'deploy-test'
git push
git checkout main