from data_upselling import UpsellingData 
from evaluator_upselling import UpsellingEvaluator

submission_file = sys.argv[1]
solution_file = sys.argv[2]

submission = UpsellingData(submission_file)
solution = UpsellingData(solution_file)

evaluator = UpsellingEvaluator(submission,solution)
return evaluator.run()
