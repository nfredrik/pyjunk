# Test Result Status Transition Matrix

| first \ others         | PASSED | FAILED | NO_RUN | BROKEN | SKIPPED | RESOURCE_NOT_FOUND |
|------------------------|--------|--------|--------|--------|---------|--------------------|
| **PASSED**             | skip   | skip   | skip   | skip   | skip    | skip               |
| **FAILED**             | update | update | skip   | skip   | skip    | skip               |
| **NO_RUN**             | update | update | skip   | update | skip    | skip               |
| **BROKEN**             | update | update | skip   | skip   | skip    | skip               |
| **SKIPPED**            | update | update | skip   | update | skip    | skip               |
| **RESOURCE_NOT_FOUND** | update | update | update | update | skip    | skip               |

## Legend
- ✓ : Transition is possible
- - : No transition (same status)

## Possible Transitions
- **PASSED** → Any status
- **FAILED** → Any status
- **NO_RUN** → Any status
- **BROKEN** → Any status
- **SKIPPED** → Any status
- **RESOURCE_NOT_FOUND** → Any status

## Notes
- All statuses can transition to any other status except to themselves
- This matrix shows all possible transitions between different test result statuses
- The diagonal is marked with "-" as a test cannot transition to the same status