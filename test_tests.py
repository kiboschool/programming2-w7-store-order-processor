
from implementations.store_order_processor import StoreOrderProcessor
from implementations.with_bugs_01 import ProcessorWithBugs01
from implementations.with_bugs_02 import ProcessorWithBugs02
from implementations.with_bugs_03 import ProcessorWithBugs03
from implementations.with_bugs_04 import ProcessorWithBugs04
from implementations.with_bugs_05 import ProcessorWithBugs05
from implementations.with_bugs_06 import ProcessorWithBugs06
from implementations.with_bugs_07 import ProcessorWithBugs07
from implementations.with_bugs_08 import ProcessorWithBugs08
from implementations.with_bugs_09 import ProcessorWithBugs09
from implementations.with_bugs_10 import ProcessorWithBugs10
from implementations.with_bugs_11 import ProcessorWithBugs11
from implementations.with_bugs_12 import ProcessorWithBugs12
from implementations.with_bugs_13 import ProcessorWithBugs13
from implementations.with_bugs_14 import ProcessorWithBugs14

from implementations.store_order_processor import StoreOrderProcessor, StoreOrderProcessorException
import test_store_order_processor

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
    StoreOrderProcessor
    ]

def run_all_tests(Cls):
    test_store_order_processor.get_instance = lambda: Cls()
    test_instance = test_store_order_processor.TestStoreOrderProcessor()
    for method_name in dir(test_instance):
        if method_name.startswith('test_'):
            try:
                getattr(test_instance, method_name)()
            except:
                raise AssertionError('test failed')

def test_tests():
    for Cls in classes:
        # all of these are broken except the reference implementation (StoreOrderProcessor )
        expect_tests_to_pass = Cls == StoreOrderProcessor
        try:
            print(f'Running tests for {Cls.__name__}')
            run_all_tests(Cls)
            tests_passed = True
        except (AssertionError, StoreOrderProcessorException):
            tests_passed = False
        
        assert expect_tests_to_pass == tests_passed
    print('Complete')

if __name__ == '__main__':
    test_tests()
    
