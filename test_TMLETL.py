import GMLETL

def test_output(capfd):
    # Run the code in GMLETL.py
    GMLETL.main()
    
    # Capture the output
    out, err = capfd.readouterr()
    
    # Assert the expected output
    expected_output = "expected output string"
    assert expected_output in out



