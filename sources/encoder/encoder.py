from subprocess import Popen, PIPE
##
# Mencoder wraper
##
class Encoder:
    def __init__(self):
        #first of all we need to find mencoder and check it version (developed with 1.0rc3-4.4.4)
        #so let it use as menspec
        #TODO: reasonable minimal version value
        try:
            proc = Popen(["mencoder", "-v"], stdout=PIPE, stderr=PIPE)
            versionStr = proc.communicate()[0]
            #TODO: check version
        except OSError:
            raise EncoderException("Unable to find mencoder.")
    def encode(self, path, settings):
        return
    def addListener(self, listener):
        return

##
# Listener for Encoder. Will receive state notifications (start,stop, progress etc)
##
class EncoderListener:
    def stage(self, stage):
        pass
    def progress(self, progressVal):
        pass
    def started(self):
        pass
    def interrupted(self, reason):
        pass
    def finished(self):
        pass
##
# Encoder own exception
##
class EncoderException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
if __name__ == "__main__":
    Encoder()
