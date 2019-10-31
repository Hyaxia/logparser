from core.model.emitter import ABCEmitter


class ConsoleEmitter(ABCEmitter):
    def emit(self, blob):
        print(blob)



