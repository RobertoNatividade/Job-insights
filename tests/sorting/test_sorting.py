import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    mock_jobs = [
        {"min_salary": 1500, "max_salary": 2000, "date_posted": '2022-03-05'},
        {"min_salary": 10000, "max_salary": 15000,
         "date_posted": '2022-02-20'},
        {"min_salary": 5000, "max_salary": 7000, "date_posted": '2022-03-10'},
        {"min_salary": 2500, "max_salary": 5000, "date_posted": '2022-01-05'},
    ]

    jobjs_by_min_salary = [
        {"min_salary": 1500, "max_salary": 2000, "date_posted": '2022-03-05'},
        {"min_salary": 2500, "max_salary": 5000, "date_posted": '2022-01-05'},
        {"min_salary": 5000, "max_salary": 7000, "date_posted": '2022-03-10'},
        {
          "min_salary": 10000, "max_salary": 15000, "date_posted": '2022-02-20'
        },
    ]

    jobjs_by_max_salary = [
        {
          "min_salary": 10000, "max_salary": 15000, "date_posted": '2022-02-20'
        },
        {"min_salary": 5000, "max_salary": 7000, "date_posted": '2022-03-10'},
        {"min_salary": 2500, "max_salary": 5000, "date_posted": '2022-01-05'},
        {"min_salary": 1500, "max_salary": 2000, "date_posted": '2022-03-05'},
    ]

    jobjs_by_date_posted = [
        {"min_salary": 5000, "max_salary": 7000, "date_posted": '2022-03-10'},
        {"min_salary": 1500, "max_salary": 2000, "date_posted": '2022-03-05'},
        {
          "min_salary": 10000, "max_salary": 15000, "date_posted": '2022-02-20'
        },
        {"min_salary": 2500, "max_salary": 5000, "date_posted": '2022-01-05'},
    ]

    sort_by(mock_jobs, 'min_salary')
    assert mock_jobs == jobjs_by_min_salary

    sort_by(mock_jobs, 'max_salary')
    assert mock_jobs == jobjs_by_max_salary

    sort_by(mock_jobs, 'date_posted')
    assert mock_jobs == jobjs_by_date_posted

    with pytest.raises(ValueError):
        sort_by(mock_jobs, 'error')
