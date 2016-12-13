#VJ Davey
#10/3/2016
#Gurobi Optimization Assignment
#Quicksum variant with Gurobi
from gurobipy import *

# create Gurobi model and assign it to a variable in python
m = Model("3_1_6")#problem 3.1-6
m.ModelSense = GRB.MAXIMIZE # tell gurobi to maximize the objective function. We want to maximize profit here
m.setParam('TimeLimit',7200)     #sets a time limit on execution to some number of seconds

#objective coefficients and constraint coefficients
obj_coeff=[5.0,2.0]
cnstrt_coeff=[[3.0,2.0],[0.0,1.0],[2.0,0.0]]
cnstrt_names=["UnderwritingHours","AdminHours","ClaimsHours"]
cnstrt_rhs=[2400.0,800.0,1200.0]
# Set up decision variables
dvars=[]
for i in range(len(obj_coeff)):
		dvars.append(m.addVar(vtype=GRB.CONTINUOUS,name='v'+str(i),lb=0.0))
#Update model to include variables
m.update() #THIS must be done so Gurobi can recognize variable names when referenced in the constraints and objective function
for i in range(len(cnstrt_coeff)):
	m.addConstr(quicksum((cnstrt_coeff[i][j] * dvars[j] for j in range(len(dvars)))), GRB.LESS_EQUAL, cnstrt_rhs[i],cnstrt_names[i])
# set up constraints
m.setObjective(quicksum(obj_coeff[i] * dvars[i] for i in range(len(dvars))), GRB.MAXIMIZE)
# Update the model - It won't run if you don't do this
m.update()

# Optimize the model
m.optimize()

#printout of results
for var in m.getVars():
    print "Variable Name = %s, Optimal Value = %s, Lower Bound = %s, Upper Bound = %s" % (var.varName, var.x,var.lb,var.ub)
