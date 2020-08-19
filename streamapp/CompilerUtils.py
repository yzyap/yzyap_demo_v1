from enum import Enum
import subprocess
import random
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


def generate_rand_name(length):
    generated = ""
    for i in range(length):
        base = 97 if random.randint(0, 1) == 0 else 65
        offset = random.randint(0, 25)
        generated += chr(base+offset)
    return generated


class Compiler:
    exec_status = None  # exec_status:None denotes that the program has'nt been executed yet (hasExecuted=False)
    code = None
    template = None
    test_cases = None
    outputs = None
    errors = None
    failed_test_cases = None  # once execute() is called, this value will be set
    language = None
    filename = None
    hasErrors = False
    hasExecuted = False
    hasFile = False
    maxExecTime = 10  # [unit: seconds] Default value, can be overridden
    process = None
    maxExecTime = 5  # [unit: seconds] Default value, can be overridden

    def set_code(self, code):
        self.code = code
        return


    def generate_code_file(self):
        self.filename = generate_rand_name(10)
        if self.filename is None:
            print("*** ERROR : Filename cannot be generated! ***")
        if self.template is not None:
            complete_code = self.template + "\r\n" + self.code
        else:
            complete_code = self.code+"\r\n"
        file_handle = open(self.filename, "w")
        file_handle.write(complete_code)
        file_handle.flush()
        file_handle.close()

    def delete_code_file(self):
        if self.filename is None:
            print("*** ERROR: filename NONE ***")
        os.remove(self.filename)
        self.hasFile = False
        self.filename = None

    def terminate(self):
        if self.process is not None:
            self.process.kill() 
            print("Killing process")      

    def execute(self):
        self.exec_status = ExecutionStatus.NYR
        if not self.hasFile or self.filename is None:
            self.generate_code_file()

        command = ["python", self.filename]

        self.outputs = []
        self.errors = []

        self.process = subprocess.Popen(command, stdout=subprocess.PIPE,  stderr=subprocess.PIPE)

       #burada bekliyor
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
            self.failed_test_cases = 0
            print("outputs:",self.outputs)
            print("errors:",self.errors)

        return self.exec_status
