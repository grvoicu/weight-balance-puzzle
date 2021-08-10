
from ortools.sat.python import cp_model


class VarArrayAndObjectiveSolutionPrinter(cp_model.CpSolverSolutionCallback):
  """Print intermediate solutions."""

  def __init__(self, variables):
    cp_model.CpSolverSolutionCallback.__init__(self)
    self.__variables = variables
    self.__solution_count = 0

  def on_solution_callback(self):
    print('Solution %i' % self.__solution_count)
    for v in self.__variables:
      print('  %s = %i' % (v, self.Value(v)), end=' ')
    print()
    self.__solution_count += 1

  def solution_count(self):
    return self.__solution_count


num_values = 4  # This must be set to 4. See TODO bellow.
min_value = 1
max_value = 40

model = cp_model.CpModel()

 # Creates the variables.
variables = [
    model.NewIntVar(min_value, max_value, 'var{}'.format(i+1))
    for i in range(num_values)
]

for i in range(min_value, max_value+1):
    # We can place weights on both sides of the scale to balance the scale.
    # We have 5 weights: the 4 in the solution + the object with an integer 
    # weight between min_value and max_value. 
    # In total there are 64 possible combinations for a total of 5 weights, 
    # with min 1 and max 4 weights on every scale. 
    # For every combination we define a boolean variable which conditions a 
    # constraint on the scale to balanced. At least one constraint must be true
    # for every unknown weight.
    # TODO: Programmatically generate the combinations and add the constraints
    # so we can add an objective to minimize the number of weights. Currently it
    # is hard-coded to 4 because we manually added the constraints.
    coefficients = [
        model.NewBoolVar('coefficients_{}'.format(j+1))
        for j in range(64)
    ]

    # Subtracting a variable is equivalent with placing it on the other side of
    # the scale, together with the object with the unknown weight.

    model.Add(variables[0] == i).OnlyEnforceIf(coefficients[0])
    model.Add(variables[1] == i).OnlyEnforceIf(coefficients[1])
    model.Add(variables[2] == i).OnlyEnforceIf(coefficients[2])
    model.Add(variables[3] == i).OnlyEnforceIf(coefficients[3])

    model.Add(variables[0] + variables[1] == i).OnlyEnforceIf(coefficients[4])
    model.Add(variables[0] - variables[1] == i).OnlyEnforceIf(coefficients[5])
    model.Add(variables[1] - variables[0] == i).OnlyEnforceIf(coefficients[6])

    model.Add(variables[0] + variables[2] == i).OnlyEnforceIf(coefficients[7])
    model.Add(variables[0] - variables[2] == i).OnlyEnforceIf(coefficients[8])
    model.Add(variables[2] - variables[0] == i).OnlyEnforceIf(coefficients[9])

    model.Add(variables[0] + variables[3] == i).OnlyEnforceIf(coefficients[10])
    model.Add(variables[0] - variables[3] == i).OnlyEnforceIf(coefficients[11])
    model.Add(variables[3] - variables[0] == i).OnlyEnforceIf(coefficients[12])

    model.Add(variables[1] + variables[2] == i).OnlyEnforceIf(coefficients[13])
    model.Add(variables[1] - variables[2] == i).OnlyEnforceIf(coefficients[14])
    model.Add(variables[2] - variables[1] == i).OnlyEnforceIf(coefficients[15])

    model.Add(variables[1] + variables[3] == i).OnlyEnforceIf(coefficients[16])
    model.Add(variables[1] - variables[3] == i).OnlyEnforceIf(coefficients[17])
    model.Add(variables[3] - variables[1] == i).OnlyEnforceIf(coefficients[18])

    model.Add(variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[19])
    model.Add(variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[20])
    model.Add(variables[3] - variables[2] == i).OnlyEnforceIf(coefficients[21])

    model.Add(variables[0] + variables[1] + variables[2] == i).OnlyEnforceIf(coefficients[22])
    model.Add(variables[0] + variables[1] - variables[2] == i).OnlyEnforceIf(coefficients[23])
    model.Add(variables[0] - variables[1] + variables[2] == i).OnlyEnforceIf(coefficients[24])
    model.Add(variables[0] - variables[1] - variables[2] == i).OnlyEnforceIf(coefficients[25])
    model.Add(-variables[0] + variables[1] + variables[2] == i).OnlyEnforceIf(coefficients[26])
    model.Add(-variables[0] + variables[1] - variables[2] == i).OnlyEnforceIf(coefficients[27])
    model.Add(-variables[0] - variables[1] + variables[2] == i).OnlyEnforceIf(coefficients[28])

    model.Add(variables[0] + variables[1] + variables[3] == i).OnlyEnforceIf(coefficients[29])
    model.Add(variables[0] + variables[1] - variables[3] == i).OnlyEnforceIf(coefficients[30])
    model.Add(variables[0] - variables[1] + variables[3] == i).OnlyEnforceIf(coefficients[31])
    model.Add(variables[0] - variables[1] - variables[3] == i).OnlyEnforceIf(coefficients[32])
    model.Add(-variables[0] + variables[1] + variables[3] == i).OnlyEnforceIf(coefficients[33])
    model.Add(-variables[0] + variables[1] - variables[3] == i).OnlyEnforceIf(coefficients[34])
    model.Add(-variables[0] - variables[1] + variables[3] == i).OnlyEnforceIf(coefficients[35])

    model.Add(variables[0] + variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[36])
    model.Add(variables[0] + variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[37])
    model.Add(variables[0] - variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[38])
    model.Add(variables[0] - variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[39])
    model.Add(-variables[0] + variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[40])
    model.Add(-variables[0] + variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[41])
    model.Add(-variables[0] - variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[42])

    model.Add(variables[1] + variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[43])
    model.Add(variables[1] + variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[44])
    model.Add(variables[1] - variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[45])
    model.Add(variables[1] - variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[46])
    model.Add(-variables[1] + variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[47])
    model.Add(-variables[1] + variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[48])
    model.Add(-variables[1] - variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[49])

    model.Add(variables[0] + variables[1] + variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[50])

    model.Add(-variables[0] + variables[1] + variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[51])
    model.Add( variables[0] - variables[1] + variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[52])
    model.Add( variables[0] + variables[1] - variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[53])
    model.Add( variables[0] + variables[1] + variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[54])

    model.Add(-variables[0] - variables[1] + variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[55])
    model.Add(-variables[0] + variables[1] - variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[56])
    model.Add(-variables[0] + variables[1] + variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[57])    
    model.Add( variables[0] - variables[1] - variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[58])
    model.Add( variables[0] - variables[1] + variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[59])
    model.Add( variables[0] + variables[1] - variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[60])

    model.Add(-variables[0] - variables[1] - variables[2] + variables[3] == i).OnlyEnforceIf(coefficients[61])
    model.Add(-variables[0] - variables[1] + variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[62])
    model.Add( variables[0] - variables[1] - variables[2] - variables[3] == i).OnlyEnforceIf(coefficients[63])
   
    # At least one combination of weights must balance the scale.
    model.AddBoolOr(coefficients)

solver = cp_model.CpSolver()
solution_printer = VarArrayAndObjectiveSolutionPrinter(variables)
status = solver.SolveWithSolutionCallback(model, solution_printer)

print('Status = %s' % solver.StatusName(status))
print('Number of solutions found: %i' % solution_printer.solution_count())
