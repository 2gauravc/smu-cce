### Git clone the repo
```
git clone https://github.com/2gauravc/smu-cce.git
```

### Create and activate an environment
```
python3 -m venv cce-env
source cce-env/bin/activate
```

### Switch to repo directory  
```
cd smu-cce
```

### Install dependencies
```
pip install -r requirements.txt
```

### Install quarto 
```
cd /tmp
curl -fL --retry 5 --retry-delay 2 -o quarto.deb \
  https://github.com/quarto-dev/quarto-cli/releases/download/v1.9.36/quarto-1.9.36-linux-amd64.deb
sudo dpkg -i quarto.deb
```

## Run Quarto and preview slides 

```
quarto preview lesson1.qmd
```