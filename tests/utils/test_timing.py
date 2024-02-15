import unittest
from time import sleep
from utils.timing import measure_execution_time


def function_to_measure(seconds):
    """
    Example function to simulate a task that takes some time.
    """
    sleep(seconds)
    return "Task completed"


class TestMeasureExecutionTime(unittest.TestCase):
    def test_measure_execution_time(self):
        result, execution_time = measure_execution_time(function_to_measure, 1)
        self.assertEqual(result, "Task completed")
        # Execution time should be at least 1 second
        self.assertGreaterEqual(execution_time, 1)
