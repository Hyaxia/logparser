def get_blob_file_emitter(path):
    def inner(blob):
        try:
            with open(path, 'a') as f:
                f.write(str(blob))
        except Exception as e:
            raise Exception('Could not write to {}'.format(path)) from e
    return inner
