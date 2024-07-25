import subprocess
import sys
import random
import os
import shutil
from loguru import logger
from typing import List

from art import *
class VideoLoopProcessor:
    """
    動画をオーディオファイルの長さに合わせてループ処理するクラス。
    """

    def __init__(
        self,
        input_file: str,
        output_file: str,
        audio_file: str,
        output_dir: str = "output",
        temp_file_prefix: str = "temp_",
        speed_min: float = 0.7,
        speed_max: float = 1.3
    ):
        self.input_file = input_file
        self.output_file = output_file
        self.audio_file = audio_file
        self.output_dir = os.path.join(output_dir, os.path.splitext(os.path.basename(self.input_file))[0])
        self.temp_file_prefix = temp_file_prefix
        self.speed_min = speed_min
        self.speed_max = speed_max

        self.reversed_file = f"{self.temp_file_prefix}reversed.mp4"
        self.temp_combined_file = f"{self.temp_file_prefix}combined.mp4"
        self.filelist_name = "filelist.txt"

        os.makedirs(self.output_dir, exist_ok=True)
        self._copy_files_to_output_dir()

    def _copy_files_to_output_dir(self):
        """入力ファイルとオーディオファイルを処理ディレクトリにコピーする"""
        logger.info(f"入力ファイル '{self.input_file}' を '{self.output_dir}' にコピーしています...")
        shutil.copy2(self.input_file, self.output_dir)
        logger.info(f"入力ファイル '{self.audio_file}' を '{self.output_dir}' にコピーしています...")
        shutil.copy2(self.audio_file, self.output_dir)

    def _get_audio_duration(self, audio_file: str) -> float:
        """指定されたオーディオファイルの長さを秒単位で取得する"""
        logger.info(f"オーディオファイル '{audio_file}' の長さを取得しています...")
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                os.path.basename(audio_file)
            ],
            capture_output=True,
            text=True,
            cwd=self.output_dir  
        )
        duration = float(result.stdout)
        logger.info(f"オーディオの長さ: {duration:.2f}秒")
        return duration

    def _concat_videos(self, file_list: List[str], output_file_path: str):
        """ファイルリスト内のビデオファイルを連結する"""
        filelist_path = os.path.join(self.output_dir, self.filelist_name)
        with open(filelist_path, "w") as f:
            for file_path in file_list:
                f.write(f"file '{file_path}'\n")
        subprocess.run(
            ["ffmpeg", "-f", "concat", "-safe", "0", "-i", self.filelist_name, "-c", "copy", output_file_path],
            check=True,
            cwd=self.output_dir,
        )
        logger.info(f"出力ファイル '{output_file_path}' を作成しました")

    def process(self):
        """動画を処理するメインのメソッド"""
        tprint(">>  VideoLoopProcessor", font="rnd-large")
        logger.info("動画を逆再生しています...")
        subprocess.run(["ffmpeg", "-i", self.input_file, "-vf", "reverse", self.reversed_file], cwd=self.output_dir)

        videos = [os.path.basename(self.input_file), self.reversed_file]
        total_duration = 0
        i = 0

        while total_duration < self._get_audio_duration(self.audio_file):
            video = videos[i % 2]
            i += 1

            speed = random.uniform(self.speed_min, self.speed_max)
            temp_file = f"{self.temp_file_prefix}{int(total_duration * 1000):06d}.mp4"

            logger.info(f"動画 '{video}' を速度 {speed:.2f}x で処理しています...")
            subprocess.run(
                [
                    "ffmpeg",
                    "-i", video,
                    "-filter:v", f"setpts={1 / speed}*PTS",
                    temp_file
                ],
                cwd=self.output_dir
            )

            videos.append(temp_file)
            total_duration += self._get_audio_duration(os.path.join(self.output_dir, temp_file))

        logger.info("動画を結合しています...")
        self._concat_videos(videos, self.temp_combined_file)

        logger.info("MP3と結合しています...")
        subprocess.run(
            [
                "ffmpeg",
                "-i", self.temp_combined_file,
                "-i", os.path.basename(self.audio_file),
                "-map", "0:v",
                "-map", "1:a",
                "-c:v", "copy",
                "-shortest",
                self.output_file
            ],
            cwd=self.output_dir
        )

        logger.info(f"最終出力ファイル '{os.path.join(self.output_dir, self.output_file)}' を作成しました")


if __name__ == "__main__":
    input_file = "cat_is_playing_dj.mp4"
    output_file = "output.mp4"
    audio_file = "input_tracks_enka/o_青い夜の響き.mp3" 

    processor = VideoLoopProcessor(input_file, output_file, audio_file)
    processor.process()
