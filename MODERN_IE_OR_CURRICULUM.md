# Modern Industrial Engineering / Operations Research Curriculum

This curriculum is a portfolio-oriented interpretation of what an Industrial Engineering (IE) / Operations Research (OR) program should teach in a data-rich, AI-integrated environment. The goal is not to replace mathematical optimization with machine learning, but to train engineers who can formulate, compute, validate, deploy, and govern decision systems.

## Design principles

1. **Keep the mathematical core.** Linear/integer optimization, networks, probability, stochastic processes, simulation, queueing, and statistics remain foundational.
2. **Teach prediction and prescription together.** Students should know when a predictive model is sufficient, when optimization is required, and how ML and OR can be combined.
3. **Treat data quality as part of modeling.** Missingness, leakage, measurement error, uncertainty, and distribution shift should be explicit parts of the decision model.
4. **Make computational scale visible.** Solver interfaces, sparse modeling, parallelism, GPU acceleration, decomposition, experiment tracking, and reproducibility belong in the curriculum.
5. **Model the sociotechnical system.** Human judgment, adoption, incentives, explainability, fairness, and implementation constraints are part of the engineering problem.
6. **Use evidence, not tool fashion.** Modern methods should be compared against strong classical baselines under reproducible evaluation.

## Bachelor's curriculum

### Year 1–2: mathematical, statistical, and computational foundations

| Course block | Core topics | Expected techniques |
|---|---|---|
| Calculus and Linear Algebra | multivariable calculus, gradients, matrix algebra, eigenstructure | vectorization, conditioning, numerical linear algebra |
| Probability and Statistics | distributions, estimation, confidence intervals, regression, Bayesian basics | likelihood, bootstrap, uncertainty intervals |
| Programming for IE | Python, NumPy, pandas, visualization, SQL, algorithms | testing, version control, reproducible scripts |
| Introduction to OR | formulation, LP, graphical methods, sensitivity | decision variables, objectives, constraints, shadow prices |
| Engineering Economics and Decisions | NPV, risk, utility, decision trees | scenario analysis, value of information |

### Year 2–3: core IE/OR methods

| Course block | Core topics | Expected techniques |
|---|---|---|
| Linear and Network Optimization | simplex, duality, flows, transportation | primal/dual reasoning, sensitivity, network algorithms |
| Integer and Combinatorial Optimization | MILP, branch-and-bound, cuts, heuristics | TSP, knapsack, assignment, CP-SAT |
| Stochastic Models | Markov chains, queues, inventory | state models, steady-state analysis, service levels |
| Simulation | DES, Monte Carlo, input/output analysis | variance reduction, calibration, simulation experiments |
| Data Analytics | EDA, supervised/unsupervised learning, time series | train/validation design, leakage control, calibration |
| Statistical Quality Engineering | SPC, capability, DOE | control charts, factorial designs, response analysis |

### Year 3–4: applications and integration

| Course block | Core topics | Expected techniques |
|---|---|---|
| Supply Chain and Logistics | network design, inventory, routing, resilience | MILP, robust/stochastic models, forecasting |
| Production and Scheduling | planning, sequencing, maintenance, lean | MRP concepts, scheduling, simulation-optimization |
| Service and Workforce Operations | capacity, staffing, rostering, queues | shift scheduling, service-level models |
| Machine Learning for IE | predictive maintenance, demand sensing, hybrid ML+OR | feature pipelines, uncertainty-aware prediction, decision-focused models |
| Human-Centered Decision Systems | behavioral OR, explainability, decision support | stakeholder constraints, override design, human-in-the-loop evaluation |
| Responsible Optimization | fairness, privacy, auditability | fairness-efficiency trade-offs, policy constraints, model cards |
| Capstone | one real decision system end-to-end | problem framing, data audit, model, baseline, validation, deployment plan |

## Master's curriculum

### Required core

| Course | Topics |
|---|---|
| Advanced Optimization | convex/nonlinear optimization, duality, large-scale methods |
| Integer and Decomposition Methods | branch-and-cut, Benders, column generation, Lagrangian methods |
| Stochastic and Robust Optimization | scenarios, chance constraints, DRO, adaptive decisions |
| Advanced Statistics and Causal Inference | multivariate methods, experiments, treatment effects, causal graphs |
| Machine Learning for Decision Systems | deep learning, probabilistic ML, reinforcement learning |
| Simulation and Uncertainty Quantification | calibration, sensitivity, metamodeling, ranking-and-selection |
| Computational Decision Systems | sparse modeling, GPU/parallel methods, cloud execution, experiment reproducibility |
| Research Methods | literature review, hypothesis design, reproducible empirical work |

### Recommended specialization clusters

**Analytics + AI:** decision-focused learning, differentiable optimization, reinforcement learning, graph learning, Bayesian optimization, causal decision-making.

**Supply Chain + Logistics:** network design, inventory, routing, revenue management, resilience, sustainable logistics.

**Manufacturing + Industry 4.0:** digital twins, predictive maintenance, quality engineering, production control, scheduling, simulation-optimization.

