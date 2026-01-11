from enum import Enum, auto
from typing import Set, Dict


class TestStatus(Enum):
    """Enum representing all possible test statuses."""
    PASSED = auto()
    FAILED = auto()
    NO_RUN = auto()
    BROKEN = auto()
    SKIPPED = auto()
    RESOURCE_NOT_FOUND = auto()


# Define the transition rules based on the table
TRANSITION_RULES:dict[TestStatus, set[TestStatus]]=\
     {
    TestStatus.PASSED: {},
    TestStatus.FAILED: {
        TestStatus.PASSED, TestStatus.FAILED
    },
    TestStatus.NO_RUN: {
        TestStatus.PASSED, TestStatus.FAILED, TestStatus.BROKEN
    },
    TestStatus.BROKEN: {
        TestStatus.PASSED, TestStatus.FAILED

    },
    TestStatus.SKIPPED: {
        TestStatus.PASSED, TestStatus.FAILED, TestStatus.BROKEN
    },
    TestStatus.RESOURCE_NOT_FOUND: {
        TestStatus.PASSED, TestStatus.FAILED,
                   TestStatus.NO_RUN, TestStatus.BROKEN

    }
     }


def should_update_status(current: TestStatus, new: TestStatus) -> bool:
    """
    Determine if we should update the status based on the transition rules.

    Args:
        current: The current status of the test
        new: The new status to transition to

    Returns:
        bool: True if the status should be updated, False if it should be skipped

    Example:
        >>> should_update_status(TestStatus.FAILED, TestStatus.PASSED)
        True
        >>> should_update_status(TestStatus.PASSED, TestStatus.FAILED)
        False
    """
    if new in TRANSITION_RULES[current]:
        return True

    return False

if __name__ == "__main__":
    # Test cases
    test_cases = [
        (TestStatus.PASSED, TestStatus.FAILED, False),
        (TestStatus.FAILED, TestStatus.PASSED, True),
        (TestStatus.NO_RUN, TestStatus.BROKEN, True),
        (TestStatus.SKIPPED, TestStatus.SKIPPED, False),
        (TestStatus.RESOURCE_NOT_FOUND, TestStatus.PASSED, True),
        (TestStatus.BROKEN, TestStatus.SKIPPED, False),
    ]

    print("Running test cases:")
    print("=" * 50)
    for current, new, expected in test_cases:
        result = should_update_status(current, new)
        print(
            f"{current.name:>16} -> {new.name:<16} | Expected: {str(expected):<5} | Got: {str(result):<5} | {'PASS' if result == expected else 'FAIL'}")