日本語入力を可能にさせる
```
sudo apt update
sudo apt install ibus-mozc
sudo reboot
```

Linux RTX4090 driver をまずはダウンロード
[link](https://www.nvidia.co.jp/download/driverResults.aspx/224356/jp)
ダウンロードした奴をインストールする前に依存関係のインストール
```
sudo apt-get install build-essential gcc-multilib dkms
sudo apt update
sudo apt install pkg-config libglvnd-dev

```
Xサーバーの停止
```
sudo systemctl isolate multi-user.target
```
実行権限の追加
普通にプロパティからプログラムとして実行可能にするでもok
```
chmod +x /home/tell/ダウンロード/NVIDIA-Linux-x86_64-550.78.run
```
ドライバのインストール
```
sudo /home/tell/ダウンロード/NVIDIA-Linux-x86_64-550.78.run
```
Xサーバーの再起動
```
sudo systemctl start graphical.target
```
ドライバの確認
```
nvidia-smi
```

CUDA toolkitのダウンロード
[公式ページ](https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local)
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda-repo-ubuntu2004-12-1-local_12.1.0-530.30.02-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-12-1-local_12.1.0-530.30.02-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2004-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```
