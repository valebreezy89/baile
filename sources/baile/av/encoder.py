from subprocess import Popen, PIPE
import re
##
# Mencoder wraper
##
class Encoder:
    #mapping human readable settings names into mencoder args names
    _preArgs = dict(vcodec=["-ovc","lavc","-lavcopts"], acodec=["-oac"], scale=["-vf"])
    _pctRegexp = "\([0-9]{1,3}\%{1}\)"
    _bufSize = 40
    _listeners = []
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
        args = ["mencoder", inputPath]
        args.extend(settings)
        args.extend(["-o", outputPath]);
        proc = Popen(args=args, stdout=PIPE, stderr=PIPE)
        self._notify_started()
        while proc.poll() == None:
            outBuf = proc.stdout.read(self._bufSize)
            #parse percentage
            m = re.search(self._pctRegexp, outBuf)
            if (m != None):
                self._notify_progress(int(m.group(0)[1:-2]))
        self._notify_finished()  
    def add_listener(self, listener):
        self._listeners.append(listener)
    def remove_listenesr(self, listener):
        self._listeners.remove(listener)
        
    #private stuff
    def _notify_progress(self, progress):
        for l in self._listeners:
            l.progress(progress)
    def _notify_started(self):
        for l in self._listeners:
            l.started()
    def _notify_finished(self):
        for l in self._listeners:
            l.finished()

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
