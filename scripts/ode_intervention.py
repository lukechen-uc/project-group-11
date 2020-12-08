from sir.ode import *
def iEq1(t, y):
    return y[3] - 0.05

# terminate if y=0 and the direction is from positive to negetive.
iEq1.terminal = True
iEq1.direction = 1
iEq1.intervention = {'q': 0.8}

def iEq2(t, y):
    return y[3] - 0.1

# terminate if y=0 and the direction is from positive to negetive.
iEq2.terminal = True
iEq2.direction = 1
iEq2.intervention = {'q': 0.99}

# init model
model = MSEIQRDS()
model.solve(t_bound=365, h=1)
model.plot(decorators=False,show=False)
plt.xlabel('day')
plt.ylabel('ratio')
plt.title('MSEIQRDS without interventions')
plt.legend()
plt.savefig('./doc/final/figures/no_intervention.png')
plt.show()


# intervention with quarantine
sol = intervention_solve(model, events=[iEq1, iEq2], t_bound=365, h=1)
intervention_plot(sol, save_path='./doc/final/figures/intervention_q.png')

# intervention with mask
iEq1.intervention = {'b': 0.1}
sol = intervention_solve(model, events=[iEq1], t_bound=365, h=1)
intervention_plot(sol, save_path='./doc/final/figures/intervention_b.png')
