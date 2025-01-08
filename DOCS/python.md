python入れる
必要なパッケージのインストール
```
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt list python3.*
```
pythonのインストール
```
sudo apt install -y python3.10 python3.10-venv python3.10-dev
```
pythonの仮想環境を作るためのやつ
```
sudo apt install python3 python3-venv
```
仮想環境の作成
```
python3.10 -m venv env
```
仮想環境の実行
```
source env/bin/activate
```
pytorchのインストール(CUDA12.1)
```
pip3 install torch torchvision torchaudio
```
