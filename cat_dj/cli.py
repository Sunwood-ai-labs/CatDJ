import click
from .cat_dj import CatDJ

@click.command()
@click.option('--input-dir', required=True, help='ディレクトリ音楽ファイル')
@click.option('--output-dir', default='output', help='生成されたファイルの出力ディレクトリ')
@click.option('--input-video', required=True, help='入力ビデオファイル')
@click.option('--track-duration', default=-1, help='各トラックの長さ（ミリ秒）。-1 で元の長さを維持')
@click.option('--crossfade-duration', default=4000, help='クロスフェードの長さ（ミリ秒）')
def main(input_dir: str, output_dir: str, input_video: str, track_duration: int, crossfade_duration: int):
    """CatDJ CLIツール"""
    cat_dj = CatDJ(input_dir, output_dir)
    output_video = cat_dj.run(input_video, track_duration, crossfade_duration)
    click.echo(f"出力ビデオ: {output_video}")

if __name__ == '__main__':
    main()
