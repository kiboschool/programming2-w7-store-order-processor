

from with_bugs_01 import ProcessorWithBugs01
from with_bugs_02 import ProcessorWithBugs02
from with_bugs_03 import ProcessorWithBugs03
from with_bugs_04 import ProcessorWithBugs04
from with_bugs_05 import ProcessorWithBugs05
from with_bugs_06 import ProcessorWithBugs06
from with_bugs_07 import ProcessorWithBugs07
from with_bugs_08 import ProcessorWithBugs08
from with_bugs_09 import ProcessorWithBugs09
from with_bugs_10 import ProcessorWithBugs10
from with_bugs_11 import ProcessorWithBugs11
from with_bugs_12 import ProcessorWithBugs12
from with_bugs_13 import ProcessorWithBugs13
from with_bugs_14 import ProcessorWithBugs14


# provide a bunch of broken implementations:
# the tests running with these implementations should fail.


classes = [
    ProcessorWithBugs01, 
    ProcessorWithBugs02, 
    ProcessorWithBugs03, 
    ProcessorWithBugs04, 
    ProcessorWithBugs05, 
    ProcessorWithBugs06, 
    ProcessorWithBugs07, 
    ProcessorWithBugs08, 
    ProcessorWithBugs09, 
    ProcessorWithBugs10, 
    ProcessorWithBugs11, 
    ProcessorWithBugs12, 
    ProcessorWithBugs13, 
    ProcessorWithBugs14, 
    ]

def run_all_tests(Cls):
    test_store_order_processor.main.StoreOrderProcessor = Cls
    test_instance = test_store_order_processor.TestStoreOrderProcessor()
    for method_name in dir(test_instance):
        if method_name.startswith('test_'):
            try:
                getattr(test_instance, method_name)()
            except:
                raise AssertionError('test failed')

def test_tests():
    for Cls in classes:
        # all of these are broken in some way, we expect it to fail
        expect_tests_to_pass = False
        try:
            run_all_tests(Cls)
            tests_passed = True
        except:
            tests_passed = False
        
        assert expect_tests_to_pass == tests_passed

if __name__ == '__main__':
    test_tests()
    
