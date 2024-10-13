import unittest

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

from implementations.store_order_processor import (
    StoreOrderProcessor,
    StoreOrderProcessorException,
)
import test_store_order_processor

from gradescope_utils.autograder_utils.decorators import weight


# These tests check if test_store_order_processor is working correctly.

# In these tests, we take an intentionally broken StoreOrderProcessor implementation
# and hand it to test_store_order_processor and run the tests,
# we then expect it to see an error because we expect at least one of the tests there to fail.

class TestTests(unittest.TestCase):
        
    @weight(1)
    def test_with_bugs_01(self):
        self._run_test(ProcessorWithBugs01, expect_pass=False)
        
    @weight(1)
    def test_with_bugs_02(self):
        self._run_test(ProcessorWithBugs02, expect_pass=False)
        
    @weight(1)
    def test_with_bugs_03(self):
        self._run_test(ProcessorWithBugs03, expect_pass=False)
        
    @weight(1)
    def test_with_bugs_04(self):
        self._run_test(ProcessorWithBugs04, expect_pass=False)
        
    @weight(1)
    def test_with_bugs_05(self):
        self._run_test(ProcessorWithBugs05, expect_pass=False)
        
    @weight(1)
    def test_with_bugs_06(self):
        self._run_test(ProcessorWithBugs06, expect_pass=False)
        
    @weight(1)
    def test_with_bugs_07(self):
        self._run_test(ProcessorWithBugs07, expect_pass=False)
        
    @weight(1)
    def test_with_bugs_08(self):
        self._run_test(ProcessorWithBugs08, expect_pass=False)
        
    @weight(1)
    def test_with_bugs_09(self):
        self._run_test(ProcessorWithBugs09, expect_pass=False)
        
    @weight(1)
    def test_with_bugs_10(self):
        self._run_test(ProcessorWithBugs10, expect_pass=False)
        
    @weight(1)
    def test_correct_implementation(self):
        self._run_test(StoreOrderProcessor, expect_pass=True)

    def _run_test(self, Cls, expect_pass):
        try:
            run_store_order_processor_tests(Cls)
            tests_passed = True
        except (AssertionError, StoreOrderProcessorException):
            tests_passed = False

        if expect_pass and not tests_passed:
            raise RuntimeError(
                f"We expected the implementation {Cls.__name__} to pass tests, but it did not"
            )

        if not expect_pass and tests_passed:
            raise RuntimeError(
                f"We expected the buggy implementation {Cls.__name__} to fail tests, but it passed the tests"
            )


# This helper function tweaks the test_store_order_processor module
# so that it gets a different instance than usual, then it looks for tests + runs them.
def run_store_order_processor_tests(Cls):
    test_store_order_processor.get_instance = lambda: Cls()
    test_instance = test_store_order_processor.TestStoreOrderProcessor()
    for method_name in dir(test_instance):
        if method_name.startswith("test_"):
            try:
                getattr(test_instance, method_name)()
            except NotImplementedError:
                raise
            except:
                raise AssertionError("test failed")


if __name__ == "__main__":
    unittest.main()

