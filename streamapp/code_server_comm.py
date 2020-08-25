from enum import Enum
import subprocess
import os

# The ExecutionStatus class is an enum, one of which will be returned by the execute method
class ExecutionStatus(Enum):
    NYR = 0  # Still Executing .... may take a few more time to get results
    ACC = 1  # Executed successfully, Solution correct, accepted
    WRA = 2  # Executed successfully, Solution wrong, rejected
    TLE = 3  # Executed, but exceeded time limit
    COE = 4  # Compilation failed
    RTE = 5  # Error encountered during Execution
    INE = 6  # Internal error has occurred, prompt user to try again! ( we'll be screwed if this happens often)


class codeServerComm:
    code = None
    exec_status = None
    outputs = None
    errors = None
    process = None
    maxExecTime = 180
    hasErrors = False
    hasExecuted = False

    def set_code(self,code):
        self.code = code
        return

    def run_server(self):
        command = ["python", "/home/mg/cv_workspace/yzyap_repos/yzyap_demo_v1/Flask_Server/flask_server.py"]
        self.outputs = []
        self.errors = []   

        self.process = subprocess.Popen(command, stdout=subprocess.PIPE,  stderr=subprocess.PIPE)  

        try:
            o, e = self.process.communicate(timeout=self.maxExecTime)
            self.outputs.append(o.decode('utf-8'))
            if len(e) != 0:
                self.errors.append(e.decode('utf-8'))
                self.hasErrors = True
            else:
                self.errors.append(None)
            self.hasExecuted = True

        except subprocess.TimeoutExpired:
            print("*** TIMEOUT, killing process... ***")
            if self.process is not None:
                self.process.kill()
            self.hasExecuted = False
            self.exec_status = ExecutionStatus.TLE

        if self.hasExecuted:
            self.exec_status = ExecutionStatus.ACC
            print("outputs:",self.outputs)
            print("errors:",self.errors) 

        return self.exec_status