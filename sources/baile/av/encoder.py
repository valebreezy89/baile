from subprocess import Popen, PIPE

##
# Mencoder wraper
##
class Encoder:
    #mapping human readable settings names into mencoder args names
    _mapping = dict(vcodec="-ovc", acodec="-oac")
    def __init__(self):
        self.listeners = []
        #first of all we need to find mencoder and check it version (developed with 1.0rc3-4.4.4)
        #so let it use as menspec
        #TODO: reasonable minimal version value
        try:
            proc = Popen(["mencoder", "-v"], stdout=PIPE, stderr=PIPE)
            versionStr = proc.communicate()[0]
            #TODO: check version
        except OSError:
            raise EncoderException("Unable to find mencoder.")
    '''
        Encodes file at inputPath with given settings. Destination file will be places
        ad outputPath. Be sure all folders at outputPath are exist.
    '''
    def encode(self, inputPath, outputPath, settings):
        proc = Popen(["mencoder", "-v"], stdout=PIPE, stderr=PIPE)
    def addListener(self, listener):
        self.listeners.append(listener)
    def removeListenesr(self, listener):
        self.listeners.remove(listener)
        
    #private stuff
    def _parseSettings(self, settings):
        args = []
        for setting in settings:
            arg = self._mapping.get(setting)
            if arg == None:
                arg = setting
            args.append(arg)
        return args

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
