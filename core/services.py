from core.parsers.blob import run_parsers_on_lines
from core.parsers.level import SeverityParser
from core.emitters.console import ConsoleEmitter
from core.emitters.file import FileEmitter
from core.readers.file import FileReader
from core.readers.folder import FolderReader
from core.model.severity import LogLineSeverity
from core.model.file import Path


def _run_parsers_and_emitters(blob, parsers, emitters):
    blob.lines = run_parsers_on_lines(blob.lines, parsers)
    [emitter.emit(blob) for emitter in emitters]


def severity_parser_service(severity):
    LogLineSeverity.validate_severity(severity)
    return SeverityParser(severity)


def console_emitter_service():
    return ConsoleEmitter()


def dest_file_emitter_service(dest_path):
    dest_path = Path(dest_path)
    return FileEmitter(dest_path)


def file_reader_service(path):
    file_path = Path(path)
    return FileReader(file_path)


def folder_reader_service(path):
    folder_path = Path(path)
    return FolderReader(folder_path)


def main_logic(readers, parsers, emitters):
    blobs = []
    for runner in readers:
        blobs.extend(runner.read())
    [_run_parsers_and_emitters(blob, parsers, emitters) for blob in blobs]




