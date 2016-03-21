import sys
from data_branch import BranchData
from evaluator_branch import BranchEvaluator

submission_file = sys.argv[1]
solution_file = sys.argv[2]

submission = BranchData(submission_file)
solution = BranchData(solution_file)

evaluator = BranchEvaluator(submission,solution)
print evaluator.run()
