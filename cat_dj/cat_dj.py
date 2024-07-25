import os
from typing import Optional
from .dj_music_mixer import DJMusicMixer
from .video_loop_processor import VideoLoopProcessor
from loguru import logger

class CatDJ:
    def __init__(self, input_dir: str, output_dir: str = "output"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.mixer = DJMusicMixer(input_dir=input_dir, output_dir=output_dir)
        os.makedirs(output_dir, exist_ok=True)

    def create_mix(self, track_duration: int = -1, crossfade_duration: int = 4000) -> str:
        logger.info("音楽ミックスの作成を開始します")
        return self.mixer.process_directory(track_duration=track_duration, crossfade_duration=crossfade_duration)

    def create_video(self, input_video: str, mixed_audio: str, output_video: str = "cat_dj_output.mp4") -> str:
        logger.info("ビデオの作成を開始します")
        processor = VideoLoopProcessor(
            input_file=input_video,
            output_file=output_video,
            audio_file=mixed_audio,
            output_dir=self.output_dir
        )
        processor.process()
        return os.path.join(self.output_dir, output_video)

    def run(self, input_video: str, track_duration: int = -1, crossfade_duration: int = 4000) -> str:
        mixed_audio = self.create_mix(track_duration, crossfade_duration)
        return self.create_video(input_video, mixed_audio)
