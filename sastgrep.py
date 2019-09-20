
import shlex,subprocess,html
import re
def initate_grep_command(Args):
   try: 
    Output=subprocess.check_output(Args)
    return Output
   except:
       Output="Grep Command Was Insuccessful"
       return Output


def sort_data_from_grep_command(CommandOutput):
    SastDataDict={}
    SastDataDict['data']=[]
    CommandOutput=CommandOutput.decode('utf-8')
    CommandOutput=CommandOutput.split('\n')
    for EachLine in CommandOutput:
       if len(EachLine)>2:
         
         try:   
           TempList=[]
           SplitInfo=re.split("(\d{1,}:)",EachLine)
          
           TempFileName=SplitInfo[0].replace(':','')
           TempLineNumber=SplitInfo[1].replace(':','')
           TempCode=html.escape(SplitInfo[2])
           TempList.append(TempFileName)
           TempList.append(TempLineNumber)
           TempList.append(TempCode)
       
           SastDataDict['data'].append(TempList)
         except:
            pass   
    print (SastDataDict)       
    return SastDataDict       

def command_rec(Command,FolderMarked):
    Command='''grep -irnE '''+''' --exclude=*.sample "'''+Command+'" '+FolderMarked
    print(Command)
    Args=shlex.split(Command)
    print(Args)
    CommandOutput=initate_grep_command(Args)
    print(CommandOutput)
    if CommandOutput=="Grep Command Was Insuccessful":
        return "Grep Command Was Insuccessful"
    Data=sort_data_from_grep_command(CommandOutput)
    return Data





