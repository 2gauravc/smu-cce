### Git clone the repo
```
git clone https://github.com/2gauravc/smu-cce.git
cd smu-cce
```

### Create and activate an environment
```
python3 -m venv cce-env
source cce-env/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Install quarto 
```
cd /tmp
curl -fL --retry 5 --retry-delay 2 -o quarto.deb \
https://github.com/quarto-dev/quarto-cli/releases/latest/download/quarto-linux-amd64.deb
sudo dpkg -i quarto.deb
```
