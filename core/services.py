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


def run_file_logic_service(path, parsers, emitters):
    file_path = Path(path)
    blob = FileReader(file_path).read()
    _run_parsers_and_emitters(blob, parsers, emitters)


def run_folder_logic_service(path, parsers, emitters):
    folder_path = Path(path)
    blobs = FolderReader(folder_path).read()
    [_run_parsers_and_emitters(blob, parsers, emitters) for blob in blobs]




