import db.settings
from request_parsers import errors
from request_parsers import json


def parse_fps(request):
    # pylint: disable=unbalanced-tuple-unpacking
    (video_fps,) = json.parse_json_body(request, required_fields=['videoFps'])
    try:
        # Note: We need to cast the value to a string first otherwise the int
        # function forces floats into integers by simply cutting off the
        # fractional part. This results in the value being incorrectly
        # validated as an integer.
        video_fps = int(str(video_fps))
        if not 1 <= video_fps <= 30:
            raise ValueError
    except ValueError as e:
        raise errors.InvalidVideoFpsError(
            'The video FPS must be an whole number between 1 and 30.') from e
    return video_fps


def parse_jpeg_quality(request):
    # pylint: disable=unbalanced-tuple-unpacking
    (video_jpeg_quality,) = json.parse_json_body(
        request, required_fields=['videoJpegQuality'])
    try:
        # Note: We need to cast the value to a string first otherwise the int
        # function forces floats into integers by simply cutting off the
        # fractional part. This results in the value being incorrectly
        # validated as an integer.
        video_jpeg_quality = int(str(video_jpeg_quality))
        if not 1 <= video_jpeg_quality <= 100:
            raise ValueError
    except ValueError as e:
        raise errors.InvalidVideoJpegQualityError(
            'The video JPEG quality must be an whole number between 1 and 100.'
        ) from e
    return video_jpeg_quality


def parse_h264_bitrate(request):
    # pylint: disable=unbalanced-tuple-unpacking
    (video_h264_bitrate,) = json.parse_json_body(
        request, required_fields=['videoH264Bitrate'])
    try:
        # Note: We need to cast the value to a string first otherwise the int
        # function forces floats into integers by simply cutting off the
        # fractional part. This results in the value being incorrectly
        # validated as an integer.
        video_h264_bitrate = int(str(video_h264_bitrate))
        if not 25 <= video_h264_bitrate <= 20000:
            raise ValueError
    except ValueError as e:
        raise errors.InvalidVideoH264BitrateError(
            'The H264 bitrate must be an whole number between 25 and 20000.'
        ) from e
    return video_h264_bitrate


def parse_streaming_mode(request):
    # pylint: disable=unbalanced-tuple-unpacking
    (video_streaming_mode,) = json.parse_json_body(
        request, required_fields=['videoStreamingMode'])
    try:
        return db.settings.StreamingMode(video_streaming_mode)
    except ValueError as e:
        raise errors.InvalidVideoStreamingModeError(
            'The video streaming mode must be `MJPEG` or `H264`.') from e
