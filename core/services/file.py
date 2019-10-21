import os.path
from core.parsers.blob import run_parsers_on_blob
from core.parsers.level import parse_by_severity
from core.emitters.console import blob_console_emitter
from core.readers.file import file_reader, folder_reader
from core.model.severity import LogLineSeverity


def _run_parsers_and_emitters(blob, parsers, emitters):
    blob.lines = run_parsers_on_blob(blob.lines, parsers)
    [emitter(blob) for emitter in emitters]


def _execute_file_logic(path, parsers, emitters):
    blob = file_reader(path)
    _run_parsers_and_emitters(blob, parsers, emitters)


def _execute_folder_logic(path, parsers, emitters):
    blobs = folder_reader(path)
    [_run_parsers_and_emitters(blob, parsers, emitters) for blob in blobs]


def file_severity_to_console(path, severity):
    if os.path.isdir(path):
        raise Exception('Following path leads to directory: {}'.format(path))
    LogLineSeverity.validate_severity(severity)
    _execute_file_logic(path, [parse_by_severity(severity)], [blob_console_emitter])


def folder_severity_to_console(path, severity):
    if not os.path.isdir(path):
        raise Exception('Following path leads to file: {}'.format(path))
    LogLineSeverity.validate_severity(severity)
    _execute_folder_logic(path, [parse_by_severity(severity)], [blob_console_emitter])



