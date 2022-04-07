from src.jobs import read


def get_unique_job_types(path):
    lista_jobs = read(path)
    # lista_tipos_unicos = []
    conjunto_de_unicos = set()
    for jobs in lista_jobs:
        conjunto_de_unicos.add(jobs["job_type"])

    return conjunto_de_unicos


def filter_by_job_type(lista_jobs, job_type):
    # fff
    filter_jobs = []
    for job in lista_jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs


def get_unique_industries(path):
    conjunto_de_unicos = set()
    list_industria = read(path)
    for industria in list_industria:
        if len(industria["industry"]) != 0:
            conjunto_de_unicos.add(industria["industry"])
    return conjunto_de_unicos


def filter_by_industry(jobs, industry):
    filter_industry = []
    for industria in jobs:
        if industria["industry"] == industry:
            filter_industry.append(industria)
    return filter_industry


def get_max_salary(path):
    lista_jobs = read(path)
    lista_de_salarios = []
    for salario in lista_jobs:
        if salario["max_salary"].isnumeric():
            lista_de_salarios.append(int(salario['max_salary']))
    return max(lista_de_salarios)

    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    pass


def get_min_salary(path):
    lista_jobs = read(path)
    lista_de_salarios = []
    for salario in lista_jobs:
        if salario["min_salary"].isnumeric():
            lista_de_salarios.append(int(salario['min_salary']))
    return min(lista_de_salarios)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities

        https://www.programiz.com/python-programming/methods/string/isnumeric
         checando se é numero ou vazio
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
