import os
import subprocess
from typing import List, Optional
from pydub import AudioSegment
import random
from loguru import logger
from art import *

class DJMusicMixer:
    # クラス定数
    DEFAULT_TRACK_DURATION = 25000  # ミリ秒
    DEFAULT_CROSSFADE_DURATION = 1000  # ミリ秒
    DEFAULT_OUTPUT_DIR = "output"
    SUPPORTED_FORMATS = ('.mp3', '.wav', '.ogg', '.flac')

    def __init__(self, input_dir: Optional[str] = None, output_dir: str = DEFAULT_OUTPUT_DIR):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self._setup_directories()

    def _setup_directories(self):
        """ディレクトリのセットアップを行う"""
        os.makedirs(self.output_dir, exist_ok=True)
        logger.info(f"出力ディレクトリを作成しました: {self.output_dir}")
        if self.input_dir:
            logger.info(f"入力ディレクトリを設定しました: {self.input_dir}")

    def _load_audio(self, full_path: str) -> AudioSegment:
        """音声ファイルを読み込む"""
        logger.info(f"音声ファイルを読み込んでいます: {full_path}")
        return AudioSegment.from_file(full_path, format=os.path.splitext(full_path)[1][1:])

    def _crossfade(self, audio1: AudioSegment, audio2: AudioSegment, duration: int) -> AudioSegment:
        """2つの音声をクロスフェードさせる"""
        logger.info(f"{duration}ミリ秒でクロスフェードを適用しています")
        return audio1.append(audio2, crossfade=duration)

    def _apply_effect(self, audio: AudioSegment) -> AudioSegment:
        """ランダムなエフェクトを適用する"""
        effects = [
            ("フェードイン", lambda a: a.fade_in(min(1000, len(a)))),
            ("フェードアウト", lambda a: a.fade_out(min(1000, len(a)))),
            ("ハイパスフィルター", lambda a: a.high_pass_filter(1000)),
            ("ローパスフィルター", lambda a: a.low_pass_filter(1000)),
            # ("リバース", lambda a: a.reverse())
        ]
        effect_name, effect_func = random.choice(effects)
        logger.info(f"エフェクトを適用しています: {effect_name}")
        return effect_func(audio)

    def _process_track(self, audio: AudioSegment, track_duration: int) -> AudioSegment:
        """トラックを指定された長さに処理する"""
        if track_duration == -1:
            return audio

        if len(audio) < track_duration:
            loops = (track_duration // len(audio)) + 1
            audio = audio * loops

        start = random.randint(0, len(audio) - track_duration)
        return audio[start:start + track_duration]

    def mix_tracks(self, input_files: List[str], output_file: str, track_duration: int = DEFAULT_TRACK_DURATION, crossfade_duration: int = DEFAULT_CROSSFADE_DURATION) -> str:
        """複数の音声トラックをDJ風にミックスする"""
        logger.info(f"トラックのミキシングを開始します: {', '.join(input_files)}")
        
        mixed = AudioSegment.empty()
        
        for i, file in enumerate(input_files, 1):
            logger.info(f"トラック {i}/{len(input_files)} を処理しています: {file}")
            full_path = os.path.join(self.input_dir, file)
            audio = self._load_audio(full_path)
            
            segment = self._process_track(audio, track_duration)
            segment = self._apply_effect(segment)
            
            if len(mixed) > 0:
                mixed = self._crossfade(mixed, segment, crossfade_duration)
            else:
                mixed += segment
            
            logger.info(f"トラック {i} をミックスしました（長さ: {len(segment)}ミリ秒）")

        output_path = os.path.join(self.output_dir, output_file)
        logger.info(f"ミックスした音声を保存しています: {output_path}")
        mixed.export(output_path, format="mp3")
        logger.success(f"ミックスが完了しました: {output_path}")
        
        return output_path

    def adjust_audio_length(self, audio_file: str, target_duration: float) -> str:
        """音声ファイルの長さを目標の長さに調整する"""
        if target_duration == -1:
            logger.info(f"音声ファイル '{audio_file}' の長さを調整せずに使用します")
            return audio_file

        logger.info(f"音声ファイル '{audio_file}' の長さを {target_duration:.2f} 秒に調整しています...")
        
        audio = self._load_audio(audio_file)
        current_duration = len(audio) / 1000.0  # ミリ秒から秒に変換
        
        if current_duration < target_duration:
            loops = int(target_duration // current_duration) + 1
            logger.info(f"音声が短いため、{loops}回ループさせています")
            audio = audio * loops
        
        logger.info(f"目標の長さ {target_duration:.2f} 秒にトリミングしています")
        audio = audio[:int(target_duration * 1000)]
        
        output_path = os.path.join(self.output_dir, f"adjusted_{os.path.basename(audio_file)}")
        logger.info(f"調整した音声を保存しています: {output_path}")
        audio.export(output_path, format="mp3")
        logger.success(f"音声の長さ調整が完了しました: {output_path}")
        
        return output_path

    def process_directory(self, track_duration: int = DEFAULT_TRACK_DURATION, crossfade_duration: int = DEFAULT_CROSSFADE_DURATION) -> str:
        """指定されたディレクトリ内のすべての音声ファイルを処理する"""
        tprint(">>  VideoLoopProcessor", font="rnd-large")
        if not self.input_dir:
            logger.error("入力ディレクトリが指定されていません")
            return ""

        audio_files = [f for f in os.listdir(self.input_dir) if f.endswith(self.SUPPORTED_FORMATS)]
        if not audio_files:
            logger.warning("指定されたディレクトリに音声ファイルが見つかりません")
            return ""

        logger.info(f"ディレクトリ内の音声ファイル: {', '.join(audio_files)}")
        output_file = f"mixed_{os.path.basename(self.input_dir)}.mp3"
        return self.mix_tracks(audio_files, output_file, track_duration, crossfade_duration)

if __name__ == "__main__":
    input_dir = "input_tracks_enka"
    output_dir = "output_mixes"
    mixer = DJMusicMixer(input_dir=input_dir, output_dir=output_dir)
    
    # ディレクトリ内のすべての音声ファイルを処理
    track_duration = 25000  # 25秒、-1 for full track
    # track_duration = -1  # 25秒、-1 for full track
    crossfade_duration = 4000  # 1秒
    mixed_track = mixer.process_directory(track_duration=track_duration, crossfade_duration=crossfade_duration)
    
    if mixed_track:
        logger.info(f"ミックスしたトラックを保存しました: {mixed_track}")

        # ビデオの長さに合わせて調整（例として180秒、-1 for no adjustment）
        # video_duration = 180  # -1 for no adjustment
        video_duration = -1  # -1 for no adjustment
        adjusted_audio = mixer.adjust_audio_length(mixed_track, video_duration)
        logger.info(f"調整した音声を保存しました: {adjusted_audio}")
    else:
        logger.error("音声ファイルの処理に失敗しました")
