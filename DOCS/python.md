python入れる
必要なパッケージのインストール
```
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```
pythonのインストール
````
sudo apt install python 3.10
``
pythonの確認
```
python3.10 --version
```
pythonの仮想環境を作るためのやつ
```
sudo apt install python3 python3-venv
```
仮想環境の作成
```
python -m venv env
```
仮想環境の実行
```
source env/bin/activate
```
pytorchのインストール(CUDA12.1)
```
pip3 install torch torchvision torchaudio
```