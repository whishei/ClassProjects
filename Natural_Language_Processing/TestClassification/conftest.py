from collections import OrderedDict


tests = OrderedDict({"test_create_tfidvectorizer": 16,
                     "test_run_vectorizer": 16,
                     "test_create_model": 16,
                     "test_run_model": 16,
                     "test_create_balanced_model": 16,
                     "test_create_column_transformer": 20})


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    terminalreporter.section("Score")
    scores = OrderedDict({test_id: 0.0 for test_id in tests})
    if 'passed' in terminalreporter.stats:
        for testreport in terminalreporter.stats['passed']:
            passed_test_id = testreport.nodeid.split("::")[-1]
            scores[passed_test_id] = tests[passed_test_id]
    total_score = 0
    for test_id, score in scores.items():
        terminalreporter.write(f'{test_id}: {score}%\n')
        total_score += score
    terminalreporter.write(f'\nTotal Score: {total_score}%\n')
    terminalreporter.currentfspath = 1
    terminalreporter.ensure_newline()
