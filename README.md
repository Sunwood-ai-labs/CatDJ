
<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/CatDJ.png" width="100%">
<br>
<h2 align="center">
  ～ Mix Tracks, Unleash Fun ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/cat-dj">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/cat-dj">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/cat-dj">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/cat-dj">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/cat-dj">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/cat-dj">
<a href="https://github.com/Sunwood-ai-labs/CatDJ" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=CatDJ&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/CatDJ">
<a href="https://github.com/Sunwood-ai-labs/CatDJ"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/Sunwood-ai-labs/CatDJ?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/CatDJ"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/CatDJ"></a>
<a href="https://github.com/Sunwood-ai-labs/CatDJ"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/CatDJ"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/CatDJ?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/CatDJ?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/CatDJ/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

# CatDJ

## 🌟 Introduction
CatDJは、複数の音楽トラックをDJスタイルで結合し、その音楽に合わせて指定した動画をループ再生するためのパッケージです。このツールを使用することで、オリジナルのパーティー体験を簡単に作成することができます。音楽と映像を組み合わせて、魅力的でエネルギッシュなパフォーマンスを実現しましょう。

## 🎥 Demo

https://github.com/user-attachments/assets/01959d8c-951e-4da4-90b4-801539a08985

## 🚀 Getting Started
このリポジトリを使い始めるには、以下の手順を守ってください：

1. CatDJをインストールします：
```bash
pip install cat-dj
```

2. 必要な入力ファイルを準備します：
   - 音楽トラックを `input_tracks` ディレクトリに配置します
   - ループさせたい動画ファイル（例：`cat_is_playing_dj2.mp4`）を用意します

3. 以下のコマンドを実行してCatDJを起動します：
```bash
cat-dj --input-dir input_tracks --input-video cat_is_playing_dj2.mp4 --track-duration 25000
```

## 🛠 Options
- `--input-dir`: 音楽ファイルが入っているディレクトリ（必須）
- `--output-dir`: 出力ファイルを保存するディレクトリ（デフォルト: `output`）
- `--input-video`: 入力ビデオファイル（必須）
- `--track-duration`: 各トラックの長さ（ミリ秒）。-1で元の長さを維持（デフォルト: -1）
- `--crossfade-duration`: クロスフェードの長さ（ミリ秒）（デフォルト: 4000）

## 📝 Updates
最新のアップデートや新機能は、リリースノートで確認できます。定期的に更新をチェックして、新機能をお楽しみください。

## 📄 License
このプロジェクトはMITライセンスの下で公開されています。詳細については[LICENSE](https://github.com/Sunwood-ai-labs/CatDJ/blob/main/LICENSE)を参照してください。

## 🙏 Acknowledgements
このプロジェクトは、オープンソースコミュニティからの多くのインスピレーションとサポートによって作成されました。特に、音楽や映像処理に関する文献やライブラリに感謝します。

## 🤝 Contributing
プロジェクトへの貢献を歓迎します！バグ報告、機能リクエスト、プルリクエストなど、どんな形での貢献も大歓迎です。

## 📬 Contact
質問や提案がある場合は、[Issues](https://github.com/Sunwood-ai-labs/CatDJ/issues)セクションでお気軽にお問い合わせください。
