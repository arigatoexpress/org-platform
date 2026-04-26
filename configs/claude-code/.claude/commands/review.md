# /review

Review the current diff as a senior staff engineer.

Focus order:
1. Behavioral regressions or safety risks.
2. Secrets, live trading, or live messaging exposure.
3. Missing tests for changed behavior.
4. Source TOS or API contract assumptions.
5. Maintainability issues that will slow future autonomy work.

Output findings first with file and line references. If no findings, say so and name residual test gaps.

