# setup ssh key on the runner
mkdir -p ~/.ssh
echo "$MANIFEST_SSH" > ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
ssh-keyscan github.com >> ~/.ssh/known_hosts

# clone on manifest repo's runner via ssh
git clone git@github.com:VeeraReddyRavuri/cloud-engineer-labs-manifests.git

cd cloud-engineer-labs-manifests

# configure git identity
git config user.email "pipeline@github.com"
git config user.name "github actions"

# update deployment.yml via sed
sed -i "s|image: veerareddyravuri/cicd-app:.*|image: veerareddyravuri/cicd-app:$1|" manifests/deployment.yml

# Commit
git add manifests/deployment.yml
git commit -m "deploy: image updated to new SHA"
git push