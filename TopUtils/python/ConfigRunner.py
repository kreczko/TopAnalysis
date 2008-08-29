import os
import sys
import getopt
import time
#set your config file here
import analyzeQCDBackground_cfg as cms


class CfgRunner:
    def __init__(self):
        self._sleeptime = 10#time in seconds to wait between commands

        #executing path is in most cases the outputpath.
        #you can change it here
        #example: self.filepath = 'outputpath/rootfiles/'
        self.filepath = '' 
        self.fileprefix = 'MatrixMethod_' #will be used as filnameprefix
        self.filesuffix = '.root' #filetype
        
        self.type_ = ''     
        self.numberofevents_ = 0
        
        self.outputfile = 'output.txt'
        self.outputerr = 'outputErr.txt'
        self.runs_ = ""
        
    def main(self):
    #possible arguments:
        # parse command line options
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'ht:e:f:', ['help', 'type=', 'events=', 'out=', 'err='])
        except getopt.error, msg:
            print msg
            print "for help use --help"
            sys.exit(2)
        # process options
        for o, a in opts:
            if o in ("-h", "--help"):
                print __doc__
                sys.exit(0)
            elif o in ("-t", "--type"):
                self.type_ = a
                #self.doAll()
            elif o in ("-e", "--events"):
                self.numberofevents_ = a
            elif o in ("-f", "--out"):
                if(not (a == '')):
                    self.outputfilename = a
            elif o in ("--err"):
                if(not a == ''):
                    self.outputerr = a
#            elif o in ("-c", "--cfg-file"):
#                if(not (a == '')):
#                    self.config = a
            else:
                print 'Argument(s) not recognized. See --help for usage'
                
        if (not self.numberofevents_ == 0) and (not self.type_ == ''):
            self.doAll()
            
    def executeCMSrun(self, configfile):
        print 'Executing cmsRun...'
        print "##################################################"
        if os.path.exists(configfile):
            print 'cmsRun ' + configfile
            if os.path.exists(self.outputfile):
                os.remove(self.outputfile)
            if os.path.exists(self.outputerr):
                os.remove(self.outputerr)   
            
            #setup runtime environment
            #os.system('eval `scramv1 runtime -sh`')# not working
            os.system('cmsRun ' + configfile + " >" + self.outputfile + " 2> " + self.outputerr + " < /dev/null&")
            time.sleep(self._sleeptime)
            self.waitForFirst()
            os.remove(configfile)
        else:
            print 'configfile does not exist'
        
    def TopInspect(self, configfile):
        print 'Executing Inspect_top...'
        print "##################################################"
        print 'Inspect_top ' + configfile
        os.system('Inspect_top ' + configfile + ">& /dev/null&")
        

    ##################################################
    # wait for 1st event to be processed
    ##################################################        
    def waitForFirst(self):
        while (self.readFromFile(self.outputerr) == ""):
            print "Waiting for the 1st event to be processed..."
            time.sleep(self._sleeptime)
        print "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"
        print self.readFromFile(self.outputerr)
        print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        
    def readFromFile(self, filename):
        file = open(filename, 'r')
        str = file.read()
        file.close()
        return str
    
    def doAll(self):
        #check if only some samples are to be done
        #top  or     qcd;top
        #more than one kind of sample
        self.runs_ = self.createRuns(self.type_)
        #check if source-type is defined
        for i in self.runs_:
            self.type_ = i

            if (self.type_ in cms.Config.allowedTypes):                    
                self.doJob(self.type_)
            elif self.type_ == 'quit':
                os._exit(0)
            else:
                print "not allowed type used"
                print "allowed types: ", cms.Config.allowedTypes
                os._exit(0)
                
    def doJob(self, type):
        #create Config
        process = cms.Config(type)
        process.events(self.numberofevents_)
        output = self.filepath + self.fileprefix + type + "_" + time.strftime("%d%m%y", time.gmtime()) + self.filesuffix
        process.out(output)
        #setup outputfiles
        if(self.outputfile == 'output.txt'):
            self.outputfile = 'output_' + type + '.txt'
        if(self.outputerr == 'outputErr.txt'):
            self.outputerr = 'outputErr_' + type + '.txt'
        self.executeCMSrun(process.returnTempCfg())
                
    def createRuns(self, command):
        print 'Parsing command...'
        sampletypes_ = []
        allruns = []
        
        if ';' in command:
            sampletypes_ = command.split(';')
        #print  o.split(';')
        else:
            sampletypes_ = [command]
    
        
        for a in sampletypes_:
            allruns.append(a)
            
        return allruns



if __name__ == '__main__':
    runner = CfgRunner()
    runner.main()
    
    