import pytest
import student 



def test_14(capsys):
    input_values=['14']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()
    
    out,err =  capsys.readouterr()
    output = out.split('\n')
    
    assert "true" in output[0][-7:].lower()
    assert "true" in output[1][-7:].lower()
    assert "true" in output[2][-7:].lower()

def test_9(capsys):
    input_values=['9']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()
    
    out,err =  capsys.readouterr()
    output = out.split('\n')
    
    assert "true" in output[0][-7:].lower()
    assert "false" in output[1][-7:].lower()
    assert "false" in output[2][-7:].lower()
    
def test_3(capsys):
    input_values=['3']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()
    
    out,err =  capsys.readouterr()
    output = out.split('\n')
    
    assert "false" in output[0][-7:].lower()
    assert "true" in output[1][-7:].lower()
    assert "true" in output[2][-7:].lower()
    
def test_20(capsys):
    input_values=['20']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()
    
    out,err =  capsys.readouterr()
    output = out.split('\n')
    
    assert "false" in output[0][-7:].lower()
    assert "true" in output[1][-7:].lower()
    assert "true" in output[2][-7:].lower()