**Finance:** portfolio/risk optimization, market microstructure, derivatives, model validation.

**Healthcare and Public-Service Operations:** patient flow, capacity planning, appointment systems, resource allocation, cost-effectiveness. This should be taught with domain-specific governance rather than as a generic optimization exercise.

## Portfolio alignment

The current Jors Academy portfolio already covers much of the technical core:

- mathematical and computational optimization: `computational-optimization-methods`, `decomposition-and-large-scale-optimization`, `benders-decomposition-methods`
- stochastic/robust decision-making: `stochastic-programming-methods`, `robust-and-distributionally-robust-optimization`, `simulation-optimization-and-uncertainty-quantification`
- scheduling, production, inventory, routing, location, and supply chain: dedicated domain repositories
- ML + OR integration: `decision-focused-learning-and-differentiable-optimization`, `learning-augmented-optimization-solvers`, `constraint-learning-for-industrial-engineering`, `graph-learning-combinatorial-optimization`
- reinforcement and sequential decision-making: `industrial-reinforcement-learning`, `sequential-decision-analytics`
- Industry 4.0 and digital manufacturing: `industry-4.0-lab`, `manufacturing-systems-optimization`
- finance: `banking-and-financial-services-optimization`, `quantitative-trading-and-market-microstructure-optimization`, `derivatives-pricing-hedging-and-xva`
- emerging optimization: `quantum-qubo-hybrid-optimization`

## Recent Management Science portfolio additions and remaining gaps

The portfolio now closes several previously identified gaps through repository-native projects inside the relevant umbrella repositories:

1. **Fairness-aware and human-centered optimization:** `resource-allocation-optimization` includes explicit fairness-efficiency trade-offs and human-centered allocation guidance.
2. **Statistical quality engineering:** `manufacturing-systems-optimization` includes executable DOE, SPC and capability-analysis material.
3. **Causal operations and experimentation:** `pricing-and-revenue-optimization/projects/causal-operations-and-experimentation` implements randomized ATE estimation, difference-in-differences, AIPW and budgeted treatment policies.
4. **Behavioral operations:** `inventory-optimization-and-control/projects/behavioral-operations-and-human-decision-making` implements behavioral newsvendor bias, anchoring and bounded human overrides.
5. **Market design and incentives:** `resource-allocation-optimization/projects/market-design-mechanism-design-and-incentives` adds welfare-maximizing assignment, VCG payments and stable matching.
6. **Service systems and queueing:** `workforce-optimization-and-analytics/projects/service-systems-and-queueing` adds Erlang C staffing, service-level constraints and simulation validation.
7. **Empirical operations and structural demand:** `pricing-and-revenue-optimization/projects/empirical-operations-and-demand-modeling` adds multinomial-logit demand estimation, elasticities and price optimization.
8. **Project portfolio and project scheduling:** `classical-scheduling-optimization/projects/project-portfolio-and-project-scheduling` adds CPM/PERT, completion-risk simulation and budgeted project selection.
9. **System dynamics for operations:** `robust-and-adaptive-supply-chain-optimization/projects/system-dynamics-for-operations` adds stock-flow feedback, delayed supply lines and bullwhip analysis.
10. **Strategic and adversarial optimization:** `resource-allocation-optimization/projects/adversarial-game-theoretic-optimization` adds Stackelberg security allocation, exact small-network interdiction and finite-scenario robust attacker-defender allocation.
11. **Production decision-system engineering:** `production-planning-optimization/projects/closed-loop-production-decision-system` adds explicit data contracts, primary/fallback planning, auditable recommendations, human overrides, execution feedback and drift-triggered reoptimization.

The principal domain gap intentionally left open is **healthcare/public-service operations**. It should be added only as a dedicated domain repository with careful governance, not forced into unrelated optimization examples.

Decision-system production engineering now has an explicit reference implementation in `production-planning-optimization/projects/closed-loop-production-decision-system`. It remains a cross-cutting implementation objective: reproducibility, data contracts, monitoring, fallbacks, auditability and deployment controls should continue to be added where they materially affect decision workflows.

## Topics that do not need priority expansion

- **Quantum optimization** is already represented; it should remain an advanced elective rather than a core requirement.
- **Generic blockchain content** should not be included unless tied to a concrete IE/OR decision problem with measurable operational value.
- **Generic MLOps** should not become a standalone OR topic when it can be taught through reproducibility, data contracts, experiment tracking, and deployment of actual decision systems.

## Capstone standard

A modern IE/OR capstone should be considered complete only when it contains:

- a decision statement and stakeholder map;
- a data-quality and leakage audit;
- an explicit mathematical or simulation model;
- at least one strong operational baseline;
- uncertainty/sensitivity analysis;
- computational reproducibility;
- fairness, safety, or implementation constraints where relevant;
- an evaluation protocol separating tuning from final testing;
- a deployment/monitoring plan;
- a limitations section that distinguishes synthetic evidence from real-world claims.

The objective is to graduate engineers who can connect rigorous optimization with data, computation, experimentation, and implementation in complex sociotechnical systems.
