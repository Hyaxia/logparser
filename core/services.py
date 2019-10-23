from core.parsers.blob import run_parsers_on_blob
from core.parsers.level import get_parser_by_severity
from core.emitters.console import console_emitter
from core.emitters.file import get_blob_file_emitter
from core.readers.file import file_reader, folder_reader
from core.model.severity import LogLineSeverity
from core.model.file import Path


def _run_parsers_and_emitters(blob, parsers, emitters):
    blob.lines = run_parsers_on_blob(blob.lines, parsers)
    [emitter(blob) for emitter in emitters]


def severity_parser_service(severity):
    LogLineSeverity.validate_severity(severity)
    return get_parser_by_severity(severity)


def console_emitter_service():
    return console_emitter


def dest_file_emitter_service(dest_path):
    dest_path = Path(dest_path)
    return get_blob_file_emitter(dest_path)


def run_file_logic_service(path, parsers, emitters):
    file_path = Path(path)
    blob = file_reader(file_path)
    _run_parsers_and_emitters(blob, parsers, emitters)


def run_folder_logic_service(path, parsers, emitters):
    folder_path = Path(path)
    blobs = folder_reader(folder_path)
    [_run_parsers_and_emitters(blob, parsers, emitters) for blob in blobs]




