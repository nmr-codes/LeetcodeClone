from django.shortcuts import render, get_object_or_404
from .models import Problem, Solution, TestCase
from .forms import SolutionForm
from .utils import run_code

def problem_detail(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    form = SolutionForm(request.POST or None)
    result = None

    if form.is_valid():
        solution = form.save(commit=False)
        solution.problem = problem

        # Har bir test sinovini ko‘rib chiqish
        for test in problem.test_cases.all():
            output = run_code(solution.code, test.input_data)
            if output != test.expected_output:
                result = f"Test Failed: Expected {test.expected_output}, but got {output}"
                solution.result = 'Failed'
                break
        else:
            result = "All Tests Passed!"
            solution.result = 'Passed'

        solution.save()

    return render(request, 'problems/problem_detail.html', {'problem': problem, 'form': form, 'result': result})
